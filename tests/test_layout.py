import os
import unittest

from learnx_parser.parsers.slide.base import SlideParser


class TestLayout(unittest.TestCase):
    def test_element_position_and_size(self):
        # Create a dummy slide XML with a shape of a known size and position
        slide_xml = """
<p:sld xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main"
       xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">
  <p:cSld>
    <p:spTree>
      <p:sp>
        <p:nvSpPr>
          <p:cNvPr id="1" name="Rectangle 1"/>
          <p:cNvSpPr/>
          <p:nvPr/>
        </p:nvSpPr>
        <p:spPr>
          <a:xfrm>
            <a:off x="1000" y="2000"/>
            <a:ext cx="3000" cy="4000"/>
          </a:xfrm>
        </p:spPr>
      </p:sp>
    </p:spTree>
  </p:cSld>
</p:sld>
"""
        # Create dummy files for the parser
        with open("test_slide.xml", "w") as f:
            f.write(slide_xml)

        # Create a dummy SlideParser instance
        parser = SlideParser(
            slide_xml_path="test_slide.xml",
            slide_rels_path="",
            pptx_unpacked_path="",
            slide_width=12192000,
            slide_height=6858000,
        )

        # Parse the slide
        slide = parser.parse_slide(slide_number=1)

        # Check that the shape's transform is correctly parsed
        self.assertEqual(len(slide.shapes), 1)
        shape = slide.shapes[0]
        self.assertEqual(shape.transform.x, 1000)
        self.assertEqual(shape.transform.y, 2000)
        self.assertEqual(shape.transform.cx, 3000)
        self.assertEqual(shape.transform.cy, 4000)

        # Clean up dummy files
        os.remove("test_slide.xml")


if __name__ == "__main__":
    unittest.main()
