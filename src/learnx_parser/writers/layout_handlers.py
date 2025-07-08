"""
Layout handling functions for HTML generation.
This module contains functions that handle different PowerPoint slide layouts.
"""

from htpy import div, p
from markupsafe import Markup

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
    content_elements = []
    used_element_ids = []

    # Render title if present
    if "title" in placeholder_elements:
        for title_element in placeholder_elements["title"]:
            title_container = div(
                class_="title-container",
                style="display: flex; justify-content: center; align-items: center; padding: 20px;"
            )[
                Markup(render_shape_html(title_element, use_absolute_pos=False))
            ]
            content_elements.append(str(title_container))
            used_element_ids.append(title_element.id)

    # Create flex container content for side-by-side layout
    flex_content = []

    # Render main picture
    if "pic" in placeholder_elements:
        for pic_element in placeholder_elements["pic"]:
            picture_container = div(
                class_="picture-container",
                style="display: flex; justify-content: center; align-items: center; flex: 1;"
            )[
                Markup(render_picture_html(pic_element, use_absolute_pos=False))
            ]
            flex_content.append(str(picture_container))
            used_element_ids.append(pic_element.id)

    # Render body text
    if "body" in placeholder_elements:
        for body_element in placeholder_elements["body"]:
            text_container = div(
                class_="text-container",
                style="display: flex; flex-direction: column; justify-content: center; padding: 20px; flex: 1;"
            )[
                Markup(render_shape_html(body_element, use_absolute_pos=False))
            ]
            flex_content.append(str(text_container))
            used_element_ids.append(body_element.id)

    # Create the main flex container
    if flex_content:
        flex_container = div(
            class_="content-flex-container",
            style="display: flex; flex-direction: row; justify-content: space-around; align-items: flex-start; flex: 1;"
        )[
            Markup("".join(flex_content))
        ]
        content_elements.append(str(flex_container))

    return "".join(content_elements), used_element_ids


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
    content_elements = []
    used_element_ids = []

    # Render body text
    if "body" in placeholder_elements:
        for body_element in placeholder_elements["body"]:
            text_container = div(
                class_="text-container",
                style="display: flex; flex-direction: column; justify-content: center; align-items: center;"
            )[
                Markup(render_shape_html(body_element, use_absolute_pos=False))
            ]
            content_elements.append(str(text_container))
            used_element_ids.append(body_element.id)

    return "".join(content_elements), used_element_ids


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
    content_elements = []
    used_element_ids = []

    # Render title
    if "title" in placeholder_elements or "ctrTitle" in placeholder_elements:
        title_elements = placeholder_elements.get(
            "title", []
        ) + placeholder_elements.get("ctrTitle", [])
        for title_element in title_elements:
            title_container = div(
                class_="title-container",
                style="display: flex; justify-content: center; align-items: center; padding: 20px;"
            )[
                Markup(render_shape_html(title_element, use_absolute_pos=False))
            ]
            content_elements.append(str(title_container))
            used_element_ids.append(title_element.id)

    # Create content container elements for remaining elements
    flex_content = []

    # Render body text
    if "body" in placeholder_elements:
        for body_element in placeholder_elements["body"]:
            text_container = div(
                class_="text-container",
                style="display: flex; flex-direction: column; justify-content: center; margin: 10px;"
            )[
                Markup(render_shape_html(body_element, use_absolute_pos=False))
            ]
            flex_content.append(str(text_container))
            used_element_ids.append(body_element.id)

    # Render any other placeholder types
    for placeholder_type, elements in placeholder_elements.items():
        if placeholder_type not in ["title", "ctrTitle", "body"]:
            for element in elements:
                if hasattr(element, "text_frame"):  # Text element
                    text_container = div(
                        class_="text-container",
                        style="display: flex; flex-direction: column; justify-content: center; margin: 10px;"
                    )[
                        Markup(render_shape_html(element, use_absolute_pos=False))
                    ]
                    flex_content.append(str(text_container))
                elif hasattr(element, "blip_fill") or hasattr(
                    element, "path"
                ):  # Picture
                    picture_container = div(
                        class_="picture-container",
                        style="display: flex; justify-content: center; align-items: center; margin: 10px;"
                    )[
                        Markup(render_picture_html(element, use_absolute_pos=False))
                    ]
                    flex_content.append(str(picture_container))
                elif hasattr(element, "is_flex_container"):  # GroupShape
                    group_container = div(
                        class_="group-container",
                        style="display: flex; flex-direction: column; justify-content: center; margin: 10px;"
                    )[
                        Markup(render_group_shape_html(element, use_absolute_pos=False))
                    ]
                    flex_content.append(str(group_container))
                else:  # GraphicFrame or other elements - render as placeholder
                    other_container = div(
                        class_="other-container",
                        style="display: flex; flex-direction: column; justify-content: center; margin: 10px; background-color: #f0f0f0; border: 1px dashed #ccc; padding: 20px;"
                    )[
                        p[f"Content placeholder ({type(element).__name__})"]
                    ]
                    flex_content.append(str(other_container))
                used_element_ids.append(element.id)

    # Create the main content flex container if there's content
    if flex_content:
        content_container = div(
            class_="content-flex-container",
            style="display: flex; flex-direction: column; justify-content: center; align-items: center; flex: 1; padding: 20px;"
        )[
            Markup("".join(flex_content))
        ]
        content_elements.append(str(content_container))

    return "".join(content_elements), used_element_ids


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
    content_elements = []
    used_element_ids = []

    # Render title
    if "title" in placeholder_elements or "ctrTitle" in placeholder_elements:
        title_elements = placeholder_elements.get(
            "title", []
        ) + placeholder_elements.get("ctrTitle", [])
        for title_element in title_elements:
            title_container = div(
                class_="title-container",
                style="text-align: center; margin-bottom: 40px;"
            )[
                Markup(render_shape_html(title_element, use_absolute_pos=False))
            ]
            content_elements.append(str(title_container))
            used_element_ids.append(title_element.id)

    # Render subtitle
    if "subTitle" in placeholder_elements:
        for subtitle_element in placeholder_elements["subTitle"]:
            subtitle_container = div(
                class_="subtitle-container",
                style="text-align: center;"
            )[
                Markup(render_shape_html(subtitle_element, use_absolute_pos=False))
            ]
            content_elements.append(str(subtitle_container))
            used_element_ids.append(subtitle_element.id)

    return "".join(content_elements), used_element_ids


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
    content_elements = []
    used_element_ids = []

    # Render title
    if "title" in placeholder_elements or "ctrTitle" in placeholder_elements:
        title_elements = placeholder_elements.get(
            "title", []
        ) + placeholder_elements.get("ctrTitle", [])
        for title_element in title_elements:
            title_container = div(
                class_="title-container",
                style="text-align: center; margin-bottom: 20px;"
            )[
                Markup(render_shape_html(title_element, use_absolute_pos=False))
            ]
            content_elements.append(str(title_container))
            used_element_ids.append(title_element.id)

    # Create content container for remaining elements
    flex_content = []

    # Render body text
    if "body" in placeholder_elements:
        for body_element in placeholder_elements["body"]:
            text_container = div(
                class_="text-container",
                style="display: flex; flex-direction: column; justify-content: center; margin: 10px;"
            )[
                Markup(render_shape_html(body_element, use_absolute_pos=False))
            ]
            flex_content.append(str(text_container))
            used_element_ids.append(body_element.id)

    # Render picture
    if "pic" in placeholder_elements:
        for pic_element in placeholder_elements["pic"]:
            picture_container = div(
                class_="picture-container",
                style="display: flex; justify-content: center; align-items: center; margin: 10px;"
            )[
                Markup(render_picture_html(pic_element, use_absolute_pos=False))
            ]
            flex_content.append(str(picture_container))
            used_element_ids.append(pic_element.id)

    # Render any other placeholder types
    for placeholder_type, elements in placeholder_elements.items():
        if placeholder_type not in ["title", "ctrTitle", "body", "pic"]:
            for element in elements:
                if hasattr(element, "text_frame"):  # Text element
                    text_container = div(
                        class_="text-container",
                        style="display: flex; flex-direction: column; justify-content: center; margin: 10px;"
                    )[
                        Markup(render_shape_html(element, use_absolute_pos=False))
                    ]
                    flex_content.append(str(text_container))
                elif hasattr(element, "blip_fill") or hasattr(
                    element, "path"
                ):  # Picture
                    picture_container = div(
                        class_="picture-container",
                        style="display: flex; justify-content: center; align-items: center; margin: 10px;"
                    )[
                        Markup(render_picture_html(element, use_absolute_pos=False))
                    ]
                    flex_content.append(str(picture_container))
                elif hasattr(element, "is_flex_container"):  # GroupShape
                    group_container = div(
                        class_="group-container",
                        style="display: flex; flex-direction: column; justify-content: center; margin: 10px;"
                    )[
                        Markup(render_group_shape_html(element, use_absolute_pos=False))
                    ]
                    flex_content.append(str(group_container))
                else:  # GraphicFrame or other elements - render as placeholder
                    other_container = div(
                        class_="other-container",
                        style="display: flex; flex-direction: column; justify-content: center; margin: 10px; background-color: #f0f0f0; border: 1px dashed #ccc; padding: 20px;"
                    )[
                        p[f"Content placeholder ({type(element).__name__})"]
                    ]
                    flex_content.append(str(other_container))
                used_element_ids.append(element.id)

    # Create the main content flex container if there's content
    if flex_content:
        content_container = div(
            class_="content-flex-container",
            style="display: flex; flex-direction: column; justify-content: center; align-items: center; flex: 1; padding: 20px;"
        )[
            Markup("".join(flex_content))
        ]
        content_elements.append(str(content_container))

    return "".join(content_elements), used_element_ids


def render_generic_layout(
    slide: Slide, placeholder_elements: dict, html_writer_instance
) -> tuple[str, list]:
    """Render generic layout using flexbox approach.

    Args:
        slide: Slide object
        placeholder_elements: Dictionary of placeholder elements by type
        html_writer_instance: HtmlWriter instance

    Returns:
        tuple: (HTML content, list of used element IDs)
    """
    content_elements = []
    used_element_ids = []

    # Render title if present
    if "title" in placeholder_elements or "ctrTitle" in placeholder_elements:
        title_elements = placeholder_elements.get(
            "title", []
        ) + placeholder_elements.get("ctrTitle", [])
        for title_element in title_elements:
            title_container = div(
                class_="title-container",
                style="display: flex; justify-content: center; align-items: center; padding: 20px;"
            )[
                Markup(render_shape_html(title_element, use_absolute_pos=False))
            ]
            content_elements.append(str(title_container))
            used_element_ids.append(title_element.id)

    # Create content container for remaining elements
    flex_content = []

    # Render all other placeholder types
    for placeholder_type, elements in placeholder_elements.items():
        if placeholder_type not in ["title", "ctrTitle"]:
            for element in elements:
                if hasattr(element, "text_frame"):  # Text element
                    text_container = div(
                        class_="text-container",
                        style="display: flex; flex-direction: column; justify-content: center; margin: 10px;"
                    )[
                        Markup(render_shape_html(element, use_absolute_pos=False))
                    ]
                    flex_content.append(str(text_container))
                elif hasattr(element, "blip_fill") or hasattr(
                    element, "path"
                ):  # Picture
                    picture_container = div(
                        class_="picture-container",
                        style="display: flex; justify-content: center; align-items: center; margin: 10px;"
                    )[
                        Markup(render_picture_html(element, use_absolute_pos=False))
                    ]
                    flex_content.append(str(picture_container))
                elif hasattr(element, "is_flex_container"):  # GroupShape
                    group_container = div(
                        class_="group-container",
                        style="display: flex; flex-direction: column; justify-content: center; margin: 10px;"
                    )[
                        Markup(render_group_shape_html(element, use_absolute_pos=False))
                    ]
                    flex_content.append(str(group_container))
                else:  # GraphicFrame or other elements - render as placeholder
                    other_container = div(
                        class_="other-container",
                        style="display: flex; flex-direction: column; justify-content: center; margin: 10px; background-color: #f0f0f0; border: 1px dashed #ccc; padding: 20px;"
                    )[
                        p[f"Content placeholder ({type(element).__name__})"]
                    ]
                    flex_content.append(str(other_container))
                used_element_ids.append(element.id)

    # Create the main content flex container if there's content
    if flex_content:
        content_container = div(
            class_="content-flex-container",
            style="display: flex; flex-direction: column; justify-content: center; align-items: center; flex: 1; padding: 20px;"
        )[
            Markup("".join(flex_content))
        ]
        content_elements.append(str(content_container))

    return "".join(content_elements), used_element_ids


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
        else:
            # For non-placeholder shapes, categorize them as 'body' if they have text
            if hasattr(shape, "text_frame") and shape.text_frame:
                if "body" not in placeholder_elements:
                    placeholder_elements["body"] = []
                placeholder_elements["body"].append(shape)

    # Group pictures by placeholder type
    for picture in slide.pictures:
        if picture.ph_type:
            if picture.ph_type not in placeholder_elements:
                placeholder_elements[picture.ph_type] = []
            placeholder_elements[picture.ph_type].append(picture)
        else:
            # For non-placeholder pictures, categorize them as 'pic'
            if "pic" not in placeholder_elements:
                placeholder_elements["pic"] = []
            placeholder_elements["pic"].append(picture)

    # Include group shapes and graphic frames
    for group_shape in slide.group_shapes:
        if "other" not in placeholder_elements:
            placeholder_elements["other"] = []
        placeholder_elements["other"].append(group_shape)

    for graphic_frame in slide.graphic_frames:
        if "other" not in placeholder_elements:
            placeholder_elements["other"] = []
        placeholder_elements["other"].append(graphic_frame)

    return placeholder_elements
