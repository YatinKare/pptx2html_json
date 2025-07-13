"""
Theme and color resolution system for PowerPoint presentations.
This module handles parsing theme XML files and resolving color references.
"""

import os
import xml.etree.ElementTree as ET


class ColorTransform:
    """Represents a color transformation (tint, shade, lumMod, satMod, alpha)."""

    def __init__(self, transform_type: str, value: int):
        self.transform_type = transform_type
        self.value = value  # Value is typically 0-100000 (percentage * 1000)

    def apply_to_color(self, color: str) -> str:
        """Apply transformation to a hex color string.

        Args:
            color: Hex color string (e.g., "FF0000")

        Returns:
            str: Transformed hex color string
        """
        if len(color) != 6:
            return color

        try:
            # Convert hex to RGB
            r = int(color[0:2], 16)
            g = int(color[2:4], 16)
            b = int(color[4:6], 16)

            # Apply transformation based on type
            factor = self.value / 100000.0  # Convert to decimal percentage

            if self.transform_type == "tint":
                # Tint: blend with white
                r = int(r + (255 - r) * factor)
                g = int(g + (255 - g) * factor)
                b = int(b + (255 - b) * factor)
            elif self.transform_type == "shade":
                # Shade: blend with black
                r = int(r * (1 - factor))
                g = int(g * (1 - factor))
                b = int(b * (1 - factor))
            elif self.transform_type == "lumMod":
                # Luminance modulation
                r = int(r * factor)
                g = int(g * factor)
                b = int(b * factor)
            elif self.transform_type == "satMod":
                # Saturation modulation (simplified implementation)
                # This is a complex operation, using luminance approximation
                luminance = 0.299 * r + 0.587 * g + 0.114 * b
                r = int(luminance + (r - luminance) * factor)
                g = int(luminance + (g - luminance) * factor)
                b = int(luminance + (b - luminance) * factor)

            # Clamp values to valid range
            r = max(0, min(255, r))
            g = max(0, min(255, g))
            b = max(0, min(255, b))

            # Convert back to hex
            return f"{r:02X}{g:02X}{b:02X}"

        except (ValueError, IndexError):
            return color


class ThemeFontScheme:
    """Represents a theme font scheme with major and minor fonts."""

    def __init__(self, name: str = ""):
        self.name = name
        self.major_font = "Calibri"  # Default major font
        self.minor_font = "Calibri"  # Default minor font

    def get_font(self, font_type: str) -> str:
        """Get font by type.

        Args:
            font_type: Font type ("major" or "minor")

        Returns:
            str: Font family name
        """
        if font_type == "major":
            return self.major_font
        elif font_type == "minor":
            return self.minor_font
        else:
            return self.minor_font  # Default to minor font

    def set_major_font(self, font_name: str):
        """Set major font."""
        self.major_font = font_name

    def set_minor_font(self, font_name: str):
        """Set minor font."""
        self.minor_font = font_name


class ThemeColorScheme:
    """Represents a theme color scheme with all base colors."""

    def __init__(self, name: str = ""):
        self.name = name
        self.colors = {
            "dk1": "000000",  # Dark 1 - default black
            "lt1": "FFFFFF",  # Light 1 - default white
            "dk2": "000000",  # Dark 2
            "lt2": "FFFFFF",  # Light 2
            "accent1": "FF0000",  # Accent 1
            "accent2": "00FF00",  # Accent 2
            "accent3": "0000FF",  # Accent 3
            "accent4": "FFFF00",  # Accent 4
            "accent5": "FF00FF",  # Accent 5
            "accent6": "00FFFF",  # Accent 6
            "hlink": "0000FF",  # Hyperlink
            "folHlink": "800080",  # Followed Hyperlink
        }

    def get_color(self, color_name: str) -> str:
        """Get color by name.

        Args:
            color_name: Color name (e.g., "dk1", "accent1")

        Returns:
            str: Hex color string
        """
        return self.colors.get(color_name, "000000")

    def set_color(self, color_name: str, color_value: str):
        """Set color value.

        Args:
            color_name: Color name
            color_value: Hex color string
        """
        self.colors[color_name] = color_value


class ThemeBackgroundFillStyle:
    """Represents a background fill style from the theme."""

    def __init__(self, fill_type: str = "solid"):
        self.fill_type = fill_type  # solid, gradient, pattern, picture
        self.color = "FFFFFF"  # Default white
        self.color_ref = None  # Reference to scheme color
        self.transforms = []  # List of ColorTransform objects
        self.gradient_stops = []  # For gradient fills
        self.image_path = None  # For picture fills

    def resolve_color(self, color_scheme: ThemeColorScheme) -> str:
        """Resolve the actual color for this fill style.

        Args:
            color_scheme: Theme color scheme to resolve references

        Returns:
            str: Resolved hex color string
        """
        # Start with base color
        if self.color_ref:
            base_color = color_scheme.get_color(self.color_ref)
        else:
            base_color = self.color

        # Apply transformations
        result_color = base_color
        for transform in self.transforms:
            result_color = transform.apply_to_color(result_color)

        return result_color


class ThemeResolver:
    """Resolves theme references and color schemes for PowerPoint presentations."""

    def __init__(self, pptx_unpacked_path: str):
        self.pptx_unpacked_path = pptx_unpacked_path
        self.color_scheme = ThemeColorScheme()
        self.font_scheme = ThemeFontScheme()
        self.background_fill_styles = []  # List of ThemeBackgroundFillStyle
        self.color_map = {}  # Slide master color map (bg1 -> dk1, etc.)
        self._load_theme()

    def _load_theme(self):
        """Load theme data from theme XML files."""
        theme_dir = os.path.join(self.pptx_unpacked_path, "ppt", "theme")
        if not os.path.exists(theme_dir):
            return

        # Find theme files (theme12.xml, theme21.xml, etc.)
        # Priority order: theme12.xml (main Galaxy theme), then others
        theme_files = ["theme12.xml", "theme21.xml", "theme33.xml"]
        for filename in theme_files:
            theme_path = os.path.join(theme_dir, filename)
            if os.path.exists(theme_path):
                self._parse_theme_file(theme_path)
                break  # Use first theme file found

    def _parse_theme_file(self, theme_path: str):
        """Parse a theme XML file.

        Args:
            theme_path: Path to theme XML file
        """
        try:
            tree = ET.parse(theme_path)
            root = tree.getroot()

            # Define namespaces
            ns = {"a": "http://schemas.openxmlformats.org/drawingml/2006/main"}

            # Parse color scheme
            color_scheme_elem = root.find(".//a:clrScheme", ns)
            if color_scheme_elem is not None:
                self._parse_color_scheme(color_scheme_elem, ns)

            # Parse font scheme
            font_scheme_elem = root.find(".//a:fontScheme", ns)
            if font_scheme_elem is not None:
                self._parse_font_scheme(font_scheme_elem, ns)

            # Parse background fill styles
            bg_fill_list = root.find(".//a:bgFillStyleLst", ns)
            if bg_fill_list is not None:
                self._parse_background_fill_styles(bg_fill_list, ns)

        except (ET.ParseError, FileNotFoundError) as e:
            print(f"Warning: Could not parse theme file {theme_path}: {e}")

    def _parse_color_scheme(self, color_scheme_elem, ns: dict[str, str]):
        """Parse color scheme from theme XML.

        Args:
            color_scheme_elem: XML element containing color scheme
            ns: XML namespaces
        """
        scheme_name = color_scheme_elem.get("name", "")
        self.color_scheme.name = scheme_name

        # Parse each color - look for direct child elements
        for color_name in [
            "dk1",
            "lt1",
            "dk2",
            "lt2",
            "accent1",
            "accent2",
            "accent3",
            "accent4",
            "accent5",
            "accent6",
            "hlink",
            "folHlink",
        ]:
            color_elem = color_scheme_elem.find(f"a:{color_name}", ns)
            if color_elem is not None:
                color_value = self._extract_color_value(color_elem, ns)
                if color_value:
                    self.color_scheme.set_color(color_name, color_value)

    def _parse_font_scheme(self, font_scheme_elem, ns: dict[str, str]):
        """Parse font scheme from theme XML.

        Args:
            font_scheme_elem: XML element containing font scheme
            ns: XML namespaces
        """
        scheme_name = font_scheme_elem.get("name", "")
        self.font_scheme.name = scheme_name

        # Parse major font
        major_font_elem = font_scheme_elem.find("a:majorFont", ns)
        if major_font_elem is not None:
            latin_elem = major_font_elem.find("a:latin", ns)
            if latin_elem is not None:
                typeface = latin_elem.get("typeface")
                if typeface:
                    self.font_scheme.set_major_font(typeface)

        # Parse minor font
        minor_font_elem = font_scheme_elem.find("a:minorFont", ns)
        if minor_font_elem is not None:
            latin_elem = minor_font_elem.find("a:latin", ns)
            if latin_elem is not None:
                typeface = latin_elem.get("typeface")
                if typeface:
                    self.font_scheme.set_minor_font(typeface)

    def _parse_background_fill_styles(self, bg_fill_list_elem, ns: dict[str, str]):
        """Parse background fill styles from theme XML.

        Args:
            bg_fill_list_elem: XML element containing background fill styles
            ns: XML namespaces
        """
        for fill_elem in bg_fill_list_elem:
            bg_fill_style = ThemeBackgroundFillStyle()

            # Determine fill type and parse accordingly
            if fill_elem.tag.endswith("solidFill"):
                bg_fill_style.fill_type = "solid"
                self._parse_solid_fill(fill_elem, bg_fill_style, ns)
            elif fill_elem.tag.endswith("gradFill"):
                bg_fill_style.fill_type = "gradient"
                self._parse_gradient_fill(fill_elem, bg_fill_style, ns)
            elif fill_elem.tag.endswith("blipFill"):
                bg_fill_style.fill_type = "picture"
                self._parse_picture_fill(fill_elem, bg_fill_style, ns)

            self.background_fill_styles.append(bg_fill_style)

    def _parse_solid_fill(
        self, fill_elem, bg_fill_style: ThemeBackgroundFillStyle, ns: dict[str, str]
    ):
        """Parse solid fill properties.

        Args:
            fill_elem: XML element containing fill properties
            bg_fill_style: Background fill style to populate
            ns: XML namespaces
        """
        # Look for color reference
        scheme_clr = fill_elem.find(".//a:schemeClr", ns)
        if scheme_clr is not None:
            bg_fill_style.color_ref = scheme_clr.get("val")
            # Parse color transformations
            bg_fill_style.transforms = self._parse_color_transforms(scheme_clr, ns)
        else:
            # Look for direct color value
            srgb_clr = fill_elem.find(".//a:srgbClr", ns)
            if srgb_clr is not None:
                bg_fill_style.color = srgb_clr.get("val", "FFFFFF")

    def _parse_gradient_fill(
        self, fill_elem, bg_fill_style: ThemeBackgroundFillStyle, ns: dict[str, str]
    ):
        """Parse gradient fill properties.

        Args:
            fill_elem: XML element containing gradient fill
            bg_fill_style: Background fill style to populate
            ns: XML namespaces
        """
        # For now, use the first gradient stop as the base color
        first_stop = fill_elem.find(".//a:gs", ns)
        if first_stop is not None:
            self._parse_solid_fill(first_stop, bg_fill_style, ns)

    def _parse_picture_fill(
        self, fill_elem, bg_fill_style: ThemeBackgroundFillStyle, ns: dict[str, str]
    ):
        """Parse picture fill properties.

        Args:
            fill_elem: XML element containing picture fill
            bg_fill_style: Background fill style to populate
            ns: XML namespaces
        """
        # Look for blip reference
        blip = fill_elem.find(".//a:blip", ns)
        if blip is not None:
            # This would need relationship resolution - for now, note the reference
            r_embed = blip.get(
                "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed"
            )
            if r_embed:
                bg_fill_style.image_path = r_embed

    def _parse_color_transforms(
        self, color_elem, ns: dict[str, str]
    ) -> list[ColorTransform]:
        """Parse color transformations from a color element.

        Args:
            color_elem: XML element containing color
            ns: XML namespaces

        Returns:
            List[ColorTransform]: List of color transformations
        """
        transforms = []

        for transform_type in ["tint", "shade", "lumMod", "satMod", "alpha"]:
            transform_elem = color_elem.find(f".//a:{transform_type}", ns)
            if transform_elem is not None:
                value = int(transform_elem.get("val", "0"))
                transforms.append(ColorTransform(transform_type, value))

        return transforms

    def _extract_color_value(self, color_elem, ns: dict[str, str]) -> str | None:
        """Extract color value from a color element.

        Args:
            color_elem: XML element containing color
            ns: XML namespaces

        Returns:
            Optional[str]: Hex color string or None
        """
        # Check for sRGB color
        srgb_clr = color_elem.find(".//a:srgbClr", ns)
        if srgb_clr is not None:
            return srgb_clr.get("val")

        # Check for system color
        sys_clr = color_elem.find(".//a:sysClr", ns)
        if sys_clr is not None:
            last_clr = sys_clr.get("lastClr")
            if last_clr:
                return last_clr
            # Map common system colors
            sys_val = sys_clr.get("val", "")
            if sys_val == "windowText":
                return "000000"
            elif sys_val == "window":
                return "FFFFFF"

        return None

    def load_slide_master_color_map(self, slide_master_path: str):
        """Load color map from slide master XML.

        Args:
            slide_master_path: Path to slide master XML file
        """
        try:
            tree = ET.parse(slide_master_path)
            root = tree.getroot()

            ns = {"p": "http://schemas.openxmlformats.org/presentationml/2006/main"}

            # Find color map
            clr_map = root.find(".//p:clrMap", ns)
            if clr_map is not None:
                # Parse color map attributes
                for attr_name, attr_value in clr_map.attrib.items():
                    self.color_map[attr_name] = attr_value

        except (ET.ParseError, FileNotFoundError) as e:
            print(f"Warning: Could not parse slide master {slide_master_path}: {e}")

    def resolve_background_reference(
        self, bg_ref_idx: int, scheme_color: str = None
    ) -> str | None:
        """Resolve background reference to actual color.

        Args:
            bg_ref_idx: Background reference index (1001+ for background fill styles)
            scheme_color: Optional scheme color override (e.g., "bg1")

        Returns:
            Optional[str]: Resolved hex color string
        """
        if bg_ref_idx == 0 or bg_ref_idx == 1000:
            return None  # No background

        if bg_ref_idx >= 1001:
            # Background fill style reference
            style_index = bg_ref_idx - 1001
            if 0 <= style_index < len(self.background_fill_styles):
                bg_style = self.background_fill_styles[style_index]

                # If scheme color is specified, use it instead of the style's color reference
                if scheme_color:
                    # Resolve scheme color through color map
                    mapped_color = self.color_map.get(scheme_color, scheme_color)
                    base_color = self.color_scheme.get_color(mapped_color)

                    # Apply any transformations from the background style
                    result_color = base_color
                    for transform in bg_style.transforms:
                        result_color = transform.apply_to_color(result_color)
                    return result_color
                else:
                    # Use the background style's color reference
                    if bg_style.color_ref == "phClr":
                        # phClr is a placeholder - use a default color
                        return "FFFFFF"  # Default to white
                    return bg_style.resolve_color(self.color_scheme)

        return None

    def resolve_scheme_color(
        self, scheme_color: str, transforms: list[ColorTransform] = None
    ) -> str:
        """Resolve scheme color reference to hex color.

        Args:
            scheme_color: Scheme color name (e.g., "tx1", "bg1", "accent1")
            transforms: Optional color transformations to apply

        Returns:
            str: Resolved hex color string
        """
        # Map scheme color through color map if needed
        mapped_color = self.color_map.get(scheme_color, scheme_color)
        base_color = self.color_scheme.get_color(mapped_color)

        # Apply transformations
        if transforms:
            result_color = base_color
            for transform in transforms:
                result_color = transform.apply_to_color(result_color)
            return result_color

        return base_color

    def get_background_css(self, bg_ref_idx: int, scheme_color: str = None) -> str:
        """Generate CSS background property for background reference.

        Args:
            bg_ref_idx: Background reference index
            scheme_color: Optional scheme color override

        Returns:
            str: CSS background property
        """
        color = self.resolve_background_reference(bg_ref_idx, scheme_color)
        if color:
            return f"background-color: #{color};"
        return ""

    def get_font_family(self, font_ref: str = "minor") -> str:
        """Get font family for font reference.

        Args:
            font_ref: Font reference ("major", "minor", or specific font name)

        Returns:
            str: Font family name
        """
        if font_ref in ["major", "minor"]:
            font_name = self.font_scheme.get_font(font_ref)
        else:
            # Direct font name reference
            font_name = font_ref

        return font_name

    def get_font_css(self, font_ref: str = "minor", fallbacks: list[str] = None) -> str:
        """Generate CSS font-family property with web font fallbacks.

        Args:
            font_ref: Font reference ("major", "minor", or specific font name)
            fallbacks: List of fallback fonts

        Returns:
            str: CSS font-family property
        """
        primary_font = self.get_font_family(font_ref)

        # Default fallbacks based on font type
        if fallbacks is None:
            fallbacks = self._get_default_fallbacks(primary_font)

        # Build font stack
        font_stack = [f'"{primary_font}"'] + [f'"{font}"' for font in fallbacks]
        return f"font-family: {', '.join(font_stack)};"

    def _get_default_fallbacks(self, primary_font: str) -> list[str]:
        """Get default fallback fonts for a primary font.

        Args:
            primary_font: Primary font name

        Returns:
            List[str]: List of fallback font names
        """
        # Common web-safe fallbacks
        default_fallbacks = ["Arial", "Helvetica", "sans-serif"]

        # Font-specific fallbacks
        font_fallbacks = {
            "Univers": ["Arial", "Helvetica", "Liberation Sans", "sans-serif"],
            "Calibri": ["Arial", "Helvetica", "sans-serif"],
            "Times New Roman": ["Times", "serif"],
            "Georgia": ["Times New Roman", "Times", "serif"],
            "Courier New": ["Courier", "monospace"],
        }

        return font_fallbacks.get(primary_font, default_fallbacks)

    def get_contrasting_text_color(self, background_color: str = None) -> str:
        """Get a contrasting text color based on background.

        Args:
            background_color: Hex background color (e.g., "FFFFFF")

        Returns:
            str: Contrasting hex color string (either black or white)
        """
        if not background_color:
            # Default to white text for unknown backgrounds
            return "FFFFFF"

        try:
            # Convert hex to RGB
            r = int(background_color[0:2], 16)
            g = int(background_color[2:4], 16)
            b = int(background_color[4:6], 16)

            # Calculate luminance using the relative luminance formula
            # Y = 0.2126 * R + 0.7152 * G + 0.0722 * B
            luminance = (0.2126 * r + 0.7152 * g + 0.0722 * b) / 255

            # Use black text for light backgrounds, white text for dark backgrounds
            if luminance > 0.5:
                return "000000"  # Black text for light backgrounds
            else:
                return "FFFFFF"  # White text for dark backgrounds

        except (ValueError, IndexError):
            # Fallback to white text if parsing fails
            return "FFFFFF"
