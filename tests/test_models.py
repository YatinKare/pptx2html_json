import pytest

from learnx_parser.models.core import (
    BlipFill,
    CommonSlideData,
    GradientFill,
    GradientStop,
    GraphicFrame,
    GroupShape,
    Hyperlink,
    JsonElement,
    JsonPresentation,
    JsonSlide,
    LayoutPlaceholder,
    Line,
    Paragraph,
    ParagraphProperties,
    PatternFill,
    Picture,
    RunProperties,
    Shape,
    Slide,
    SlideLayout,
    SolidFill,
    TextFrame,
    TextRun,
    Transform,
)


def test_data_models_instantiation():
    # This test simply checks if all data models can be instantiated without errors.
    try:
        Transform()
        SolidFill()
        GradientStop(pos=0)
        GradientFill()
        BlipFill(path="")
        PatternFill()
        Line()
        RunProperties()
        TextRun(text="test")
        ParagraphProperties()
        Paragraph()
        TextFrame()
        Hyperlink(type="hyperlink", target="http://example.com")
        CommonSlideData()
        Picture()
        GroupShape()
        GraphicFrame()
        Shape(type="shape")
        LayoutPlaceholder()
        SlideLayout()
        Slide(slide_number=1)
        JsonElement(type="element")
        JsonSlide(id="slide1", layout="layout")
        JsonPresentation(id="pres1", title="title")
    except Exception as e:
        pytest.fail(f"Failed to instantiate data models: {e}")
