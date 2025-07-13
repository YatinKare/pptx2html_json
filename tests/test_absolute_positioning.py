"""Test absolute positioning functionality."""

import os
import tempfile

from learnx_parser.models.core import CommonSlideData, Slide, SlideLayout
from learnx_parser.writers.css_utils import PositioningConfig
from learnx_parser.writers.html_writer import HtmlWriter


class TestAbsolutePositioning:
    """Test absolute positioning HTML generation."""

    def test_html_writer_absolute_mode(self):
        """Test HtmlWriter with absolute positioning mode."""
        with tempfile.TemporaryDirectory() as temp_dir:
            writer = HtmlWriter(
                output_directory=temp_dir, positioning_mode=PositioningConfig.ABSOLUTE
            )

            assert writer.positioning_config.mode == PositioningConfig.ABSOLUTE
            assert writer.positioning_config.slide_width == 1280
            assert writer.positioning_config.slide_height == 720

    def test_html_writer_responsive_mode_default(self):
        """Test HtmlWriter defaults to responsive positioning mode."""
        with tempfile.TemporaryDirectory() as temp_dir:
            writer = HtmlWriter(output_directory=temp_dir)

            assert writer.positioning_config.mode == PositioningConfig.RESPONSIVE

    def test_absolute_slide_generation(self):
        """Test HTML generation with absolute positioning."""
        with tempfile.TemporaryDirectory() as temp_dir:
            writer = HtmlWriter(
                output_directory=temp_dir, positioning_mode=PositioningConfig.ABSOLUTE
            )

            # Create a simple test slide
            slide = Slide(
                slide_number=1,
                common_slide_data=CommonSlideData(
                    cx=12192000,  # 1280px
                    cy=6858000,  # 720px
                ),
                slide_layout=SlideLayout(name="test-layout", type="blank"),
            )

            # Generate HTML
            output_path = writer.write_slide_html(slide, 1)

            # Verify file was created
            assert os.path.exists(output_path)

            # Read and verify HTML content
            with open(output_path, encoding="utf-8") as f:
                html_content = f.read()

            # Check for absolute positioning CSS structure (HTML5Point-inspired)
            assert "#resizer" in html_content
            assert "#player" in html_content
            assert "element-absolute" in html_content

            # Check for fixed dimensions
            assert "width: 1280px" in html_content
            assert "height: 720px" in html_content

            # Check for responsive scaling CSS
            assert "transform: scale" in html_content
            assert "@media" in html_content

            # Check for absolute positioning properties
            assert "position: absolute" in html_content
            assert "transform-origin: 0 0" in html_content

    def test_responsive_slide_generation(self):
        """Test HTML generation with responsive positioning (original behavior)."""
        with tempfile.TemporaryDirectory() as temp_dir:
            writer = HtmlWriter(
                output_directory=temp_dir, positioning_mode=PositioningConfig.RESPONSIVE
            )

            # Create a simple test slide
            slide = Slide(
                slide_number=1,
                common_slide_data=CommonSlideData(
                    cx=12192000,  # 1280px
                    cy=6858000,  # 720px
                ),
                slide_layout=SlideLayout(name="test-layout", type="blank"),
            )

            # Generate HTML
            output_path = writer.write_slide_html(slide, 1)

            # Verify file was created
            assert os.path.exists(output_path)

            # Read and verify HTML content
            with open(output_path, encoding="utf-8") as f:
                html_content = f.read()

            # Check for responsive positioning CSS classes (not absolute)
            assert "slide-container" in html_content
            assert "#resizer" not in html_content
            assert "#player" not in html_content

            # Check for flexbox layout CSS
            assert "display: flex" in html_content
            assert "flex-direction" in html_content

    def test_absolute_slide_dimensions(self):
        """Test that absolute positioning uses fixed dimensions."""
        with tempfile.TemporaryDirectory() as temp_dir:
            writer = HtmlWriter(
                output_directory=temp_dir, positioning_mode=PositioningConfig.ABSOLUTE
            )

            # Create slide with different dimensions
            slide = Slide(
                slide_number=2,
                common_slide_data=CommonSlideData(
                    cx=9144000,  # Different width (960px)
                    cy=5144000,  # Different height (540px)
                ),
                slide_layout=SlideLayout(name="test-layout", type="blank"),
            )

            # Generate HTML
            output_path = writer.write_slide_html(slide, 1)

            # Read HTML content
            with open(output_path, encoding="utf-8") as f:
                html_content = f.read()

            # Should use fixed dimensions (1280x720) not slide dimensions (960x540)
            assert "width: 1280px" in html_content
            assert "height: 720px" in html_content
            # Note: Different slide dimensions don't matter in absolute mode
            # as we always use fixed 1280x720 container
