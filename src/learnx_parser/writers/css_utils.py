"""
CSS utility functions for HTML generation.
This module contains functions that generate CSS styles for various PowerPoint elements.
"""

from learnx_parser.models.core import (
    BlipFill,
    GradientFill,
    Paragraph,
    Shape,
    TextRun,
    Transform,
)


def emu_to_px(emu):
    """Convert English Metric Units (EMU) to pixels.

    Args:
        emu: Value in EMU units

    Returns:
        int: Value in pixels (1 inch = 914400 EMUs = 96 pixels)
    """
    return round(emu / 9525)


def get_gradient_css(gradient_fill: GradientFill) -> str:
    """Generate CSS for a linear gradient background.

    Args:
        gradient_fill: GradientFill object containing gradient information

    Returns:
        str: CSS linear-gradient property
    """
    if not gradient_fill or not gradient_fill.stops:
        return ""

    # PowerPoint rotation is in 60000ths of a degree. CSS uses degrees, where 0deg is to bottom.
    # Adjust angle to CSS standard (0deg is bottom, 90deg is right) if necessary.
    angle = gradient_fill.angle if gradient_fill.angle is not None else 0
    css_angle = (angle + 90) % 360

    color_stops = []
    # Iterate through each gradient stop to format color and position
    for stop in gradient_fill.stops:
        color = f"#{stop.color}"
        # Convert stop position (0-100000) to percentage (0-100%)
        position = f"{stop.pos * 100}%"
        color_stops.append(f"{color} {position}")

    # Return the complete linear-gradient CSS property
    return f"background: linear-gradient({css_angle}deg, {', '.join(color_stops)});"


def get_transform_css(transform: Transform) -> str:
    """Generate CSS transform properties for rotation and flipping.

    Args:
        transform: Transform object containing rotation and flip information

    Returns:
        str: CSS transform property
    """
    transform_parts = []

    # Add rotation if present
    if transform.rot != 0:
        # PowerPoint rotation is in 60000ths of a degree
        degrees = transform.rot / 60000
        transform_parts.append(f"rotate({degrees}deg)")

    # Add horizontal flip if present
    if transform.flipH:
        transform_parts.append("scaleX(-1)")

    # Add vertical flip if present
    if transform.flipV:
        transform_parts.append("scaleY(-1)")

    if transform_parts:
        return f"transform: {' '.join(transform_parts)};"

    return ""


def get_image_crop_css(blip_fill: BlipFill) -> str:
    """Generate CSS clip-path for image cropping.

    Args:
        blip_fill: BlipFill object containing cropping information

    Returns:
        str: CSS clip-path property for cropping
    """
    if not blip_fill:
        return ""

    # Check if any cropping is applied
    if (
        blip_fill.src_rect_t
        or blip_fill.src_rect_b
        or blip_fill.src_rect_l
        or blip_fill.src_rect_r
    ):
        # Convert cropping values (0-100000) to percentages (0-100%)
        top = (blip_fill.src_rect_t or 0) / 1000
        bottom = 100 - ((blip_fill.src_rect_b or 0) / 1000)
        left = (blip_fill.src_rect_l or 0) / 1000
        right = 100 - ((blip_fill.src_rect_r or 0) / 1000)

        return f"clip-path: inset({top}% {100 - right}% {100 - bottom}% {left}%);"

    return ""


def get_shape_style_css(element: Shape) -> str:
    """Generate CSS styles for shape-specific properties.

    Args:
        element: Shape object

    Returns:
        str: CSS styles for the shape
    """
    styles = []

    # Add background color for solid fill
    if element.fill and hasattr(element.fill, "color") and element.fill.color:
        styles.append(f"background-color: #{element.fill.color};")

    # Add border for line properties
    if element.line and element.line.width:
        width_px = emu_to_px(element.line.width)
        color = f"#{element.line.color}" if element.line.color else "#000000"
        styles.append(f"border: {width_px}px solid {color};")

    return " ".join(styles)


def get_paragraph_style_css(paragraph: Paragraph) -> str:
    """Generate CSS styles for paragraph-level formatting.

    Args:
        paragraph: Paragraph object

    Returns:
        str: CSS styles for the paragraph
    """
    styles = []

    # Add text alignment
    if paragraph.properties and paragraph.properties.align:
        alignment_map = {
            "left": "left",
            "center": "center",
            "right": "right",
            "justify": "justify",
        }
        if paragraph.properties.align in alignment_map:
            styles.append(f"text-align: {alignment_map[paragraph.properties.align]};")

    return " ".join(styles)


def get_run_style_css(run: TextRun) -> str:
    """Generate CSS styles for text run formatting.

    Args:
        run: TextRun object containing text formatting

    Returns:
        str: CSS styles for the text run
    """
    styles = []

    # Add font properties
    if run.properties:
        if run.properties.font_face:
            styles.append(f"font-family: '{run.properties.font_face}';")

        if run.properties.font_size:
            # Convert half-points to pixels (approximation)
            font_size_px = run.properties.font_size / 100 * 0.75
            styles.append(f"font-size: {font_size_px}px;")

        if run.properties.bold:
            styles.append("font-weight: bold;")

        if run.properties.italic:
            styles.append("font-style: italic;")

        if run.properties.underline:
            styles.append("text-decoration: underline;")

        if run.properties.color:
            styles.append(f"color: #{run.properties.color};")

    return " ".join(styles)


def get_flex_properties_from_name(name: str) -> str:
    """Extract flexbox CSS properties from element name.

    Args:
        name: Element name that may contain flexbox keywords

    Returns:
        str: CSS flexbox properties
    """
    if not name:
        return ""

    name_lower = name.lower()
    flex_props = []

    # Check for flex container
    if "flex-container" in name_lower:
        flex_props.append("display: flex;")

    # Check for flex direction
    if "flex-row" in name_lower:
        flex_props.append("flex-direction: row;")
    elif "flex-column" in name_lower:
        flex_props.append("flex-direction: column;")

    # Check for justify-content
    if "justify-start" in name_lower:
        flex_props.append("justify-content: flex-start;")
    elif "justify-center" in name_lower:
        flex_props.append("justify-content: center;")
    elif "justify-end" in name_lower:
        flex_props.append("justify-content: flex-end;")
    elif "justify-between" in name_lower:
        flex_props.append("justify-content: space-between;")
    elif "justify-around" in name_lower:
        flex_props.append("justify-content: space-around;")

    # Check for align-items
    if "align-start" in name_lower:
        flex_props.append("align-items: flex-start;")
    elif "align-center" in name_lower:
        flex_props.append("align-items: center;")
    elif "align-end" in name_lower:
        flex_props.append("align-items: flex-end;")

    return " ".join(flex_props)
