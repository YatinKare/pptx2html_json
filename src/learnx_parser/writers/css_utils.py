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


class CoordinateConverter:
    """Convert PowerPoint coordinates to CSS positioning for absolute positioning mode.

    This class provides utilities to convert PowerPoint's EMU (English Metric Units)
    coordinate system to pixel-based CSS positioning. PowerPoint uses EMUs for precise
    positioning where 1 inch = 914400 EMUs = 96 pixels, making the conversion factor
    1 EMU = 1/9525 pixels.

    Enhanced for version 0.2.7 with overflow detection and prevention capabilities
    to ensure all elements fit within the slide container bounds while maintaining
    aspect ratios when possible.
    """

    EMU_TO_PIXEL = 1 / 9525

    @staticmethod
    def emu_to_px(emu: int) -> int:
        """Convert EMU to pixels with proper rounding.

        Args:
            emu: Value in EMU units

        Returns:
            int: Value in pixels
        """
        return round(emu * CoordinateConverter.EMU_TO_PIXEL)

    @staticmethod
    def extract_position(transform: Transform) -> dict:
        """Extract position from Transform object.

        Args:
            transform: Transform object containing position and size

        Returns:
            dict: Position dictionary with x, y, width, height in pixels
        """
        if transform is None:
            return None

        return {
            "x": CoordinateConverter.emu_to_px(transform.x),
            "y": CoordinateConverter.emu_to_px(transform.y),
            "width": CoordinateConverter.emu_to_px(transform.cx),
            "height": CoordinateConverter.emu_to_px(transform.cy),
        }

    @staticmethod
    def check_overflow(
        position: dict, container_width: int = 1280, container_height: int = 720
    ) -> dict:
        """Check if element position causes overflow beyond container bounds.

        Args:
            position: Position dictionary with x, y, width, height
            container_width: Container width in pixels (default: 1280)
            container_height: Container height in pixels (default: 720)

        Returns:
            dict: Overflow information with right, bottom overflow amounts and flags
        """
        if position is None:
            return None

        right = position["x"] + position["width"]
        bottom = position["y"] + position["height"]

        overflow_right = max(0, right - container_width)
        overflow_bottom = max(0, bottom - container_height)
        overflow_left = max(0, -position["x"])
        overflow_top = max(0, -position["y"])

        return {
            "has_overflow": overflow_right > 0
            or overflow_bottom > 0
            or overflow_left > 0
            or overflow_top > 0,
            "overflow_right": overflow_right,
            "overflow_bottom": overflow_bottom,
            "overflow_left": overflow_left,
            "overflow_top": overflow_top,
            "element_right": right,
            "element_bottom": bottom,
        }

    @staticmethod
    def prevent_overflow(
        position: dict,
        container_width: int = 1280,
        container_height: int = 720,
        preserve_aspect_ratio: bool = True,
    ) -> dict:
        """Prevent element overflow by adjusting position and size while preserving aspect ratio.

        Args:
            position: Position dictionary with x, y, width, height
            container_width: Container width in pixels (default: 1280)
            container_height: Container height in pixels (default: 720)
            preserve_aspect_ratio: Whether to maintain element aspect ratio when resizing

        Returns:
            dict: Adjusted position dictionary that fits within container bounds
        """
        if position is None:
            return None

        adjusted = position.copy()

        # Check for negative positions and adjust
        if adjusted["x"] < 0:
            adjusted["width"] += adjusted["x"]  # Reduce width by amount moved
            adjusted["x"] = 0

        if adjusted["y"] < 0:
            adjusted["height"] += adjusted["y"]  # Reduce height by amount moved
            adjusted["y"] = 0

        # Ensure minimum size
        adjusted["width"] = max(1, adjusted["width"])
        adjusted["height"] = max(1, adjusted["height"])

        # Check for overflow and resize if necessary
        overflow = CoordinateConverter.check_overflow(
            adjusted, container_width, container_height
        )

        if overflow["has_overflow"]:
            if preserve_aspect_ratio:
                # Calculate aspect ratio
                aspect_ratio = adjusted["width"] / adjusted["height"]

                # Calculate maximum possible size that fits
                max_width = container_width - adjusted["x"]
                max_height = container_height - adjusted["y"]

                # Scale to fit while preserving aspect ratio
                if max_width / aspect_ratio <= max_height:
                    # Constrained by width
                    adjusted["width"] = max_width
                    adjusted["height"] = round(max_width / aspect_ratio)
                else:
                    # Constrained by height
                    adjusted["height"] = max_height
                    adjusted["width"] = round(max_height * aspect_ratio)
            else:
                # Simply clamp to container bounds
                adjusted["width"] = min(
                    adjusted["width"], container_width - adjusted["x"]
                )
                adjusted["height"] = min(
                    adjusted["height"], container_height - adjusted["y"]
                )

        return adjusted

    @staticmethod
    def generate_absolute_css(
        position: dict,
        z_index: int = 1,
        container_width: int = 1280,
        container_height: int = 720,
        prevent_overflow: bool = True,
    ) -> str:
        """Generate CSS for absolute positioning with optional overflow prevention.

        Args:
            position: Position dictionary with x, y, width, height
            z_index: Z-index for element layering
            container_width: Container width in pixels (default: 1280)
            container_height: Container height in pixels (default: 720)
            prevent_overflow: Whether to prevent element overflow

        Returns:
            str: CSS string for absolute positioning
        """
        if position is None:
            return ""

        # Apply overflow prevention if requested
        if prevent_overflow:
            position = CoordinateConverter.prevent_overflow(
                position, container_width, container_height
            )

        return f"""position: absolute; left: {position["x"]}px; top: {position["y"]}px; width: {position["width"]}px; height: {position["height"]}px; z-index: {z_index};"""


class ZIndexLayers:
    """Z-index management for element layering in absolute positioning mode.

    Provides a hierarchical z-index system to ensure proper element layering
    that matches PowerPoint's element stacking order. Elements are assigned
    z-index values based on their type and order within the slide.

    Z-index Hierarchy:
        - Background: 0 (slide backgrounds)
        - Shapes: 100+ (shapes and text boxes)
        - Text: 200+ (text elements)
        - Images: 300+ (pictures and graphics)
        - Overlays: 400+ (overlays and special elements)

    Each element type gets a base z-index plus its order in the slide,
    ensuring proper layering within each type.
    """

    BACKGROUND = 0
    SHAPES = 100
    TEXT = 200
    IMAGES = 300
    OVERLAYS = 400

    @staticmethod
    def get_element_z_index(element_type: str, order: int = 0) -> int:
        """Get z-index for element type.

        Args:
            element_type: Type of element (shape, text, image, group)
            order: Order of element in slide (0-based)

        Returns:
            int: Z-index value
        """
        base_z = {
            "shape": ZIndexLayers.SHAPES,
            "text": ZIndexLayers.TEXT,
            "image": ZIndexLayers.IMAGES,
            "group": ZIndexLayers.SHAPES,
        }.get(element_type, ZIndexLayers.SHAPES)

        return base_z + order


class PositioningConfig:
    """Configuration for positioning modes in version 0.2.6.

    Manages configuration settings for different positioning modes:
    - RESPONSIVE: Original flexbox-based layout that adapts to screen size
    - ABSOLUTE: Fixed 1280x720 container with pixel-perfect positioning
    - HYBRID: Combination mode (planned for future implementation)

    The absolute positioning mode provides pixel-perfect rendering that matches
    PowerPoint's exact layout, while responsive mode maintains flexible layouts
    suitable for various screen sizes.
    """

    RESPONSIVE = "responsive"
    ABSOLUTE = "absolute"
    HYBRID = "hybrid"

    def __init__(self, mode=RESPONSIVE):
        self.mode = mode
        # Use actual slide dimensions from Galaxy presentation (16:9 aspect ratio)
        self.slide_width = 1280
        self.slide_height = 720
        self.enable_scaling = True
        self.z_index_auto = True


def get_gradient_css(gradient_fill: GradientFill) -> str:
    """Generate CSS for a linear gradient background.

    Args:
        gradient_fill: GradientFill object containing gradient information

    Returns:
        str: CSS linear-gradient property
    """
    if not gradient_fill or not gradient_fill.stops:
        return ""

    # PowerPoint rotation is in 60000ths of a degree. Convert to CSS degrees.
    # Add 180 degrees to manually flip the gradient direction
    angle = gradient_fill.angle if gradient_fill.angle is not None else 0
    css_angle = (angle + 180) % 360

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


def get_paragraph_style_css(paragraph: Paragraph, placeholder_type: str = None) -> str:
    """Generate CSS styles for paragraph-level formatting.

    Args:
        paragraph: Paragraph object
        placeholder_type: Placeholder type for layout-based defaults

    Returns:
        str: CSS styles for the paragraph
    """
    styles = []

    # Add text alignment
    if paragraph.properties and paragraph.properties.align:
        alignment_map = {
            "l": "left",  # PowerPoint uses "l" for left
            "r": "right",  # PowerPoint uses "r" for right
            "ctr": "center",  # PowerPoint uses "ctr" for center
            "just": "justify",  # PowerPoint uses "just" for justify
        }
        if paragraph.properties.align in alignment_map:
            styles.append(f"text-align: {alignment_map[paragraph.properties.align]};")
    # Remove hard-coded alignment override - use XML-based alignment instead

    return " ".join(styles)


def get_text_frame_alignment_css(text_frame) -> str:
    """Generate CSS for text frame vertical and horizontal alignment.

    Args:
        text_frame: TextFrame object with anchor and alignment properties

    Returns:
        str: CSS flexbox properties for alignment
    """
    if not text_frame:
        return ""

    styles = []

    # Add flexbox container
    styles.append("display: flex; flex-direction: column;")

    # Vertical alignment based on anchor attribute
    if text_frame.anchor:
        anchor_map = {
            "t": "flex-start",  # top
            "ctr": "center",  # center
            "b": "flex-end",  # bottom
            "just": "stretch",  # justified
            "dist": "space-between",  # distributed
        }
        if text_frame.anchor in anchor_map:
            styles.append(f"justify-content: {anchor_map[text_frame.anchor]};")

    # Horizontal centering if anchor_ctr is true
    if text_frame.anchor_ctr:
        styles.append("align-items: center;")

    return " ".join(styles)


def get_run_style_css(
    run: TextRun,
    theme_resolver=None,
    placeholder_type=None,
    slide_background_color=None,
) -> str:
    """Generate CSS styles for text run formatting.

    Args:
        run: TextRun object containing text formatting
        theme_resolver: ThemeResolver instance for theme-based styling
        placeholder_type: Placeholder type (title, body, etc.) for default sizing

    Returns:
        str: CSS styles for the text run
    """
    styles = []

    # Add font properties
    if run.properties:
        # Font family - use placeholder-based font selection or explicit font face
        if run.properties.font_face:
            styles.append(f"font-family: '{run.properties.font_face}';")
        else:
            # Always use Univers fonts based on placeholder type, or default if no placeholder
            if placeholder_type == "title":
                # Title uses Univers (Headings)
                styles.append(
                    "font-family: 'Univers', 'Arial', 'Helvetica', 'Liberation Sans', 'sans-serif';"
                )
            elif placeholder_type == "body":
                # Body uses Univers (Body) - same font family but different semantic meaning
                styles.append(
                    "font-family: 'Univers', 'Arial', 'Helvetica', 'Liberation Sans', 'sans-serif';"
                )
            else:
                # Default Univers font for any text without specific placeholder type
                styles.append(
                    "font-family: 'Univers', 'Arial', 'Helvetica', 'Liberation Sans', 'sans-serif';"
                )

        if run.properties.font_size:
            # Convert half-points to pixels (approximation)
            font_size_px = run.properties.font_size / 100 * 0.75
            styles.append(f"font-size: {font_size_px}px;")
        elif placeholder_type:
            # Apply slide master default font sizes based on placeholder type
            if placeholder_type == "title":
                # Title style: 40 points from slide master
                styles.append("font-size: 30px;")
            elif placeholder_type == "body":
                # Body style: 28 points from slide master
                styles.append("font-size: 21px;")
            # Add more placeholder types as needed

        if run.properties.bold:
            styles.append("font-weight: bold;")

        if run.properties.italic:
            styles.append("font-style: italic;")

        if run.properties.underline:
            styles.append("text-decoration: underline;")

        # Handle capitalization
        if run.properties.cap:
            if run.properties.cap == "all":
                styles.append("text-transform: uppercase;")
            elif run.properties.cap == "small":
                styles.append("text-transform: lowercase;")

        # Color - use explicit color or theme color
        if run.properties.color:
            styles.append(f"color: #{run.properties.color};")
        elif theme_resolver:
            # Use contrasting text color based on slide background
            if slide_background_color:
                text_color = theme_resolver.get_contrasting_text_color(
                    slide_background_color
                )
            else:
                # Fallback to bg1 color for unknown backgrounds
                text_color = theme_resolver.resolve_scheme_color("bg1")
            styles.append(f"color: #{text_color};")
    else:
        # No run properties - apply defaults
        # Always use Univers font family
        if placeholder_type == "title":
            # Title uses Univers (Headings)
            styles.append(
                "font-family: 'Univers', 'Arial', 'Helvetica', 'Liberation Sans', 'sans-serif';"
            )
            styles.append("font-size: 30px;")
        elif placeholder_type == "body":
            # Body uses Univers (Body)
            styles.append(
                "font-family: 'Univers', 'Arial', 'Helvetica', 'Liberation Sans', 'sans-serif';"
            )
            styles.append("font-size: 21px;")
        else:
            # Default Univers font for any text without specific placeholder type
            styles.append(
                "font-family: 'Univers', 'Arial', 'Helvetica', 'Liberation Sans', 'sans-serif';"
            )
            # Add large font size for main title slides
            styles.append("font-size: 48px;")

        if theme_resolver:
            # Use contrasting text color based on slide background
            if slide_background_color:
                text_color = theme_resolver.get_contrasting_text_color(
                    slide_background_color
                )
            else:
                # Fallback to bg1 color for unknown backgrounds
                text_color = theme_resolver.resolve_scheme_color("bg1")
            styles.append(f"color: #{text_color};")

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
