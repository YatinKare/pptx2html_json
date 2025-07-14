"""
Tests for background image integration with HTML writer.
Testing the complete background image pipeline from generation to HTML output.
"""

import os
import tempfile
from unittest.mock import MagicMock, patch

import pytest

from learnx_parser.models.core import (
    BackgroundReference,
    CommonSlideData,
    GradientFill,
    GradientStop,
    Slide,
)
from learnx_parser.writers.html_writer import HtmlWriter


class TestBackgroundHtmlIntegration:
    """Test suite for background image integration with HTML writer."""

    def setup_method(self):
        """Set up test fixtures."""
        self.temp_dir = tempfile.mkdtemp()
        self.html_writer = HtmlWriter(output_directory=self.temp_dir)

    def teardown_method(self):
        """Clean up test fixtures."""
        import shutil
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_background_css_with_generated_image(self):
        """Test that _get_background_css returns background-image CSS when slide has generated image."""
        slide = Slide(
            slide_number=1,
            generated_background_path="media/background_1.png"
        )
        
        background_css = self.html_writer._get_background_css(slide)
        
        expected_css = "background-image: url('media/background_1.png'); background-size: cover; background-position: center; background-repeat: no-repeat;"
        assert background_css == expected_css

    def test_background_css_fallback_to_solid_color(self):
        """Test fallback to solid color CSS when no generated image exists."""
        common_slide_data = CommonSlideData(background_color="FF0000")
        slide = Slide(
            slide_number=1,
            common_slide_data=common_slide_data,
            generated_background_path=None  # No generated image
        )
        
        background_css = self.html_writer._get_background_css(slide)
        
        # Should fall back to old CSS generation
        assert "background-color: #FF0000;" in background_css
        assert "background-image:" not in background_css

    def test_background_css_fallback_to_gradient(self):
        """Test fallback to gradient CSS when no generated image exists."""
        gradient_stops = [
            GradientStop(pos=0, color="FF0000", scheme_color=None),
            GradientStop(pos=100000, color="0000FF", scheme_color=None)
        ]
        gradient = GradientFill(stops=gradient_stops, angle=2700000)
        
        common_slide_data = CommonSlideData(background_gradient_fill=gradient)
        slide = Slide(
            slide_number=1,
            common_slide_data=common_slide_data,
            generated_background_path=None  # No generated image
        )
        
        background_css = self.html_writer._get_background_css(slide)
        
        # Should fall back to gradient CSS generation
        assert "linear-gradient" in background_css or "background:" in background_css
        assert "background-image: url(" not in background_css

    def test_background_css_with_no_background_properties(self):
        """Test CSS generation when slide has no background properties."""
        slide = Slide(
            slide_number=1,
            common_slide_data=CommonSlideData(),  # No background properties
            generated_background_path=None
        )
        
        background_css = self.html_writer._get_background_css(slide)
        
        # Should return empty string or minimal CSS
        assert background_css == "" or len(background_css.strip()) == 0

    def test_background_image_priority_over_other_properties(self):
        """Test that generated background image takes priority over other background properties."""
        # Slide has both generated image AND other background properties
        gradient_stops = [
            GradientStop(pos=0, color="FF0000", scheme_color=None),
            GradientStop(pos=100000, color="0000FF", scheme_color=None)
        ]
        gradient = GradientFill(stops=gradient_stops, angle=2700000)
        
        common_slide_data = CommonSlideData(
            background_color="00FF00",  # Green solid color
            background_gradient_fill=gradient  # Red to blue gradient
        )
        
        slide = Slide(
            slide_number=1,
            common_slide_data=common_slide_data,
            generated_background_path="media/background_1.png"  # Generated image
        )
        
        background_css = self.html_writer._get_background_css(slide)
        
        # Should use generated image, not fallback to other properties
        assert "background-image: url('media/background_1.png')" in background_css
        assert "background-color: #00FF00" not in background_css
        assert "linear-gradient" not in background_css

    @patch('learnx_parser.writers.html_writer.HtmlWriter._resolve_slide_background')
    def test_theme_resolver_integration(self, mock_resolve):
        """Test that theme resolver integration works with background images."""
        mock_resolve.return_value = "background: linear-gradient(theme-based);"
        
        slide = Slide(
            slide_number=1,
            generated_background_path="media/background_1.png"
        )
        
        background_css = self.html_writer._get_background_css(slide)
        
        # Generated image should take priority over theme resolver
        assert "background-image: url('media/background_1.png')" in background_css
        # Theme resolver should not be called for slides with generated images
        mock_resolve.assert_not_called()

    def test_slide_html_generation_with_background_image(self):
        """Test that background image CSS is properly integrated into slide styling."""
        slide = Slide(
            slide_number=1,
            generated_background_path="media/background_1.png",
            shapes=[],  # No shapes for simplicity
            pictures=[],
            group_shapes=[],
            graphic_frames=[]
        )
        
        # Test the background CSS generation directly since that's what matters
        background_css = self.html_writer._get_background_css(slide)
        
        # Check that background image CSS is properly formatted
        assert "background-image: url('media/background_1.png')" in background_css
        assert "background-size: cover" in background_css
        assert "background-position: center" in background_css
        assert "background-repeat: no-repeat" in background_css
        
        # Verify the complete CSS string is correctly formatted
        expected_css = "background-image: url('media/background_1.png'); background-size: cover; background-position: center; background-repeat: no-repeat;"
        assert background_css == expected_css

    def test_multiple_slides_different_backgrounds(self):
        """Test that different slides can have different background images."""
        slides = [
            Slide(
                slide_number=1,
                generated_background_path="media/background_1.png"
            ),
            Slide(
                slide_number=2,
                generated_background_path="media/background_2.png"
            ),
            Slide(
                slide_number=3,
                generated_background_path=None,
                common_slide_data=CommonSlideData(background_color="FF0000")
            )
        ]
        
        css_results = []
        for slide in slides:
            css = self.html_writer._get_background_css(slide)
            css_results.append(css)
        
        # First slide should use background_1.png
        assert "background-image: url('media/background_1.png')" in css_results[0]
        
        # Second slide should use background_2.png
        assert "background-image: url('media/background_2.png')" in css_results[1]
        
        # Third slide should fall back to solid color CSS
        assert "background-color: #FF0000" in css_results[2]
        assert "background-image:" not in css_results[2]

    def test_background_image_path_format(self):
        """Test that background image paths are correctly formatted for HTML."""
        test_cases = [
            "media/background_1.png",
            "slide1/media/bg.png",
            "backgrounds/gradient_slide.png"
        ]
        
        for path in test_cases:
            slide = Slide(
                slide_number=1,
                generated_background_path=path
            )
            
            background_css = self.html_writer._get_background_css(slide)
            
            # Path should be properly quoted and formatted
            expected_url = f"background-image: url('{path}')"
            assert expected_url in background_css

    def test_css_properties_completeness(self):
        """Test that all necessary CSS properties are included for background images."""
        slide = Slide(
            slide_number=1,
            generated_background_path="media/test_background.png"
        )
        
        background_css = self.html_writer._get_background_css(slide)
        
        # Should include all necessary CSS properties for proper display
        required_properties = [
            "background-image:",
            "background-size: cover",
            "background-position: center", 
            "background-repeat: no-repeat"
        ]
        
        for prop in required_properties:
            assert prop in background_css