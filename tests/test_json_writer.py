import json
import os

import pytest

from learnx_parser.models.core import (
    BlipFill,
    CommonSlideData,
    LayoutPlaceholder,
    Paragraph,
    Picture,
    Shape,
    Slide,
    SlideLayout,
    TextFrame,
    TextRun,
    Transform,
)
from learnx_parser.parsers.slide.base import SlideParser
from learnx_parser.writers.json_writer import JsonWriter


@pytest.fixture
def slide_data():
    slide_xml_path = os.path.abspath("temp_pptx/ppt/slides/slide23.xml")
    slide_rels_path = os.path.abspath("temp_pptx/ppt/slides/_rels/slide23.xml.rels")
    parser = SlideParser(
        slide_xml_path, slide_rels_path, os.path.abspath("temp_pptx"), 12192000, 6858000
    )
    return parser.parse_slide(slide_number=23)


@pytest.fixture
def json_writer():
    # Use a temporary directory for output during tests
    output_dir = "./test_output"
    os.makedirs(output_dir, exist_ok=True)
    yield JsonWriter(output_directory=output_dir)
    # Clean up after test
    import shutil

    shutil.rmtree(output_dir)


def test_write_slide_json(slide_data, json_writer):
    # Use the new API to transform slides to JSON presentation
    json_presentation = json_writer.transform_to_json_presentation(
        [slide_data], "test-presentation", "Test Presentation"
    )
    output_file = json_writer.write_presentation_json(json_presentation)

    assert os.path.exists(output_file)

    with open(output_file, encoding="utf-8") as f:
        json_content = json.load(f)

    # Basic checks for JSON content
    assert "presentation" in json_content
    presentation = json_content["presentation"]
    assert "slides" in presentation
    assert "id" in presentation
    assert "title" in presentation
    assert presentation["id"] == "test-presentation"
    assert len(presentation["slides"]) == 1

    # Check the slide content
    slide_json = presentation["slides"][0]
    assert "elements" in slide_json
    assert "id" in slide_json
    assert slide_json["id"] == "slide-23"


def test_flexbox_layout_json_output(json_writer):
    # Create a dummy slide with a title, an image on the left, and text on the right
    title_shape = Shape(
        type="shape",
        id="1",
        ph_type="title",
        transform=Transform(x=100, y=50, cx=800, cy=100),
        text_frame=TextFrame(
            paragraphs=[Paragraph(text_runs=[TextRun(text="Slide Title")])]
        ),
    )
    main_image = Picture(
        id="2",
        ph_type="pic",
        transform=Transform(x=100, y=200, cx=400, cy=400),
        blip_fill=BlipFill(path="media/image1.png"),
    )
    body_shape = Shape(
        type="shape",
        id="3",
        ph_type="body",
        transform=Transform(x=550, y=200, cx=400, cy=400),
        text_frame=TextFrame(
            paragraphs=[Paragraph(text_runs=[TextRun(text="Some body text")])]
        ),
    )

    slide = Slide(
        slide_number=2,
        common_slide_data=CommonSlideData(),
        shapes=[title_shape, body_shape],
        pictures=[main_image],
        group_shapes=[],
        graphic_frames=[],
        hyperlinks=[],
        slide_layout=SlideLayout(
            name="Test Layout",
            type="test_layout",
            placeholders=[
                LayoutPlaceholder(
                    ph_type="title", transform=Transform(x=100, y=50, cx=800, cy=100)
                ),
                LayoutPlaceholder(
                    ph_type="pic", transform=Transform(x=100, y=200, cx=400, cy=400)
                ),
                LayoutPlaceholder(
                    ph_type="body", transform=Transform(x=550, y=200, cx=400, cy=400)
                ),
            ],
        ),
    )

    # Use the new API to transform slides to JSON presentation
    json_presentation = json_writer.transform_to_json_presentation(
        [slide], "test-presentation", "Test Presentation"
    )
    output_file = json_writer.write_presentation_json(json_presentation)
    assert os.path.exists(output_file)

    with open(output_file) as f:
        json_content = json.load(f)

    # Check the slide content
    presentation = json_content["presentation"]
    slide_json = presentation["slides"][0]
    assert slide_json["id"] == "slide-2"
    assert len(slide_json["elements"]) >= 2  # At least title and text elements

    # Check that we have the expected element types
    element_types = [elem["type"] for elem in slide_json["elements"]]
    assert "title" in element_types
    assert "text-box" in element_types
