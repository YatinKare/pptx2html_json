"""
Element rendering functions for HTML generation.
This module contains functions that render individual PowerPoint elements to HTML.
"""

import os

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

    return f"""
        <div class="graphic-frame" style="left: {x}px; top: {y}px; width: {cx}px; height: {cy}px; position: absolute; border: 1px dashed #ccc;">
            <!-- Graphic Frame content (e.g., charts, tables) would go here -->
        </div>
"""


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

    return f"""
        <div class="{container_class}" style="{container_style}">
            {content_html}
        </div>
"""


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
    return f"""
        <img class="image" src="{image_src}" style="{style_string}" />
"""


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

    return f"""
        <div class="shape" style="{style_string}">
            {content_html}
        </div>
"""


def render_text_frame_html(text_frame) -> str:
    """Render a text frame to HTML.

    Args:
        text_frame: TextFrame object containing paragraphs

    Returns:
        str: HTML representation of the text frame content
    """
    if not text_frame or not text_frame.paragraphs:
        return ""

    content_html = ""
    for paragraph in text_frame.paragraphs:
        paragraph_style = get_paragraph_style_css(paragraph)
        paragraph_content = ""

        if paragraph.text_runs:
            for run in paragraph.text_runs:
                run_style = get_run_style_css(run)
                if run_style:
                    paragraph_content += f'<span style="{run_style}">{run.text}</span>'
                else:
                    paragraph_content += run.text

        if paragraph_style:
            content_html += f'<p style="{paragraph_style}">{paragraph_content}</p>'
        else:
            content_html += f"<p>{paragraph_content}</p>"

    return content_html
