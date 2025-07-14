"""
Tests for background property extraction functionality.
Testing the complete background property inheritance hierarchy: slide → layout → master.
"""

import os
import tempfile
from unittest.mock import MagicMock, patch

import pytest
from lxml import etree

from learnx_parser.models.core import BackgroundReference, GradientFill, GradientStop
from learnx_parser.parsers.slide.base import SlideParser
from learnx_parser.parsers.layout import LayoutParser
from learnx_parser.parsers.master import SlideMasterParser


class TestBackgroundPropertyExtraction:
    """Test suite for background property extraction from slide XML."""

    def test_slide_level_solid_background_extraction(self):
        """Test extracting solid color background from slide XML."""
        slide_xml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
        <p:sld xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main"
               xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">
            <p:cSld>
                <p:bg>
                    <p:bgPr>
                        <a:solidFill>
                            <a:srgbClr val="FF0000"/>
                        </a:solidFill>
                    </p:bgPr>
                </p:bg>
            </p:cSld>
        </p:sld>"""
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.xml', delete=False) as temp_file:
            temp_file.write(slide_xml)
            temp_file.flush()
            
            try:
                parser = SlideParser(
                    slide_xml_path=temp_file.name,
                    slide_rels_path=None,
                    pptx_unpacked_path="/dummy",
                    slide_width=1280,
                    slide_height=720
                )
                
                common_slide_data = parser._extract_common_slide_data()
                
                assert common_slide_data.background_color == "FF0000"
                assert common_slide_data.background_gradient_fill is None
                assert common_slide_data.background_reference is None
                
            finally:
                os.unlink(temp_file.name)

    def test_slide_level_gradient_background_extraction(self):
        """Test extracting gradient background from slide XML."""
        slide_xml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
        <p:sld xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main"
               xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">
            <p:cSld>
                <p:bg>
                    <p:bgPr>
                        <a:gradFill>
                            <a:gsLst>
                                <a:gs pos="0">
                                    <a:schemeClr val="accent2"/>
                                </a:gs>
                                <a:gs pos="100000">
                                    <a:schemeClr val="accent4"/>
                                </a:gs>
                            </a:gsLst>
                            <a:lin ang="2700000"/>
                        </a:gradFill>
                    </p:bgPr>
                </p:bg>
            </p:cSld>
        </p:sld>"""
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.xml', delete=False) as temp_file:
            temp_file.write(slide_xml)
            temp_file.flush()
            
            try:
                parser = SlideParser(
                    slide_xml_path=temp_file.name,
                    slide_rels_path=None,
                    pptx_unpacked_path="/dummy",
                    slide_width=1280,
                    slide_height=720
                )
                
                common_slide_data = parser._extract_common_slide_data()
                
                assert common_slide_data.background_color is None
                assert common_slide_data.background_reference is None
                assert common_slide_data.background_gradient_fill is not None
                
                gradient = common_slide_data.background_gradient_fill
                assert len(gradient.stops) == 2
                assert gradient.angle == 2700000
                assert gradient.stops[0].pos == 0
                assert gradient.stops[0].scheme_color == "accent2"
                assert gradient.stops[1].pos == 100000
                assert gradient.stops[1].scheme_color == "accent4"
                
            finally:
                os.unlink(temp_file.name)

    def test_slide_level_background_reference_extraction(self):
        """Test extracting background reference from slide XML."""
        slide_xml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
        <p:sld xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main"
               xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">
            <p:cSld>
                <p:bg>
                    <p:bgRef idx="1001">
                        <a:schemeClr val="bg1"/>
                    </p:bgRef>
                </p:bg>
            </p:cSld>
        </p:sld>"""
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.xml', delete=False) as temp_file:
            temp_file.write(slide_xml)
            temp_file.flush()
            
            try:
                parser = SlideParser(
                    slide_xml_path=temp_file.name,
                    slide_rels_path=None,
                    pptx_unpacked_path="/dummy",
                    slide_width=1280,
                    slide_height=720
                )
                
                common_slide_data = parser._extract_common_slide_data()
                
                assert common_slide_data.background_color is None
                assert common_slide_data.background_gradient_fill is None
                assert common_slide_data.background_reference is not None
                
                bg_ref = common_slide_data.background_reference
                assert bg_ref.idx == 1001
                assert bg_ref.scheme_color == "bg1"
                
            finally:
                os.unlink(temp_file.name)

    def test_layout_level_background_extraction(self):
        """Test extracting background properties from layout XML."""
        layout_xml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
        <p:sldLayout xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main"
                     xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">
            <p:cSld name="Title Slide">
                <p:bg>
                    <p:bgPr>
                        <a:solidFill>
                            <a:srgbClr val="0000FF"/>
                        </a:solidFill>
                    </p:bgPr>
                </p:bg>
            </p:cSld>
        </p:sldLayout>"""
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.xml', delete=False) as temp_file:
            temp_file.write(layout_xml)
            temp_file.flush()
            
            try:
                parser = LayoutParser(
                    layout_xml_path=temp_file.name,
                    pptx_unpacked_path="/dummy"
                )
                
                layout = parser.parse_layout()
                
                assert layout.background_color == "0000FF"
                assert layout.background_gradient_fill is None
                assert layout.background_reference is None
                
            finally:
                os.unlink(temp_file.name)

    def test_master_level_background_extraction(self):
        """Test extracting background properties from slide master XML."""
        master_xml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
        <p:sldMaster xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main"
                     xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">
            <p:cSld>
                <p:bg>
                    <p:bgRef idx="1001">
                        <a:schemeClr val="bg1"/>
                    </p:bgRef>
                </p:bg>
            </p:cSld>
        </p:sldMaster>"""
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.xml', delete=False) as temp_file:
            temp_file.write(master_xml)
            temp_file.flush()
            
            try:
                parser = SlideMasterParser(
                    master_xml_path=temp_file.name,
                    pptx_unpacked_path="/dummy"
                )
                
                master = parser.parse_master()
                
                assert master.background_color is None
                assert master.background_gradient_fill is None
                assert master.background_reference is not None
                
                bg_ref = master.background_reference
                assert bg_ref.idx == 1001
                assert bg_ref.scheme_color == "bg1"
                
            finally:
                os.unlink(temp_file.name)

    def test_no_background_properties(self):
        """Test handling slides with no background properties."""
        slide_xml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
        <p:sld xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main"
               xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">
            <p:cSld>
                <p:spTree>
                    <!-- Some shapes but no background -->
                </p:spTree>
            </p:cSld>
        </p:sld>"""
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.xml', delete=False) as temp_file:
            temp_file.write(slide_xml)
            temp_file.flush()
            
            try:
                parser = SlideParser(
                    slide_xml_path=temp_file.name,
                    slide_rels_path=None,
                    pptx_unpacked_path="/dummy",
                    slide_width=1280,
                    slide_height=720
                )
                
                common_slide_data = parser._extract_common_slide_data()
                
                assert common_slide_data.background_color is None
                assert common_slide_data.background_gradient_fill is None
                assert common_slide_data.background_reference is None
                
            finally:
                os.unlink(temp_file.name)


class TestBackgroundInheritanceHierarchy:
    """Test suite for background property inheritance from layout and master."""

    def test_layout_to_slide_inheritance(self):
        """Test that slides inherit background from layout when no slide-level background exists."""
        # This would require a more complex setup with actual layout files
        # For now, test the logic directly by creating mock objects
        
        from learnx_parser.models.core import SlideLayout, CommonSlideData
        
        # Create a layout with background properties
        layout = SlideLayout(
            name="Test Layout",
            background_color="FF0000"
        )
        
        # Test the inheritance logic in slide parser
        slide_xml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
        <p:sld xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main">
            <p:cSld>
                <!-- No background properties -->
            </p:cSld>
        </p:sld>"""
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.xml', delete=False) as temp_file:
            temp_file.write(slide_xml)
            temp_file.flush()
            
            try:
                parser = SlideParser(
                    slide_xml_path=temp_file.name,
                    slide_rels_path=None,
                    pptx_unpacked_path="/dummy",
                    slide_width=1280,
                    slide_height=720
                )
                
                # Test inheritance logic
                common_slide_data = parser._extract_common_slide_data(layout)
                
                # Should inherit from layout since slide has no background
                assert common_slide_data.background_color == "FF0000"
                
            finally:
                os.unlink(temp_file.name)

    def test_no_inheritance_when_slide_has_background(self):
        """Test that slides don't inherit when they have their own background properties."""
        from learnx_parser.models.core import SlideLayout
        
        # Create a layout with background properties
        layout = SlideLayout(
            name="Test Layout",
            background_color="FF0000"  # Red layout background
        )
        
        # Slide with its own background
        slide_xml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
        <p:sld xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main"
               xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">
            <p:cSld>
                <p:bg>
                    <p:bgPr>
                        <a:solidFill>
                            <a:srgbClr val="0000FF"/>
                        </a:solidFill>
                    </p:bgPr>
                </p:bg>
            </p:cSld>
        </p:sld>"""
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.xml', delete=False) as temp_file:
            temp_file.write(slide_xml)
            temp_file.flush()
            
            try:
                parser = SlideParser(
                    slide_xml_path=temp_file.name,
                    slide_rels_path=None,
                    pptx_unpacked_path="/dummy",
                    slide_width=1280,
                    slide_height=720
                )
                
                common_slide_data = parser._extract_common_slide_data(layout)
                
                # Should use slide's own background, not inherit from layout
                assert common_slide_data.background_color == "0000FF"  # Blue slide background
                
            finally:
                os.unlink(temp_file.name)