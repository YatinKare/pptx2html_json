from lxml import etree

class PresentationParser:
    def __init__(self, presentation_xml_path):
        self.presentation_xml_path = presentation_xml_path
        self.tree = etree.parse(self.presentation_xml_path)
        self.root = self.tree.getroot()

    def get_slide_order(self):
        slide_ids = []
        # Namespace map for p: and r: elements
        nsmap = self.root.nsmap
        # Find the slide ID list
        sld_id_lst = self.root.find(".//p:sldIdLst", namespaces=nsmap)
        if sld_id_lst is not None:
            for sld_id in sld_id_lst.findall(".//p:sldId", namespaces=nsmap):
                slide_ids.append(sld_id.get("{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id"))
        return slide_ids
