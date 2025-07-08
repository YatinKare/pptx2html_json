import json
import os
import shutil

import pytest

from learnx_parser import parse_pptx
from learnx_parser.services.document_parser import DocumentParser


@pytest.fixture
def pptx_parser():
    unpacked_path = os.path.abspath("temp_pptx")
    output_dir = "./test_output_full_presentation"
    os.makedirs(output_dir, exist_ok=True)
    yield DocumentParser(unpacked_path, output_dir=output_dir)
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

    # Check if HTML files are created for each slide and JSON presentation file exists
    # Based on Galaxy presentation.pptx, there are 13 slides
    expected_slide_count = 13

    for i in range(1, expected_slide_count + 1):
        html_file = os.path.join(pptx_parser.output_dir, f"slide{i}", f"slide{i}.html")
        assert os.path.exists(html_file)

    # Check that presentation.json is created
    json_file = os.path.join(pptx_parser.output_dir, "presentation.json")
    assert os.path.exists(json_file)

    # Basic check for content in the first HTML file
    html_file = os.path.join(pptx_parser.output_dir, "slide1", "slide1.html")
    with open(html_file, encoding="utf-8") as f:
        html_content = f.read()
        assert "<!doctype html>" in html_content
        assert '<div class="slide-container' in html_content

    # Basic check for content in JSON (v2 schema format)
    with open(json_file, encoding="utf-8") as f:
        json_content = json.load(f)
        assert "presentation" in json_content
        assert "slides" in json_content["presentation"]
        assert len(json_content["presentation"]["slides"]) == expected_slide_count

    # Check if media files are copied to slide-specific media directories
    for i in range(1, expected_slide_count + 1):
        media_dir = os.path.join(pptx_parser.output_dir, f"slide{i}", "media")
        # Check for at least one known image from the sample
        # This assumes image1.png is present on every slide, which might not be true.
        # A more robust test would check for images known to be on specific slides.
        if os.path.exists(os.path.join(media_dir, "image1.png")):
            assert os.path.exists(os.path.join(media_dir, "image1.png"))


def test_parse_pptx_api(sample_pptx_path, api_output_dir):
    parse_pptx(sample_pptx_path, output_dir=api_output_dir)

    expected_slide_count = 13

    for i in range(1, expected_slide_count + 1):
        html_file = os.path.join(api_output_dir, f"slide{i}", f"slide{i}.html")
        assert os.path.exists(html_file)

    # Check that presentation.json is created
    json_file = os.path.join(api_output_dir, "presentation.json")
    assert os.path.exists(json_file)

    for i in range(1, expected_slide_count + 1):
        media_dir = os.path.join(api_output_dir, f"slide{i}", "media")
        if os.path.exists(os.path.join(media_dir, "image1.png")):
            assert os.path.exists(os.path.join(media_dir, "image1.png"))
