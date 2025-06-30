import unittest
import os
import re
from lxml import etree
from learnx_parser.data_models import GroupShape, Transform, Picture, Shape, Slide, BlipFill
from learnx_parser.slide_parser import SlideParser
from learnx_parser.html_writer import HtmlWriter

class TestFlexboxLayout(unittest.TestCase):
    def test_flex_container_detection(self):
        # Create a dummy group shape element with a flex-container name
        group_shape_xml = """
<p:grpSp xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main">
    <p:nvGrpSpPr>
        <p:cNvPr id="1" name="flex-container"/>
    </p:nvGrpSpPr>
    <p:grpSpPr>
        <a:xfrm xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">
            <a:off x="100" y="200"/>
            <a:ext cx="300" cy="400"/>
        </a:xfrm>
    </p:grpSpPr>
</p:grpSp>
"""
        # Create a dummy file for the parser
        temp_slide_xml_path = "temp_flexbox_slide.xml"
        with open(temp_slide_xml_path, "w") as f:
            f.write(group_shape_xml)

        # Create a dummy SlideParser instance
        slide_parser = SlideParser(slide_xml_path=temp_slide_xml_path, slide_rels_path="", pptx_unpacked_path="", slide_width=12192000, slide_height=6858000)
        
        # Parse the group shape element
        group_shape = slide_parser._parse_group_shape_element(etree.fromstring(group_shape_xml))

        # Assert that the is_flex_container flag is set to True
        self.assertTrue(group_shape.is_flex_container)

        # Clean up dummy file
        os.remove(temp_slide_xml_path)

    def test_flexbox_html_output(self):
        # Create a GroupShape object with the is_flex_container flag set
        group_shape = GroupShape(
            id="1",
            name="flex-container flex-row justify-center",
            transform=Transform(x=104775, y=209550, cx=304800, cy=406400),
            is_flex_container=True,
            children=([], [], [], []) # Initialize children as a tuple of empty lists
        )

        # Create an HtmlWriter instance
        html_writer = HtmlWriter()

        # Render the HTML for the group shape
        html_output = html_writer._render_group_shape_html(group_shape)

        # Assert that the output HTML contains the flexbox styles
        self.assertIn('style="left: 11px; top: 22px; width: 32px; height: 43px; display: flex; flex-direction: row;justify-content: center;"', html_output)

    def test_nested_flexbox_layout_html_output(self):
        # Define a group shape that is a flex container
        group_shape = GroupShape(
            id="100",
            name="flex-container flex-row justify-between",
            transform=Transform(x=914400, y=685800, cx=9144000, cy=6858000), # 1 inch, 1 inch, 10 inch, 7.5 inch
            is_flex_container=True
        )

        # Define a nested picture
        nested_picture = Picture(
            id="101",
            name="Nested Picture",
            path="/ppt/media/image1.png",
            transform=Transform(x=914400, y=685800, cx=914400, cy=685800), # 1 inch, 1 inch, 1 inch, 0.75 inch
            blip_fill=BlipFill(path="/ppt/media/image1.png")
        )

        # Define a nested shape (text box)
        nested_shape = Shape(
            type="shape",
            id="102",
            name="Nested Text Box",
            transform=Transform(x=1828800, y=685800, cx=1828800, cy=685800), # 2 inch, 1 inch, 2 inch, 0.75 inch
            text_frame=None
        )

        # Add children to the group shape
        group_shape.children = ([], [nested_picture], [], []) # shapes, pictures, group_shapes, graphic_frames
        group_shape.children[0].append(nested_shape)

        # Create a dummy slide with the group shape
        dummy_slide = Slide(
            slide_number=999,
            shapes=[],
            pictures=[],
            group_shapes=[group_shape],
            graphic_frames=[]
        )

        # Create an HtmlWriter instance
        html_writer = HtmlWriter(pptx_unpacked_path="temp_pptx")

        # Render the HTML for the slide
        output_file = html_writer.write_slide_html(dummy_slide, 999)

        with open(output_file, "r", encoding="utf-8") as f:
            html_content = f.read()

        # Assert that the group shape has absolute positioning and flexbox styles
        group_match = re.search(r'<div class="group-shape" style="left: (\d+)px; top: (\d+)px; width: (\d+)px; height: (\d+)px; display: flex; flex-direction: row;justify-content: space-between;">', html_content)
        self.assertIsNotNone(group_match, "Group shape div not found or styles incorrect")
        self.assertEqual(int(group_match.group(1)), 96) # 914400 EMUs = 96px
        self.assertEqual(int(group_match.group(2)), 72) # 685800 EMUs = 72px
        self.assertEqual(int(group_match.group(3)), 960) # 9144000 EMUs = 960px
        self.assertEqual(int(group_match.group(4)), 720) # 6858000 EMUs = 720px

        # Assert that the nested picture is positioned relative to the group shape
        pic_match = re.search(r'<img class="image" src=".*?" style="left: (\d+)px; top: (\d+)px; width: (\d+)px; height: (\d+)px;.*" />', html_content)
        self.assertIsNotNone(pic_match, "Nested picture img not found or styles incorrect")
        self.assertEqual(int(pic_match.group(1)), 0) # 914400 - 914400 = 0 EMUs = 0px
        self.assertEqual(int(pic_match.group(2)), 0) # 685800 - 685800 = 0 EMUs = 0px
        self.assertEqual(int(pic_match.group(3)), 96) # 914400 EMUs = 96px
        self.assertEqual(int(pic_match.group(4)), 72) # 685800 EMUs = 72px

        # Assert that the nested shape is positioned relative to the group shape
        shape_match = re.search(r'<div class="shape" id="shape-102" style="left: (\d+)px; top: (\d+)px; width: (\d+)px; height: (\d+)px;.*">', html_content)
        self.assertIsNotNone(shape_match, "Nested shape div not found or styles incorrect")
        self.assertEqual(int(shape_match.group(1)), 96) # 1828800 - 914400 = 914400 EMUs = 96px
        self.assertEqual(int(shape_match.group(2)), 0) # 685800 - 685800 = 0 EMUs = 0px
        self.assertEqual(int(shape_match.group(3)), 192) # 1828800 EMUs = 192px
        self.assertEqual(int(shape_match.group(4)), 72) # 685800 EMUs = 72px

        # Clean up dummy files
        import shutil
        shutil.rmtree(html_writer.output_dir)

if __name__ == '__main__':
    unittest.main()
