import os
import shutil
from lxml import etree
from learnx_parser.presentation_parser import PresentationParser
from learnx_parser.slide_parser import SlideParser
from learnx_parser.html_writer import HtmlWriter
from learnx_parser.json_writer import JsonWriter
from learnx_parser.data_models import Slide

class PptxParser:
    def __init__(self, pptx_unpacked_path, output_dir="./output"):
        self.pptx_unpacked_path = pptx_unpacked_path
        self.output_dir = output_dir

        self.presentation_xml_path = os.path.join(self.pptx_unpacked_path, "ppt", "presentation.xml")
        self.presentation_parser = PresentationParser(self.presentation_xml_path)
        self.html_writer = HtmlWriter(output_dir=self.output_dir, pptx_unpacked_path=self.pptx_unpacked_path)
        self.json_writer = JsonWriter(output_dir=self.output_dir)

    def _copy_media_for_slide(self, slide: Slide, slide_number: int):
        media_output_dir = os.path.join(self.output_dir, f"slide{slide_number}", "media")
        os.makedirs(media_output_dir, exist_ok=True)

        for picture in slide.pictures:
            if picture.blip_fill:
                original_media_path = os.path.join(self.pptx_unpacked_path, picture.blip_fill.path.lstrip("/"))
                dest_media_path = os.path.join(media_output_dir, os.path.basename(picture.blip_fill.path))

                if os.path.exists(original_media_path):
                    shutil.copy(original_media_path, dest_media_path)
                else:
                    print(f"Warning: Media file not found: {original_media_path}")

    def parse_presentation(self):
        slide_r_ids = self.presentation_parser.get_slide_order()
        slide_width, slide_height = self.presentation_parser.get_slide_size()
        
        # Parse presentation.xml.rels to map r:id to slide paths
        presentation_rels_path = os.path.join(self.pptx_unpacked_path, "ppt", "_rels", "presentation.xml.rels")
        rels_tree = etree.parse(presentation_rels_path)
        presentation_rels = {}
        for rel in rels_tree.findall(".//{*}Relationship"):
            presentation_rels[rel.get("Id")] = rel.get("Target")

        for i, r_id in enumerate(slide_r_ids):
            slide_number = i + 1
            # Resolve slide path from presentation_rels
            slide_target = presentation_rels.get(r_id)
            if slide_target is None:
                print(f"Warning: Could not resolve slide r:id {r_id}")
                continue

            # Remove leading '/' if present, and '..' for relative paths
            slide_xml_relative_path = slide_target.lstrip("/").replace("../", "")
            slide_xml_path = os.path.join(self.pptx_unpacked_path, slide_xml_relative_path)

            # Construct slide rels path
            # Example: ppt/slides/slide1.xml -> ppt/slides/_rels/slide1.xml.rels
            slide_dir = os.path.dirname(slide_xml_path)
            slide_name = os.path.basename(slide_xml_path)
            slide_rels_path = os.path.join(slide_dir, "_rels", slide_name + ".rels")

            if not os.path.exists(slide_xml_path):
                print(f"Warning: Slide XML not found: {slide_xml_path}")
                continue
            if not os.path.exists(slide_rels_path):
                print(f"Warning: Slide relationships not found: {slide_rels_path}")
                # Some slides might not have a rels file if they don't link to anything
                slide_rels_path = None # Pass None if rels file doesn't exist

            slide_parser = SlideParser(slide_xml_path, slide_rels_path, self.pptx_unpacked_path, slide_width, slide_height)
            slide_data = slide_parser.parse_slide(slide_number=slide_number)

            # Copy media files for the current slide
            self._copy_media_for_slide(slide_data, slide_number)

            # Use 1-based indexing for slide number in output
            self.html_writer.write_slide_html(slide_data, slide_number)
            self.json_writer.write_slide_json(slide_data, slide_number)

        print(f"Successfully parsed {len(slide_r_ids)} slides.")
