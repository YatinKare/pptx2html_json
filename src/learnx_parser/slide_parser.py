from typing import List, Optional
import os
from lxml import etree
from learnx_parser.data_models import (
    CommonSlideData,
    Hyperlink,
    Slide,
    Shape,
    Picture,
    GroupShape,
    GraphicFrame,
    Transform,
    SolidFill,
    Line,
    BlipFill,
    GradientFill,
    GradientStop,
    TextFrame,
    Paragraph,
    ParagraphProperties,
    TextRun,
    RunProperties,
    SlideLayout
)
from learnx_parser.slide_layout_parser import SlideLayoutParser

class SlideParser:
    def __init__(self, slide_xml_path, slide_rels_path, pptx_unpacked_path, slide_width, slide_height):
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

    def _parse_rels(self):
        # Initialize an empty dictionary to store relationships
        relationships = {}
        # Check if the slide's relationship file path exists
        if self.slide_rels_path and os.path.exists(self.slide_rels_path):
            # Parse the relationships XML tree
            relationships_tree = etree.parse(self.slide_rels_path)
            # Iterate through each Relationship element in the relationships XML
            for relationship in relationships_tree.findall("{http://schemas.openxmlformats.org/package/2006/relationships}Relationship"):
                # Store the relationship ID and its target (e.g., media file path, slide layout path)
                relationships[relationship.get("Id")] = relationship.get("Target")
        return relationships

    def _extract_common_slide_data(self) -> CommonSlideData:
        # Initialize CommonSlideData with slide width and height
        common_slide_data = CommonSlideData(cx=self.slide_width, cy=self.slide_height)

        # Find the common slide data element (p:cSld) in the XML
        common_slide_element = self.root.find(".//p:cSld", namespaces=self.nsmap)
        if common_slide_element is not None:
            # Find the background element (p:bg)
            background_element = common_slide_element.find(".//p:bg", namespaces=self.nsmap)
            if background_element is not None:
                # Find the background properties element (p:bgPr)
                background_properties_element = background_element.find(".//p:bgPr", namespaces=self.nsmap)
                if background_properties_element is not None:
                    # Check for solid fill background
                    solid_fill_element = background_properties_element.find(".//a:solidFill", namespaces=self.nsmap)
                    if solid_fill_element is not None:
                        # Extract SRGB color value if present
                        srgb_color_element = solid_fill_element.find(".//a:srgbClr", namespaces=self.nsmap)
                        if srgb_color_element is not None:
                            common_slide_data.background_color = srgb_color_element.get("val")
                    else:
                        # Check for gradient fill background
                        gradient_fill_element = background_properties_element.find(".//a:gradFill", namespaces=self.nsmap)
                        if gradient_fill_element is not None:
                            gradient_fill = GradientFill()
                            # Extract linear gradient properties (angle, scaled)
                            linear_element = gradient_fill_element.find(".//a:lin", namespaces=self.nsmap)
                            if linear_element is not None:
                                gradient_fill.angle = int(linear_element.get("ang", 0)) if linear_element.get("ang") is not None else None
                                gradient_fill.scaled = linear_element.get("scaled", "0") == "1"
                            
                            # Extract gradient stop list
                            gradient_stop_list_element = gradient_fill_element.find(".//a:gsLst", namespaces=self.nsmap)
                            if gradient_stop_list_element is not None:
                                # Iterate through each gradient stop
                                for gradient_stop_element in gradient_stop_list_element.findall(".//a:gs", namespaces=self.nsmap):
                                    position = int(gradient_stop_element.get("pos", 0))
                                    stop_color = None
                                    stop_scheme_color = None
                                    # Extract SRGB color for the stop
                                    srgb_color_element = gradient_stop_element.find(".//a:srgbClr", namespaces=self.nsmap)
                                    if srgb_color_element is not None:
                                        stop_color = srgb_color_element.get("val")
                                    else:
                                        # Extract scheme color for the stop
                                        scheme_color_element = gradient_stop_element.find(".//a:schemeClr", namespaces=self.nsmap)
                                        if scheme_color_element is not None:
                                            stop_scheme_color = scheme_color_element.get("val")
                                    # Append the gradient stop to the list
                                    gradient_fill.stops.append(GradientStop(pos=position, color=stop_color, scheme_color=stop_scheme_color))
                            common_slide_data.background_gradient_fill = gradient_fill

        return common_slide_data

    def _extract_transform(self, element_root) -> Transform:
        # Initialize a Transform object with default values
        transform = Transform()
        # Find the shape properties element (p:spPr) which contains transform information for shapes
        shape_properties_element = element_root.find(".//p:spPr", namespaces=self.nsmap)
        transform_element = None

        # Determine where the transform element (a:xfrm) is located based on the element type
        if shape_properties_element is not None:
            transform_element = shape_properties_element.find(".//a:xfrm", namespaces=self.nsmap)
        # For graphic frames, the transform element is directly under the graphicFrame element
        elif element_root.tag == "{http://schemas.openxmlformats.org/presentationml/2006/main}graphicFrame":
            transform_element = element_root.find(".//a:xfrm", namespaces=self.nsmap)

        # If a transform element is found, extract its properties
        if transform_element is not None:
            # Extract offset (x, y position) information
            offset_element = transform_element.find(".//a:off", namespaces=self.nsmap)
            # Extract extent (width, height) information
            extent_element = transform_element.find(".//a:ext", namespaces=self.nsmap)
            if offset_element is not None:
                transform.x = int(offset_element.get("x", 0))
                transform.y = int(offset_element.get("y", 0))
            if extent_element is not None:
                transform.cx = int(extent_element.get("cx", 0))
                transform.cy = int(extent_element.get("cy", 0))

            # Extract rotation, horizontal flip, and vertical flip properties
            transform.rot = int(transform_element.get("rot", 0)) if transform_element.get("rot") is not None else 0
            transform.flipH = transform_element.get("flipH", "0") == "1"
            transform.flipV = transform_element.get("flipV", "0") == "1"
        
        return transform

    def _extract_fill_properties(self, shape_properties_element):
        # Initialize fill to None
        fill = None
        # Find solid fill element (a:solidFill)
        solid_fill_element = shape_properties_element.find(".//a:solidFill", namespaces=self.nsmap)
        if solid_fill_element is not None:
            # If solid fill is found, create a SolidFill object
            fill = SolidFill()
            # Extract SRGB color value
            srgb_color_element = solid_fill_element.find(".//a:srgbClr", namespaces=self.nsmap)
            if srgb_color_element is not None:
                fill.color = srgb_color_element.get("val")
            else:
                # Extract scheme color value if SRGB color is not present
                scheme_color_element = solid_fill_element.find(".//a:schemeClr", namespaces=self.nsmap)
                if scheme_color_element is not None:
                    fill.scheme_color = scheme_color_element.get("val")
        else:
            # If no solid fill, check for gradient fill
            gradient_fill_element = shape_properties_element.find(".//a:gradFill", namespaces=self.nsmap)
            if gradient_fill_element is not None:
                # If gradient fill is found, create a GradientFill object
                gradient_fill = GradientFill()
                # Extract linear gradient properties (angle, scaled)
                linear_element = gradient_fill_element.find(".//a:lin", namespaces=self.nsmap)
                if linear_element is not None:
                    gradient_fill.angle = int(linear_element.get("ang", 0)) if linear_element.get("ang") is not None else None
                    gradient_fill.scaled = linear_element.get("scaled", "0") == "1"
                
                # Extract gradient stop list
                gradient_stop_list_element = gradient_fill_element.find(".//a:gsLst", namespaces=self.nsmap)
                if gradient_stop_list_element is not None:
                    # Iterate through each gradient stop
                    for gradient_stop_element in gradient_stop_list_element.findall(".//a:gs", namespaces=self.nsmap):
                        position = int(gradient_stop_element.get("pos", 0))
                        stop_color = None
                        stop_scheme_color = None
                        # Extract SRGB color for the stop
                        srgb_color_element = gradient_stop_element.find(".//a:srgbClr", namespaces=self.nsmap)
                        if srgb_color_element is not None:
                            stop_color = srgb_color_element.get("val")
                        else:
                            # Extract scheme color for the stop
                            scheme_color_element = gradient_stop_element.find(".//a:schemeClr", namespaces=self.nsmap)
                            if scheme_color_element is not None:
                                stop_scheme_color = scheme_color_element.get("val")
                        # Append the gradient stop to the list
                        gradient_fill.stops.append(GradientStop(pos=position, color=stop_color, scheme_color=stop_scheme_color))
                fill = gradient_fill
        return fill

    def _extract_line_properties(self, shape_properties_element):
        # Initialize line to None
        line = None
        # Find the line element (a:ln) within the shape properties
        line_element = shape_properties_element.find(".//a:ln", namespaces=self.nsmap)
        if line_element is not None:
            # If a line element is found, create a Line object
            line = Line()
            # Extract line width, cap type, compound type, and alignment
            line.width = int(line_element.get("w", 0))
            line.cap = line_element.get("cap")
            line.cmpd = line_element.get("cmpd")
            line.algn = line_element.get("algn")

            # Extract solid fill properties for the line (color)
            solid_fill_element = line_element.find(".//a:solidFill", namespaces=self.nsmap)
            if solid_fill_element is not None:
                # Extract SRGB color value
                srgb_color_element = solid_fill_element.find(".//a:srgbClr", namespaces=self.nsmap)
                if srgb_color_element is not None:
                    line.color = srgb_color_element.get("val")
                else:
                    # Extract scheme color value if SRGB color is not present
                    scheme_color_element = solid_fill_element.find(".//a:schemeClr", namespaces=self.nsmap)
                    if scheme_color_element is not None:
                        line.scheme_color = scheme_color_element.get("val")
        return line

    def _extract_text_frame_properties(self, shape_element) -> TextFrame:
        # Initialize an empty TextFrame object to store parsed text data
        text_frame = TextFrame()
        # Iterate through all paragraph elements (a:p) within the shape
        for paragraph_element in shape_element.findall(".//a:p", namespaces=self.nsmap):
            # Extract properties for the current paragraph
            paragraph_object = self._extract_paragraph_properties(paragraph_element)
            # Only add the paragraph to the text frame if it contains actual text runs
            if paragraph_object.text_runs: 
                text_frame.paragraphs.append(paragraph_object)
        return text_frame

    def _extract_paragraph_properties(self, paragraph_element) -> Paragraph:
        # Initialize a Paragraph object to store parsed paragraph data
        paragraph_object = Paragraph()
        
        # Extract paragraph properties (e.g., alignment, indentation)
        paragraph_properties_element = paragraph_element.find(".//a:pPr", namespaces=self.nsmap)
        if paragraph_properties_element is not None:
            if paragraph_properties_element.get("algn") is not None:
                paragraph_object.properties.align = paragraph_properties_element.get("algn")
            if paragraph_properties_element.get("indent") is not None:
                paragraph_object.properties.indent = int(paragraph_properties_element.get("indent"))

        # Iterate through all run elements (a:r) within the paragraph
        for run_element in paragraph_element.findall(".//a:r", namespaces=self.nsmap):
            # Find the text element (a:t) within the run
            run_text_element = run_element.find(".//a:t", namespaces=self.nsmap)
            # If text content exists, extract it and its properties
            if run_text_element is not None and run_text_element.text is not None:
                text_content = run_text_element.text
                run_properties = self._extract_run_properties(run_element)
                # Append a new TextRun object to the paragraph's text runs
                paragraph_object.text_runs.append(TextRun(text=text_content, properties=run_properties))
        return paragraph_object

    def _extract_run_properties(self, run_element) -> RunProperties:
        # Initialize a RunProperties object to store parsed run properties
        run_properties = RunProperties()
        # Find the run properties element (a:rPr)
        run_properties_element = run_element.find(".//a:rPr", namespaces=self.nsmap)
        if run_properties_element is not None:
            # Extract font size
            if run_properties_element.get("sz") is not None:
                run_properties.font_size = int(run_properties_element.get("sz"))
            # Extract bold property
            if run_properties_element.get("b") == "1":
                run_properties.bold = True
            # Extract italic property
            if run_properties_element.get("i") == "1":
                run_properties.italic = True
            
            # Extract color
            solid_fill_element = run_properties_element.find(".//a:solidFill", namespaces=self.nsmap)
            if solid_fill_element is not None:
                srgb_color_element = solid_fill_element.find(".//a:srgbClr", namespaces=self.nsmap)
                if srgb_color_element is not None:
                    run_properties.color = srgb_color_element.get("val")
                else:
                    scheme_color_element = solid_fill_element.find(".//a:schemeClr", namespaces=self.nsmap)
                    if scheme_color_element is not None:
                        run_properties.scheme_color = scheme_color_element.get("val")

            # Extract font face
            latin_font_element = run_properties_element.find(".//a:latin", namespaces=self.nsmap)
            if latin_font_element is not None:
                run_properties.font_face = latin_font_element.get("typeface")

            # Extract underline
            underline_element = run_properties_element.find(".//a:u", namespaces=self.nsmap)
            if underline_element is not None:
                run_properties.underline = True
        return run_properties

    def _parse_shape_element(self, shape_element) -> Shape:
        # Extract the shape's ID and name from its properties
        shape_id = shape_element.find(".//p:cNvPr", namespaces=self.nsmap).get("id")
        shape_name = shape_element.find(".//p:cNvPr", namespaces=self.nsmap).get("name")
        
        # Extract placeholder information if the shape is a placeholder
        placeholder_element = shape_element.find(".//p:nvPr/p:ph", namespaces=self.nsmap)
        ph_type = placeholder_element.get("type") if placeholder_element is not None else None
        ph_idx = int(placeholder_element.get("idx")) if placeholder_element is not None and placeholder_element.get("idx") is not None else None
        ph_orient = placeholder_element.get("orient") if placeholder_element is not None else None
        ph_sz = placeholder_element.get("sz") if placeholder_element is not None else None

        # Extract the transform properties (position, size, rotation, flip) of the shape
        transform = self._extract_transform(shape_element)
        fill = None
        line = None
        text_frame = TextFrame()
        preset_geometry_value = None

        # Find the shape properties element (p:spPr) which contains fill, line, and geometry information
        shape_properties_element = shape_element.find(".//p:spPr", namespaces=self.nsmap)
        if shape_properties_element is not None:
            # Extract geometry information (e.g., rectangle, oval, custom shape)
            preset_geometry = shape_properties_element.find(".//a:prstGeom", namespaces=self.nsmap)
            if preset_geometry is not None:
                preset_geometry_value = preset_geometry.get("prst")

            # Extract fill properties (solid color, gradient, etc.)
            fill = self._extract_fill_properties(shape_properties_element)

            # Extract line properties (border, outline)
            line = self._extract_line_properties(shape_properties_element)

        # Extract text frame properties if the shape contains text
        text_frame = self._extract_text_frame_properties(shape_element)

        # Return a new Shape object populated with the extracted data
        return Shape(type="shape", id=shape_id, name=shape_name, transform=transform, prst_geom=preset_geometry_value, fill=fill, line=line, text_frame=text_frame, ph_type=ph_type, ph_idx=ph_idx, ph_orient=ph_orient, ph_sz=ph_sz)

    def _parse_picture_element(self, picture_element) -> Picture:
        # Extract the picture's ID and name from its properties
        picture_id = picture_element.find(".//p:nvPicPr/p:cNvPr", namespaces=self.nsmap).get("id")
        picture_name = picture_element.find(".//p:nvPicPr/p:cNvPr", namespaces=self.nsmap).get("name")
        picture_path = ""

        # Extract placeholder information for pictures if it's a placeholder
        placeholder_element = picture_element.find(".//p:nvPicPr/p:nvPr/p:ph", namespaces=self.nsmap)
        ph_type = placeholder_element.get("type") if placeholder_element is not None else None
        ph_idx = int(placeholder_element.get("idx")) if placeholder_element is not None and placeholder_element.get("idx") is not None else None

        # Extract the transform properties (position, size, rotation, flip) of the picture
        transform = self._extract_transform(picture_element)

        # Find the blip element (a:blip) which contains the relationship ID to the image file
        blip_element = picture_element.find(".//a:blip", namespaces=self.nsmap)
        if blip_element is not None:
            embed_id = blip_element.get("{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed")
            # Resolve the image path using the relationship ID
            if embed_id in self.rels:
                picture_path = self.rels[embed_id]

        # Find the blip fill element (p:blipFill) which contains image fill properties like cropping
        blip_fill_element = picture_element.find(".//p:blipFill", namespaces=self.nsmap)
        blip_fill_object = None
        if blip_fill_element is not None:
            # Extract whether the image rotates with the shape
            rotate_with_shape = blip_fill_element.get("rotWithShape", "0") == "1"
            blip_fill_object = BlipFill(path=picture_path, rot_with_shape=rotate_with_shape)

            # Extract source rectangle (cropping) information
            source_rectangle_element = blip_fill_element.find(".//a:srcRect", namespaces=self.nsmap)
            if source_rectangle_element is not None:
                blip_fill_object.src_rect_t = int(source_rectangle_element.get("t")) if source_rectangle_element.get("t") is not None else None
                blip_fill_object.src_rect_b = int(source_rectangle_element.get("b")) if source_rectangle_element.get("b") is not None else None
                blip_fill_object.src_rect_l = int(source_rectangle_element.get("l")) if source_rectangle_element.get("l") is not None else None
                blip_fill_object.src_rect_r = int(source_rectangle_element.get("r")) if source_rectangle_element.get("r") is not None else None

        # Return a new Picture object populated with the extracted data
        return Picture(id=picture_id, name=picture_name, path=picture_path, transform=transform, blip_fill=blip_fill_object, ph_type=ph_type, ph_idx=ph_idx)

    def _parse_group_shape_element(self, group_shape_element) -> GroupShape:
        # Extract the group shape's ID and name
        group_id = group_shape_element.find(".//p:nvGrpSpPr/p:cNvPr", namespaces=self.nsmap).get("id")
        group_name = group_shape_element.find(".//p:nvGrpSpPr/p:cNvPr", namespaces=self.nsmap).get("name")
        
        # Determine if the group shape is a flex container based on its name
        is_flex_container = False
        if group_name and "flex-container" in group_name:
            is_flex_container = True

        # Extract the transform properties of the group shape
        transform = self._extract_transform(group_shape_element)
        # Recursively parse child shapes within the group shape
        shapes, pictures, group_shapes, graphic_frames = self._parse_shape_tree(group_shape_element)
        # Return a new GroupShape object populated with the extracted data and its children
        return GroupShape(id=group_id, name=group_name, transform=transform, children=(shapes, pictures, group_shapes, graphic_frames), is_flex_container=is_flex_container)

    def _parse_graphic_frame_element(self, graphic_frame_element) -> GraphicFrame:
        # Extract the graphic frame's ID and name
        graphic_frame_id = graphic_frame_element.find(".//p:nvGraphicFramePr/p:cNvPr", namespaces=self.nsmap).get("id")
        graphic_frame_name = graphic_frame_element.find(".//p:nvGraphicFramePr/p:cNvPr", namespaces=self.nsmap).get("name")
        
        # Extract the transform properties of the graphic frame
        transform = self._extract_transform(graphic_frame_element)
        # Return a new GraphicFrame object populated with the extracted data
        return GraphicFrame(id=graphic_frame_id, name=graphic_frame_name, transform=transform)

    def _parse_shape_tree(self, shape_tree_root):
        # Initialize lists to store different types of elements found in the shape tree
        shapes = []
        pictures = []
        group_shapes = []
        graphic_frames = []

        # Iterate through each child element within the shape tree root
        for child_element in shape_tree_root:
            # Check the tag of the child element to determine its type and parse accordingly
            if child_element.tag == "{http://schemas.openxmlformats.org/presentationml/2006/main}sp":
                # Parse a regular shape element
                shape = self._parse_shape_element(child_element)
                shapes.append(shape)

            elif child_element.tag == "{http://schemas.openxmlformats.org/presentationml/2006/main}pic":
                # Parse a picture element
                picture = self._parse_picture_element(child_element)
                pictures.append(picture)

            elif child_element.tag == "{http://schemas.openxmlformats.org/presentationml/2006/main}grpSp":
                # Parse a group shape element (which can contain other shapes)
                group_shape = self._parse_group_shape_element(child_element)
                group_shapes.append(group_shape)

            elif child_element.tag == "{http://schemas.openxmlformats.org/presentationml/2006/main}graphicFrame":
                # Parse a graphic frame element (e.g., charts, tables)
                graphic_frame = self._parse_graphic_frame_element(child_element)
                graphic_frames.append(graphic_frame)
        # Return the categorized lists of parsed elements
        return shapes, pictures, group_shapes, graphic_frames

    

    def extract_hyperlinks(self) -> List[Hyperlink]:
        # Initialize an empty list to store Hyperlink objects
        hyperlinks = []
        # Find all hyperlink click elements (a:hlinkClick) in the slide XML
        for hyperlink_click_element in self.root.findall(".//a:hlinkClick", namespaces=self.nsmap):
            # Extract the relationship ID (r:id) from the hyperlink click element
            r_id = hyperlink_click_element.get("{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id")
            # If a relationship ID exists and is found in the slide's relationships
            if r_id and r_id in self.rels:
                # Create a new Hyperlink object with type "hyperlink" and the resolved target URL
                hyperlinks.append(Hyperlink(type="hyperlink", target=self.rels[r_id]))
        return hyperlinks

    def _get_slide_layout_obj(self) -> Optional[SlideLayout]:
        # Initialize slide layout relationship ID to None
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
                slide_layout_path = os.path.join(self.pptx_unpacked_path, slide_layout_target.lstrip("/").replace("../", ""))

        slide_layout_object = None
        # If the slide layout XML file exists, parse it
        if slide_layout_path and os.path.exists(slide_layout_path):
            slide_layout_parser = SlideLayoutParser(slide_layout_path)
            slide_layout_object = slide_layout_parser.parse_layout()
        return slide_layout_object

    def _parse_slide_elements(self):
        # Find the root of the shape tree (p:spTree) in the slide XML
        shape_tree_root = self.root.find(".//p:spTree", namespaces=self.nsmap)
        # If spTree is not found, fallback to the root element itself
        if shape_tree_root is None:
            shape_tree_root = self.root
        # Parse the shape tree to extract all shapes, pictures, group shapes, and graphic frames
        return self._parse_shape_tree(shape_tree_root)

    def _apply_inherited_transforms(self, shapes, pictures, slide_layout_object):
        # If a slide layout object exists, apply inherited transforms to placeholders
        if slide_layout_object:
            # Iterate through each placeholder defined in the slide layout
            for layout_placeholder in slide_layout_object.placeholders:
                found_element = None
                # Search for a matching shape on the slide
                for shape in shapes:
                    if shape.ph_type == layout_placeholder.ph_type and (layout_placeholder.ph_idx is None or shape.ph_idx == layout_placeholder.ph_idx):
                        found_element = shape
                        break
                # If no matching shape is found, search for a matching picture
                if not found_element:
                    for picture in pictures:
                        if picture.ph_type == layout_placeholder.ph_type and (layout_placeholder.ph_idx is None or picture.ph_idx == layout_placeholder.ph_idx):
                            found_element = picture
                            break
                
                # If a matching element is found and it doesn't have its own transform properties,
                # inherit the transform from the slide layout placeholder
                if found_element and not (found_element.transform.x or found_element.transform.y or found_element.transform.cx or found_element.transform.cy):
                    found_element.transform = layout_placeholder.transform

    def parse_slide(self, slide_number: int) -> Slide:
        slide_layout_obj = self._get_slide_layout_obj()
        shapes, pictures, group_shapes, graphic_frames = self._parse_slide_elements()
        self._apply_inherited_transforms(shapes, pictures, slide_layout_obj)

        return Slide(
            slide_number=slide_number,
            common_slide_data=self._extract_common_slide_data(),
            shapes=shapes,
            pictures=pictures,
            group_shapes=group_shapes,
            graphic_frames=graphic_frames,
            hyperlinks=self.extract_hyperlinks(),
            slide_layout=slide_layout_obj
        )