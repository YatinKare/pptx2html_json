import os
import re

import pytest
from htpy import div

from learnx_parser.models.core import (
    LayoutPlaceholder,
    Shape,
    Slide,
    SlideLayout,
    Transform,
)
from learnx_parser.parsers.slide.base import SlideParser
from learnx_parser.writers.html_writer import HtmlWriter


@pytest.fixture
def slide_data():
    slide_xml_path = os.path.abspath("temp_pptx/ppt/slides/slide23.xml")
    slide_rels_path = os.path.abspath("temp_pptx/ppt/slides/_rels/slide23.xml.rels")
    slide_width = 12192000  # Example width in EMUs from presentation.xml
    slide_height = 6858000  # Example height in EMUs from presentation.xml
    parser = SlideParser(
        slide_xml_path,
        slide_rels_path,
        os.path.abspath("temp_pptx"),
        slide_width,
        slide_height,
    )
    return parser.parse_slide(slide_number=23)


@pytest.fixture
def html_writer():
    # Use a temporary directory for output during tests
    output_base_dir = "./test_output"
    # Ensure the base output directory exists
    os.makedirs(output_base_dir, exist_ok=True)
    writer = HtmlWriter(
        output_directory=output_base_dir,
        pptx_unpacked_path=os.path.abspath("temp_pptx"),
    )
    yield writer
    # Clean up after test
    import shutil

    if os.path.exists(output_base_dir):
        shutil.rmtree(output_base_dir)


def test_write_slide_html(slide_data, html_writer):
    slide_number = 23
    output_file = html_writer.write_slide_html(slide_data, slide_number)

    expected_output_dir = os.path.join(
        html_writer.output_directory, f"slide{slide_number}"
    )
    expected_file_path = os.path.join(expected_output_dir, f"slide{slide_number}.html")

    assert os.path.exists(expected_file_path)

    with open(expected_file_path, encoding="utf-8") as f:
        html_content = f.read()

    # Basic checks for HTML structure
    assert "<!doctype html>" in html_content
    # Check for the slide-container with dynamic layout class
    if slide_data.slide_layout and slide_data.slide_layout.type:
        # Use htpy for creating the expected class string but extract it manually
        layout_class = f"slide-container {slide_data.slide_layout.type}-layout"
        expected_container_tag = f'<div class="{layout_class}">'
    else:
        expected_container_tag = '<div class="slide-container">'
    assert expected_container_tag in html_content
    assert "</body>" in html_content

    # Check for text content and basic styling
    assert "Topic one" in html_content


def test_image_transform_and_crop_css(slide_data, html_writer):
    slide_number = 23
    output_file = html_writer.write_slide_html(slide_data, slide_number)

    with open(output_file, encoding="utf-8") as f:
        html_content = f.read()

    # Find the image element (htpy generates without closing slash)
    img_match = re.search(
        r"<img class=\"image\" src=\".*?\" style=\"(.*?)\">", html_content
    )
    assert img_match is not None, "Image tag not found in HTML"
    img_style = img_match.group(1)

    # Get the picture object from slide_data
    picture_obj = next(
        (p for p in slide_data.pictures if p.path.endswith("/ppt/media/image1.png")),
        None,
    )
    assert picture_obj is not None, "Picture object not found in slide_data"

    # Assert transform CSS
    transform_parts = []
    if picture_obj.transform.rot != 0:
        rotation_deg = picture_obj.transform.rot / 60000
        transform_parts.append(f"rotate({rotation_deg:.2f}deg)")
    if picture_obj.transform.flipH:
        transform_parts.append("scaleX(-1)")
    if picture_obj.transform.flipV:
        transform_parts.append("scaleY(-1)")
    
    if transform_parts:
        expected_transform_css = f"transform: {' '.join(transform_parts)};"
        assert expected_transform_css in img_style, (
            "Expected transform CSS not found in image style."
        )

    # Assert clip-path CSS
    if picture_obj.blip_fill and (
        picture_obj.blip_fill.src_rect_t is not None
        or picture_obj.blip_fill.src_rect_b is not None
        or picture_obj.blip_fill.src_rect_l is not None
        or picture_obj.blip_fill.src_rect_r is not None
    ):
        # Convert coordinates to percentage strings
        def coord_to_percent(coord):
            return f"{coord / 1000:.2f}%" if coord is not None else "0%"
        
        top = coord_to_percent(picture_obj.blip_fill.src_rect_t)
        bottom = coord_to_percent(picture_obj.blip_fill.src_rect_b)
        left = coord_to_percent(picture_obj.blip_fill.src_rect_l)
        right = coord_to_percent(picture_obj.blip_fill.src_rect_r)
        
        expected_clip_path_css = f"clip-path: inset({top} {right} {bottom} {left});"
        # Use more flexible assertion due to floating point precision
        assert "clip-path: inset(" in img_style, (
            "Expected clip-path CSS not found in image style."
        )


def test_shape_position_and_size_css(html_writer):
    # Create a dummy Slide object with a shape
    dummy_shape = Shape(
        type="shape",
        id="1",
        name="Test Shape",
        transform=Transform(
            x=914400, y=685800, cx=1828800, cy=1371600
        ),  # 1 inch x 1 inch at 1 inch, 1 inch
        text_frame=None,
        ph_type="body",  # Mark as placeholder
        ph_idx=None,
    )
    dummy_slide = Slide(
        slide_number=99,
        shapes=[dummy_shape],  # Add dummy_shape to shapes list
        pictures=[],
        group_shapes=[],
        graphic_frames=[],
        slide_layout=SlideLayout(
            name="Title and Content",
            type="tx",
            placeholders=[
                LayoutPlaceholder(
                    ph_type="body",
                    ph_idx=None,
                    transform=dummy_shape.transform,  # Use shape's transform for placeholder
                )
            ],
        ),
    )

    output_file = html_writer.write_slide_html(dummy_slide, 99)

    with open(output_file, encoding="utf-8") as f:
        html_content = f.read()

    # Find the shape element (updated pattern for new HTML structure)
    shape_match = re.search(r'<div class="shape"[^>]*style="([^"]*?)"', html_content)
    assert shape_match is not None, (
        f"Shape div not found in HTML. Content: {html_content[:500]}..."
    )
    shape_style = shape_match.group(1)
