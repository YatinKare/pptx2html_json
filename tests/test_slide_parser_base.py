from unittest.mock import MagicMock, patch

import pytest

from learnx_parser.parsers.slide.base import SlideParser


@pytest.fixture
def mock_slide_parser():
    with patch("learnx_parser.parsers.slide.base.etree.parse") as mock_parse:
        mock_tree = MagicMock()
        mock_root = MagicMock()
        mock_parse.return_value = mock_tree
        mock_tree.getroot.return_value = mock_root
        mock_root.nsmap = {
            "p": "http://schemas.openxmlformats.org/presentationml/2006/main"
        }

        parser = SlideParser(
            slide_xml_path="dummy.xml",
            slide_rels_path="dummy.rels.xml",
            pptx_unpacked_path="/path/to/unpacked",
            slide_width=100,
            slide_height=100,
        )
        return parser


def test_slide_parser_initialization(mock_slide_parser):
    assert mock_slide_parser.slide_width == 100
    assert mock_slide_parser.slide_height == 100
    assert mock_slide_parser.pptx_unpacked_path == "/path/to/unpacked"
