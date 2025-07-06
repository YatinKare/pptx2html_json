"""
Layout handling functions for HTML generation.
This module contains functions that handle different PowerPoint slide layouts.
"""

from learnx_parser.models.core import Slide
from learnx_parser.writers.element_renderers import (
    render_group_shape_html,
    render_picture_html,
    render_shape_html,
)


def render_slide_content(slide: Slide, html_writer_instance) -> str:
    """Render slide content based on its layout type.

    Args:
        slide: Slide object containing elements to render
        html_writer_instance: HtmlWriter instance for accessing helper methods

    Returns:
        str: HTML content for the slide
    """
    # Determine layout type from slide layout
    layout_type = "generic"
    if slide.slide_layout and slide.slide_layout.type:
        layout_type = slide.slide_layout.type

    # Get placeholder elements grouped by type
    placeholder_elements = _get_placeholder_elements(slide)

    # Route to appropriate layout handler
    layout_handlers = {
        "picTx": render_pic_tx_layout,
        "tx": render_tx_layout,
        "obj": render_obj_layout,
        "titleOnly": render_title_only_layout,
        "blank": render_blank_layout,
        "title": render_title_layout,
        "titlePic": render_title_pic_layout,
    }

    handler = layout_handlers.get(layout_type, render_generic_layout)
    content_html, used_element_ids = handler(
        slide, placeholder_elements, html_writer_instance
    )
    return content_html


def render_pic_tx_layout(
    slide: Slide, placeholder_elements: dict, html_writer_instance
) -> tuple[str, list]:
    """Render picture-text layout (image on left, text on right).

    Args:
        slide: Slide object
        placeholder_elements: Dictionary of placeholder elements by type
        html_writer_instance: HtmlWriter instance

    Returns:
        tuple: (HTML content, list of used element IDs)
    """
    content_html = ""
    used_element_ids = []

    # Render main picture
    if "pic" in placeholder_elements:
        for pic_element in placeholder_elements["pic"]:
            content_html += f"""
        <div class="picture-container" style="display: flex; justify-content: center; align-items: center;">
            {render_picture_html(pic_element, use_absolute_pos=False)}
        </div>
    """
            used_element_ids.append(pic_element.id)

    # Render body text
    if "body" in placeholder_elements:
        for body_element in placeholder_elements["body"]:
            content_html += f"""
        <div class="text-container" style="display: flex; flex-direction: column; justify-content: center; padding: 20px;">
            {render_shape_html(body_element, use_absolute_pos=False)}
        </div>
    """
            used_element_ids.append(body_element.id)

    return content_html, used_element_ids


def render_tx_layout(
    slide: Slide, placeholder_elements: dict, html_writer_instance
) -> tuple[str, list]:
    """Render text-only layout.

    Args:
        slide: Slide object
        placeholder_elements: Dictionary of placeholder elements by type
        html_writer_instance: HtmlWriter instance

    Returns:
        tuple: (HTML content, list of used element IDs)
    """
    content_html = ""
    used_element_ids = []

    # Render body text
    if "body" in placeholder_elements:
        for body_element in placeholder_elements["body"]:
            content_html += f"""
        <div class="text-container" style="display: flex; flex-direction: column; justify-content: center; align-items: center;">
            {render_shape_html(body_element, use_absolute_pos=False)}
        </div>
    """
            used_element_ids.append(body_element.id)

    return content_html, used_element_ids


def render_obj_layout(
    slide: Slide, placeholder_elements: dict, html_writer_instance
) -> tuple[str, list]:
    """Render object layout.

    Args:
        slide: Slide object
        placeholder_elements: Dictionary of placeholder elements by type
        html_writer_instance: HtmlWriter instance

    Returns:
        tuple: (HTML content, list of used element IDs)
    """
    return render_generic_layout(slide, placeholder_elements, html_writer_instance)


def render_title_only_layout(
    slide: Slide, placeholder_elements: dict, html_writer_instance
) -> tuple[str, list]:
    """Render title-only layout.

    Args:
        slide: Slide object
        placeholder_elements: Dictionary of placeholder elements by type
        html_writer_instance: HtmlWriter instance

    Returns:
        tuple: (HTML content, list of used element IDs)
    """
    content_html = ""
    used_element_ids = []

    # Center the title
    if "title" in placeholder_elements or "ctrTitle" in placeholder_elements:
        title_elements = placeholder_elements.get(
            "title", []
        ) + placeholder_elements.get("ctrTitle", [])
        for title_element in title_elements:
            content_html += f"""
        <div class="title-container" style="display: flex; justify-content: center; align-items: center; height: 100%;">
            {render_shape_html(title_element, use_absolute_pos=False)}
        </div>
    """
            used_element_ids.append(title_element.id)

    return content_html, used_element_ids


def render_blank_layout(
    slide: Slide, placeholder_elements: dict, html_writer_instance
) -> tuple[str, list]:
    """Render blank layout.

    Args:
        slide: Slide object
        placeholder_elements: Dictionary of placeholder elements by type
        html_writer_instance: HtmlWriter instance

    Returns:
        tuple: (HTML content, list of used element IDs)
    """
    return "", []


def render_title_layout(
    slide: Slide, placeholder_elements: dict, html_writer_instance
) -> tuple[str, list]:
    """Render title slide layout.

    Args:
        slide: Slide object
        placeholder_elements: Dictionary of placeholder elements by type
        html_writer_instance: HtmlWriter instance

    Returns:
        tuple: (HTML content, list of used element IDs)
    """
    content_html = ""
    used_element_ids = []

    # Render title
    if "title" in placeholder_elements or "ctrTitle" in placeholder_elements:
        title_elements = placeholder_elements.get(
            "title", []
        ) + placeholder_elements.get("ctrTitle", [])
        for title_element in title_elements:
            content_html += f"""
        <div class="title-container" style="text-align: center; margin-bottom: 40px;">
            {render_shape_html(title_element, use_absolute_pos=False)}
        </div>
    """
            used_element_ids.append(title_element.id)

    # Render subtitle
    if "subTitle" in placeholder_elements:
        for subtitle_element in placeholder_elements["subTitle"]:
            content_html += f"""
        <div class="subtitle-container" style="text-align: center;">
            {render_shape_html(subtitle_element, use_absolute_pos=False)}
        </div>
    """
            used_element_ids.append(subtitle_element.id)

    return content_html, used_element_ids


def render_title_pic_layout(
    slide: Slide, placeholder_elements: dict, html_writer_instance
) -> tuple[str, list]:
    """Render title with picture layout.

    Args:
        slide: Slide object
        placeholder_elements: Dictionary of placeholder elements by type
        html_writer_instance: HtmlWriter instance

    Returns:
        tuple: (HTML content, list of used element IDs)
    """
    content_html = ""
    used_element_ids = []

    # Render title
    if "title" in placeholder_elements or "ctrTitle" in placeholder_elements:
        title_elements = placeholder_elements.get(
            "title", []
        ) + placeholder_elements.get("ctrTitle", [])
        for title_element in title_elements:
            content_html += f"""
        <div class="title-container" style="text-align: center; margin-bottom: 20px;">
            {render_shape_html(title_element, use_absolute_pos=False)}
        </div>
    """
            used_element_ids.append(title_element.id)

    # Render picture
    if "pic" in placeholder_elements:
        for pic_element in placeholder_elements["pic"]:
            content_html += f"""
        <div class="picture-container" style="display: flex; justify-content: center; align-items: center;">
            {render_picture_html(pic_element, use_absolute_pos=False)}
        </div>
    """
            used_element_ids.append(pic_element.id)

    return content_html, used_element_ids


def render_generic_layout(
    slide: Slide, placeholder_elements: dict, html_writer_instance
) -> tuple[str, list]:
    """Render generic layout with absolute positioning.

    Args:
        slide: Slide object
        placeholder_elements: Dictionary of placeholder elements by type
        html_writer_instance: HtmlWriter instance

    Returns:
        tuple: (HTML content, list of used element IDs)
    """
    content_html = ""
    used_element_ids = []

    # Render all elements with absolute positioning
    all_elements = []
    all_elements.extend(slide.shapes)
    all_elements.extend(slide.pictures)
    all_elements.extend(slide.group_shapes)
    all_elements.extend(slide.graphic_frames)

    for element in all_elements:
        if hasattr(element, "transform"):
            if hasattr(element, "text_frame"):  # Shape
                content_html += render_shape_html(element)
            elif hasattr(element, "blip_fill"):  # Picture
                content_html += render_picture_html(element)
            elif hasattr(element, "is_flex_container"):  # GroupShape
                content_html += render_group_shape_html(element)
            else:  # GraphicFrame or other
                content_html += """
        <div class="generic-container" style="display: flex; justify-content: center; align-items: center;">
"""
                if hasattr(element, "type") and element.type == "shape":
                    content_html += render_shape_html(element, use_absolute_pos=False)
                elif hasattr(element, "path"):  # Picture
                    content_html += render_picture_html(element, use_absolute_pos=False)
                elif hasattr(element, "is_flex_container"):  # GroupShape
                    content_html += render_group_shape_html(
                        element, use_absolute_pos=False
                    )
                content_html += """
        </div>
"""
            used_element_ids.append(element.id)

    return content_html, used_element_ids


def _get_placeholder_elements(slide: Slide) -> dict:
    """Group slide elements by their placeholder type.

    Args:
        slide: Slide object

    Returns:
        dict: Elements grouped by placeholder type
    """
    placeholder_elements = {}

    # Group shapes by placeholder type
    for shape in slide.shapes:
        if shape.ph_type:
            if shape.ph_type not in placeholder_elements:
                placeholder_elements[shape.ph_type] = []
            placeholder_elements[shape.ph_type].append(shape)

    # Group pictures by placeholder type
    for picture in slide.pictures:
        if picture.ph_type:
            if picture.ph_type not in placeholder_elements:
                placeholder_elements[picture.ph_type] = []
            placeholder_elements[picture.ph_type].append(picture)

    return placeholder_elements
