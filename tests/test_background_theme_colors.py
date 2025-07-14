"""
Tests for theme color resolution accuracy in background generation.
Testing the correct resolution of scheme colors to actual hex colors.
"""

import os
import tempfile
from PIL import Image

import pytest

from learnx_parser.models.core import (
    BackgroundReference,
    CommonSlideData,
    GradientFill,
    GradientStop,
)
from learnx_parser.services.background_renderer import BackgroundRenderer


class TestBackgroundThemeColorResolution:
    """Test suite for theme color resolution in background generation."""

    def setup_method(self):
        """Set up test fixtures."""
        self.renderer = BackgroundRenderer(slide_width=100, slide_height=100)  # Small size for testing
        self.temp_dir = tempfile.mkdtemp()

    def teardown_method(self):
        """Clean up test fixtures."""
        import shutil
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_galaxy_theme_bg1_resolution(self):
        """Test that bg1 scheme color resolves to black for Galaxy theme."""
        bg_ref = BackgroundReference(idx=1001, scheme_color="bg1")
        common_slide_data = CommonSlideData(background_reference=bg_ref)
        
        output_path = os.path.join(self.temp_dir, "bg1_test.png")
        
        # Test with Galaxy theme colors
        galaxy_theme = {"bg1": "#000000"}
        
        result_path = self.renderer.generate_background_image(
            common_slide_data, output_path, galaxy_theme
        )
        
        assert result_path == output_path
        assert os.path.exists(output_path)
        
        # Verify the color is actually black
        with Image.open(output_path) as img:
            pixel = img.getpixel((50, 50))  # Center pixel
            assert pixel == (0, 0, 0)  # RGB for black

    def test_galaxy_theme_accent_colors_resolution(self):
        """Test that Galaxy theme accent colors resolve correctly."""
        galaxy_theme = {
            "accent2": "#243FFF",  # Blue
            "accent4": "#FF9022",  # Orange
            "bg1": "#000000",      # Black
            "bg2": "#FFFFFF"       # White
        }
        
        test_cases = [
            ("accent2", (36, 63, 255)),    # Blue RGB
            ("accent4", (255, 144, 34)),   # Orange RGB  
            ("bg1", (0, 0, 0)),           # Black RGB
            ("bg2", (255, 255, 255))      # White RGB
        ]
        
        for scheme_color, expected_rgb in test_cases:
            bg_ref = BackgroundReference(idx=1001, scheme_color=scheme_color)
            common_slide_data = CommonSlideData(background_reference=bg_ref)
            
            output_path = os.path.join(self.temp_dir, f"{scheme_color}_test.png")
            
            result_path = self.renderer.generate_background_image(
                common_slide_data, output_path, galaxy_theme
            )
            
            assert result_path == output_path
            assert os.path.exists(output_path)
            
            # Verify the color matches expected RGB
            with Image.open(output_path) as img:
                pixel = img.getpixel((50, 50))
                assert pixel == expected_rgb, f"Failed for {scheme_color}: got {pixel}, expected {expected_rgb}"

    def test_theme_color_fallback_to_defaults(self):
        """Test that scheme colors fall back to defaults when no theme is provided."""
        # Only bg1 has special hardcoded fallback in _render_background_reference
        # Other scheme colors need to be tested via gradient or _resolve_color
        
        # Test bg1 background reference (has hardcoded fallback)
        bg_ref = BackgroundReference(idx=1001, scheme_color="bg1")
        common_slide_data = CommonSlideData(background_reference=bg_ref)
        
        output_path = os.path.join(self.temp_dir, "default_bg1.png")
        
        # No theme colors provided - should use defaults
        result_path = self.renderer.generate_background_image(
            common_slide_data, output_path
        )
        
        assert result_path == output_path
        assert os.path.exists(output_path)
        
        with Image.open(output_path) as img:
            pixel = img.getpixel((50, 50))
            assert pixel == (0, 0, 0), "Default color failed for bg1"
        
        # Test other scheme colors via gradient (uses _resolve_color with defaults)
        gradient_test_cases = [
            ("accent2", (36, 63, 255)),   # Blue
            ("accent4", (255, 144, 34))   # Orange
        ]
        
        for scheme_color, expected_rgb in gradient_test_cases:
            gradient_stops = [
                GradientStop(pos=0, color=None, scheme_color=scheme_color),
                GradientStop(pos=100000, color=None, scheme_color=scheme_color)
            ]
            gradient = GradientFill(stops=gradient_stops, angle=0)
            common_slide_data = CommonSlideData(background_gradient_fill=gradient)
            
            output_path = os.path.join(self.temp_dir, f"default_{scheme_color}_gradient.png")
            
            result_path = self.renderer.generate_background_image(
                common_slide_data, output_path
            )
            
            assert result_path == output_path
            assert os.path.exists(output_path)
            
            with Image.open(output_path) as img:
                pixel = img.getpixel((50, 50))
                assert pixel == expected_rgb, f"Default color failed for {scheme_color} in gradient"

    def test_white_background_with_theme_colors(self):
        """Test that white backgrounds are generated when theme colors are provided."""
        bg_ref = BackgroundReference(idx=1001, scheme_color="bg2")
        common_slide_data = CommonSlideData(background_reference=bg_ref)
        
        output_path = os.path.join(self.temp_dir, "white_bg.png")
        
        # Provide theme colors to ensure bg2 resolves
        theme_colors = {"bg2": "#FFFFFF"}
        
        result_path = self.renderer.generate_background_image(
            common_slide_data, output_path, theme_colors
        )
        
        # White backgrounds should be generated when theme is provided
        assert result_path == output_path
        assert os.path.exists(output_path)
        
        with Image.open(output_path) as img:
            pixel = img.getpixel((50, 50))
            assert pixel == (255, 255, 255)  # RGB for white

    def test_background_reference_fallback_limitation(self):
        """Test documenting current limitation: bg2 without theme colors doesn't generate."""
        bg_ref = BackgroundReference(idx=1001, scheme_color="bg2")
        common_slide_data = CommonSlideData(background_reference=bg_ref)
        
        output_path = os.path.join(self.temp_dir, "bg2_no_theme.png")
        
        # No theme colors provided - bg2 won't generate (current limitation)
        result_path = self.renderer.generate_background_image(
            common_slide_data, output_path
        )
        
        # Current implementation limitation: only bg1 has hardcoded fallback
        assert result_path is None
        assert not os.path.exists(output_path)

    def test_gradient_theme_color_resolution(self):
        """Test theme color resolution in gradient backgrounds."""
        gradient_stops = [
            GradientStop(pos=0, color=None, scheme_color="accent2"),      # Blue
            GradientStop(pos=100000, color=None, scheme_color="accent4")  # Orange
        ]
        gradient = GradientFill(stops=gradient_stops, angle=2700000)  # Vertical
        
        common_slide_data = CommonSlideData(background_gradient_fill=gradient)
        
        output_path = os.path.join(self.temp_dir, "gradient_theme.png")
        
        galaxy_theme = {
            "accent2": "#243FFF",  # Blue
            "accent4": "#FF9022"   # Orange
        }
        
        result_path = self.renderer.generate_background_image(
            common_slide_data, output_path, galaxy_theme
        )
        
        assert result_path == output_path
        assert os.path.exists(output_path)
        
        with Image.open(output_path) as img:
            # Check top pixel (should be more blue)
            top_pixel = img.getpixel((50, 10))
            # Check bottom pixel (should be more orange)
            bottom_pixel = img.getpixel((50, 90))
            
            # Top should have more blue component
            assert top_pixel[2] > bottom_pixel[2], "Top should be bluer"
            # Bottom should have more red component (orange)
            assert bottom_pixel[0] > top_pixel[0], "Bottom should be more orange"

    def test_mixed_color_types_in_gradient(self):
        """Test gradient with both direct colors and scheme colors."""
        gradient_stops = [
            GradientStop(pos=0, color="FF0000", scheme_color=None),       # Direct red
            GradientStop(pos=100000, color=None, scheme_color="accent2")  # Scheme blue
        ]
        gradient = GradientFill(stops=gradient_stops, angle=0)  # Horizontal
        
        common_slide_data = CommonSlideData(background_gradient_fill=gradient)
        
        output_path = os.path.join(self.temp_dir, "mixed_gradient.png")
        
        theme_colors = {"accent2": "#0000FF"}  # Blue
        
        result_path = self.renderer.generate_background_image(
            common_slide_data, output_path, theme_colors
        )
        
        assert result_path == output_path
        assert os.path.exists(output_path)
        
        with Image.open(output_path) as img:
            # Should generate successfully with mixed color types
            assert img.size == (100, 100)

    def test_unknown_scheme_color_handling(self):
        """Test handling of unknown scheme colors."""
        bg_ref = BackgroundReference(idx=1001, scheme_color="unknownColor")
        common_slide_data = CommonSlideData(background_reference=bg_ref)
        
        output_path = os.path.join(self.temp_dir, "unknown_color.png")
        
        result_path = self.renderer.generate_background_image(
            common_slide_data, output_path
        )
        
        # Should return None for unknown colors
        assert result_path is None
        assert not os.path.exists(output_path)

    def test_scheme_color_with_hash_prefix(self):
        """Test that theme colors work with or without # prefix."""
        test_cases = [
            {"accent2": "#FF0000"},  # With hash
            {"accent2": "FF0000"}    # Without hash
        ]
        
        for i, theme_colors in enumerate(test_cases):
            bg_ref = BackgroundReference(idx=1001, scheme_color="accent2")
            common_slide_data = CommonSlideData(background_reference=bg_ref)
            
            output_path = os.path.join(self.temp_dir, f"hash_test_{i}.png")
            
            result_path = self.renderer.generate_background_image(
                common_slide_data, output_path, theme_colors
            )
            
            assert result_path == output_path
            assert os.path.exists(output_path)
            
            # Both should result in red color
            with Image.open(output_path) as img:
                pixel = img.getpixel((50, 50))
                assert pixel == (255, 0, 0), f"Hash test {i} failed"

    def test_case_sensitive_scheme_colors(self):
        """Test that scheme color names are case-sensitive."""
        bg_ref = BackgroundReference(idx=1001, scheme_color="BG1")  # Uppercase
        common_slide_data = CommonSlideData(background_reference=bg_ref)
        
        output_path = os.path.join(self.temp_dir, "case_test.png")
        
        theme_colors = {"bg1": "#FF0000"}  # lowercase in theme
        
        result_path = self.renderer.generate_background_image(
            common_slide_data, output_path, theme_colors
        )
        
        # The implementation looks for exact match but falls back to defaults
        # BG1 (uppercase) should fall back to defaults if available
        # Since BG1 is not in defaults, it should return None
        if result_path:
            # If it does generate (fallback worked), verify the color
            assert os.path.exists(output_path)
            with Image.open(output_path) as img:
                pixel = img.getpixel((50, 50))
                # Should use default for bg1 (black) since uppercase BG1 isn't found
                assert pixel == (0, 0, 0)
        else:
            # If no fallback, that's also valid behavior
            assert not os.path.exists(output_path)

    def test_color_resolution_helper_methods(self):
        """Test the internal color resolution methods of BackgroundRenderer."""
        # Test _resolve_color method directly
        
        # Test with direct color
        resolved = self.renderer._resolve_color("FF0000", None, None)
        assert resolved == "#FF0000"
        
        # Test with scheme color and theme
        theme = {"accent2": "#0000FF"}
        resolved = self.renderer._resolve_color(None, "accent2", theme)
        assert resolved == "#0000FF"
        
        # Test with scheme color and default
        resolved = self.renderer._resolve_color(None, "bg1", None)
        assert resolved == "#000000"  # Default for bg1
        
        # Test with unknown scheme color
        resolved = self.renderer._resolve_color(None, "unknown", None)
        assert resolved is None

    def test_hex_to_rgb_conversion(self):
        """Test the internal hex to RGB conversion method."""
        # Test valid hex colors
        assert self.renderer._hex_to_rgb("#FF0000") == (255, 0, 0)
        assert self.renderer._hex_to_rgb("FF0000") == (255, 0, 0)
        assert self.renderer._hex_to_rgb("#00FF00") == (0, 255, 0)
        assert self.renderer._hex_to_rgb("0000FF") == (0, 0, 255)
        assert self.renderer._hex_to_rgb("FFFFFF") == (255, 255, 255)
        assert self.renderer._hex_to_rgb("000000") == (0, 0, 0)
        
        # Test invalid hex colors
        assert self.renderer._hex_to_rgb("invalid") is None
        assert self.renderer._hex_to_rgb("FF00") is None  # Too short
        assert self.renderer._hex_to_rgb("FF00000") is None  # Too long