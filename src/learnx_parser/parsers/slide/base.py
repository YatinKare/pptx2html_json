import os

from lxml import etree

from learnx_parser.models.core import (
    BackgroundReference,
    CommonSlideData,
    GradientFill,
    GradientStop,
    Hyperlink,
    PresentationDefaults,
    Slide,
    SlideLayout,
)
from learnx_parser.models.presentation import Presentation
from learnx_parser.parsers.layout import LayoutParser
from learnx_parser.parsers.slide.shapes import (
    parse_shape_tree,
)
from learnx_parser.services.style_resolver import StyleResolver


class SlideParser:
    def __init__(
        self,
        slide_xml_path,
        slide_rels_path,
        pptx_unpacked_path,
        slide_width,
        slide_height,
        presentation=None,
        presentation_defaults=None,
        style_resolver=None,
    ):
        # Path to the XML file for the current slide
        self.slide_xml_path = slide_xml_path
        # Path to the relationships XML file for the current slide (can be None)
        self.slide_rels_path = slide_rels_path
        # Parse the slide XML tree
        self.tree = etree.parse(self.slide_xml_path)
        # Get the root element of the slide XML
        self.root = self.tree.getroot()
        # Parse relationships from the slide's .rels file
        self.rels = self._parse_rels()
        # Store namespace map for easier access to XML elements
        self.nsmap = self.root.nsmap
        # Path to the root of the unpacked PPTX archive
        self.pptx_unpacked_path = pptx_unpacked_path
        # Width of the slide in EMUs, inherited from presentation properties
        self.slide_width = slide_width
        # Height of the slide in EMUs, inherited from presentation properties
        self.slide_height = slide_height
        
        # Store the presentation object containing all shared resources
        self.presentation = presentation
        
        # Presentation-level default text styles for theme inheritance
        self.presentation_defaults = presentation_defaults or (presentation.presentation_defaults if presentation else {})
        
        # Style resolver instance - create from presentation data or use passed instance
        if style_resolver:
            self.style_resolver = style_resolver
        elif presentation:
            # Create StyleResolver with presentation data
            # We'll need the slide layout to determine the slide master
            slide_layout = self._get_slide_layout_obj()
            if slide_layout and slide_layout.slide_master:
                presentation_defaults_obj = PresentationDefaults()
                self.style_resolver = StyleResolver(
                    slide_master=slide_layout.slide_master,
                    presentation_defaults=presentation_defaults_obj
                )
            else:
                self.style_resolver = None
        else:
            self.style_resolver = None

    def _parse_rels(self):
        # Initialize an empty dictionary to store relationships
        relationships = {}
        # Check if the slide's relationship file path exists
        if self.slide_rels_path and os.path.exists(self.slide_rels_path):
            # Parse the relationships XML tree
            relationships_tree = etree.parse(self.slide_rels_path)
            # Iterate through each Relationship element in the relationships XML
            for relationship in relationships_tree.findall(
                "{http://schemas.openxmlformats.org/package/2006/relationships}Relationship"
            ):
                # Store the relationship ID and its target (e.g., media file path, slide layout path)
                relationships[relationship.get("Id")] = relationship.get("Target")
        return relationships

    def _resolve_relationship(self, r_embed: str) -> str | None:
        """Resolve a relationship ID to an absolute file path.
        
        Args:
            r_embed: Relationship ID (e.g., "rId2")
            
        Returns:
            Absolute path to the resolved file, or None if not found
        """
        if r_embed in self.rels:
            relative_path = self.rels[r_embed]
            # Convert relative path to absolute path
            if relative_path.startswith("../"):
                # Handle relative paths like "../media/image1.jpeg"
                absolute_path = os.path.join(self.pptx_unpacked_path, "ppt", relative_path[3:])
            else:
                # Handle direct paths like "media/image1.jpeg"
                absolute_path = os.path.join(self.pptx_unpacked_path, "ppt", relative_path)
            
            # Verify the file exists
            if os.path.exists(absolute_path):
                return absolute_path
        
        return None

    def _extract_common_slide_data(self, slide_layout_obj: SlideLayout | None = None) -> CommonSlideData:
        # Initialize CommonSlideData with slide width and height
        common_slide_data = CommonSlideData(cx=self.slide_width, cy=self.slide_height)

        # Find the common slide data element (p:cSld) in the XML
        common_slide_element = self.root.find(".//p:cSld", namespaces=self.nsmap)
        if common_slide_element is not None:
            # Find the background element (p:bg)
            background_element = common_slide_element.find(
                ".//p:bg", namespaces=self.nsmap
            )
            if background_element is not None:
                # Check for background reference first (p:bgRef)
                background_reference_element = background_element.find(
                    ".//p:bgRef", namespaces=self.nsmap
                )
                if background_reference_element is not None:
                    # Extract background reference index and scheme color
                    idx = int(background_reference_element.get("idx", "0"))
                    scheme_color = None
                    scheme_color_element = background_reference_element.find(
                        ".//a:schemeClr", namespaces=self.nsmap
                    )
                    if scheme_color_element is not None:
                        scheme_color = scheme_color_element.get("val")
                    
                    common_slide_data.background_reference = BackgroundReference(
                        idx=idx, scheme_color=scheme_color
                    )
                else:
                    # Find the background properties element (p:bgPr)
                    background_properties_element = background_element.find(
                        ".//p:bgPr", namespaces=self.nsmap
                    )
                    if background_properties_element is not None:
                        # Check for solid fill background
                        solid_fill_element = background_properties_element.find(
                            ".//a:solidFill", namespaces=self.nsmap
                        )
                        if solid_fill_element is not None:
                            # Extract SRGB color value if present
                            srgb_color_element = solid_fill_element.find(
                                ".//a:srgbClr", namespaces=self.nsmap
                            )
                            if srgb_color_element is not None:
                                common_slide_data.background_color = srgb_color_element.get(
                                    "val"
                                )
                        else:
                            # Check for gradient fill background
                            gradient_fill_element = background_properties_element.find(
                                ".//a:gradFill", namespaces=self.nsmap
                            )
                            if gradient_fill_element is not None:
                                gradient_fill = GradientFill()
                                # Extract linear gradient properties (angle, scaled)
                                linear_element = gradient_fill_element.find(
                                    ".//a:lin", namespaces=self.nsmap
                                )
                                if linear_element is not None:
                                    gradient_fill.angle = (
                                        int(linear_element.get("ang", 0))
                                        if linear_element.get("ang") is not None
                                        else None
                                    )
                                    gradient_fill.scaled = (
                                        linear_element.get("scaled", "0") == "1"
                                    )

                                # Extract gradient stop list
                                gradient_stop_list_element = gradient_fill_element.find(
                                    ".//a:gsLst", namespaces=self.nsmap
                                )
                                if gradient_stop_list_element is not None:
                                    # Iterate through each gradient stop
                                    for (
                                        gradient_stop_element
                                    ) in gradient_stop_list_element.findall(
                                        ".//a:gs", namespaces=self.nsmap
                                    ):
                                        position = int(gradient_stop_element.get("pos", 0))
                                        stop_color = None
                                        stop_scheme_color = None
                                        # Extract SRGB color for the stop
                                        srgb_color_element = gradient_stop_element.find(
                                            ".//a:srgbClr", namespaces=self.nsmap
                                        )
                                        if srgb_color_element is not None:
                                            stop_color = srgb_color_element.get("val")
                                        else:
                                            # Extract scheme color for the stop
                                            scheme_color_element = (
                                                gradient_stop_element.find(
                                                    ".//a:schemeClr", namespaces=self.nsmap
                                                )
                                            )
                                            if scheme_color_element is not None:
                                                stop_scheme_color = (
                                                    scheme_color_element.get("val")
                                                )
                                        # Append the gradient stop to the list
                                        gradient_fill.stops.append(
                                            GradientStop(
                                                pos=position,
                                                color=stop_color,
                                                scheme_color=stop_scheme_color,
                                            )
                                        )
                                common_slide_data.background_gradient_fill = gradient_fill
                            else:
                                # Check for image fill background (blipFill)
                                blip_fill_element = background_properties_element.find(
                                    ".//a:blipFill", namespaces=self.nsmap
                                )
                                if blip_fill_element is not None:
                                    # Extract the relationship ID (r:embed)
                                    blip_element = blip_fill_element.find(
                                        ".//a:blip", namespaces=self.nsmap
                                    )
                                    if blip_element is not None:
                                        r_embed = blip_element.get(
                                            "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed"
                                        )
                                        if r_embed:
                                            # Resolve the relationship to get the image path
                                            image_path = self._resolve_relationship(r_embed)
                                            if image_path:
                                                common_slide_data.background_image_path = image_path

        # Inherit background properties from layout if no slide-level background is found
        if (not common_slide_data.background_color and 
            not common_slide_data.background_gradient_fill and 
            not common_slide_data.background_reference and 
            not common_slide_data.background_image_path and 
            slide_layout_obj):
            
            # Inherit background properties from layout
            if slide_layout_obj.background_color:
                common_slide_data.background_color = slide_layout_obj.background_color
            elif slide_layout_obj.background_gradient_fill:
                common_slide_data.background_gradient_fill = slide_layout_obj.background_gradient_fill
            elif slide_layout_obj.background_reference:
                common_slide_data.background_reference = slide_layout_obj.background_reference

        return common_slide_data

    def _get_slide_layout_obj(self) -> SlideLayout | None:
        # If we have the presentation object with pre-parsed layouts, use those
        if self.presentation and self.presentation.slide_layouts:
            # Find the slide layout relationship
            for rel_id, target in self.rels.items():
                if "slideLayout" in target:
                    # Extract the layout filename from the target path
                    layout_filename = os.path.basename(target)
                    
                    # Look up the pre-parsed layout from the presentation object
                    if layout_filename in self.presentation.slide_layouts:
                        layout_obj = self.presentation.slide_layouts[layout_filename]
                        return layout_obj
                    break

        # Fallback to the original parsing logic if presentation object is not available
        slide_layout_relationship_id = None
        # Iterate through all relationships to find the one pointing to the slide layout
        for rel_id, target in self.rels.items():
            if "slideLayout" in target:
                slide_layout_relationship_id = rel_id
                break

        slide_layout_path = None
        # If a slide layout relationship ID is found
        if slide_layout_relationship_id:
            # Resolve the target path of the slide layout from the relationships
            slide_layout_target = self.rels.get(slide_layout_relationship_id)
            if slide_layout_target:
                # Construct the absolute path to the slide layout XML file
                # Example: ../slideLayouts/slideLayout1.xml -> temp_pptx/ppt/slideLayouts/slideLayout1.xml
                slide_layout_path = os.path.join(
                    self.pptx_unpacked_path,
                    slide_layout_target.lstrip("/").replace("../", ""),
                )

        slide_layout_object = None
        # If the slide layout XML file exists, parse it
        if slide_layout_path and os.path.exists(slide_layout_path):
            slide_layout_parser = LayoutParser(
                slide_layout_path, self.pptx_unpacked_path
            )
            slide_layout_object = slide_layout_parser.parse_layout()
        return slide_layout_object

    def _parse_slide_elements(self, slide_layout_obj: SlideLayout | None):
        # Find the root of the shape tree (p:spTree) in the slide XML
        shape_tree_root = self.root.find(".//p:spTree", namespaces=self.nsmap)
        # If spTree is not found, fallback to the root element itself
        if shape_tree_root is None:
            shape_tree_root = self.root
        # Parse the shape tree to extract all shapes, pictures, group shapes, and graphic frames
        return parse_shape_tree(self, shape_tree_root, slide_layout_obj, self.style_resolver)

    def _apply_inherited_transforms(self, shapes, pictures, slide_layout_object):
        # If a slide layout object exists, apply inherited transforms to placeholders
        if slide_layout_object:
            # Iterate through each placeholder defined in the slide layout
            for layout_placeholder in slide_layout_object.placeholders:
                found_element = None
                # Search for a matching shape on the slide
                for shape in shapes:
                    if shape.ph_type == layout_placeholder.ph_type and (
                        layout_placeholder.ph_idx is None
                        or shape.ph_idx == layout_placeholder.ph_idx
                    ):
                        found_element = shape
                        break
                # If no matching shape is found, search for a matching picture
                if not found_element:
                    for picture in pictures:
                        if picture.ph_type == layout_placeholder.ph_type and (
                            layout_placeholder.ph_idx is None
                            or picture.ph_idx == layout_placeholder.ph_idx
                        ):
                            found_element = picture
                            break

                # If a matching element is found and it doesn't have its own transform properties,
                # inherit the transform from the slide layout placeholder
                if found_element and not (
                    found_element.transform.x
                    or found_element.transform.y
                    or found_element.transform.cx
                    or found_element.transform.cy
                ):
                    found_element.transform = layout_placeholder.transform

    def parse_slide(self, slide_number: int) -> Slide:
        slide_layout_obj = self._get_slide_layout_obj()
        
        shapes, pictures, group_shapes, graphic_frames = self._parse_slide_elements(
            slide_layout_obj
        )
        self._apply_inherited_transforms(shapes, pictures, slide_layout_obj)

        return Slide(
            slide_number=slide_number,
            common_slide_data=self._extract_common_slide_data(slide_layout_obj),
            shapes=shapes,
            pictures=pictures,
            group_shapes=group_shapes,
            graphic_frames=graphic_frames,
            hyperlinks=self.extract_hyperlinks(),
            slide_layout=slide_layout_obj,
        )

    def extract_hyperlinks(self) -> list[Hyperlink]:
        # Initialize an empty list to store Hyperlink objects
        hyperlinks = []
        # Find all hyperlink click elements (a:hlinkClick) in the slide XML
        for hyperlink_click_element in self.root.findall(
            ".//a:hlinkClick", namespaces=self.nsmap
        ):
            # Extract the relationship ID (r:id) from the hyperlink click element
            r_id = hyperlink_click_element.get(
                "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id"
            )
            # If a relationship ID exists and is found in the slide's relationships
            if r_id and r_id in self.rels:
                # Create a new Hyperlink object with type "hyperlink" and the resolved target URL
                hyperlinks.append(Hyperlink(type="hyperlink", target=self.rels[r_id]))
        return hyperlinks
