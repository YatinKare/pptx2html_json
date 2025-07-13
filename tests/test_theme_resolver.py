"""Test cases for theme resolution functionality in version 0.2.7."""

import os
import tempfile

from learnx_parser.writers.theme_resolver import (
    ColorTransform,
    ThemeBackgroundFillStyle,
    ThemeColorScheme,
    ThemeResolver,
)


class TestColorTransform:
    """Test color transformation functionality."""

    def test_tint_transform(self):
        """Test tint transformation (blend with white)."""
        transform = ColorTransform("tint", 50000)  # 50%

        # Test with red color
        result = transform.apply_to_color("FF0000")

        # 50% tint: R = 255 + (255-255)*0.5 = 255, G = 0 + (255-0)*0.5 = 127.5, B = 0 + (255-0)*0.5 = 127.5
        # Expected: approximately FF7F7F (light red)
        assert result == "FF7F7F"

    def test_shade_transform(self):
        """Test shade transformation (blend with black)."""
        transform = ColorTransform("shade", 50000)  # 50%

        # Test with white color
        result = transform.apply_to_color("FFFFFF")

        # 50% shade: RGB = 255 * (1-0.5) = 127.5
        # Expected: approximately 7F7F7F (gray)
        assert result == "7F7F7F"

    def test_luminance_modulation(self):
        """Test luminance modulation transformation."""
        transform = ColorTransform("lumMod", 75000)  # 75%

        # Test with red color
        result = transform.apply_to_color("FF0000")

        # 75% lumMod: RGB = original * 0.75
        # Expected: BF0000 (darker red)
        assert result == "BF0000"

    def test_invalid_color(self):
        """Test transformation with invalid color."""
        transform = ColorTransform("tint", 50000)

        # Should return original color unchanged
        assert transform.apply_to_color("invalid") == "invalid"
        assert transform.apply_to_color("FF") == "FF"


class TestThemeColorScheme:
    """Test theme color scheme functionality."""

    def test_default_colors(self):
        """Test default color scheme initialization."""
        scheme = ThemeColorScheme("Test Scheme")

        assert scheme.name == "Test Scheme"
        assert scheme.get_color("dk1") == "000000"  # Black
        assert scheme.get_color("lt1") == "FFFFFF"  # White
        assert scheme.get_color("accent1") == "FF0000"  # Red

    def test_set_and_get_color(self):
        """Test setting and getting colors."""
        scheme = ThemeColorScheme()

        scheme.set_color("accent1", "0000FF")
        assert scheme.get_color("accent1") == "0000FF"

        # Test unknown color returns default
        assert scheme.get_color("unknown") == "000000"


class TestThemeBackgroundFillStyle:
    """Test theme background fill style functionality."""

    def test_solid_fill_with_direct_color(self):
        """Test solid fill with direct color."""
        fill_style = ThemeBackgroundFillStyle("solid")
        fill_style.color = "FF0000"

        scheme = ThemeColorScheme()
        result = fill_style.resolve_color(scheme)

        assert result == "FF0000"

    def test_solid_fill_with_color_reference(self):
        """Test solid fill with color reference."""
        fill_style = ThemeBackgroundFillStyle("solid")
        fill_style.color_ref = "accent1"

        scheme = ThemeColorScheme()
        scheme.set_color("accent1", "00FF00")

        result = fill_style.resolve_color(scheme)
        assert result == "00FF00"

    def test_color_with_transforms(self):
        """Test color resolution with transformations."""
        fill_style = ThemeBackgroundFillStyle("solid")
        fill_style.color_ref = "dk1"
        fill_style.transforms = [ColorTransform("tint", 75000)]  # 75% tint

        scheme = ThemeColorScheme()
        scheme.set_color("dk1", "000000")  # Black

        result = fill_style.resolve_color(scheme)

        # 75% tint of black: 0 + (255-0)*0.75 = 191.25 ≈ BF
        assert result == "BFBFBF"


class TestThemeResolver:
    """Test theme resolver functionality."""

    def create_test_theme_xml(self, temp_dir: str) -> str:
        """Create a test theme XML file.

        Args:
            temp_dir: Temporary directory path

        Returns:
            str: Path to created theme file
        """
        theme_content = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<a:theme xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" name="TestTheme">
    <a:themeElements>
        <a:clrScheme name="TestColors">
            <a:dk1><a:sysClr val="windowText" lastClr="000000"/></a:dk1>
            <a:lt1><a:sysClr val="window" lastClr="FFFFFF"/></a:lt1>
            <a:dk2><a:srgbClr val="1F497D"/></a:dk2>
            <a:lt2><a:srgbClr val="EEECE1"/></a:lt2>
            <a:accent1><a:srgbClr val="4F81BD"/></a:accent1>
            <a:accent2><a:srgbClr val="F79646"/></a:accent2>
            <a:accent3><a:srgbClr val="9BBB59"/></a:accent3>
            <a:accent4><a:srgbClr val="8064A2"/></a:accent4>
            <a:accent5><a:srgbClr val="4BACC6"/></a:accent5>
            <a:accent6><a:srgbClr val="F366A7"/></a:accent6>
            <a:hlink><a:srgbClr val="0000FF"/></a:hlink>
            <a:folHlink><a:srgbClr val="800080"/></a:folHlink>
        </a:clrScheme>
        <a:fmtScheme name="Office">
            <a:bgFillStyleLst>
                <a:solidFill>
                    <a:schemeClr val="phClr"/>
                </a:solidFill>
                <a:solidFill>
                    <a:schemeClr val="phClr">
                        <a:tint val="95000"/>
                    </a:schemeClr>
                </a:solidFill>
                <a:gradFill rotWithShape="1">
                    <a:gsLst>
                        <a:gs pos="0">
                            <a:schemeClr val="phClr">
                                <a:tint val="93000"/>
                            </a:schemeClr>
                        </a:gs>
                    </a:gsLst>
                </a:gradFill>
            </a:bgFillStyleLst>
        </a:fmtScheme>
    </a:themeElements>
</a:theme>"""

        ppt_dir = os.path.join(temp_dir, "ppt")
        theme_dir = os.path.join(ppt_dir, "theme")
        os.makedirs(theme_dir, exist_ok=True)

        theme_path = os.path.join(theme_dir, "theme1.xml")
        with open(theme_path, "w", encoding="utf-8") as f:
            f.write(theme_content)

        return theme_path

    def create_test_slide_master_xml(self, temp_dir: str) -> str:
        """Create a test slide master XML file.

        Args:
            temp_dir: Temporary directory path

        Returns:
            str: Path to created slide master file
        """
        master_content = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:sldMaster xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" 
             xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">
    <p:cSld>
        <p:bg>
            <p:bgRef idx="1001">
                <a:schemeClr val="bg1"/>
            </p:bgRef>
        </p:bg>
    </p:cSld>
    <p:clrMap bg1="lt1" tx1="dk1" bg2="lt2" tx2="dk2" 
             accent1="accent1" accent2="accent2" accent3="accent3" 
             accent4="accent4" accent5="accent5" accent6="accent6" 
             hlink="hlink" folHlink="folHlink"/>
</p:sldMaster>"""

        ppt_dir = os.path.join(temp_dir, "ppt")
        masters_dir = os.path.join(ppt_dir, "slideMasters")
        os.makedirs(masters_dir, exist_ok=True)

        master_path = os.path.join(masters_dir, "slideMaster1.xml")
        with open(master_path, "w", encoding="utf-8") as f:
            f.write(master_content)

        return master_path

    def test_theme_resolver_initialization(self):
        """Test theme resolver initialization with test files."""
        with tempfile.TemporaryDirectory() as temp_dir:
            # Create test theme file
            self.create_test_theme_xml(temp_dir)
            self.create_test_slide_master_xml(temp_dir)

            # Initialize theme resolver
            resolver = ThemeResolver(temp_dir)

            # Test color scheme was loaded
            assert resolver.color_scheme.name == "TestColors"
            assert resolver.color_scheme.get_color("dk1") == "000000"
            assert resolver.color_scheme.get_color("accent1") == "4F81BD"

            # Test background fill styles were loaded
            assert len(resolver.background_fill_styles) == 3
            assert resolver.background_fill_styles[0].fill_type == "solid"

    def test_color_map_loading(self):
        """Test color map loading from slide master."""
        with tempfile.TemporaryDirectory() as temp_dir:
            self.create_test_theme_xml(temp_dir)
            master_path = self.create_test_slide_master_xml(temp_dir)

            resolver = ThemeResolver(temp_dir)
            resolver.load_slide_master_color_map(master_path)

            # Test color map was loaded
            assert resolver.color_map["bg1"] == "lt1"
            assert resolver.color_map["tx1"] == "dk1"

    def test_background_reference_resolution(self):
        """Test background reference resolution."""
        with tempfile.TemporaryDirectory() as temp_dir:
            self.create_test_theme_xml(temp_dir)
            master_path = self.create_test_slide_master_xml(temp_dir)

            resolver = ThemeResolver(temp_dir)
            resolver.load_slide_master_color_map(master_path)

            # Test background reference resolution
            # bg1 -> lt1 -> FFFFFF (white)
            result = resolver.resolve_background_reference(1001, "bg1")
            assert result == "FFFFFF"

            # Test no background
            result = resolver.resolve_background_reference(0)
            assert result is None

            result = resolver.resolve_background_reference(1000)
            assert result is None

    def test_scheme_color_resolution(self):
        """Test scheme color resolution."""
        with tempfile.TemporaryDirectory() as temp_dir:
            self.create_test_theme_xml(temp_dir)
            master_path = self.create_test_slide_master_xml(temp_dir)

            resolver = ThemeResolver(temp_dir)
            resolver.load_slide_master_color_map(master_path)

            # Test direct scheme color resolution
            result = resolver.resolve_scheme_color("accent1")
            assert result == "4F81BD"

            # Test mapped scheme color resolution
            result = resolver.resolve_scheme_color("bg1")  # bg1 -> lt1 -> FFFFFF
            assert result == "FFFFFF"

            # Test with transformations
            transforms = [ColorTransform("tint", 50000)]
            result = resolver.resolve_scheme_color(
                "dk1", transforms
            )  # Black with 50% tint
            assert result == "7F7F7F"

    def test_background_css_generation(self):
        """Test CSS background generation."""
        with tempfile.TemporaryDirectory() as temp_dir:
            self.create_test_theme_xml(temp_dir)
            master_path = self.create_test_slide_master_xml(temp_dir)

            resolver = ThemeResolver(temp_dir)
            resolver.load_slide_master_color_map(master_path)

            # Test CSS generation
            css = resolver.get_background_css(1001, "bg1")
            assert css == "background-color: #FFFFFF;"

            # Test no background
            css = resolver.get_background_css(0)
            assert css == ""
