"""
Tests for background image generation using Pillow.
Testing the BackgroundRenderer service for generating PNG images from background properties.
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


class TestBackgroundImageGeneration:
    """Test suite for background image generation with Pillow."""

    def setup_method(self):
        """Set up test fixtures."""
        self.renderer = BackgroundRenderer(slide_width=1280, slide_height=720)
        self.temp_dir = tempfile.mkdtemp()

    def teardown_method(self):
        """Clean up test fixtures."""
        # Clean up any generated test files
        import shutil
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_solid_color_background_generation(self):
        """Test generating PNG image from solid color background."""
        common_slide_data = CommonSlideData(
            background_color="FF0000",  # Red background
            cx=1280,
            cy=720
        )
        
        output_path = os.path.join(self.temp_dir, "solid_background.png")
        
        result_path = self.renderer.generate_background_image(
            common_slide_data, output_path
        )
        
        # Verify image was generated
        assert result_path == output_path
        assert os.path.exists(output_path)
        
        # Verify image properties
        with Image.open(output_path) as img:
            assert img.size == (1280, 720)
            assert img.mode == "RGB"
            
            # Check that the image is actually red
            # Sample pixel from center should be red
            center_pixel = img.getpixel((640, 360))
            assert center_pixel == (255, 0, 0)  # RGB for red

    def test_gradient_background_generation(self):
        """Test generating PNG image from gradient background."""
        gradient_stops = [
            GradientStop(pos=0, color="FF0000", scheme_color=None),      # Red start
            GradientStop(pos=100000, color="0000FF", scheme_color=None)  # Blue end
        ]
        gradient = GradientFill(stops=gradient_stops, angle=2700000)  # Vertical gradient
        
        common_slide_data = CommonSlideData(
            background_gradient_fill=gradient,
            cx=1280,
            cy=720
        )
        
        output_path = os.path.join(self.temp_dir, "gradient_background.png")
        
        result_path = self.renderer.generate_background_image(
            common_slide_data, output_path
        )
        
        # Verify image was generated
        assert result_path == output_path
        assert os.path.exists(output_path)
        
        # Verify image properties
        with Image.open(output_path) as img:
            assert img.size == (1280, 720)
            assert img.mode == "RGB"
            
            # Check gradient - top should be more red, bottom should be more blue
            top_pixel = img.getpixel((640, 100))
            bottom_pixel = img.getpixel((640, 620))
            
            # Top should have more red component
            assert top_pixel[0] > bottom_pixel[0]  # More red at top
            # Bottom should have more blue component  
            assert bottom_pixel[2] > top_pixel[2]  # More blue at bottom

    def test_background_reference_generation(self):
        """Test generating PNG image from background reference with theme colors."""
        bg_ref = BackgroundReference(idx=1001, scheme_color="bg1")
        
        common_slide_data = CommonSlideData(
            background_reference=bg_ref,
            cx=1280,
            cy=720
        )
        
        output_path = os.path.join(self.temp_dir, "reference_background.png")
        
        # Test with Galaxy theme colors (bg1 = black)
        theme_colors = {"bg1": "#000000"}
        
        result_path = self.renderer.generate_background_image(
            common_slide_data, output_path, theme_colors
        )
        
        # Verify image was generated
        assert result_path == output_path
        assert os.path.exists(output_path)
        
        # Verify image properties
        with Image.open(output_path) as img:
            assert img.size == (1280, 720)
            assert img.mode == "RGB"
            
            # Check that the image is black (Galaxy bg1 default)
            center_pixel = img.getpixel((640, 360))
            assert center_pixel == (0, 0, 0)  # RGB for black

    def test_background_reference_with_default_colors(self):
        """Test background reference generation with default theme colors."""
        bg_ref = BackgroundReference(idx=1001, scheme_color="bg1")
        
        common_slide_data = CommonSlideData(
            background_reference=bg_ref,
            cx=1280,
            cy=720
        )
        
        output_path = os.path.join(self.temp_dir, "default_background.png")
        
        # Test without providing theme colors (should use defaults)
        result_path = self.renderer.generate_background_image(
            common_slide_data, output_path
        )
        
        # Verify image was generated
        assert result_path == output_path
        assert os.path.exists(output_path)
        
        # Verify image properties
        with Image.open(output_path) as img:
            assert img.size == (1280, 720)
            assert img.mode == "RGB"
            
            # Should default to black for bg1
            center_pixel = img.getpixel((640, 360))
            assert center_pixel == (0, 0, 0)  # RGB for black

    def test_no_background_properties(self):
        """Test that no image is generated when slide has no background properties."""
        common_slide_data = CommonSlideData(
            cx=1280,
            cy=720
            # No background properties set
        )
        
        output_path = os.path.join(self.temp_dir, "no_background.png")
        
        result_path = self.renderer.generate_background_image(
            common_slide_data, output_path
        )
        
        # Should return None and not create file
        assert result_path is None
        assert not os.path.exists(output_path)

    def test_complex_gradient_with_multiple_stops(self):
        """Test generating gradient with multiple color stops."""
        gradient_stops = [
            GradientStop(pos=0, color="FF0000", scheme_color=None),      # Red
            GradientStop(pos=50000, color="00FF00", scheme_color=None),  # Green  
            GradientStop(pos=100000, color="0000FF", scheme_color=None)  # Blue
        ]
        gradient = GradientFill(stops=gradient_stops, angle=0)  # Horizontal
        
        common_slide_data = CommonSlideData(
            background_gradient_fill=gradient,
            cx=1280,
            cy=720
        )
        
        output_path = os.path.join(self.temp_dir, "multi_stop_gradient.png")
        
        result_path = self.renderer.generate_background_image(
            common_slide_data, output_path
        )
        
        # Verify image was generated
        assert result_path == output_path
        assert os.path.exists(output_path)
        
        with Image.open(output_path) as img:
            assert img.size == (1280, 720)
            # Note: Current implementation uses first and last stops only
            # This test validates the current behavior

    def test_gradient_with_scheme_colors(self):
        """Test generating gradient with scheme colors instead of direct colors."""
        gradient_stops = [
            GradientStop(pos=0, color=None, scheme_color="accent2"),
            GradientStop(pos=100000, color=None, scheme_color="accent4")
        ]
        gradient = GradientFill(stops=gradient_stops, angle=2700000)
        
        common_slide_data = CommonSlideData(
            background_gradient_fill=gradient,
            cx=1280,
            cy=720
        )
        
        output_path = os.path.join(self.temp_dir, "scheme_gradient.png")
        
        # Provide theme colors for Galaxy theme
        theme_colors = {
            "accent2": "#243FFF",  # Blue
            "accent4": "#FF9022"   # Orange
        }
        
        result_path = self.renderer.generate_background_image(
            common_slide_data, output_path, theme_colors
        )
        
        # Verify image was generated
        assert result_path == output_path
        assert os.path.exists(output_path)
        
        with Image.open(output_path) as img:
            assert img.size == (1280, 720)
            assert img.mode == "RGB"

    def test_custom_slide_dimensions(self):
        """Test generating background with custom slide dimensions."""
        custom_renderer = BackgroundRenderer(slide_width=800, slide_height=600)
        
        common_slide_data = CommonSlideData(
            background_color="00FF00",  # Green
            cx=800,
            cy=600
        )
        
        output_path = os.path.join(self.temp_dir, "custom_size.png")
        
        result_path = custom_renderer.generate_background_image(
            common_slide_data, output_path
        )
        
        # Verify image was generated with custom size
        assert result_path == output_path
        assert os.path.exists(output_path)
        
        with Image.open(output_path) as img:
            assert img.size == (800, 600)
            assert img.mode == "RGB"
            
            center_pixel = img.getpixel((400, 300))
            assert center_pixel == (0, 255, 0)  # RGB for green

    def test_output_directory_creation(self):
        """Test that output directories are created automatically."""
        nested_dir = os.path.join(self.temp_dir, "nested", "subdirs")
        output_path = os.path.join(nested_dir, "auto_created.png")
        
        common_slide_data = CommonSlideData(
            background_color="FFFF00",  # Yellow
            cx=1280,
            cy=720
        )
        
        # Directory doesn't exist yet
        assert not os.path.exists(nested_dir)
        
        result_path = self.renderer.generate_background_image(
            common_slide_data, output_path
        )
        
        # Should create directory and file
        assert result_path == output_path
        assert os.path.exists(nested_dir)
        assert os.path.exists(output_path)
        
        with Image.open(output_path) as img:
            assert img.size == (1280, 720)
            center_pixel = img.getpixel((640, 360))
            assert center_pixel == (255, 255, 0)  # RGB for yellow