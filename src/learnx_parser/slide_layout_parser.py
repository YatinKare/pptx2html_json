from typing import Dict, Optional
from lxml import etree
from learnx_parser.data_models import Transform

class SlideLayoutParser:
    def __init__(self, layout_xml_path):
        self.layout_xml_path = layout_xml_path
        self.tree = etree.parse(self.layout_xml_path)
        self.root = self.tree.getroot()
        self.nsmap = self.root.nsmap
        self.placeholders = self._parse_placeholders()

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

    def _parse_placeholders(self) -> Dict[str, Transform]:
        placeholders = {}
        # Search for all shapes and pictures that are placeholders
        for sp_elem in self.root.findall(".//p:sp", namespaces=self.nsmap):
            ph_elem = sp_elem.find(".//p:nvPr/p:ph", namespaces=self.nsmap)
            if ph_elem is not None:
                ph_type = ph_elem.get("type")
                ph_idx = ph_elem.get("idx")
                # Create a unique key for the placeholder (type + idx if available, otherwise just type)
                key = f"{ph_type}_{ph_idx}" if ph_idx is not None else ph_type
                placeholders[key] = self._extract_transform(sp_elem)
        
        for pic_elem in self.root.findall(".//p:pic", namespaces=self.nsmap):
            ph_elem = pic_elem.find(".//p:nvPicPr/p:nvPr/p:ph", namespaces=self.nsmap)
            if ph_elem is not None:
                ph_type = ph_elem.get("type")
                ph_idx = ph_elem.get("idx")
                key = f"{ph_type}_{ph_idx}" if ph_idx is not None else ph_type
                placeholders[key] = self._extract_transform(pic_elem)

        return placeholders

    def get_placeholder_transform(self, ph_type: str, ph_idx: Optional[str] = None) -> Optional[Transform]:
        key = f"{ph_type}_{ph_idx}" if ph_idx is not None else ph_type
        return self.placeholders.get(key)
