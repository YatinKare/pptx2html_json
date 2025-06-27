import os
import pytest
from learnx_parser.presentation_parser import PresentationParser

@pytest.fixture
def presentation_parser():
    presentation_xml_path = os.path.abspath("temp_pptx/ppt/presentation.xml")
    return PresentationParser(presentation_xml_path)

def test_get_slide_order(presentation_parser):
    slide_order = presentation_parser.get_slide_order()
    assert isinstance(slide_order, list)
    assert len(slide_order) > 0
    # Check if the first slide ID is present (from Galaxy presentation.pptx)
    assert "rId2" in slide_order
