from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional, Union

@dataclass
class Transform:
    x: int = 0
    y: int = 0
    cx: int = 0
    cy: int = 0
    rot: int = 0
    flipH: bool = False
    flipV: bool = False

@dataclass
class SolidFill:
    color: Optional[str] = None
    scheme_color: Optional[str] = None

@dataclass
class GradientStop:
    pos: int
    color: Optional[str] = None
    scheme_color: Optional[str] = None

@dataclass
class GradientFill:
    stops: List[GradientStop] = field(default_factory=list)
    angle: Optional[int] = None
    scaled: Optional[bool] = None

@dataclass
class BlipFill:
    path: str
    rot_with_shape: bool = False
    src_rect_t: Optional[float] = None
    src_rect_b: Optional[float] = None
    src_rect_l: Optional[float] = None
    src_rect_r: Optional[float] = None

@dataclass
class PatternFill:
    preset: Optional[str] = None
    fg_color: Optional[str] = None
    bg_color: Optional[str] = None

# Define Fill after all its constituent types
Fill = Union[SolidFill, GradientFill, BlipFill, PatternFill]

@dataclass
class Line:
    width: int = 0
    cap: Optional[str] = None
    cmpd: Optional[str] = None
    algn: Optional[str] = None
    color: Optional[str] = None
    scheme_color: Optional[str] = None

@dataclass
class RunProperties:
    font_size: Optional[int] = None
    bold: bool = False
    italic: bool = False
    color: Optional[str] = None
    scheme_color: Optional[str] = None
    font_face: Optional[str] = None
    underline: bool = False

@dataclass
class TextRun:
    text: str
    properties: RunProperties = field(default_factory=RunProperties)

@dataclass
class ParagraphProperties:
    align: Optional[str] = None
    indent: Optional[int] = None

@dataclass
class Paragraph:
    text_runs: List[TextRun] = field(default_factory=list)
    properties: ParagraphProperties = field(default_factory=ParagraphProperties)

@dataclass
class TextFrame:
    paragraphs: List[Paragraph] = field(default_factory=list)

@dataclass
class Hyperlink:
    type: str
    target: str

@dataclass
class CommonSlideData:
    background_color: Optional[str] = None
    background_gradient_fill: Optional[GradientFill] = None

@dataclass
class Picture:
    id: Optional[str] = None
    name: Optional[str] = None
    path: str = ""
    transform: Transform = field(default_factory=Transform)
    blip_fill: Optional[BlipFill] = None
    ph_type: Optional[str] = None
    ph_idx: Optional[int] = None

@dataclass
class GroupShape:
    id: Optional[str] = None
    name: Optional[str] = None
    transform: Transform = field(default_factory=Transform)
    children: List[Any] = field(default_factory=list) # Can contain Shape, Picture, GroupShape

@dataclass
class GraphicFrame:
    id: Optional[str] = None
    name: Optional[str] = None
    transform: Transform = field(default_factory=Transform)

@dataclass
class Shape:
    type: str
    id: Optional[str] = None
    name: Optional[str] = None
    transform: Transform = field(default_factory=Transform)
    prst_geom: Optional[str] = None
    fill: Optional[Fill] = None
    line: Optional[Line] = None
    text_frame: Optional[TextFrame] = None
    ph_type: Optional[str] = None
    ph_idx: Optional[int] = None
    ph_orient: Optional[str] = None
    ph_sz: Optional[str] = None

@dataclass
class Slide:
    slide_number: int
    common_slide_data: CommonSlideData = field(default_factory=CommonSlideData)
    shapes: List[Shape] = field(default_factory=list)
    pictures: List[Picture] = field(default_factory=list)
    group_shapes: List[GroupShape] = field(default_factory=list)
    graphic_frames: List[GraphicFrame] = field(default_factory=list)
    hyperlinks: List[Hyperlink] = field(default_factory=list)

