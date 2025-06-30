from lxml import etree

from lxml import etree

class PresentationParser:
    def __init__(self, presentation_xml_path):
        self.presentation_xml_path = presentation_xml_path
        self.tree = etree.parse(self.presentation_xml_path)
        self.root = self.tree.getroot()
        self.nsmap = self.root.nsmap

    def get_slide_order(self):
        slide_ids = []
        # Find the slide ID list
        sld_id_lst = self.root.find(".//p:sldIdLst", namespaces=self.nsmap)
        if sld_id_lst is not None:
            for sld_id in sld_id_lst.findall(".//p:sldId", namespaces=self.nsmap):
                slide_ids.append(sld_id.get("{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id"))
        return slide_ids

    def get_slide_size(self):
        sld_sz = self.root.find(".//p:sldSz", namespaces=self.nsmap)
        if sld_sz is not None:
            cx = int(sld_sz.get("cx", 0))
            cy = int(sld_sz.get("cy", 0))
            return cx, cy
        return 0, 0
