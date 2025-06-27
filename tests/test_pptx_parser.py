import os
import pytest
import shutil
import json
from learnx_parser.pptx_parser import PptxParser
from learnx_parser import parse_pptx

@pytest.fixture
def pptx_parser():
    unpacked_path = os.path.abspath("temp_pptx")
    output_dir = "./test_output_full_presentation"
    os.makedirs(output_dir, exist_ok=True)
    yield PptxParser(unpacked_path, output_dir=output_dir)
    shutil.rmtree(output_dir)

@pytest.fixture
def sample_pptx_path():
    return os.path.abspath("example/Galaxy presentation.pptx")

@pytest.fixture
def api_output_dir():
    output_dir = "./test_api_output"
    os.makedirs(output_dir, exist_ok=True)
    yield output_dir
    shutil.rmtree(output_dir)

def test_parse_presentation(pptx_parser):
    pptx_parser.parse_presentation()

    # Check if HTML and JSON files are created for each slide
    # Based on Galaxy presentation.pptx, there are 13 slides
    expected_slide_count = 13

    for i in range(1, expected_slide_count + 1):
        html_file = os.path.join(pptx_parser.output_dir, f"slide{i}.html")
        json_file = os.path.join(pptx_parser.output_dir, f"slide{i}.json")

        assert os.path.exists(html_file)
        assert os.path.exists(json_file)

        # Basic check for content in HTML
        with open(html_file, "r", encoding="utf-8") as f:
            html_content = f.read()
            assert "<!DOCTYPE html>" in html_content
            assert "<div class=\"slide-container\">" in html_content

        # Basic check for content in JSON
        with open(json_file, "r", encoding="utf-8") as f:
            json_content = json.load(f)
            assert "shapes" in json_content
            assert "media" in json_content

    # Check if media files are copied
    media_dir = os.path.join(pptx_parser.output_dir, "media")
    assert os.path.exists(media_dir)
    # Check for at least one known image from the sample
    assert os.path.exists(os.path.join(media_dir, "image1.png"))

def test_parse_pptx_api(sample_pptx_path, api_output_dir):
    parse_pptx(sample_pptx_path, output_dir=api_output_dir)

    expected_slide_count = 13

    for i in range(1, expected_slide_count + 1):
        html_file = os.path.join(api_output_dir, f"slide{i}.html")
        json_file = os.path.join(api_output_dir, f"slide{i}.json")

        assert os.path.exists(html_file)
        assert os.path.exists(json_file)

    media_dir = os.path.join(api_output_dir, "media")
    assert os.path.exists(media_dir)
    assert os.path.exists(os.path.join(media_dir, "image1.png"))
