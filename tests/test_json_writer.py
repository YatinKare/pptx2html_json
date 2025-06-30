import os
import pytest
import json
from learnx_parser.slide_parser import SlideParser
from learnx_parser.json_writer import JsonWriter
from learnx_parser.data_models import Slide, Shape, Picture, GroupShape, GraphicFrame, Transform, CommonSlideData, TextFrame, Paragraph, TextRun, BlipFill, SlideLayout, LayoutPlaceholder

@pytest.fixture
def slide_data():
    slide_xml_path = os.path.abspath("temp_pptx/ppt/slides/slide23.xml")
    slide_rels_path = os.path.abspath("temp_pptx/ppt/slides/_rels/slide23.xml.rels")
    parser = SlideParser(slide_xml_path, slide_rels_path, os.path.abspath("temp_pptx"), 12192000, 6858000)
    return parser.parse_slide(slide_number=23)

@pytest.fixture
def json_writer():
    # Use a temporary directory for output during tests
    output_dir = "./test_output"
    os.makedirs(output_dir, exist_ok=True)
    yield JsonWriter(output_dir=output_dir)
    # Clean up after test
    import shutil
    shutil.rmtree(output_dir)

def test_write_slide_json(slide_data, json_writer):
    slide_number = 23
    output_file = json_writer.write_slide_json(slide_data, slide_number)

    assert os.path.exists(output_file)

    with open(output_file, "r", encoding="utf-8") as f:
        json_content = json.load(f)

    # Basic checks for JSON content
    assert "elements" in json_content
    assert "slide_number" in json_content
    assert json_content["slide_number"] == 23


def test_flexbox_layout_json_output(json_writer):
    # Create a dummy slide with a title, an image on the left, and text on the right
    title_shape = Shape(type="shape", id="1", ph_type="title", transform=Transform(x=100, y=50, cx=800, cy=100),
                        text_frame=TextFrame(paragraphs=[Paragraph(text_runs=[TextRun(text="Slide Title")])]))
    main_image = Picture(id="2", ph_type="pic", transform=Transform(x=100, y=200, cx=400, cy=400),
                         blip_fill=BlipFill(path="media/image1.png"))
    body_shape = Shape(type="shape", id="3", ph_type="body", transform=Transform(x=550, y=200, cx=400, cy=400),
                       text_frame=TextFrame(paragraphs=[Paragraph(text_runs=[TextRun(text="Some body text")])]))

    slide = Slide(
                slide_number=2,
                common_slide_data=CommonSlideData(),
            shapes=[title_shape, body_shape],
            pictures=[main_image],
            group_shapes=[],
            graphic_frames=[],
            hyperlinks=[],
            slide_layout=SlideLayout(name="Test Layout", type="test_layout", placeholders=[LayoutPlaceholder(ph_type="title", transform=Transform(x=100, y=50, cx=800, cy=100)), LayoutPlaceholder(ph_type="pic", transform=Transform(x=100, y=200, cx=400, cy=400)), LayoutPlaceholder(ph_type="body", transform=Transform(x=550, y=200, cx=400, cy=400))])
        )

    output_file = json_writer.write_slide_json(slide, 2)
    assert os.path.exists(output_file)

    with open(output_file, "r") as f:
        data = json.load(f)

    assert data["slide_number"] == 2
    assert "slide_layout" in data # New: Check for slide_layout
    assert data["slide_layout"]["type"] == "test_layout" # Assuming no specific type for dummy layout
    assert len(data["elements"]) == 3  # Title, Picture, and Body placeholder containers

    # Check title placeholder container
    title_ph_container = data["elements"][0]
    assert title_ph_container["type"] == "placeholder_container"
    assert title_ph_container["ph_type"] == "title"
    assert title_ph_container["children"][0]["ph_type"] == "title"
    assert title_ph_container["children"][0]["transform"]["x"] == 0 # Relative X
    assert title_ph_container["children"][0]["transform"]["y"] == 0 # Relative Y

    # Check picture placeholder container
    pic_ph_container = data["elements"][1]
    assert pic_ph_container["type"] == "placeholder_container"
    assert pic_ph_container["ph_type"] == "pic"
    assert pic_ph_container["children"][0]["ph_type"] == "pic"
    assert pic_ph_container["children"][0]["transform"]["x"] == 0 # Relative X
    assert pic_ph_container["children"][0]["transform"]["y"] == 0 # Relative Y

    # Check body placeholder container
    body_ph_container = data["elements"][2]
    assert body_ph_container["type"] == "placeholder_container"
    assert body_ph_container["ph_type"] == "body"
    assert body_ph_container["children"][0]["ph_type"] == "body"
    assert body_ph_container["children"][0]["transform"]["x"] == 0 # Relative X
    assert body_ph_container["children"][0]["transform"]["y"] == 0 # Relative Y
    
