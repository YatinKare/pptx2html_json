import os
import re
import unittest

from lxml import etree

from learnx_parser.models.core import (
    BlipFill,
    GroupShape,
    Picture,
    Shape,
    Slide,
    Transform,
)
from learnx_parser.parsers.slide.base import SlideParser
from learnx_parser.parsers.slide.elements import parse_group_shape_element
from learnx_parser.writers.element_renderers import render_group_shape_html
from learnx_parser.writers.html_writer import HtmlWriter


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
        slide_parser = SlideParser(
            slide_xml_path=temp_slide_xml_path,
            slide_rels_path="",
            pptx_unpacked_path="",
            slide_width=12192000,
            slide_height=6858000,
        )

        # Parse the group shape element
        group_shape = parse_group_shape_element(
            slide_parser, etree.fromstring(group_shape_xml), None
        )

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
            children=([], [], [], []),  # Initialize children as a tuple of empty lists
        )

        # Create an HtmlWriter instance
        HtmlWriter()

        # Render the HTML for the group shape
        html_output = render_group_shape_html(group_shape)

        # Assert that the output HTML contains the flexbox styles
        self.assertIn("display: flex", html_output)
        self.assertIn("flex-direction: row", html_output)
        self.assertIn("justify-content: center", html_output)
        self.assertIn("width: 32px", html_output)
        self.assertIn("height: 43px", html_output)

    def test_nested_flexbox_layout_html_output(self):
        # Define a group shape that is a flex container
        group_shape = GroupShape(
            id="100",
            name="flex-container flex-row justify-between",
            transform=Transform(
                x=914400, y=685800, cx=9144000, cy=6858000
            ),  # 1 inch, 1 inch, 10 inch, 7.5 inch
            is_flex_container=True,
        )

        # Define a nested picture
        nested_picture = Picture(
            id="101",
            name="Nested Picture",
            path="/ppt/media/image1.png",
            transform=Transform(
                x=914400, y=685800, cx=914400, cy=685800
            ),  # 1 inch, 1 inch, 1 inch, 0.75 inch
            blip_fill=BlipFill(path="/ppt/media/image1.png"),
        )

        # Define a nested shape (text box)
        nested_shape = Shape(
            type="shape",
            id="102",
            name="Nested Text Box",
            transform=Transform(
                x=1828800, y=685800, cx=1828800, cy=685800
            ),  # 2 inch, 1 inch, 2 inch, 0.75 inch
            text_frame=None,
        )

        # Add children to the group shape
        group_shape.children = (
            [],
            [nested_picture],
            [],
            [],
        )  # shapes, pictures, group_shapes, graphic_frames
        group_shape.children[0].append(nested_shape)

        # Create a dummy slide with the group shape
        dummy_slide = Slide(
            slide_number=999,
            shapes=[],
            pictures=[],
            group_shapes=[group_shape],
            graphic_frames=[],
        )

        # Create an HtmlWriter instance
        html_writer = HtmlWriter(
            output_directory="./test_output", pptx_unpacked_path="temp_pptx"
        )

        # Render the HTML for the slide
        output_file = html_writer.write_slide_html(dummy_slide, 999)

        with open(output_file, encoding="utf-8") as f:
            html_content = f.read()

        # Assert that the group shape has relative positioning and flexbox styles
        group_match = re.search(
            r'<div class="group-shape flex-container" style="width: (\d+)px; height: (\d+)px; display: flex; flex-direction: row; justify-content: space-between;">',
            html_content,
        )
        self.assertIsNotNone(
            group_match, "Group shape div not found or styles incorrect"
        )
        self.assertEqual(int(group_match.group(1)), 960)  # 9144000 EMUs = 960px
        self.assertEqual(int(group_match.group(2)), 720)  # 6858000 EMUs = 720px

        # Assert that the nested picture is in the HTML output
        self.assertIn('<img class="image"', html_content)
        self.assertIn('src="media/image1.png"', html_content)

        # Assert that the nested shape is in the HTML output
        self.assertIn('<div class="shape"', html_content)
        self.assertIn("width: 192px", html_content)  # 1828800 EMUs = 192px
        self.assertIn("height: 72px", html_content)  # 685800 EMUs = 72px

        # Clean up dummy files
        import shutil

        shutil.rmtree(html_writer.output_directory)


if __name__ == "__main__":
    unittest.main()
