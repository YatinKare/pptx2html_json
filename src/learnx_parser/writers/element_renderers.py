"""
Element rendering functions for HTML generation.
This module contains functions that render individual PowerPoint elements to HTML.
"""

import os

from htpy import div, img, li, p, span, ul
from markupsafe import Markup

from learnx_parser.models.core import (
    GraphicFrame,
    GroupShape,
    Picture,
    Shape,
)
from learnx_parser.writers.css_utils import (
    emu_to_px,
    get_flex_properties_from_name,
    get_image_crop_css,
    get_paragraph_style_css,
    get_run_style_css,
    get_shape_style_css,
    get_transform_css,
)


def render_graphic_frame_html(
    element: GraphicFrame, parent_x: int = 0, parent_y: int = 0
) -> str:
    """Render a graphic frame element (charts, tables) to HTML.

    Args:
        element: GraphicFrame object
        parent_x: Parent container X offset
        parent_y: Parent container Y offset

    Returns:
        str: HTML representation of the graphic frame
    """
    # Calculate position and size relative to parent
    x = emu_to_px(element.transform.x - parent_x)
    y = emu_to_px(element.transform.y - parent_y)
    cx = emu_to_px(element.transform.cx)
    cy = emu_to_px(element.transform.cy)

    graphic_frame = div(
        class_="graphic-frame",
        style=f"left: {x}px; top: {y}px; width: {cx}px; height: {cy}px; position: absolute; border: 1px dashed #ccc;"
    )[
        Markup("<!-- Graphic Frame content (e.g., charts, tables) would go here -->")
    ]

    return str(graphic_frame)


def render_group_shape_html(
    element: GroupShape,
    parent_x: int = 0,
    parent_y: int = 0,
    use_absolute_pos: bool = True,
) -> str:
    """Render a group shape element to HTML.

    Args:
        element: GroupShape object
        parent_x: Parent container X offset
        parent_y: Parent container Y offset
        use_absolute_pos: Whether to use absolute positioning

    Returns:
        str: HTML representation of the group shape
    """
    # Calculate the relative position and size of the group shape in pixels
    # These are relative to its parent container (if any), hence parent_x and parent_y are subtracted.
    relative_x = emu_to_px(element.transform.x - parent_x)
    relative_y = emu_to_px(element.transform.y - parent_y)
    cx = emu_to_px(element.transform.cx)
    cy = emu_to_px(element.transform.cy)

    # Extract flexbox properties from the group shape's name (if any)
    flex_properties = get_flex_properties_from_name(element.name)

    # Set up the container style
    container_style = f"width: {cx}px; height: {cy}px;"
    if use_absolute_pos:
        container_style += (
            f" left: {relative_x}px; top: {relative_y}px; position: absolute;"
        )
    if flex_properties:
        container_style += f" {flex_properties}"

    # Generate HTML for child elements
    content_html = ""
    if hasattr(element, "children") and element.children:
        shapes, pictures, group_shapes, graphic_frames = element.children

        # Render child shapes
        for child_shape in shapes:
            content_html += render_shape_html(
                child_shape,
                element.transform.x,
                element.transform.y,
                use_absolute_pos=False,
            )

        # Render child pictures
        for child_picture in pictures:
            content_html += render_picture_html(
                child_picture,
                element.transform.x,
                element.transform.y,
                use_absolute_pos=False,
            )

        # Render child group shapes
        for child_group in group_shapes:
            content_html += render_group_shape_html(
                child_group,
                element.transform.x,
                element.transform.y,
                use_absolute_pos=False,
            )

    # Determine container class based on flexbox properties
    container_class = "group-shape"
    if element.is_flex_container:
        container_class += " flex-container"

    group_div = div(
        class_=container_class,
        style=container_style
    )[
        Markup(content_html)
    ]

    return str(group_div)


def render_picture_html(
    element: Picture,
    parent_x: int = 0,
    parent_y: int = 0,
    parent_cx: int = 0,
    parent_cy: int = 0,
    use_absolute_pos: bool = True,
) -> str:
    """Render a picture element to HTML.

    Args:
        element: Picture object
        parent_x: Parent container X offset
        parent_y: Parent container Y offset
        parent_cx: Parent container width
        parent_cy: Parent container height
        use_absolute_pos: Whether to use absolute positioning

    Returns:
        str: HTML representation of the picture
    """
    # Calculate the position and size of the picture in pixels, relative to its parent
    x = emu_to_px(element.transform.x - parent_x)
    y = emu_to_px(element.transform.y - parent_y)
    cx = emu_to_px(element.transform.cx)
    cy = emu_to_px(element.transform.cy)

    # Construct the image source path, assuming media files are in a 'media' subdirectory
    if element.blip_fill and element.blip_fill.path:
        image_src = os.path.join("media", os.path.basename(element.blip_fill.path))
    else:
        image_src = "placeholder.png"  # Use placeholder when no image data is available

    style_attributes = []
    # If absolute positioning is enabled, add left, top, width, and height styles
    if use_absolute_pos:
        style_attributes.append(f"left: {x}px;")
        style_attributes.append(f"top: {y}px;")
        style_attributes.append(f"width: {cx}px;")
        style_attributes.append(f"height: {cy}px;")

    # Add transform (rotation, flip) and image crop (clip-path) CSS properties
    style_attributes.append(get_transform_css(element.transform))
    if element.blip_fill:
        style_attributes.append(get_image_crop_css(element.blip_fill))

    # Join all collected style attributes into a single string
    style_string = " ".join(filter(None, style_attributes))

    # Return an HTML img tag representing the picture with its styles
    image_element = img(
        class_="image",
        src=image_src,
        style=style_string
    )

    return str(image_element)


def render_shape_html(
    element: Shape,
    parent_x: int = 0,
    parent_y: int = 0,
    parent_cx: int = 0,
    parent_cy: int = 0,
    use_absolute_pos: bool = True,
) -> str:
    """Render a shape element to HTML.

    Args:
        element: Shape object
        parent_x: Parent container X offset
        parent_y: Parent container Y offset
        parent_cx: Parent container width
        parent_cy: Parent container height
        use_absolute_pos: Whether to use absolute positioning

    Returns:
        str: HTML representation of the shape
    """
    # Calculate position and size relative to parent
    x = emu_to_px(element.transform.x - parent_x)
    y = emu_to_px(element.transform.y - parent_y)
    cx = emu_to_px(element.transform.cx)
    cy = emu_to_px(element.transform.cy)

    # Start building style attributes
    style_attributes = []
    if use_absolute_pos:
        style_attributes.append(f"left: {x}px;")
        style_attributes.append(f"top: {y}px;")
    style_attributes.append(f"width: {cx}px;")
    style_attributes.append(f"height: {cy}px;")

    # Add shape-specific styles
    style_attributes.append(get_shape_style_css(element))
    style_attributes.append(get_transform_css(element.transform))

    # Generate content HTML
    content_html = ""
    if element.text_frame:
        content_html = render_text_frame_html(element.text_frame)

    # Join style attributes
    style_string = " ".join(filter(None, style_attributes))

    shape_div = div(
        class_="shape",
        style=style_string
    )[
        Markup(content_html)
    ]

    return str(shape_div)


def render_text_frame_html(text_frame) -> str:
    """Render a text frame to HTML.

    Args:
        text_frame: TextFrame object containing paragraphs

    Returns:
        str: HTML representation of the text frame content
    """
    if not text_frame or not text_frame.paragraphs:
        return ""

    # Check if this text frame should be rendered as a bullet list
    if _should_render_as_bullet_list(text_frame.paragraphs):
        return _render_as_bullet_list(text_frame.paragraphs)

    # Default paragraph rendering
    content_html = ""
    for paragraph in text_frame.paragraphs:
        paragraph_style = get_paragraph_style_css(paragraph)
        paragraph_content = ""

        if paragraph.text_runs:
            for run in paragraph.text_runs:
                run_style = get_run_style_css(run)
                if run_style:
                    run_span = span(style=run_style)[run.text]
                    paragraph_content += str(run_span)
                else:
                    paragraph_content += run.text

        if paragraph_style:
            paragraph_element = p(style=paragraph_style)[Markup(paragraph_content)]
        else:
            paragraph_element = p[Markup(paragraph_content)]
        
        content_html += str(paragraph_element)

    return content_html


def _should_render_as_bullet_list(paragraphs) -> bool:
    """Check if paragraphs should be rendered as a bullet list."""
    if len(paragraphs) <= 1:
        return False

    # Get all non-empty paragraph texts
    all_texts = [
        "".join([run.text for run in p.text_runs]).strip()
        for p in paragraphs
        if "".join([run.text for run in p.text_runs]).strip()
    ]

    if len(all_texts) <= 1:
        return False

    # Check if texts are list-like (short, similar length)
    avg_length = sum(len(text) for text in all_texts) / len(all_texts)
    if avg_length < 50:  # Short items are likely bullets
        # Check if they start with similar patterns (Topic, etc.)
        starts_with_topic = any(text.startswith("Topic") for text in all_texts)
        if starts_with_topic and len(all_texts) >= 3:
            return True

    # Check explicit bullet properties
    for paragraph in paragraphs:
        if (
            paragraph.properties.bullet_type is not None
            and paragraph.properties.bullet_type != "none"
        ):
            return True
        if paragraph.properties.level is not None and paragraph.properties.level > 0:
            return True

    return False


def _render_as_bullet_list(paragraphs) -> str:
    """Render paragraphs as an HTML bullet list."""
    list_items = []

    for paragraph in paragraphs:
        paragraph_text = "".join([run.text for run in paragraph.text_runs]).strip()
        if paragraph_text:
            # Apply run styles within list items
            item_content = ""
            for run in paragraph.text_runs:
                run_style = get_run_style_css(run)
                if run_style:
                    run_span = span(style=run_style)[run.text]
                    item_content += str(run_span)
                else:
                    item_content += run.text

            list_item = li[Markup(item_content)]
            list_items.append(str(list_item))

    bullet_list = ul[Markup("".join(list_items))]
    return str(bullet_list)
