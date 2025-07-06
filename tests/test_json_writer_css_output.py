import json

import pytest

from learnx_parser.models.core import (
    CommonSlideData,
    LayoutPlaceholder,
    Shape,
    Slide,
    SlideLayout,
    Transform,
)
from learnx_parser.writers.json_writer import JsonWriter


@pytest.fixture
def slide_data():
    """Provides a sample Slide object for testing."""
    common_slide_data = CommonSlideData(cx=12192000, cy=6858000)
    transform = Transform(x=1219200, y=685800, cx=6096000, cy=3429000, rot=0)
    shape = Shape(id="1", name="Test Shape", transform=transform, type="shape")
    slide_layout = SlideLayout(
        name="Test Layout",
        placeholders=[
            LayoutPlaceholder(
                ph_type="title", transform=Transform(x=10, y=10, cx=100, cy=100)
            )
        ],
    )
    return Slide(
        slide_number=1,
        common_slide_data=common_slide_data,
        shapes=[shape],
        slide_layout=slide_layout,
    )


@pytest.fixture
def json_writer(tmp_path):
    """Provides a JsonWriter instance with a temporary output directory."""
    return JsonWriter(output_directory=str(tmp_path))


def test_write_slide_json_css_like_output(json_writer, slide_data):
    """Tests that the JSON output has the new CSS-like transform structure."""
    # Use the new API to transform slides to JSON presentation
    json_presentation = json_writer.transform_to_json_presentation(
        [slide_data], "test-presentation", "Test Presentation"
    )
    output_file = json_writer.write_presentation_json(json_presentation)

    with open(output_file) as f:
        json_content = json.load(f)

    # Check the root properties
    assert "slides" in json_content
    assert "id" in json_content
    assert len(json_content["slides"]) == 1
    
    slide_json = json_content["slides"][0]
    assert "elements" in slide_json

    # Check that the slide elements structure is present
    elements = slide_json["elements"]
    assert isinstance(elements, list)
    
    # Basic JSON structure verification
    assert slide_json["id"] == "slide-1"
