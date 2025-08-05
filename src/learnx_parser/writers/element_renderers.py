"""
Element rendering functions for HTML generation.
This module contains functions that render individual PowerPoint elements to HTML.
"""

import os

from htpy import div, img, span
from markupsafe import Markup

from learnx_parser.models.core import (
    GraphicFrame,
    GroupShape,
    Picture,
    Shape,
)
from learnx_parser.writers.css_utils import (
    CoordinateConverter,
    ZIndexLayers,
    emu_to_px,
    get_image_crop_css,
    get_paragraph_style_css,
    get_run_style_css,
    get_shape_style_css,
    get_text_frame_alignment_css,
    get_transform_css,
)


def render_graphic_frame_html(
    element: GraphicFrame,
    parent_x: int = 0,
    parent_y: int = 0,
    z_index: int = 1,
    prevent_overflow: bool = True,
) -> str:
    """Render a graphic frame element (charts, tables) to HTML.

    Args:
        element: GraphicFrame object
        parent_x: Parent container X offset
        parent_y: Parent container Y offset
        z_index: Z-index for element layering
        prevent_overflow: Whether to prevent element overflow

    Returns:
        str: HTML representation of the graphic frame
    """
    # Extract position using enhanced coordinate converter
    position = CoordinateConverter.extract_position(element.transform)
    if position is None:
        return ""

    # Adjust for parent offset
    position["x"] -= emu_to_px(parent_x)
    position["y"] -= emu_to_px(parent_y)

    # Generate CSS with overflow prevention
    css_style = CoordinateConverter.generate_absolute_css(
        position, z_index, prevent_overflow=prevent_overflow
    )

    graphic_frame = div(
        class_="graphic-frame", style=f"{css_style} border: 1px dashed #ccc;"
    )[Markup("<!-- Graphic Frame content (e.g., charts, tables) would go here -->")]

    return str(graphic_frame)


def render_group_shape_html(
    element: GroupShape,
    parent_x: int = 0,
    parent_y: int = 0,
    z_index_base: int = 1,
    prevent_overflow: bool = True,
    theme_resolver=None,
    slide_background_color=None,
) -> str:
    """Render a group shape element to HTML using absolute positioning.

    Args:
        element: GroupShape object
        parent_x: Parent container X offset
        parent_y: Parent container Y offset
        z_index_base: Base z-index for child elements
        prevent_overflow: Whether to prevent element overflow

    Returns:
        str: HTML representation of the group shape
    """
    # Use enhanced coordinate converter for absolute positioning
    container_style = ""
    position = CoordinateConverter.extract_position(element.transform)
    if position is not None:
        # Adjust for parent offset
        position["x"] -= emu_to_px(parent_x)
        position["y"] -= emu_to_px(parent_y)

        # Generate CSS with overflow prevention
        container_style = CoordinateConverter.generate_absolute_css(
            position, z_index_base, prevent_overflow=prevent_overflow
        )

    # Generate HTML for child elements with proper z-indexing
    content_html = ""
    if hasattr(element, "children") and element.children:
        shapes, pictures, group_shapes, graphic_frames = element.children

        # Render child shapes with incremented z-index
        for i, child_shape in enumerate(shapes):
            content_html += render_shape_html(
                child_shape,
                element.transform.x,
                element.transform.y,
                z_index=ZIndexLayers.get_element_z_index("shape", z_index_base + i),
                slide_background_color=slide_background_color,
                prevent_overflow=prevent_overflow,
                theme_resolver=theme_resolver,
            )

        # Render child pictures with incremented z-index
        for i, child_picture in enumerate(pictures):
            content_html += render_picture_html(
                child_picture,
                element.transform.x,
                element.transform.y,
                z_index=ZIndexLayers.get_element_z_index("image", z_index_base + i),
                prevent_overflow=prevent_overflow,
            )

        # Render child group shapes with incremented z-index
        for i, child_group in enumerate(group_shapes):
            content_html += render_group_shape_html(
                child_group,
                element.transform.x,
                element.transform.y,
                z_index_base=z_index_base + i + 1,
                prevent_overflow=prevent_overflow,
                theme_resolver=theme_resolver,
            )

        # Render child graphic frames with incremented z-index
        for i, child_frame in enumerate(graphic_frames):
            content_html += render_graphic_frame_html(
                child_frame,
                element.transform.x,
                element.transform.y,
                z_index=z_index_base + i + 1,
                prevent_overflow=prevent_overflow,
            )

    # Determine container class based on flexbox properties
    container_class = "group-shape"
    if hasattr(element, "is_flex_container") and element.is_flex_container:
        container_class += " flex-container"

    group_div = div(class_=container_class, style=container_style)[Markup(content_html)]

    return str(group_div)


def render_picture_html(
    element: Picture,
    parent_x: int = 0,
    parent_y: int = 0,
    parent_cx: int = 0,
    parent_cy: int = 0,
    z_index: int = 1,
    prevent_overflow: bool = True,
) -> str:
    """Render a picture element to HTML using absolute positioning.

    Args:
        element: Picture object
        parent_x: Parent container X offset
        parent_y: Parent container Y offset
        parent_cx: Parent container width
        parent_cy: Parent container height
        z_index: Z-index for element layering
        prevent_overflow: Whether to prevent element overflow

    Returns:
        str: HTML representation of the picture
    """
    # Construct the image source path, assuming media files are in a 'media' subdirectory
    if element.blip_fill and element.blip_fill.path:
        image_src = os.path.join("media", os.path.basename(element.blip_fill.path))
    else:
        image_src = "placeholder.png"  # Use placeholder when no image data is available

    style_attributes = []

    # Use enhanced coordinate converter for absolute positioning
    position = CoordinateConverter.extract_position(element.transform)
    if position is not None:
        # Adjust for parent offset
        position["x"] -= emu_to_px(parent_x)
        position["y"] -= emu_to_px(parent_y)

        # Generate CSS with overflow prevention
        positioning_css = CoordinateConverter.generate_absolute_css(
            position, z_index, prevent_overflow=prevent_overflow
        )
        style_attributes.append(positioning_css)

    # Add transform (rotation, flip) and image crop (clip-path) CSS properties
    style_attributes.append(get_transform_css(element.transform))
    if element.blip_fill:
        style_attributes.append(get_image_crop_css(element.blip_fill))

    # Join all collected style attributes into a single string
    style_string = " ".join(filter(None, style_attributes))

    # Return an HTML img tag representing the picture with its styles
    image_element = img(class_="image", src=image_src, style=style_string)

    return str(image_element)


def render_shape_html(
    element: Shape,
    parent_x: int = 0,
    parent_y: int = 0,
    parent_cx: int = 0,
    parent_cy: int = 0,
    z_index: int = 1,
    prevent_overflow: bool = True,
    theme_resolver=None,
    slide_background_color=None,
    style_resolver=None,
) -> str:
    """Render a shape element to HTML using absolute positioning.

    Args:
        element: Shape object
        parent_x: Parent container X offset
        parent_y: Parent container Y offset
        parent_cx: Parent container width
        parent_cy: Parent container height
        z_index: Z-index for element layering
        prevent_overflow: Whether to prevent element overflow

    Returns:
        str: HTML representation of the shape
    """
    # Start building style attributes
    style_attributes = []

    # Use enhanced coordinate converter for absolute positioning
    position = CoordinateConverter.extract_position(element.transform)
    if position is not None:
        # Adjust for parent offset
        position["x"] -= emu_to_px(parent_x)
        position["y"] -= emu_to_px(parent_y)

        # Generate CSS with overflow prevention
        positioning_css = CoordinateConverter.generate_absolute_css(
            position, z_index, prevent_overflow=prevent_overflow
        )
        style_attributes.append(positioning_css)

    # Add shape-specific styles
    style_attributes.append(get_shape_style_css(element))
    style_attributes.append(get_transform_css(element.transform))

    # Add flexbox properties for alignment based on XML-parsed text frame properties
    if element.text_frame:
        text_frame_alignment = get_text_frame_alignment_css(element.text_frame)
        if text_frame_alignment:
            style_attributes.append(text_frame_alignment)

    # Generate content HTML
    content_html = ""
    if element.text_frame:
        content_html = render_text_frame_html(
            element.text_frame,
            theme_resolver=theme_resolver,
            placeholder_type=element.ph_type,
            slide_background_color=slide_background_color,
            style_resolver=style_resolver,
        )

    # Join style attributes
    style_string = " ".join(filter(None, style_attributes))

    shape_div = div(class_="shape", style=style_string)[Markup(content_html)]

    return str(shape_div)


def render_text_frame_html(
    text_frame,
    theme_resolver=None,
    placeholder_type=None,
    slide_background_color=None,
    style_resolver=None,
) -> str:
    """Render a text frame to HTML with proper list grouping and nesting.

    Args:
        text_frame: TextFrame object containing paragraphs
        theme_resolver: ThemeResolver instance for theme-based styling
        placeholder_type: Placeholder type for font sizing (title, body, etc.)

    Returns:
        str: HTML representation of the text frame content
    """
    if not text_frame or not text_frame.paragraphs:
        return ""

    html_elements = []
    list_stack = []  # Stack of (list_items, level, list_type) for nested lists

    for para in text_frame.paragraphs:
        # Determine if the current paragraph is a bullet item
        is_bullet_item = (
            para.properties
            and para.properties.bullet_type is not None
            and para.properties.bullet_type != "none"
        )

        # Get the paragraph's level (treat None level as 0)
        para_level = (
            para.properties.level
            if para.properties and para.properties.level is not None
            else 0
        )

        if is_bullet_item:
            # Determine list type for this paragraph
            para_list_type = "ol" if para.properties.bullet_type == "autoNum" else "ul"

            # Handle level changes
            if list_stack:
                current_level = list_stack[-1][1]

                if para_level > current_level:
                    # Level increased - start nested list inside last <li> of current list
                    list_stack.append(([], para_level, para_list_type))

                elif para_level < current_level:
                    # Level decreased - close lists until we reach the appropriate level
                    while list_stack and list_stack[-1][1] > para_level:
                        list_items, level, list_type = list_stack.pop()
                        completed_list = (
                            f"<{list_type}>{''.join(list_items)}</{list_type}>"
                        )

                        if list_stack:
                            # Insert nested list into the last <li> of parent list
                            parent_items = list_stack[-1][0]
                            if parent_items:
                                # Remove closing </li> from last item, add nested list, then close </li>
                                parent_items[-1] = (
                                    parent_items[-1][:-5] + completed_list + "</li>"
                                )
                        else:
                            # No parent list, add to main elements
                            html_elements.append(completed_list)

                    # If no list at current level exists, create one
                    if not list_stack or list_stack[-1][1] != para_level:
                        list_stack.append(([], para_level, para_list_type))

                # Same level - continue with current list (list_stack[-1])
            else:
                # No open lists - start first list
                list_stack.append(([], para_level, para_list_type))

            # Render the paragraph's content (its runs) into an HTML string
            item_content = _render_paragraph_runs(
                para, theme_resolver, placeholder_type, slide_background_color
            )

            # Add this rendered content as a new item to current list
            paragraph_css = get_paragraph_style_css(para)
            if paragraph_css:
                list_item_html = f'<li style="{paragraph_css}">{item_content}</li>'
            else:
                list_item_html = f"<li>{item_content}</li>"

            # Add to the current (top) list in the stack
            list_stack[-1][0].append(list_item_html)

        else:
            # Non-bullet paragraph - close all open lists
            while list_stack:
                list_items, level, list_type = list_stack.pop()
                completed_list = f"<{list_type}>{''.join(list_items)}</{list_type}>"

                if list_stack:
                    # Insert nested list into the last <li> of parent list
                    parent_items = list_stack[-1][0]
                    if parent_items:
                        # Remove closing </li> from last item, add nested list, then close </li>
                        parent_items[-1] = (
                            parent_items[-1][:-5] + completed_list + "</li>"
                        )
                else:
                    # No parent list, add to main elements
                    html_elements.append(completed_list)

            # Render the paragraph as a standard <p> tag
            paragraph_html = _render_paragraph_runs(
                para, theme_resolver, placeholder_type, slide_background_color
            )

            paragraph_css = get_paragraph_style_css(para)
            if paragraph_html:
                if paragraph_css:
                    html_elements.append(
                        f'<p style="{paragraph_css}">{paragraph_html}</p>'
                    )
                else:
                    html_elements.append(f"<p>{paragraph_html}</p>")

    # After the loop finishes, close any remaining open lists
    while list_stack:
        list_items, level, list_type = list_stack.pop()
        completed_list = f"<{list_type}>{''.join(list_items)}</{list_type}>"

        if list_stack:
            # Insert nested list into the last <li> of parent list
            parent_items = list_stack[-1][0]
            if parent_items:
                # Remove closing </li> from last item, add nested list, then close </li>
                parent_items[-1] = parent_items[-1][:-5] + completed_list + "</li>"
        else:
            # No parent list, add to main elements
            html_elements.append(completed_list)

    return "".join(html_elements)


def _render_paragraph_runs(
    paragraph, theme_resolver=None, placeholder_type=None, slide_background_color=None
) -> str:
    """Render the text runs within a paragraph for list item content."""
    item_content = ""

    for run in paragraph.text_runs:
        run_style = get_run_style_css(
            run,
            theme_resolver=theme_resolver,
            placeholder_type=placeholder_type,
            slide_background_color=slide_background_color,
        )
        if run_style:
            run_span = span(style=run_style)[run.text]
            item_content += str(run_span)
        else:
            item_content += run.text

    return item_content


def _get_css_list_style_type(bullet_auto_num_type: str) -> str:
    """Map OOXML auto-numbering types to CSS list-style-type values."""
    mapping = {
        "arabicPeriod": "decimal",
        "alphaLcPeriod": "lower-alpha",
        "romanLcPeriod": "lower-roman",
        "alphaUcPeriod": "upper-alpha",
        "romanUcPeriod": "upper-roman",
        "arabicParenR": "decimal",
        "alphaLcParenR": "lower-alpha",
        "romanLcParenR": "lower-roman",
    }
    return mapping.get(bullet_auto_num_type, "decimal")
