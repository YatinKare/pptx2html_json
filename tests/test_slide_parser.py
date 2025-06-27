import os
import pytest
from learnx_parser.slide_parser import SlideParser

@pytest.fixture
def slide_parser():
    # Use the sample slide data from the temp_pptx directory
    slide_xml_path = os.path.abspath("temp_pptx/ppt/slides/slide23.xml")
    slide_rels_path = os.path.abspath("temp_pptx/ppt/slides/_rels/slide23.xml.rels")
    return SlideParser(slide_xml_path, slide_rels_path)

def test_extract_shapes_and_text(slide_parser):
    shapes = slide_parser.extract_shapes_and_text()
    assert len(shapes) > 0
    # Check for a known piece of text and its properties
    agenda_shape = next((s for s in shapes if "Agenda" in s["text"]), None)
    assert agenda_shape is not None
    assert isinstance(agenda_shape["x"], int)
    assert isinstance(agenda_shape["y"], int)
    assert isinstance(agenda_shape["cx"], int)
    assert isinstance(agenda_shape["cy"], int)
    assert any(run["text"] == "Agenda" and "properties" in run for run in agenda_shape["runs"])

    topic_one_shape = next((s for s in shapes if "Topic one" in s["text"]), None)
    assert topic_one_shape is not None
    assert isinstance(topic_one_shape["x"], int)
    assert isinstance(topic_one_shape["y"], int)
    assert isinstance(topic_one_shape["cx"], int)
    assert isinstance(topic_one_shape["cy"], int)
    assert any(run["text"] == "Topic one" and "properties" in run for run in topic_one_shape["runs"])

def test_extract_media(slide_parser):
    media = slide_parser.extract_media()
    assert len(media) > 0
    # Check for a known image path
    assert any("/ppt/media/image1.png" in item["path"] for item in media)

def test_extract_hyperlinks(slide_parser):
    hyperlinks = slide_parser.extract_hyperlinks()
    assert len(hyperlinks) == 0

def test_parse_slide(slide_parser):
    slide_data = slide_parser.parse_slide()
    assert "shapes" in slide_data
    assert "media" in slide_data
    assert "hyperlinks" in slide_data
    assert len(slide_data["shapes"]) > 0
    assert len(slide_data["media"]) > 0
    assert len(slide_data["hyperlinks"]) == 0
