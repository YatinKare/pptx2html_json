import os
import pytest
from learnx_parser.slide_parser import SlideParser
from learnx_parser.html_writer import HtmlWriter

@pytest.fixture
def slide_data():
    slide_xml_path = os.path.abspath("temp_pptx/ppt/slides/slide23.xml")
    slide_rels_path = os.path.abspath("temp_pptx/ppt/slides/_rels/slide23.xml.rels")
    parser = SlideParser(slide_xml_path, slide_rels_path)
    return parser.parse_slide()

@pytest.fixture
def html_writer():
    # Use a temporary directory for output during tests
    output_dir = "./test_output"
    os.makedirs(output_dir, exist_ok=True)
    yield HtmlWriter(output_dir=output_dir, pptx_unpacked_path=os.path.abspath("temp_pptx"))
    # Clean up after test
    import shutil
    shutil.rmtree(output_dir)

def test_write_slide_html(slide_data, html_writer):
    slide_number = 23
    output_file = html_writer.write_slide_html(slide_data, slide_number)

    assert os.path.exists(output_file)

    with open(output_file, "r", encoding="utf-8") as f:
        html_content = f.read()

    # Basic checks for HTML structure
    assert "<!DOCTYPE html>" in html_content
    assert "<div class=\"slide-container\">" in html_content
    assert "</body>" in html_content

    # Check for text content and basic styling
    assert "Agenda" in html_content
    assert "Topic one" in html_content

    # Check for image and that it's copied
    assert "src=\"media/image1.png\"" in html_content
    assert os.path.exists(os.path.join(html_writer.output_dir, "media", "image1.png"))
