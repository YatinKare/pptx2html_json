import os
import pytest
from learnx_parser.slide_parser import SlideParser
from learnx_parser.data_models import Slide, Shape, Picture, GroupShape, GraphicFrame, Hyperlink, CommonSlideData, Transform, SolidFill, Line, TextFrame, Paragraph, ParagraphProperties, TextRun, RunProperties, GradientFill, GradientStop

@pytest.fixture
def slide_parser():
    # Use the sample slide data from the temp_pptx directory
    slide_xml_path = os.path.abspath("temp_pptx/ppt/slides/slide23.xml")
    slide_rels_path = os.path.abspath("temp_pptx/ppt/slides/_rels/slide23.xml.rels")
    pptx_unpacked_path = os.path.abspath("temp_pptx")
    slide_width = 12192000  # Example width in EMUs from presentation.xml
    slide_height = 6858000  # Example height in EMUs from presentation.xml
    return SlideParser(slide_xml_path, slide_rels_path, pptx_unpacked_path, slide_width, slide_height)

def test_parse_slide_common_data(slide_parser):
    slide_obj = slide_parser.parse_slide(slide_number=23)
    assert isinstance(slide_obj, Slide)
    assert isinstance(slide_obj.common_slide_data, CommonSlideData)

    # Test for gradient fill in slideLayout133.xml (background)
    slide_xml_path_grad = os.path.abspath("temp_pptx/ppt/slideLayouts/slideLayout133.xml")
    slide_rels_path_grad = os.path.abspath("temp_pptx/ppt/slideLayouts/_rels/slideLayout133.xml.rels")
    parser_grad = SlideParser(slide_xml_path_grad, slide_rels_path_grad, os.path.abspath("temp_pptx"), slide_width=12192000, slide_height=6858000)
    slide_obj_grad = parser_grad.parse_slide(slide_number=0) # Slide number doesn't matter for layout

    assert slide_obj_grad.common_slide_data.background_color is None # Background color is not directly set, but via gradFill
    assert slide_obj_grad.common_slide_data.background_gradient_fill is not None
    assert isinstance(slide_obj_grad.common_slide_data.background_gradient_fill, GradientFill)
    assert len(slide_obj_grad.common_slide_data.background_gradient_fill.stops) == 2
    assert slide_obj_grad.common_slide_data.background_gradient_fill.stops[0].pos == 100000
    assert slide_obj_grad.common_slide_data.background_gradient_fill.stops[0].scheme_color == "accent4"
    assert slide_obj_grad.common_slide_data.background_gradient_fill.stops[1].pos == 0
    assert slide_obj_grad.common_slide_data.background_gradient_fill.stops[1].scheme_color == "accent2"
    assert slide_obj_grad.common_slide_data.background_gradient_fill.angle == 8100000
    assert slide_obj_grad.common_slide_data.background_gradient_fill.scaled == True

def test_parse_slide_shapes_and_media(slide_parser):
    slide_obj = slide_parser.parse_slide(slide_number=23)
    
    assert isinstance(slide_obj.shapes, list)
    assert isinstance(slide_obj.pictures, list)
    assert isinstance(slide_obj.group_shapes, list)
    assert isinstance(slide_obj.graphic_frames, list)

    # Test for a text shape (p:sp)
    text_shape = next((s for s in slide_obj.shapes if s.type == "shape" and s.text_frame and s.text_frame.paragraphs and "Agenda" in s.text_frame.paragraphs[0].text_runs[0].text), None)
    assert text_shape is not None
    assert isinstance(text_shape, Shape)
    assert isinstance(text_shape.transform, Transform)
    assert text_shape.transform.x == 5116544 # Inherited from slideLayout26.xml
    assert text_shape.transform.y == 614202 # Inherited from slideLayout26.xml
    assert text_shape.transform.cx == 5918072 # Inherited from slideLayout26.xml
    assert text_shape.transform.cy == 2276856 # Inherited from slideLayout26.xml
    assert text_shape.transform.rot == 0
    assert text_shape.transform.flipH == False
    assert text_shape.transform.flipV == False
    assert text_shape.ph_type == "title"
    assert text_shape.ph_idx is None # No idx for title placeholder in slide23.xml
    assert text_shape.ph_orient is None
    assert text_shape.ph_sz is None

    # Test for run properties of the "Agenda" text
    agenda_run = text_shape.text_frame.paragraphs[0].text_runs[0]
    assert agenda_run.text == "Agenda"
    assert agenda_run.properties.font_size is None
    assert agenda_run.properties.bold == False
    assert agenda_run.properties.italic == False
    assert agenda_run.properties.color is None # Assuming no explicit color for Agenda
    assert agenda_run.properties.scheme_color is None # Assuming no explicit scheme color for Agenda
    assert agenda_run.properties.font_face is None # Assuming no explicit font face for Agenda
    assert agenda_run.properties.underline == False # Assuming no explicit underline for Agenda

    # Test for a picture (p:pic)
    picture_obj = next((p for p in slide_obj.pictures if p.path.endswith("/ppt/media/image1.png")), None)
    assert picture_obj is not None
    assert isinstance(picture_obj, Picture)
    assert isinstance(picture_obj.transform, Transform)
    assert picture_obj.transform.x == 1280160 # Inherited from slideLayout26.xml
    assert picture_obj.transform.y == 2530058 # Inherited from slideLayout26.xml
    assert picture_obj.transform.cx == 3707972 # Inherited from slideLayout26.xml
    assert picture_obj.transform.cy == 3707971 # Inherited from slideLayout26.xml
    assert picture_obj.transform.rot == 0
    assert picture_obj.transform.flipH == False
    assert picture_obj.transform.flipV == False
    assert picture_obj.blip_fill is not None
    assert picture_obj.blip_fill.path.endswith("/ppt/media/image1.png")
    assert picture_obj.blip_fill.rot_with_shape == True
    assert picture_obj.blip_fill.src_rect_t == 21
    assert picture_obj.blip_fill.src_rect_b == 21
    assert picture_obj.blip_fill.src_rect_l is None
    assert picture_obj.blip_fill.src_rect_r is None
    assert picture_obj.ph_type == "pic"
    assert picture_obj.ph_idx == 14

    # Test for group shapes (p:grpSp) - assuming slide23.xml has one
    # For now, we'll just check if a group shape exists and has children
    # group_shape = next((s for s in slide_obj.group_shapes), None)
    # assert group_shape is not None # Uncomment if slide23.xml is confirmed to have a group shape
    # if group_shape:
    #     assert isinstance(group_shape, GroupShape)
    #     assert isinstance(group_shape.children, list)

    # Test for graphic frames (p:graphicFrame) - assuming slide23.xml has one
    # For now, we'll just check if a graphic frame exists
    # graphic_frame = next((s for s in slide_obj.graphic_frames), None)
    # assert graphic_frame is not None # Uncomment if slide23.xml is confirmed to have a graphic frame

def test_parse_slide_hyperlinks(slide_parser):
    slide_obj = slide_parser.parse_slide(slide_number=23)
    hyperlinks = slide_obj.hyperlinks
    assert isinstance(hyperlinks, list)
    assert len(hyperlinks) == 0

def test_parse_slide_overall_structure(slide_parser):
    slide_obj = slide_parser.parse_slide(slide_number=23)
    assert isinstance(slide_obj, Slide)
    assert isinstance(slide_obj.common_slide_data, CommonSlideData)
    assert isinstance(slide_obj.shapes, list)
    assert isinstance(slide_obj.pictures, list)
    assert isinstance(slide_obj.group_shapes, list)
    assert isinstance(slide_obj.graphic_frames, list)
    assert isinstance(slide_obj.hyperlinks, list)
    assert len(slide_obj.shapes) > 0