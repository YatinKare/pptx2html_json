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
    RunProperties
)
from learnx_parser.slide_layout_parser import SlideLayoutParser

class SlideParser:
    def __init__(self, slide_xml_path, slide_rels_path, pptx_unpacked_path):
        self.slide_xml_path = slide_xml_path
        self.slide_rels_path = slide_rels_path
        self.tree = etree.parse(self.slide_xml_path)
        self.root = self.tree.getroot()
        self.rels = self._parse_rels()
        self.nsmap = self.root.nsmap # Store namespace map for easier access
        self.pptx_unpacked_path = pptx_unpacked_path

    def _parse_rels(self):
        rels = {}
        if self.slide_rels_path and os.path.exists(self.slide_rels_path):
            rels_tree = etree.parse(self.slide_rels_path)
            for rel in rels_tree.findall("{http://schemas.openxmlformats.org/package/2006/relationships}Relationship"):
                rels[rel.get("Id")] = rel.get("Target")
        return rels

    def _extract_common_slide_data(self) -> CommonSlideData:
        common_slide_data = CommonSlideData()

        # Extract background properties from p:cSld
        c_sld_elem = self.root.find(".//p:cSld", namespaces=self.nsmap)
        if c_sld_elem is not None:
            bg_elem = c_sld_elem.find(".//p:bg", namespaces=self.nsmap)
            if bg_elem is not None:
                bg_pr_elem = bg_elem.find(".//p:bgPr", namespaces=self.nsmap)
                if bg_pr_elem is not None:
                    solid_fill_elem = bg_pr_elem.find(".//a:solidFill", namespaces=self.nsmap)
                    if solid_fill_elem is not None:
                        srgb_clr_elem = solid_fill_elem.find(".//a:srgbClr", namespaces=self.nsmap)
                        if srgb_clr_elem is not None:
                            common_slide_data.background_color = srgb_clr_elem.get("val")
                    else:
                        grad_fill_elem = bg_pr_elem.find(".//a:gradFill", namespaces=self.nsmap)
                        if grad_fill_elem is not None:
                            grad_fill = GradientFill()
                            lin_elem = grad_fill_elem.find(".//a:lin", namespaces=self.nsmap)
                            if lin_elem is not None:
                                grad_fill.angle = int(lin_elem.get("ang", 0)) if lin_elem.get("ang") is not None else None
                                grad_fill.scaled = lin_elem.get("scaled", "0") == "1"
                            
                            gs_lst_elem = grad_fill_elem.find(".//a:gsLst", namespaces=self.nsmap)
                            if gs_lst_elem is not None:
                                for gs_elem in gs_lst_elem.findall(".//a:gs", namespaces=self.nsmap):
                                    pos = int(gs_elem.get("pos", 0))
                                    gs_color = None
                                    gs_scheme_color = None
                                    srgb_clr_elem = gs_elem.find(".//a:srgbClr", namespaces=self.nsmap)
                                    if srgb_clr_elem is not None:
                                        gs_color = srgb_clr_elem.get("val")
                                    else:
                                        scheme_clr_elem = gs_elem.find(".//a:schemeClr", namespaces=self.nsmap)
                                        if scheme_clr_elem is not None:
                                            gs_scheme_color = scheme_clr_elem.get("val")
                                    grad_fill.stops.append(GradientStop(pos=pos, color=gs_color, scheme_color=gs_scheme_color))
                            common_slide_data.background_gradient_fill = grad_fill

        return common_slide_data

    def _extract_transform(self, element_root) -> Transform:
        transform = Transform(x=0, y=0, cx=0, cy=0) # Initialize with default zero values
        # Look for spPr for shapes and pictures, or directly for graphicFrame
        sp_pr = element_root.find(".//p:spPr", namespaces=self.nsmap)
        xfrm = None

        if sp_pr is not None:
            xfrm = sp_pr.find(".//a:xfrm", namespaces=self.nsmap)
        elif element_root.tag == "{http://schemas.openxmlformats.org/presentationml/2006/main}graphicFrame":
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
                if cx_val != 0: # Only override if non-zero value is found
                    transform.cx = cx_val
                if cy_val != 0: # Only override if non-zero value is found
                    transform.cy = cy_val

            transform.rot = int(xfrm.get("rot", 0)) if xfrm.get("rot") is not None else 0
            transform.flipH = xfrm.get("flipH", "0") == "1"
            transform.flipV = xfrm.get("flipV", "0") == "1"
        
        return Transform(x=0, y=0, cx=0, cy=0)

    def _extract_fill_properties(self, sp_pr_element):
        fill = None
        solid_fill_elem = sp_pr_element.find(".//a:solidFill", namespaces=self.nsmap)
        if solid_fill_elem is not None:
            fill = SolidFill()
            srgb_clr_elem = solid_fill_elem.find(".//a:srgbClr", namespaces=self.nsmap)
            if srgb_clr_elem is not None:
                fill.color = srgb_clr_elem.get("val")
            else:
                scheme_clr_elem = solid_fill_elem.find(".//a:schemeClr", namespaces=self.nsmap)
                if scheme_clr_elem is not None:
                    fill.scheme_color = scheme_clr_elem.get("val")
        else:
            grad_fill_elem = sp_pr_element.find(".//a:gradFill", namespaces=self.nsmap)
            if grad_fill_elem is not None:
                grad_fill = GradientFill()
                grad_fill.angle = int(grad_fill_elem.get("ang", 0)) if grad_fill_elem.get("ang") is not None else None
                grad_fill.scaled = grad_fill_elem.get("scaled", "0") == "1"
                
                gs_lst_elem = grad_fill_elem.find(".//a:gsLst", namespaces=self.nsmap)
                if gs_lst_elem is not None:
                    for gs_elem in gs_lst_elem.findall(".//a:gs", namespaces=self.nsmap):
                        pos = int(gs_elem.get("pos", 0))
                        gs_color = None
                        gs_scheme_color = None
                        srgb_clr_elem = gs_elem.find(".//a:srgbClr", namespaces=self.nsmap)
                        if srgb_clr_elem is not None:
                            gs_color = srgb_clr_elem.get("val")
                        else:
                            scheme_clr_elem = gs_elem.find(".//a:schemeClr", namespaces=self.nsmap)
                            if scheme_clr_elem is not None:
                                gs_scheme_color = scheme_clr_elem.get("val")
                        grad_fill.stops.append(GradientStop(pos=pos, color=gs_color, scheme_color=gs_scheme_color))
                fill = grad_fill
        return fill

    def _parse_shape_element(self, shape_element) -> Shape:
        shape_id = shape_element.find(".//p:cNvPr", namespaces=self.nsmap).get("id")
        shape_name = shape_element.find(".//p:cNvPr", namespaces=self.nsmap).get("name")
        
        # Extract placeholder information
        ph_elem = shape_element.find(".//p:nvPr/p:ph", namespaces=self.nsmap)
        ph_type = ph_elem.get("type") if ph_elem is not None else None
        ph_idx = int(ph_elem.get("idx")) if ph_elem is not None and ph_elem.get("idx") is not None else None
        ph_orient = ph_elem.get("orient") if ph_elem is not None else None
        ph_sz = ph_elem.get("sz") if ph_elem is not None else None

        transform = self._extract_transform(shape_element)
        fill = None
        line = None
        text_frame = TextFrame()
        prst_geom_val = None

        sp_pr = shape_element.find(".//p:spPr", namespaces=self.nsmap)
        if sp_pr is not None:
            # Extract geometry
            prst_geom = sp_pr.find(".//a:prstGeom", namespaces=self.nsmap)
            if prst_geom is not None:
                prst_geom_val = prst_geom.get("prst")

            # Extract fills
            fill = self._extract_fill_properties(sp_pr)

            # Extract lines
            ln_elem = sp_pr.find(".//a:ln", namespaces=self.nsmap)
            if ln_elem is not None:
                line = Line()
                line.width = int(ln_elem.get("w", 0))
                line.cap = ln_elem.get("cap")
                line.cmpd = ln_elem.get("cmpd")
                line.algn = ln_elem.get("algn")

                solid_fill_elem = ln_elem.find(".//a:solidFill", namespaces=self.nsmap)
                if solid_fill_elem is not None:
                    srgb_clr_elem = solid_fill_elem.find(".//a:srgbClr", namespaces=self.nsmap)
                    if srgb_clr_elem is not None:
                        line.color = srgb_clr_elem.get("val")
                    else:
                        scheme_clr_elem = solid_fill_elem.find(".//a:schemeClr", namespaces=self.nsmap)
                        if scheme_clr_elem is not None:
                            line.scheme_color = scheme_clr_elem.get("val")

        # Extract text and run properties
        for p_tag in shape_element.findall(".//a:p", namespaces=self.nsmap):
            paragraph_obj = Paragraph()
            
            # Extract paragraph properties
            p_pr_tag = p_tag.find(".//a:pPr", namespaces=self.nsmap)
            if p_pr_tag is not None:
                if p_pr_tag.get("algn") is not None:
                    paragraph_obj.properties.align = p_pr_tag.get("algn")
                if p_pr_tag.get("indent") is not None:
                    paragraph_obj.properties.indent = int(p_pr_tag.get("indent"))

            for r_tag in p_tag.findall(".//a:r", namespaces=self.nsmap):
                run_text_elem = r_tag.find(".//a:t", namespaces=self.nsmap)
                if run_text_elem is not None and run_text_elem.text is not None:
                    text_content = run_text_elem.text
                    run_properties = RunProperties()

                    rpr_tag = r_tag.find(".//a:rPr", namespaces=self.nsmap)
                    if rpr_tag is not None:
                        if rpr_tag.get("sz") is not None:
                            run_properties.font_size = int(rpr_tag.get("sz"))
                        if rpr_tag.get("b") == "1":
                            run_properties.bold = True
                        if rpr_tag.get("i") == "1":
                            run_properties.italic = True
                        
                        # Extract color
                        solid_fill_elem = rpr_tag.find(".//a:solidFill", namespaces=self.nsmap)
                        if solid_fill_elem is not None:
                            srgb_clr_elem = solid_fill_elem.find(".//a:srgbClr", namespaces=self.nsmap)
                            if srgb_clr_elem is not None:
                                run_properties.color = srgb_clr_elem.get("val")
                            else:
                                scheme_clr_elem = solid_fill_elem.find(".//a:schemeClr", namespaces=self.nsmap)
                                if scheme_clr_elem is not None:
                                    run_properties.scheme_color = scheme_clr_elem.get("val")

                        # Extract font face
                        latin_font_elem = rpr_tag.find(".//a:latin", namespaces=self.nsmap)
                        if latin_font_elem is not None:
                            run_properties.font_face = latin_font_elem.get("typeface")

                        # Extract underline
                        u_elem = rpr_tag.find(".//a:u", namespaces=self.nsmap)
                        if u_elem is not None:
                            run_properties.underline = True

                    paragraph_obj.text_runs.append(TextRun(text=text_content, properties=run_properties))
            if paragraph_obj.text_runs: # Only add if there's actual text in the paragraph
                text_frame.paragraphs.append(paragraph_obj)

        return Shape(type="shape", id=shape_id, name=shape_name, transform=transform, prst_geom=prst_geom_val, fill=fill, line=line, text_frame=text_frame, ph_type=ph_type, ph_idx=ph_idx, ph_orient=ph_orient, ph_sz=ph_sz)

    def _parse_picture_element(self, picture_element) -> Picture:
        pic_id = picture_element.find(".//p:nvPicPr/p:cNvPr", namespaces=self.nsmap).get("id")
        pic_name = picture_element.find(".//p:nvPicPr/p:cNvPr", namespaces=self.nsmap).get("name")
        pic_path = ""

        # Extract placeholder information for pictures
        ph_elem = picture_element.find(".//p:nvPicPr/p:nvPr/p:ph", namespaces=self.nsmap)
        ph_type = ph_elem.get("type") if ph_elem is not None else None
        ph_idx = int(ph_elem.get("idx")) if ph_elem is not None and ph_elem.get("idx") is not None else None

        transform = self._extract_transform(picture_element)

        blip = picture_element.find(".//a:blip", namespaces=self.nsmap)
        if blip is not None:
            embed_id = blip.get("{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed")
            if embed_id in self.rels:
                pic_path = self.rels[embed_id]

        blip_fill_elem = picture_element.find(".//p:blipFill", namespaces=self.nsmap)
        blip_fill_obj = None
        if blip_fill_elem is not None:
            rot_with_shape = blip_fill_elem.get("rotWithShape", "0") == "1"
            blip_fill_obj = BlipFill(path=pic_path, rot_with_shape=rot_with_shape)

            src_rect_elem = blip_fill_elem.find(".//a:srcRect", namespaces=self.nsmap)
            if src_rect_elem is not None:
                blip_fill_obj.src_rect_t = int(src_rect_elem.get("t")) if src_rect_elem.get("t") is not None else None
                blip_fill_obj.src_rect_b = int(src_rect_elem.get("b")) if src_rect_elem.get("b") is not None else None
                blip_fill_obj.src_rect_l = int(src_rect_elem.get("l")) if src_rect_elem.get("l") is not None else None
                blip_fill_obj.src_rect_r = int(src_rect_elem.get("r")) if src_rect_elem.get("r") is not None else None

        return Picture(id=pic_id, name=pic_name, path=pic_path, transform=transform, blip_fill=blip_fill_obj, ph_type=ph_type, ph_idx=ph_idx)

    def _parse_group_shape_element(self, group_shape_element) -> GroupShape:
        grp_id = group_shape_element.find(".//p:nvGrpSpPr/p:cNvPr", namespaces=self.nsmap).get("id")
        grp_name = group_shape_element.find(".//p:nvGrpSpPr/p:cNvPr", namespaces=self.nsmap).get("name")
        
        transform = self._extract_transform(group_shape_element)
        shapes, pictures, group_shapes, graphic_frames = self._parse_shape_tree(group_shape_element)
        return GroupShape(id=grp_id, name=grp_name, transform=transform, children=(shapes, pictures, group_shapes, graphic_frames))

    def _parse_graphic_frame_element(self, graphic_frame_element) -> GraphicFrame:
        graphic_frame_id = graphic_frame_element.find(".//p:nvGraphicFramePr/p:cNvPr", namespaces=self.nsmap).get("id")
        graphic_frame_name = graphic_frame_element.find(".//p:nvGraphicFramePr/p:cNvPr", namespaces=self.nsmap).get("name")
        
        transform = self._extract_transform(graphic_frame_element)
        return GraphicFrame(id=graphic_frame_id, name=graphic_frame_name, transform=transform)

    def _parse_shape_tree(self, sp_tree_root):
        shapes = []
        pictures = []
        group_shapes = []
        graphic_frames = []

        for child in sp_tree_root:
            if child.tag == "{http://schemas.openxmlformats.org/presentationml/2006/main}sp":
                shape = self._parse_shape_element(child)
                shapes.append(shape)

            elif child.tag == "{http://schemas.openxmlformats.org/presentationml/2006/main}pic":
                picture = self._parse_picture_element(child)
                pictures.append(picture)

            elif child.tag == "{http://schemas.openxmlformats.org/presentationml/2006/main}grpSp":
                group_shape = self._parse_group_shape_element(child)
                group_shapes.append(group_shape)

            elif child.tag == "{http://schemas.openxmlformats.org/presentationml/2006/main}graphicFrame":
                graphic_frame = self._parse_graphic_frame_element(child)
                graphic_frames.append(graphic_frame)
        return shapes, pictures, group_shapes, graphic_frames

    

    def extract_hyperlinks(self) -> List[Hyperlink]:
        hyperlinks = []
        for hlink_click in self.root.findall(".//a:hlinkClick", namespaces=self.nsmap):
            r_id = hlink_click.get("{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id")
            if r_id and r_id in self.rels:
                hyperlinks.append(Hyperlink(type="hyperlink", target=self.rels[r_id]))
        return hyperlinks

    def parse_slide(self, slide_number: int) -> Slide:
        # Determine slide layout path
        slide_layout_r_id = None
        for rel_id, target in self.rels.items():
            if "slideLayout" in target:
                slide_layout_r_id = rel_id
                break

        slide_layout_path = None
        if slide_layout_r_id:
            # Resolve slide layout path from slide rels
            slide_layout_target = self.rels.get(slide_layout_r_id)
            if slide_layout_target:
                # Construct absolute path to slide layout XML
                # Example: ../slideLayouts/slideLayout1.xml -> temp_pptx/ppt/slideLayouts/slideLayout1.xml
                slide_layout_path = os.path.join(self.pptx_unpacked_path, slide_layout_target.lstrip("/").replace("../", ""))

        slide_layout_parser = None
        if slide_layout_path and os.path.exists(slide_layout_path):
            slide_layout_parser = SlideLayoutParser(slide_layout_path)

        sp_tree_root = self.root.find(".//p:spTree", namespaces=self.nsmap)
        if sp_tree_root is None:
            sp_tree_root = self.root # Fallback if spTree is not found directly

        shapes, pictures, group_shapes, graphic_frames = self._parse_shape_tree(sp_tree_root)

        # Apply inherited transforms from slide layout for placeholders
        if slide_layout_parser:
            for shape in shapes:
                if shape.ph_type and not (shape.transform.x or shape.transform.y or shape.transform.cx or shape.transform.cy):
                    inherited_transform = slide_layout_parser.get_placeholder_transform(shape.ph_type, str(shape.ph_idx) if shape.ph_idx is not None else None)
                    if inherited_transform:
                        shape.transform = inherited_transform
            for picture in pictures:
                if picture.ph_type and not (picture.transform.x or picture.transform.y or picture.transform.cx or picture.transform.cy):
                    inherited_transform = slide_layout_parser.get_placeholder_transform(picture.ph_type, str(picture.ph_idx) if picture.ph_idx is not None else None)
                    if inherited_transform:
                        picture.transform = inherited_transform

        return Slide(
            slide_number=slide_number,
            common_slide_data=self._extract_common_slide_data(),
            shapes=shapes,
            pictures=pictures,
            group_shapes=group_shapes,
            graphic_frames=graphic_frames,
            hyperlinks=self.extract_hyperlinks()
        )