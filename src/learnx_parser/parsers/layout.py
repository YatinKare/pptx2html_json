import os

from lxml import etree

from learnx_parser.models.core import (
    BackgroundReference,
    GradientFill,
    GradientStop,
    LayoutPlaceholder,
    ParagraphProperties,
    RunProperties,
    SlideLayout,
    SlideMaster,
    Transform,
)
from learnx_parser.parsers.master import SlideMasterParser


class LayoutParser:
    def __init__(self, layout_xml_path, pptx_unpacked_path=None):
        self.layout_xml_path = layout_xml_path
        self.pptx_unpacked_path = pptx_unpacked_path
        self.tree = etree.parse(self.layout_xml_path)
        self.root = self.tree.getroot()
        self.nsmap = self.root.nsmap
        self.rels = self._parse_rels()  # Parse relationships for the layout file

    def _parse_rels(self):
        relationships = {}
        layout_rels_path = os.path.join(
            os.path.dirname(self.layout_xml_path),
            "_rels",
            os.path.basename(self.layout_xml_path) + ".rels",
        )
        if os.path.exists(layout_rels_path):
            relationships_tree = etree.parse(layout_rels_path)
            for relationship in relationships_tree.findall(
                "{http://schemas.openxmlformats.org/package/2006/relationships}Relationship"
            ):
                relationships[relationship.get("Id")] = relationship.get("Target")
        return relationships

    def _extract_transform(self, element_root) -> Transform:
        transform = Transform(x=0, y=0, cx=914400, cy=914400)  # Default values
        # Look for spPr for shapes and pictures, or directly for graphicFrame
        sp_pr = element_root.find(".//p:spPr", namespaces=self.nsmap)
        xfrm = None

        if sp_pr is not None:
            xfrm = sp_pr.find(".//a:xfrm", namespaces=self.nsmap)
        elif (
            element_root.tag
            == "{http://schemas.openxmlformats.org/presentationml/2006/main}graphicFrame"
        ):
            # For graphicFrame, xfrm is directly under the graphicFrame element
            xfrm = element_root.find(".//a:xfrm", namespaces=self.nsmap)

        if xfrm is not None:
            off = xfrm.find(".//a:off", namespaces=self.nsmap)
            ext = xfrm.find(".//a:ext", namespaces=self.nsmap)
            if off is not None:
                transform.x = int(off.get("x", 0))
                transform.y = int(off.get("y", 0))
            if ext is not None:
                cx_val = int(ext.get("cx", 0))
                cy_val = int(ext.get("cy", 0))
                if cx_val != 0:
                    transform.cx = cx_val
                if cy_val != 0:
                    transform.cy = cy_val
            transform.rot = (
                int(xfrm.get("rot", 0)) if xfrm.get("rot") is not None else 0
            )
            transform.flipH = xfrm.get("flipH", "0") == "1"
            transform.flipV = xfrm.get("flipV", "0") == "1"
        return transform

    def _parse_placeholders(self) -> list[LayoutPlaceholder]:
        placeholders = []
        # Search for all shapes and pictures that are placeholders
        for sp_elem in self.root.findall(".//p:sp", namespaces=self.nsmap):
            ph_elem = sp_elem.find(".//p:nvPr/p:ph", namespaces=self.nsmap)
            if ph_elem is not None:
                ph_type = ph_elem.get("type")
                ph_idx = (
                    int(ph_elem.get("idx")) if ph_elem.get("idx") is not None else None
                )
                transform = self._extract_transform(sp_elem)

                # Extract text frame properties from layout XML
                anchor, anchor_ctr, insets = self._extract_bodypr_properties(sp_elem)
                paragraph_align = self._extract_paragraph_align_from_layout(
                    sp_elem, ph_type
                )

                placeholders.append(
                    LayoutPlaceholder(
                        ph_type=ph_type,
                        ph_idx=ph_idx,
                        transform=transform,
                        anchor=anchor,
                        anchor_ctr=anchor_ctr,
                        left_inset=insets.get("lIns"),
                        top_inset=insets.get("tIns"),
                        right_inset=insets.get("rIns"),
                        bottom_inset=insets.get("bIns"),
                        paragraph_align=paragraph_align,
                    )
                )

        for pic_elem in self.root.findall(".//p:pic", namespaces=self.nsmap):
            ph_elem = pic_elem.find(".//p:nvPicPr/p:nvPr/p:ph", namespaces=self.nsmap)
            if ph_elem is not None:
                ph_type = ph_elem.get("type")
                ph_idx = (
                    int(ph_elem.get("idx")) if ph_elem.get("idx") is not None else None
                )
                transform = self._extract_transform(pic_elem)
                placeholders.append(
                    LayoutPlaceholder(
                        ph_type=ph_type, ph_idx=ph_idx, transform=transform
                    )
                )

        return placeholders

    def _infer_layout_type(self, placeholders: list[LayoutPlaceholder]) -> str | None:
        ph_types = {ph.ph_type for ph in placeholders if ph.ph_type is not None}

        has_title = "title" in ph_types or "ctrTitle" in ph_types
        has_body = "body" in ph_types or (
            None in ph_types
            and any(ph.ph_idx == 1 for ph in placeholders if ph.ph_type is None)
        )
        has_pic = "pic" in ph_types
        has_subtitle = "subTitle" in ph_types

        # Check for specific combinations of placeholders
        if has_title and has_body and has_pic:
            return "picTx"  # Title, Picture and Text
        elif has_title and has_body:
            return "tx"  # Title and Text
        elif has_title and has_pic and not has_body:
            return "titlePic"  # Title and Picture (no body)
        elif has_title and has_subtitle:
            return "title"  # Title and Subtitle
        elif has_title and not has_body and not has_pic and not has_subtitle:
            return "titleOnly"  # Only a title
        elif not ph_types:
            return "blank"  # No placeholders

        # Fallback for layouts that might have a title and picture, but the body is not explicitly marked as 'body'
        if (
            has_title
            and has_pic
            and (
                None in ph_types
                and any(ph.ph_idx == 1 for ph in placeholders if ph.ph_type is None)
            )
        ):
            return "titlePic"  # Title and Picture with a generic body placeholder

        # Add more heuristics for other common layouts as needed
        return None

    def _extract_list_styles(self) -> dict[int, ParagraphProperties]:
        list_styles = {}
        list_style_element = self.root.find(".//a:lstStyle", namespaces=self.nsmap)
        if list_style_element is not None:
            for i in range(9):  # Levels 0 to 8
                lvl_p_pr_element = list_style_element.find(
                    f".//a:lvl{i}pPr", namespaces=self.nsmap
                )
                if lvl_p_pr_element is not None:
                    props = ParagraphProperties()
                    # Extract common paragraph properties
                    if lvl_p_pr_element.get("algn") is not None:
                        props.align = lvl_p_pr_element.get("algn")
                    if lvl_p_pr_element.get("indent") is not None:
                        props.indent = int(lvl_p_pr_element.get("indent"))
                    props.level = i

                    # Extract bullet properties
                    bu_none_element = lvl_p_pr_element.find(
                        ".//a:buNone", namespaces=self.nsmap
                    )
                    bu_char_element = lvl_p_pr_element.find(
                        ".//a:buChar", namespaces=self.nsmap
                    )
                    bu_auto_num_element = lvl_p_pr_element.find(
                        ".//a:buAutoNum", namespaces=self.nsmap
                    )
                    bu_blip_element = lvl_p_pr_element.find(
                        ".//a:buBlip", namespaces=self.nsmap
                    )

                    if bu_none_element is not None:
                        props.bullet_type = "none"
                    elif bu_char_element is not None:
                        props.bullet_type = "char"
                        props.bullet_char = bu_char_element.get("char")
                        bu_font_element = lvl_p_pr_element.find(
                            ".//a:buFont", namespaces=self.nsmap
                        )
                        if bu_font_element is not None:
                            props.bullet_font_face = bu_font_element.get("typeface")
                        bu_sz_pct_element = lvl_p_pr_element.find(
                            ".//a:buSzPct", namespaces=self.nsmap
                        )
                        if bu_sz_pct_element is not None:
                            props.bullet_size_pct = int(bu_sz_pct_element.get("val"))
                        bu_sz_pts_element = lvl_p_pr_element.find(
                            ".//a:buSzPts", namespaces=self.nsmap
                        )
                        if bu_sz_pts_element is not None:
                            props.bullet_size_pts = int(bu_sz_pts_element.get("val"))
                    elif bu_auto_num_element is not None:
                        props.bullet_type = "autoNum"
                        props.bullet_auto_num_type = bu_auto_num_element.get("type")
                        if bu_auto_num_element.get("startAt") is not None:
                            props.bullet_start_at = int(
                                bu_auto_num_element.get("startAt")
                            )
                    elif bu_blip_element is not None:
                        props.bullet_type = "blip"
                        embed_id = bu_blip_element.find(
                            ".//a:blip", namespaces=self.nsmap
                        ).get(
                            "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed"
                        )
                        if (
                            embed_id
                            and embed_id in self.rels
                            and self.pptx_unpacked_path
                        ):
                            # Resolve the image path using the layout's relationships and the unpacked path
                            relative_path = self.rels[embed_id]
                            # Construct absolute path, assuming relative_path is like ../media/image1.png
                            abs_path = os.path.normpath(
                                os.path.join(
                                    self.pptx_unpacked_path,
                                    relative_path.lstrip("/").replace("../", ""),
                                )
                            )
                            props.bullet_image_path = abs_path

                    # Parse default run properties (defRPr) for font size inheritance
                    def_rpr_element = lvl_p_pr_element.find(
                        ".//a:defRPr", namespaces=self.nsmap
                    )
                    if def_rpr_element is not None:
                        props.default_run_properties = (
                            self._parse_default_run_properties(def_rpr_element)
                        )

                    list_styles[i] = props
        return list_styles

    def _extract_bodypr_properties(self, sp_elem):
        """Extract bodyPr anchor and inset properties from shape element."""
        anchor = None
        anchor_ctr = False
        insets = {}

        # Look for bodyPr element in the shape's text body
        body_pr_elem = sp_elem.find(".//a:bodyPr", namespaces=self.nsmap)
        if body_pr_elem is not None:
            anchor = body_pr_elem.get("anchor")
            anchor_ctr = body_pr_elem.get("anchorCtr", "0") == "1"

            # Extract insets
            for inset_attr in ["lIns", "tIns", "rIns", "bIns"]:
                inset_value = body_pr_elem.get(inset_attr)
                if inset_value is not None:
                    insets[inset_attr] = int(inset_value)

        return anchor, anchor_ctr, insets

    def _extract_paragraph_align_from_layout(self, sp_elem, ph_type):
        """Extract paragraph alignment from layout's lstStyle for this placeholder type."""
        # Look for lstStyle in the shape's text body
        lst_style_elem = sp_elem.find(".//a:lstStyle", namespaces=self.nsmap)
        if lst_style_elem is not None:
            # Get level 0 paragraph properties (most common)
            lvl0_elem = lst_style_elem.find(".//a:lvl1pPr", namespaces=self.nsmap)
            if lvl0_elem is not None:
                return lvl0_elem.get("algn")

        return None

    def _parse_default_run_properties(self, def_rpr_element) -> RunProperties:
        """Parse default run properties (defRPr) from a level element.

        This extracts font size and other run properties for the inheritance hierarchy.

        Args:
            def_rpr_element: XML element containing default run properties

        Returns:
            RunProperties: Parsed run properties with font size and other attributes
        """
        run_props = RunProperties()

        # Parse font size (sz attribute) - most important for hierarchy
        if def_rpr_element.get("sz") is not None:
            run_props.font_size = int(def_rpr_element.get("sz"))

        # Parse other run properties that can be inherited
        if def_rpr_element.get("b") == "1":
            run_props.bold = True

        if def_rpr_element.get("i") == "1":
            run_props.italic = True

        if def_rpr_element.get("cap") is not None:
            run_props.cap = def_rpr_element.get("cap")

        # Parse font face (explicit font)
        latin_font_element = def_rpr_element.find(".//a:latin", namespaces=self.nsmap)
        if latin_font_element is not None:
            run_props.font_face = latin_font_element.get("typeface")

        # Parse font reference (theme-based font)
        font_ref_element = def_rpr_element.find(".//a:fontRef", namespaces=self.nsmap)
        if font_ref_element is not None:
            run_props.font_ref = font_ref_element.get("idx")  # "major" or "minor"

        # Parse color
        solid_fill_element = def_rpr_element.find(
            ".//a:solidFill", namespaces=self.nsmap
        )
        if solid_fill_element is not None:
            srgb_color_element = solid_fill_element.find(
                ".//a:srgbClr", namespaces=self.nsmap
            )
            if srgb_color_element is not None:
                run_props.color = srgb_color_element.get("val")
            else:
                scheme_color_element = solid_fill_element.find(
                    ".//a:schemeClr", namespaces=self.nsmap
                )
                if scheme_color_element is not None:
                    run_props.scheme_color = scheme_color_element.get("val")

        return run_props

    def _extract_background_properties(self) -> tuple[str | None, GradientFill | None, BackgroundReference | None]:
        """Extract background properties from layout XML.
        
        Returns:
            Tuple of (background_color, background_gradient_fill, background_reference)
        """
        background_color = None
        background_gradient_fill = None
        background_reference = None
        
        # Look for background element in common slide data
        cSld_element = self.root.find(".//p:cSld", namespaces=self.nsmap)
        if cSld_element is not None:
            background_element = cSld_element.find(".//p:bg", namespaces=self.nsmap)
            if background_element is not None:
                # Check for background properties (p:bgPr)
                background_properties_element = background_element.find(".//p:bgPr", namespaces=self.nsmap)
                if background_properties_element is not None:
                    # Extract solid fill
                    solid_fill_element = background_properties_element.find(".//a:solidFill", namespaces=self.nsmap)
                    if solid_fill_element is not None:
                        srgb_color_element = solid_fill_element.find(".//a:srgbClr", namespaces=self.nsmap)
                        if srgb_color_element is not None:
                            background_color = srgb_color_element.get("val")
                    
                    # Extract gradient fill
                    gradient_fill_element = background_properties_element.find(".//a:gradFill", namespaces=self.nsmap)
                    if gradient_fill_element is not None:
                        gradient_stops = []
                        for gs_element in gradient_fill_element.findall(".//a:gs", namespaces=self.nsmap):
                            pos = int(gs_element.get("pos", "0"))
                            
                            # Extract color from gradient stop
                            color = None
                            scheme_color = None
                            srgb_color_element = gs_element.find(".//a:srgbClr", namespaces=self.nsmap)
                            if srgb_color_element is not None:
                                color = srgb_color_element.get("val")
                            else:
                                scheme_color_element = gs_element.find(".//a:schemeClr", namespaces=self.nsmap)
                                if scheme_color_element is not None:
                                    scheme_color = scheme_color_element.get("val")
                            
                            gradient_stops.append(GradientStop(pos=pos, color=color, scheme_color=scheme_color))
                        
                        if gradient_stops:
                            # Extract gradient direction/angle
                            angle = None
                            lin_element = gradient_fill_element.find(".//a:lin", namespaces=self.nsmap)
                            if lin_element is not None:
                                angle = int(lin_element.get("ang", "0"))
                            
                            background_gradient_fill = GradientFill(stops=gradient_stops, angle=angle)
                
                # Check for background reference (p:bgRef)
                background_reference_element = background_element.find(".//p:bgRef", namespaces=self.nsmap)
                if background_reference_element is not None:
                    idx = int(background_reference_element.get("idx", "0"))
                    scheme_color = None
                    scheme_color_element = background_reference_element.find(".//a:schemeClr", namespaces=self.nsmap)
                    if scheme_color_element is not None:
                        scheme_color = scheme_color_element.get("val")
                    background_reference = BackgroundReference(idx=idx, scheme_color=scheme_color)
        
        return background_color, background_gradient_fill, background_reference

    def _get_slide_master_obj(self) -> SlideMaster | None:
        """Get the slide master object referenced by this layout."""
        slide_master_relationship_id = None
        # Look for slide master relationship
        for rel_id, target in self.rels.items():
            if "slideMaster" in target:
                slide_master_relationship_id = rel_id
                break

        slide_master_path = None
        if slide_master_relationship_id:
            slide_master_target = self.rels.get(slide_master_relationship_id)
            if slide_master_target:
                # Construct the absolute path to the slide master XML file
                slide_master_path = os.path.join(
                    self.pptx_unpacked_path,
                    slide_master_target.lstrip("/").replace("../", ""),
                )

        slide_master_object = None
        if slide_master_path and os.path.exists(slide_master_path):
            slide_master_parser = SlideMasterParser(
                slide_master_path, self.pptx_unpacked_path
            )
            slide_master_object = slide_master_parser.parse_master()
        return slide_master_object

    def parse_layout(self) -> SlideLayout:
        layout_name = self.root.find(".//p:cSld", namespaces=self.nsmap).get("name")
        layout_type = self.root.get("type")
        if layout_type is None:
            # Try to get from matchingName if 'type' is not directly on sldLayout
            matching_name = self.root.get("matchingName")
            if matching_name is not None:
                layout_type = matching_name.replace(" ", "").replace("-", "").lower()

        placeholders = self._parse_placeholders()
        list_styles = self._extract_list_styles()
        background_color, background_gradient_fill, background_reference = self._extract_background_properties()

        # Inherit background properties from slide master if no layout-level background is found
        if (not background_color and 
            not background_gradient_fill and 
            not background_reference):
            
            slide_master_obj = self._get_slide_master_obj()
            if slide_master_obj:
                if slide_master_obj.background_color:
                    background_color = slide_master_obj.background_color
                elif slide_master_obj.background_gradient_fill:
                    background_gradient_fill = slide_master_obj.background_gradient_fill
                elif slide_master_obj.background_reference:
                    background_reference = slide_master_obj.background_reference

        # If layout_type is still None, infer from placeholders
        if layout_type is None:
            layout_type = self._infer_layout_type(placeholders)

        return SlideLayout(
            name=layout_name,
            type=layout_type,
            placeholders=placeholders,
            list_styles=list_styles,
            background_color=background_color,
            background_gradient_fill=background_gradient_fill,
            background_reference=background_reference,
        )
