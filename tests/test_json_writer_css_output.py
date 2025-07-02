import json
import os
import pytest
from learnx_parser.data_models import Slide, CommonSlideData, Transform, SlideLayout, LayoutPlaceholder, Shape
from learnx_parser.json_writer import JsonWriter

@pytest.fixture
def slide_data():
    """Provides a sample Slide object for testing."""
    common_slide_data = CommonSlideData(cx=12192000, cy=6858000)
    transform = Transform(x=1219200, y=685800, cx=6096000, cy=3429000, rot=0)
    shape = Shape(id="1", name="Test Shape", transform=transform, type="shape")
    slide_layout = SlideLayout(name="Test Layout", placeholders=[
        LayoutPlaceholder(ph_type="title", transform=Transform(x=10, y=10, cx=100, cy=100))
    ])
    return Slide(slide_number=1, common_slide_data=common_slide_data, shapes=[shape], slide_layout=slide_layout)

@pytest.fixture
def json_writer(tmp_path):
    """Provides a JsonWriter instance with a temporary output directory."""
    return JsonWriter(output_directory=str(tmp_path))

def test_write_slide_json_css_like_output(json_writer, slide_data):
    """Tests that the JSON output has the new CSS-like transform structure."""
    output_file = json_writer.write_slide_json(slide_data, 1)

    with open(output_file, 'r') as f:
        data = json.load(f)

    # Check the root properties
    assert "slide_number" in data
    assert "common_slide_data" in data
    assert "elements" in data

    # Check that EMU values are removed from common_slide_data
    assert "cx" not in data["common_slide_data"]
    assert "cy" not in data["common_slide_data"]

    # Check the transform of the first element
    elements = data["elements"]
    assert len(elements) > 0
    first_element = elements[0]
    assert "transform" in first_element
    transform = first_element["transform"]

    # Verify the CSS-like properties
    assert "position" in transform
    assert "left" in transform
    assert "top" in transform
    assert "width" in transform
    assert "height" in transform
    assert "rotation" in transform

    # Verify the percentage-based values
    assert transform["left"] == "10.00%"
    assert transform["top"] == "10.00%"
    assert transform["width"] == "50.00%"
    assert transform["height"] == "50.00%"
