import os
import pytest
import re
from learnx_parser.slide_parser import SlideParser
from learnx_parser.html_writer import HtmlWriter
from learnx_parser.data_models import Picture, Transform, BlipFill

@pytest.fixture
def slide_data():
    slide_xml_path = os.path.abspath("temp_pptx/ppt/slides/slide23.xml")
    slide_rels_path = os.path.abspath("temp_pptx/ppt/slides/_rels/slide23.xml.rels")
    parser = SlideParser(slide_xml_path, slide_rels_path)
    return parser.parse_slide(slide_number=23)

@pytest.fixture
def html_writer():
    # Use a temporary directory for output during tests
    output_base_dir = "./test_output"
    # Ensure the base output directory exists
    os.makedirs(output_base_dir, exist_ok=True)
    writer = HtmlWriter(output_dir=output_base_dir, pptx_unpacked_path=os.path.abspath("temp_pptx"))
    yield writer
    # Clean up after test
    import shutil
    if os.path.exists(output_base_dir):
        shutil.rmtree(output_base_dir)

def test_write_slide_html(slide_data, html_writer):
    slide_number = 23
    output_file = html_writer.write_slide_html(slide_data, slide_number)

    expected_output_dir = os.path.join(html_writer.output_dir, f"slide{slide_number}")
    expected_file_path = os.path.join(expected_output_dir, f"slide{slide_number}.html")

    assert os.path.exists(expected_file_path)

    with open(expected_file_path, "r", encoding="utf-8") as f:
        html_content = f.read()

    # Basic checks for HTML structure
    assert "<!DOCTYPE html>" in html_content
    assert "<div class=\"slide-container\">" in html_content
    assert "</body>" in html_content

    # Check for text content and basic styling
    assert "Agenda" in html_content
    assert "Topic one" in html_content

def test_image_transform_and_crop_css(slide_data, html_writer):
    slide_number = 23
    output_file = html_writer.write_slide_html(slide_data, slide_number)

    with open(output_file, "r", encoding="utf-8") as f:
        html_content = f.read()

    # Find the image element
    img_match = re.search(r'<img class=\"image\" src=\".*?\" style=\"(.*?)\" />', html_content)
    assert img_match is not None, "Image tag not found in HTML"
    img_style = img_match.group(1)

    # Get the picture object from slide_data
    picture_obj = next((p for p in slide_data.pictures if p.path.endswith("/ppt/media/image1.png")), None)
    assert picture_obj is not None, "Picture object not found in slide_data"

    # Assert transform CSS
    expected_transform_css = ""
    if picture_obj.transform.rot != 0:
        expected_transform_css += f"rotate({picture_obj.transform.rot / 60000:.2f}deg) "
    if picture_obj.transform.flipH:
        expected_transform_css += "scaleX(-1) "
    if picture_obj.transform.flipV:
        expected_transform_css += "scaleY(-1) "
    if expected_transform_css:
        expected_transform_css = f"transform: {expected_transform_css.strip()};"
        assert expected_transform_css in img_style, "Expected transform CSS not found in image style."

    # Assert clip-path CSS
    expected_clip_path_css = ""
    if picture_obj.blip_fill and (picture_obj.blip_fill.src_rect_t is not None or
                                  picture_obj.blip_fill.src_rect_b is not None or
                                  picture_obj.blip_fill.src_rect_l is not None or
                                  picture_obj.blip_fill.src_rect_r is not None):
        top = f"{picture_obj.blip_fill.src_rect_t / 1000:.2f}%" if picture_obj.blip_fill.src_rect_t is not None else "0%"
        bottom = f"{picture_obj.blip_fill.src_rect_b / 1000:.2f}%" if picture_obj.blip_fill.src_rect_b is not None else "0%"
        left = f"{picture_obj.blip_fill.src_rect_l / 1000:.2f}%" if picture_obj.blip_fill.src_rect_l is not None else "0%"
        right = f"{picture_obj.blip_fill.src_rect_r / 1000:.2f}%" if picture_obj.blip_fill.src_rect_r is not None else "0%"
        expected_clip_path_css = f"clip-path: inset({top} {right} {bottom} {left});"
        assert expected_clip_path_css in img_style, "Expected clip-path CSS not found in image style."
