import os
import pytest
import json
from learnx_parser.slide_parser import SlideParser
from learnx_parser.json_writer import JsonWriter

@pytest.fixture
def slide_data():
    slide_xml_path = os.path.abspath("temp_pptx/ppt/slides/slide23.xml")
    slide_rels_path = os.path.abspath("temp_pptx/ppt/slides/_rels/slide23.xml.rels")
    parser = SlideParser(slide_xml_path, slide_rels_path)
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
    assert "shapes" in json_content
    
    assert "hyperlinks" in json_content
    assert len(json_content["shapes"]) > 0
    
    assert len(json_content["hyperlinks"]) == 0

    # Check for specific data points
    assert any("Agenda" in run["text"] for shape in json_content["shapes"] if shape.get("text_frame") for paragraph in shape["text_frame"]["paragraphs"] for run in paragraph["text_runs"])
    
