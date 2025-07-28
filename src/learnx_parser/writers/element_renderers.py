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
        )

    # Join style attributes
    style_string = " ".join(filter(None, style_attributes))

    shape_div = div(class_="shape", style=style_string)[Markup(content_html)]

    return str(shape_div)


def render_text_frame_html(
    text_frame, theme_resolver=None, placeholder_type=None, slide_background_color=None
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
    list_stack = []  # Stack of (list_html_parts, level, list_type) for nested lists
    
    for para in text_frame.paragraphs:
        # Skip empty paragraphs
        text_content = "".join([run.text for run in para.text_runs]).strip()
        if not text_content:
            continue
            
        is_list_item = (
            para.properties and 
            para.properties.bullet_type is not None
        )
        
        para_level = para.properties.level if para.properties and para.properties.level is not None else 0
        
        if is_list_item:
            # Handle list scenarios (A and B)
            
            # Pop stack until we're at the correct parent level for nesting
            while list_stack and list_stack[-1][1] > para_level:
                list_parts, level, list_type = list_stack.pop()
                completed_list = f"<{list_type}>{''.join(list_parts)}</{list_type}>"
                
                if list_stack:
                    # Add completed list to parent's last item
                    parent_parts, parent_level, parent_list_type = list_stack[-1]
                    if parent_parts:
                        # Insert nested list before closing the last </li>
                        parent_parts[-1] = parent_parts[-1][:-5] + completed_list + "</li>"
                else:
                    # Add completed list to final elements
                    html_elements.append(completed_list)
            
            # Determine list type based on bullet type
            list_type = "ol" if para.properties.bullet_type == "autoNum" else "ul"
            
            # Check if we need to start a new list or continue existing one
            if not list_stack or list_stack[-1][1] != para_level:
                # Scenario A: Start new list
                list_stack.append(([], para_level, list_type))
            
            # Scenario B: Add to existing list (current list is on top of stack)
            current_list_parts, current_level, current_list_type = list_stack[-1]
            
            # Create list item content
            item_content = _render_paragraph_runs(
                para, theme_resolver, placeholder_type, slide_background_color
            )
            
            # Apply paragraph-level styling to list item
            paragraph_css = get_paragraph_style_css(para)
            
            # Handle bullet_type="none" - hide bullet for this list item
            if para.properties.bullet_type == "none":
                if paragraph_css:
                    list_item_html = f'<li style="{paragraph_css} list-style-type: none;">{item_content}</li>'
                else:
                    list_item_html = f'<li style="list-style-type: none;">{item_content}</li>'
            else:
                # Normal list item with bullet
                if paragraph_css:
                    list_item_html = f'<li style="{paragraph_css}">{item_content}</li>'
                else:
                    list_item_html = f"<li>{item_content}</li>"
            
            # Add the list item to the current list
            current_list_parts.append(list_item_html)
            
        else:
            # Handle non-bullet scenarios (C and D)
            
            # Scenario C: Close any open lists
            while list_stack:
                list_parts, level, list_type = list_stack.pop()
                completed_list = f"<{list_type}>{''.join(list_parts)}</{list_type}>"
                
                if list_stack:
                    # Add completed list to parent's last item
                    parent_parts, parent_level, parent_list_type = list_stack[-1]
                    if parent_parts:
                        # Insert nested list before closing the last </li>
                        parent_parts[-1] = parent_parts[-1][:-5] + completed_list + "</li>"
                else:
                    # Add completed list to final elements
                    html_elements.append(completed_list)
            
            # Scenario D: Create normal paragraph
            paragraph_html = _render_paragraph_runs(
                para, theme_resolver, placeholder_type, slide_background_color
            )
            
            paragraph_css = get_paragraph_style_css(para)
            
            if paragraph_html:
                if paragraph_css:
                    html_elements.append(f'<p style="{paragraph_css}">{paragraph_html}</p>')
                else:
                    html_elements.append(f"<p>{paragraph_html}</p>")
    
    # Handle any remaining lists at the end
    while list_stack:
        list_parts, level, list_type = list_stack.pop()
        completed_list = f"<{list_type}>{''.join(list_parts)}</{list_type}>"
        
        if list_stack:
            # Add completed list to parent's last item
            parent_parts, parent_level, parent_list_type = list_stack[-1]
            if parent_parts:
                # Insert nested list before closing the last </li>
                parent_parts[-1] = parent_parts[-1][:-5] + completed_list + "</li>"
        else:
            # Add completed list to final elements
            html_elements.append(completed_list)
    
    return "".join(html_elements)


def _render_as_regular_text(
    paragraphs, theme_resolver=None, placeholder_type=None, slide_background_color=None
) -> str:
    """Render paragraphs as regular text without bullet formatting."""
    if not paragraphs:
        return ""

    html_content = ""
    for paragraph in paragraphs:
        # Skip empty paragraphs
        text_content = "".join([run.text for run in paragraph.text_runs]).strip()
        if not text_content:
            continue
            
        # Render paragraph content
        paragraph_html = _render_paragraph_runs(
            paragraph, theme_resolver, placeholder_type, slide_background_color
        )
        
        # Apply paragraph-level styling (including text alignment)
        paragraph_css = get_paragraph_style_css(paragraph)
        
        # Wrap in paragraph tag with styling
        if paragraph_html:
            if paragraph_css:
                html_content += f'<p style="{paragraph_css}">{paragraph_html}</p>'
            else:
                html_content += f"<p>{paragraph_html}</p>"

    return html_content


def _render_as_bullet_list(
    paragraphs, theme_resolver=None, placeholder_type=None, slide_background_color=None
) -> str:
    """Render paragraphs as properly nested HTML bullet list based on paragraph levels."""
    if not paragraphs:
        return ""

    # Filter out empty paragraphs
    non_empty_paragraphs = [
        p for p in paragraphs if "".join([run.text for run in p.text_runs]).strip()
    ]

    if not non_empty_paragraphs:
        return ""

    # Build nested structure based on paragraph levels
    return _build_nested_list(
        non_empty_paragraphs, theme_resolver, placeholder_type, slide_background_color
    )


def _build_nested_list(
    paragraphs,
    theme_resolver=None,
    placeholder_type=None,
    slide_background_color=None,
    current_level=0,
) -> str:
    """Recursively build nested HTML lists based on paragraph levels."""
    if not paragraphs:
        return ""

    result_html = ""
    i = 0

    while i < len(paragraphs):
        paragraph = paragraphs[i]
        para_level = (
            paragraph.properties.level if paragraph.properties.level is not None else 0
        )

        if para_level < current_level:
            # This paragraph belongs to a higher level, stop processing
            break
        elif para_level == current_level:
            # Same level - add as list item
            if not result_html:
                # Start the list
                list_style = _get_list_style_for_level(
                    paragraph, theme_resolver, placeholder_type, slide_background_color
                )
                list_type = _get_list_type_for_paragraph(paragraph)

                if list_type == "ol":
                    result_html = f'<ol style="{list_style}">'
                else:
                    result_html = f'<ul style="{list_style}">'

            # Create list item content
            item_content = _render_paragraph_runs(
                paragraph, theme_resolver, placeholder_type, slide_background_color
            )

            # Apply paragraph-level styling to list item
            paragraph_css = get_paragraph_style_css(paragraph)

            # Look ahead for nested items
            nested_start = i + 1
            nested_paragraphs = []
            j = nested_start
            while j < len(paragraphs):
                next_para = paragraphs[j]
                next_level = (
                    next_para.properties.level
                    if next_para.properties.level is not None
                    else 0
                )
                if next_level <= current_level:
                    break
                nested_paragraphs.append(next_para)
                j += 1

            # Render nested content if found
            nested_html = ""
            if nested_paragraphs:
                nested_html = _build_nested_list(
                    nested_paragraphs,
                    theme_resolver,
                    placeholder_type,
                    slide_background_color,
                    current_level + 1,
                )
                i = j - 1  # Skip the nested paragraphs we just processed

            # Add the list item with paragraph styling
            if paragraph_css:
                result_html += f'<li style="{paragraph_css}">{item_content}{nested_html}</li>'
            else:
                result_html += f"<li>{item_content}{nested_html}</li>"
            i += 1
        else:
            # para_level > current_level - this shouldn't happen in well-formed lists
            i += 1

    # Close the list
    if result_html:
        if result_html.startswith("<ol"):
            result_html += "</ol>"
        else:
            result_html += "</ul>"

    return result_html


def _get_list_style_for_level(
    paragraph, theme_resolver=None, placeholder_type=None, slide_background_color=None
) -> str:
    """Get CSS style for the list container based on paragraph properties."""
    from learnx_parser.writers.css_utils import get_paragraph_style_css

    # Get base paragraph style (alignment, spacing)
    base_style = get_paragraph_style_css(paragraph, placeholder_type)

    # Remove hardcoded colors - let text color come from run properties
    # Add proper bullet positioning
    additional_styles = "list-style-position: outside; padding-left: 20px;"
    
    # Add CSS list-style-type for auto-numbering
    if (paragraph.properties and 
        paragraph.properties.bullet_type == "autoNum" and 
        paragraph.properties.bullet_auto_num_type):
        list_style_type = _get_css_list_style_type(paragraph.properties.bullet_auto_num_type)
        additional_styles += f" list-style-type: {list_style_type};"

    if base_style:
        return f"{base_style} {additional_styles}"
    else:
        return additional_styles


def _get_list_type_for_paragraph(paragraph) -> str:
    """Determine HTML list type (ul/ol) based on bullet properties."""
    if not paragraph.properties or not paragraph.properties.bullet_type:
        return "ul"  # Default to unordered list

    bullet_type = paragraph.properties.bullet_type

    if bullet_type == "autoNum":
        return "ol"  # Numbered list
    elif bullet_type in ["char", "blip"]:
        return "ul"  # Bullet list
    elif bullet_type == "none":
        return "ul"  # Still use ul but with no bullets
    else:
        return "ul"  # Default


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
