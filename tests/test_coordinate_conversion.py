"""Test coordinate conversion utilities."""
import pytest
from learnx_parser.models.core import Transform
from learnx_parser.writers.css_utils import CoordinateConverter, ZIndexLayers, PositioningConfig


class TestCoordinateConverter:
    """Test coordinate conversion functions."""
    
    def test_emu_to_px_conversion(self):
        """Test EMU to pixel conversion accuracy."""
        # Test known conversions from XML analysis
        assert CoordinateConverter.emu_to_px(1280159) == 134  # Title X position
        assert CoordinateConverter.emu_to_px(357809) == 38   # Title Y position
        assert CoordinateConverter.emu_to_px(7983110) == 838  # Title width
        assert CoordinateConverter.emu_to_px(3080335) == 323  # Title height (correct rounding)
        
        # Test slide dimensions
        assert CoordinateConverter.emu_to_px(12192000) == 1280  # Slide width
        assert CoordinateConverter.emu_to_px(6858000) == 720   # Slide height
        
        # Test zero and negative values
        assert CoordinateConverter.emu_to_px(0) == 0
        assert CoordinateConverter.emu_to_px(-9525) == -1
    
    def test_extract_position_from_transform(self):
        """Test position extraction from Transform object."""
        transform = Transform(
            x=1280159,
            y=357809,
            cx=7983110,
            cy=3080335,
            rot=0,
            flipH=False,
            flipV=False
        )
        
        position = CoordinateConverter.extract_position(transform)
        
        assert position is not None
        assert position['x'] == 134
        assert position['y'] == 38
        assert position['width'] == 838
        assert position['height'] == 323
    
    def test_extract_position_none_transform(self):
        """Test position extraction with None transform."""
        position = CoordinateConverter.extract_position(None)
        assert position is None
    
    def test_generate_absolute_css(self):
        """Test CSS generation for absolute positioning."""
        position = {
            'x': 134,
            'y': 38,
            'width': 838,
            'height': 324
        }
        
        css = CoordinateConverter.generate_absolute_css(position, 2)
        
        assert "position: absolute;" in css
        assert "left: 134px;" in css
        assert "top: 38px;" in css
        assert "width: 838px;" in css
        assert "height: 324px;" in css
        assert "z-index: 2;" in css
    
    def test_generate_absolute_css_none_position(self):
        """Test CSS generation with None position."""
        css = CoordinateConverter.generate_absolute_css(None)
        assert css == ""


class TestZIndexLayers:
    """Test z-index management system."""
    
    def test_element_z_index_assignment(self):
        """Test z-index assignment for different element types."""
        # Test base z-index values
        assert ZIndexLayers.get_element_z_index('shape') == 100
        assert ZIndexLayers.get_element_z_index('text') == 200
        assert ZIndexLayers.get_element_z_index('image') == 300
        assert ZIndexLayers.get_element_z_index('group') == 100
        
        # Test unknown element type defaults to shape
        assert ZIndexLayers.get_element_z_index('unknown') == 100
    
    def test_element_z_index_with_order(self):
        """Test z-index assignment with order."""
        # Test order-based z-index
        assert ZIndexLayers.get_element_z_index('shape', 5) == 105
        assert ZIndexLayers.get_element_z_index('text', 3) == 203
        assert ZIndexLayers.get_element_z_index('image', 1) == 301


class TestPositioningConfig:
    """Test positioning configuration."""
    
    def test_default_config(self):
        """Test default positioning configuration."""
        config = PositioningConfig()
        
        assert config.mode == PositioningConfig.RESPONSIVE
        assert config.slide_width == 1280
        assert config.slide_height == 720
        assert config.enable_scaling is True
        assert config.z_index_auto is True
    
    def test_absolute_config(self):
        """Test absolute positioning configuration."""
        config = PositioningConfig(mode=PositioningConfig.ABSOLUTE)
        
        assert config.mode == PositioningConfig.ABSOLUTE
        assert config.slide_width == 1280
        assert config.slide_height == 720
    
    def test_hybrid_config(self):
        """Test hybrid positioning configuration."""
        config = PositioningConfig(mode=PositioningConfig.HYBRID)
        
        assert config.mode == PositioningConfig.HYBRID