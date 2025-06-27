from lxml import etree

class SlideParser:
    def __init__(self, slide_xml_path, slide_rels_path):
        self.slide_xml_path = slide_xml_path
        self.slide_rels_path = slide_rels_path
        self.tree = etree.parse(self.slide_xml_path)
        self.root = self.tree.getroot()
        self.rels = self._parse_rels()

    def _parse_rels(self):
        rels = {}
        if self.slide_rels_path:
            rels_tree = etree.parse(self.slide_rels_path)
            for rel in rels_tree.findall(".//{*}Relationship"):
                rels[rel.get("Id")] = rel.get("Target")
        return rels

    def extract_shapes_and_text(self):
        shapes = []
        for shape in self.root.findall(".//p:sp", namespaces=self.root.nsmap):
            shape_data = {"type": "shape", "text": "", "x": 0, "y": 0, "cx": 0, "cy": 0, "runs": []}

            # Extract position and size
            sp_pr = shape.find(".//p:spPr", namespaces=self.root.nsmap)
            if sp_pr is not None:
                xfrm = sp_pr.find(".//a:xfrm", namespaces=self.root.nsmap)
                if xfrm is not None:
                    off = xfrm.find(".//a:off", namespaces=self.root.nsmap)
                    ext = xfrm.find(".//a:ext", namespaces=self.root.nsmap)
                    if off is not None:
                        shape_data["x"] = int(off.get("x", 0))
                        shape_data["y"] = int(off.get("y", 0))
                    if ext is not None:
                        shape_data["cx"] = int(ext.get("cx", 0))
                        shape_data["cy"] = int(ext.get("cy", 0))

            # Extract text and run properties
            for p_tag in shape.findall(".//a:p", namespaces=self.root.nsmap):
                paragraph_text = ""
                runs = []
                for r_tag in p_tag.findall(".//a:r", namespaces=self.root.nsmap):
                    run_text = r_tag.find(".//a:t", namespaces=self.root.nsmap)
                    if run_text is not None and run_text.text is not None:
                        text_content = run_text.text
                        paragraph_text += text_content

                        rpr_tag = r_tag.find(".//a:rPr", namespaces=self.root.nsmap)
                        run_properties = {}
                        if rpr_tag is not None:
                            if rpr_tag.get("sz") is not None:
                                run_properties["font_size"] = int(rpr_tag.get("sz"))
                            if rpr_tag.get("b") == "1":
                                run_properties["bold"] = True
                            if rpr_tag.get("i") == "1":
                                run_properties["italic"] = True
                            # Add more properties as needed (e.g., color, font face)

                        runs.append({"text": text_content, "properties": run_properties})
                if paragraph_text: # Only add if there's actual text in the paragraph
                    shape_data["text"] += paragraph_text + "\n" # Add newline for paragraphs
                    shape_data["runs"].extend(runs)

            shapes.append(shape_data)
        return shapes

    def extract_media(self):
        media = []
        for pic in self.root.findall(".//p:pic", namespaces=self.root.nsmap):
            blip = pic.find(".//a:blip", namespaces=self.root.nsmap)
            if blip is not None:
                embed_id = blip.get("{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed")
                if embed_id in self.rels:
                    media.append({"type": "image", "path": self.rels[embed_id]})
        return media

    def extract_hyperlinks(self):
        hyperlinks = []
        for hlink_click in self.root.findall(".//a:hlinkClick", namespaces=self.root.nsmap):
            r_id = hlink_click.get("{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id")
            if r_id and r_id in self.rels:
                hyperlinks.append({"type": "hyperlink", "target": self.rels[r_id]})
        return hyperlinks

    def parse_slide(self):
        return {
            "shapes": self.extract_shapes_and_text(),
            "media": self.extract_media(),
            "hyperlinks": self.extract_hyperlinks()
        }
