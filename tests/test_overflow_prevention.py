"""Test cases for overflow prevention functionality in version 0.2.7."""

from learnx_parser.writers.css_utils import CoordinateConverter


class TestOverflowPrevention:
    """Test overflow prevention and detection functionality."""

    def test_check_overflow_no_overflow(self):
        """Test overflow detection when element fits within bounds."""
        position = {"x": 100, "y": 50, "width": 200, "height": 150}

        overflow = CoordinateConverter.check_overflow(position, 1280, 720)

        assert overflow is not None
        assert overflow["has_overflow"] is False
        assert overflow["overflow_right"] == 0
        assert overflow["overflow_bottom"] == 0
        assert overflow["overflow_left"] == 0
        assert overflow["overflow_top"] == 0
        assert overflow["element_right"] == 300
        assert overflow["element_bottom"] == 200

    def test_check_overflow_right_overflow(self):
        """Test overflow detection when element extends beyond right boundary."""
        position = {"x": 1200, "y": 100, "width": 200, "height": 150}

        overflow = CoordinateConverter.check_overflow(position, 1280, 720)

        assert overflow is not None
        assert overflow["has_overflow"] is True
        assert overflow["overflow_right"] == 120  # 1400 - 1280
        assert overflow["overflow_bottom"] == 0
        assert overflow["overflow_left"] == 0
        assert overflow["overflow_top"] == 0

    def test_check_overflow_bottom_overflow(self):
        """Test overflow detection when element extends beyond bottom boundary."""
        position = {"x": 100, "y": 650, "width": 200, "height": 150}

        overflow = CoordinateConverter.check_overflow(position, 1280, 720)

        assert overflow is not None
        assert overflow["has_overflow"] is True
        assert overflow["overflow_right"] == 0
        assert overflow["overflow_bottom"] == 80  # 800 - 720
        assert overflow["overflow_left"] == 0
        assert overflow["overflow_top"] == 0

    def test_check_overflow_negative_position(self):
        """Test overflow detection when element has negative position."""
        position = {"x": -50, "y": -20, "width": 200, "height": 150}

        overflow = CoordinateConverter.check_overflow(position, 1280, 720)

        assert overflow is not None
        assert overflow["has_overflow"] is True
        assert overflow["overflow_right"] == 0
        assert overflow["overflow_bottom"] == 0
        assert overflow["overflow_left"] == 50
        assert overflow["overflow_top"] == 20

    def test_prevent_overflow_no_adjustment_needed(self):
        """Test overflow prevention when no adjustment is needed."""
        position = {"x": 100, "y": 50, "width": 200, "height": 150}

        adjusted = CoordinateConverter.prevent_overflow(position, 1280, 720)

        assert adjusted == position  # No changes needed

    def test_prevent_overflow_right_boundary(self):
        """Test overflow prevention when element extends beyond right boundary."""
        position = {"x": 1200, "y": 100, "width": 200, "height": 150}

        adjusted = CoordinateConverter.prevent_overflow(
            position, 1280, 720, preserve_aspect_ratio=False
        )

        assert adjusted["x"] == 1200
        assert adjusted["y"] == 100
        assert adjusted["width"] == 80  # Clamped to fit: 1280 - 1200
        assert adjusted["height"] == 150  # Unchanged when not preserving aspect ratio

    def test_prevent_overflow_bottom_boundary(self):
        """Test overflow prevention when element extends beyond bottom boundary."""
        position = {"x": 100, "y": 650, "width": 200, "height": 150}

        adjusted = CoordinateConverter.prevent_overflow(
            position, 1280, 720, preserve_aspect_ratio=False
        )

        assert adjusted["x"] == 100
        assert adjusted["y"] == 650
        assert adjusted["width"] == 200  # Unchanged
        assert adjusted["height"] == 70  # Clamped to fit: 720 - 650

    def test_prevent_overflow_negative_position(self):
        """Test overflow prevention when element has negative position."""
        position = {"x": -50, "y": -20, "width": 200, "height": 150}

        adjusted = CoordinateConverter.prevent_overflow(position, 1280, 720)

        assert adjusted["x"] == 0  # Moved to boundary
        assert adjusted["y"] == 0  # Moved to boundary
        assert adjusted["width"] == 150  # Reduced by amount moved: 200 - 50
        assert adjusted["height"] == 130  # Reduced by amount moved: 150 - 20

    def test_prevent_overflow_preserve_aspect_ratio(self):
        """Test overflow prevention with aspect ratio preservation."""
        position = {
            "x": 1000,
            "y": 500,
            "width": 400,
            "height": 300,
        }  # Aspect ratio 4:3

        adjusted = CoordinateConverter.prevent_overflow(
            position, 1280, 720, preserve_aspect_ratio=True
        )

        # Should be constrained by width: max_width = 280, max_height = 220
        # Width constrained: 280, height = 280 * (3/4) = 210
        assert adjusted["x"] == 1000
        assert adjusted["y"] == 500
        assert adjusted["width"] == 280  # 1280 - 1000
        assert adjusted["height"] == 210  # Aspect ratio preserved

    def test_prevent_overflow_height_constrained_aspect_ratio(self):
        """Test overflow prevention when height is the constraining factor."""
        position = {"x": 100, "y": 600, "width": 300, "height": 200}  # Aspect ratio 3:2

        adjusted = CoordinateConverter.prevent_overflow(
            position, 1280, 720, preserve_aspect_ratio=True
        )

        # Should be constrained by height: max_width = 1180, max_height = 120
        # Height constrained: 120, width = 120 * (3/2) = 180
        assert adjusted["x"] == 100
        assert adjusted["y"] == 600
        assert adjusted["width"] == 180  # Aspect ratio preserved
        assert adjusted["height"] == 120  # 720 - 600

    def test_generate_absolute_css_with_overflow_prevention(self):
        """Test CSS generation with overflow prevention enabled."""
        position = {"x": 1200, "y": 100, "width": 200, "height": 150}

        css = CoordinateConverter.generate_absolute_css(
            position, z_index=5, prevent_overflow=True
        )

        # Should have adjusted dimensions to fit (aspect ratio preserved)
        # Width: 1280 - 1200 = 80px (scale factor: 80/200 = 0.4)
        # Height: 150 * 0.4 = 60px
        assert "position: absolute;" in css
        assert "left: 1200px;" in css
        assert "top: 100px;" in css
        assert "width: 80px;" in css  # Adjusted to fit
        assert "height: 60px;" in css  # Aspect ratio preserved
        assert "z-index: 5;" in css

    def test_generate_absolute_css_without_overflow_prevention(self):
        """Test CSS generation with overflow prevention disabled."""
        position = {"x": 1200, "y": 100, "width": 200, "height": 150}

        css = CoordinateConverter.generate_absolute_css(
            position, z_index=5, prevent_overflow=False
        )

        # Should preserve original dimensions
        assert "position: absolute;" in css
        assert "left: 1200px;" in css
        assert "top: 100px;" in css
        assert "width: 200px;" in css  # Original width
        assert "height: 150px;" in css
        assert "z-index: 5;" in css

    def test_check_overflow_none_position(self):
        """Test overflow detection with None position."""
        overflow = CoordinateConverter.check_overflow(None)
        assert overflow is None

    def test_prevent_overflow_none_position(self):
        """Test overflow prevention with None position."""
        adjusted = CoordinateConverter.prevent_overflow(None)
        assert adjusted is None
