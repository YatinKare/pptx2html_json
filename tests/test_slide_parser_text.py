from unittest.mock import MagicMock

import pytest
from lxml import etree

from learnx_parser.parsers.slide.text import (
    extract_paragraph_properties,
    extract_run_properties,
    extract_text_frame_properties,
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
    mock_instance.rels = {"rId1": "../media/bullet.png"}
    return mock_instance


# Test extract_run_properties
def test_extract_run_properties(mock_parser_instance):
    xml_str = """
    <a:r xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">
        <a:rPr sz="1800" b="1" i="1">
            <a:solidFill><a:srgbClr val="FF0000"/></a:solidFill>
            <a:latin typeface="Arial"/>
            <a:u val="sng"/>
        </a:rPr>
        <a:t>Hello</a:t>
    </a:r>
    """
    element = etree.fromstring(xml_str)
    run_properties = extract_run_properties(mock_parser_instance, element)
    assert run_properties.font_size == 1800
    assert run_properties.bold is True
    assert run_properties.italic is True
    assert run_properties.color == "FF0000"
    assert run_properties.font_face == "Arial"
    assert run_properties.underline is True


# Test extract_paragraph_properties
def test_extract_paragraph_properties(mock_parser_instance):
    xml_str = """
    <a:p xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">
        <a:pPr algn="ctr" indent="1000">
            <a:buChar char="•"/>
        </a:pPr>
        <a:r><a:t>Paragraph Text</a:t></a:r>
    </a:p>
    """
    element = etree.fromstring(xml_str)
    paragraph = extract_paragraph_properties(mock_parser_instance, element, None)
    assert paragraph.properties.align == "ctr"
    assert paragraph.properties.indent == 1000
    assert paragraph.properties.bullet_type == "char"
    assert paragraph.properties.bullet_char == "•"
    assert len(paragraph.text_runs) == 1
    assert paragraph.text_runs[0].text == "Paragraph Text"


# Test extract_text_frame_properties
def test_extract_text_frame_properties(mock_parser_instance):
    xml_str = """
    <p:txBody xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main">
        <a:p>
            <a:r><a:t>Line 1</a:t></a:r>
        </a:p>
        <a:p>
            <a:r><a:t>Line 2</a:t></a:r>
        </a:p>
    </p:txBody>
    """
    element = etree.fromstring(xml_str)
    text_frame = extract_text_frame_properties(mock_parser_instance, element, None)
    assert len(text_frame.paragraphs) == 2
    assert text_frame.paragraphs[0].text_runs[0].text == "Line 1"
    assert text_frame.paragraphs[1].text_runs[0].text == "Line 2"
