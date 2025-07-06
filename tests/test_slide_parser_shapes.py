from unittest.mock import MagicMock

import pytest
from lxml import etree

from learnx_parser.models.core import (
    GradientFill,
    Line,
    SolidFill,
    TextFrame,
)
from learnx_parser.parsers.slide.shapes import (
    extract_fill_properties,
    extract_line_properties,
    extract_transform,
    parse_graphic_frame_element,
    parse_group_shape_element,
    parse_picture_element,
    parse_shape_element,
    parse_shape_tree,
)


# Mock parser_instance for functions that require it
@pytest.fixture
def mock_parser_instance():
    mock_instance = MagicMock()
    mock_instance.nsmap = {
        "p": "http://schemas.openxmlformats.org/presentationml/2006/main",
        "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
        "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
    }
    mock_instance.rels = {"rId1": "../media/image1.png"}
    # Mock the text extraction methods that parse_shape_element calls
    mock_instance._extract_text_frame_properties = MagicMock(return_value=TextFrame())
    return mock_instance


# Test extract_transform
def test_extract_transform(mock_parser_instance):
    xml_str = """
    <p:spPr xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">
        <a:xfrm rot="30000" flipH="1" flipV="0">
            <a:off x="100" y="200"/>
            <a:ext cx="300" cy="400"/>
        </a:xfrm>
    </p:spPr>
    """
    element = etree.fromstring(xml_str)
    
    # Set up the mock parser instance with the correct namespace map
    mock_parser_instance.nsmap = {
        'p': 'http://schemas.openxmlformats.org/presentationml/2006/main',
        'a': 'http://schemas.openxmlformats.org/drawingml/2006/main'
    }
    
    transform = extract_transform(mock_parser_instance, element)
    assert transform.x == 100
    assert transform.y == 200
    assert transform.cx == 300
    assert transform.cy == 400
    assert transform.rot == 30000
    assert transform.flipH is True
    assert transform.flipV is False


# Test extract_fill_properties
def test_extract_solid_fill_properties(mock_parser_instance):
    xml_str = """
    <a:solidFill xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">
        <a:srgbClr val="FF0000"/>
    </a:solidFill>
    """
    element = etree.fromstring(xml_str)
    
    # Set up the mock parser instance with the correct namespace map
    mock_parser_instance.nsmap = {
        'a': 'http://schemas.openxmlformats.org/drawingml/2006/main'
    }
    
    fill = extract_fill_properties(mock_parser_instance, element)
    assert isinstance(fill, SolidFill)
    assert fill.color == "FF0000"


def test_extract_gradient_fill_properties(mock_parser_instance):
    xml_str = """
    <p:spPr xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">
        <a:gradFill>
            <a:lin ang="5400000" scaled="1"/>
            <a:gsLst>
                <a:gs pos="0"><a:srgbClr val="FFFFFF"/></a:gs>
                <a:gs pos="100000"><a:srgbClr val="000000"/></a:gs>
            </a:gsLst>
        </a:gradFill>
    </p:spPr>
    """
    element = etree.fromstring(xml_str)
    fill = extract_fill_properties(mock_parser_instance, element)
    assert isinstance(fill, GradientFill)
    assert fill.angle == 5400000
    assert fill.scaled is True
    assert len(fill.stops) == 2
    assert fill.stops[0].color == "FFFFFF"
    assert fill.stops[1].color == "000000"


# Test extract_line_properties
def test_extract_line_properties(mock_parser_instance):
    xml_str = """
    <p:spPr xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">
        <a:ln w="12700">
            <a:solidFill><a:srgbClr val="0000FF"/></a:solidFill>
        </a:ln>
    </p:spPr>
    """
    element = etree.fromstring(xml_str)
    line = extract_line_properties(mock_parser_instance, element)
    assert isinstance(line, Line)
    assert line.width == 12700
    assert line.color == "0000FF"


# Test parse_shape_element
def test_parse_shape_element(mock_parser_instance):
    xml_str = """
    <p:sp xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">
        <p:nvSpPr>
            <p:cNvPr id="1" name="Shape 1"/>
            <p:cNvSpPr/>
            <p:nvPr><p:ph type="title" idx="0"/></p:nvPr>
        </p:nvSpPr>
        <p:spPr>
            <a:xfrm><a:off x="100" y="100"/><a:ext cx="200" cy="50"/></a:xfrm>
            <a:prstGeom prst="rect"/>
            <a:solidFill><a:srgbClr val="FF0000"/></a:solidFill>
        </p:spPr>
        <p:txBody/>
    </p:sp>
    """
    element = etree.fromstring(xml_str)
    
    # Set up the mock parser instance with the correct namespace map
    mock_parser_instance.nsmap = {
        'p': 'http://schemas.openxmlformats.org/presentationml/2006/main',
        'a': 'http://schemas.openxmlformats.org/drawingml/2006/main'
    }
    
    shape = parse_shape_element(mock_parser_instance, element, None)
    assert shape.id == "1"
    assert shape.name == "Shape 1"
    assert shape.ph_type == "title"
    assert shape.ph_idx == 0
    assert shape.transform.x == 100
    assert shape.prst_geom == "rect"
    assert isinstance(shape.fill, SolidFill)


# Test parse_picture_element
def test_parse_picture_element(mock_parser_instance):
    xml_str = """
    <p:pic xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">
        <p:nvPicPr>
            <p:cNvPr id="2" name="Picture 1"/>
            <p:cNvPicPr/>
            <p:nvPr><p:ph type="pic" idx="1"/></p:nvPr>
        </p:nvPicPr>
        <p:blipFill rotWithShape="0">
            <a:blip r:embed="rId1"/>
            <a:srcRect t="10000" b="10000" l="10000" r="10000"/>
        </p:blipFill>
        <p:spPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="100" cy="100"/></a:xfrm></p:spPr>
    </p:pic>
    """
    element = etree.fromstring(xml_str)
    
    # Set up the mock parser instance with the correct namespace map and relationships
    mock_parser_instance.nsmap = {
        'p': 'http://schemas.openxmlformats.org/presentationml/2006/main',
        'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
        'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'
    }
    mock_parser_instance.rels = {'rId1': '../media/image1.png'}
    
    picture = parse_picture_element(mock_parser_instance, element)
    assert picture.id == "2"
    assert picture.name == "Picture 1"
    assert picture.path == "../media/image1.png"
    assert picture.ph_type == "pic"
    assert picture.ph_idx == 1
    assert picture.blip_fill.rot_with_shape is False
    assert picture.blip_fill.src_rect_t == 10000


# Test parse_group_shape_element
def test_parse_group_shape_element(mock_parser_instance):
    xml_str = """
    <p:grpSp xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">
        <p:nvGrpSpPr>
            <p:cNvPr id="3" name="Group 1"/>
            <p:cNvGrpSpPr/>
        </p:nvGrpSpPr>
        <p:grpSpPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="100" cy="100"/></a:xfrm></p:grpSpPr>
        <p:sp>
            <p:nvSpPr><p:cNvPr id="4" name="Shape in Group"/></p:nvSpPr>
            <p:spPr><a:xfrm><a:off x="10" y="10"/><a:ext cx="20" cy="20"/></a:xfrm></p:spPr>
            <p:txBody/>
        </p:sp>
    </p:grpSp>
    """
    element = etree.fromstring(xml_str)
    group_shape = parse_group_shape_element(mock_parser_instance, element, None)
    assert group_shape.id == "3"
    assert group_shape.name == "Group 1"
    assert len(group_shape.children[0]) == 1  # One shape child
    assert group_shape.children[0][0].name == "Shape in Group"


# Test parse_graphic_frame_element
def test_parse_graphic_frame_element(mock_parser_instance):
    xml_str = """
    <p:graphicFrame xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">
        <p:nvGraphicFramePr>
            <p:cNvPr id="5" name="Chart 1"/>
            <p:cNvGraphicFramePr/>
        </p:nvGraphicFramePr>
        <a:xfrm><a:off x="0" y="0"/><a:ext cx="100" cy="100"/></a:xfrm>
    </p:graphicFrame>
    """
    element = etree.fromstring(xml_str)
    graphic_frame = parse_graphic_frame_element(mock_parser_instance, element)
    assert graphic_frame.id == "5"
    assert graphic_frame.name == "Chart 1"


# Test parse_shape_tree
def test_parse_shape_tree(mock_parser_instance):
    xml_str = """
    <p:spTree xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">
        <p:sp>
            <p:nvSpPr><p:cNvPr id="1" name="Shape 1"/></p:nvSpPr>
            <p:spPr><a:xfrm><a:off x="100" y="100"/><a:ext cx="200" cy="50"/></a:xfrm></p:spPr>
            <p:txBody/>
        </p:sp>
        <p:pic>
            <p:nvPicPr><p:cNvPr id="2" name="Picture 1"/></p:nvPicPr>
            <p:blipFill><a:blip r:embed="rId1"/></p:blipFill>
            <p:spPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="100" cy="100"/></a:xfrm></p:spPr>
        </p:pic>
        <p:grpSp>
            <p:nvGrpSpPr><p:cNvPr id="3" name="Group 1"/></p:nvGrpSpPr>
            <p:grpSpPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="100" cy="100"/></a:xfrm></p:grpSpPr>
        </p:grpSp>
        <p:graphicFrame>
            <p:nvGraphicFramePr><p:cNvPr id="4" name="Chart 1"/></p:nvGraphicFramePr>
            <a:xfrm><a:off x="0" y="0"/><a:ext cx="100" cy="100"/></a:xfrm>
        </p:graphicFrame>
    </p:spTree>
    """
    element = etree.fromstring(xml_str)
    shapes, pictures, group_shapes, graphic_frames = parse_shape_tree(
        mock_parser_instance, element, None
    )
    assert len(shapes) == 1
    assert len(pictures) == 1
    assert len(group_shapes) == 1
    assert len(graphic_frames) == 1
    assert shapes[0].name == "Shape 1"
    assert pictures[0].name == "Picture 1"
    assert group_shapes[0].name == "Group 1"
    assert graphic_frames[0].name == "Chart 1"
