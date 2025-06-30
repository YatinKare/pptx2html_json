from typing import Dict, Optional, List
from lxml import etree
from learnx_parser.data_models import Transform, SlideLayout, LayoutPlaceholder

class SlideLayoutParser:
    def __init__(self, layout_xml_path):
        self.layout_xml_path = layout_xml_path
        self.tree = etree.parse(self.layout_xml_path)
        self.root = self.tree.getroot()
        self.nsmap = self.root.nsmap

    def _extract_transform(self, element_root) -> Transform:
        transform = Transform(x=0, y=0, cx=914400, cy=914400) # Default values
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
                if cx_val != 0:
                    transform.cx = cx_val
                if cy_val != 0:
                    transform.cy = cy_val
            transform.rot = int(xfrm.get("rot", 0)) if xfrm.get("rot") is not None else 0
            transform.flipH = xfrm.get("flipH", "0") == "1"
            transform.flipV = xfrm.get("flipV", "0") == "1"
        return transform

    def _parse_placeholders(self) -> List[LayoutPlaceholder]:
        placeholders = []
        # Search for all shapes and pictures that are placeholders
        for sp_elem in self.root.findall(".//p:sp", namespaces=self.nsmap):
            ph_elem = sp_elem.find(".//p:nvPr/p:ph", namespaces=self.nsmap)
            if ph_elem is not None:
                ph_type = ph_elem.get("type")
                ph_idx = int(ph_elem.get("idx")) if ph_elem.get("idx") is not None else None
                transform = self._extract_transform(sp_elem)
                placeholders.append(LayoutPlaceholder(ph_type=ph_type, ph_idx=ph_idx, transform=transform))
        
        for pic_elem in self.root.findall(".//p:pic", namespaces=self.nsmap):
            ph_elem = pic_elem.find(".//p:nvPicPr/p:nvPr/p:ph", namespaces=self.nsmap)
            if ph_elem is not None:
                ph_type = ph_elem.get("type")
                ph_idx = int(ph_elem.get("idx")) if ph_elem.get("idx") is not None else None
                transform = self._extract_transform(pic_elem)
                placeholders.append(LayoutPlaceholder(ph_type=ph_type, ph_idx=ph_idx, transform=transform))

        return placeholders

    def _infer_layout_type(self, placeholders: List[LayoutPlaceholder]) -> Optional[str]:
        ph_types = {ph.ph_type for ph in placeholders if ph.ph_type is not None}

        if "title" in ph_types and "body" in ph_types and "pic" in ph_types:
            return "picTx" # Title, Picture and Text
        elif "title" in ph_types and "body" in ph_types:
            return "tx" # Title and Text
        elif "title" in ph_types and len(ph_types) == 1:
            return "titleOnly" # Only a title
        elif not ph_types:
            return "blank" # No placeholders
        
        # Add more heuristics for other common layouts as needed
        return None

    def parse_layout(self) -> SlideLayout:
        layout_name = self.root.find(".//p:cSld", namespaces=self.nsmap).get("name")
        layout_type = self.root.get("type")
        if layout_type is None:
            # Try to get from matchingName if 'type' is not directly on sldLayout
            matching_name = self.root.get("matchingName")
            if matching_name is not None:
                layout_type = matching_name.replace(" ", "").replace("-", "").lower()

        placeholders = self._parse_placeholders()
        
        # If layout_type is still None, infer from placeholders
        if layout_type is None:
            layout_type = self._infer_layout_type(placeholders)

        return SlideLayout(name=layout_name, type=layout_type, placeholders=placeholders)
