from dataclasses import dataclass, field
from typing import Any


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
    color: str | None = None
    scheme_color: str | None = None


@dataclass
class GradientStop:
    pos: int
    color: str | None = None
    scheme_color: str | None = None


@dataclass
class GradientFill:
    stops: list[GradientStop] = field(default_factory=list)
    angle: int | None = None
    scaled: bool | None = None


@dataclass
class BlipFill:
    path: str
    rot_with_shape: bool = False
    src_rect_t: float | None = None
    src_rect_b: float | None = None
    src_rect_l: float | None = None
    src_rect_r: float | None = None


@dataclass
class PatternFill:
    preset: str | None = None
    fg_color: str | None = None
    bg_color: str | None = None


# Define Fill after all its constituent types
Fill = SolidFill | GradientFill | BlipFill | PatternFill


@dataclass
class Line:
    width: int = 0
    cap: str | None = None
    cmpd: str | None = None
    algn: str | None = None
    color: str | None = None
    scheme_color: str | None = None


@dataclass
class RunProperties:
    font_size: int | None = None
    bold: bool = False
    italic: bool = False
    color: str | None = None
    scheme_color: str | None = None
    font_face: str | None = None
    font_ref: str | None = None  # Font reference (major, minor) for theme resolution
    underline: bool = False
    cap: str | None = None  # Text capitalization (all, small, none)


@dataclass
class TextRun:
    text: str
    properties: RunProperties = field(default_factory=RunProperties)


@dataclass
class ParagraphProperties:
    align: str | None = None
    indent: int | None = None
    # Bullet properties
    bullet_type: str | None = None  # 'char', 'autoNum', 'blip', 'none'
    bullet_char: str | None = None
    bullet_font_face: str | None = None
    bullet_size_pct: int | None = None
    bullet_size_pts: int | None = None
    bullet_auto_num_type: str | None = None
    bullet_start_at: int | None = None
    bullet_image_path: str | None = None
    level: int | None = None
    # Default run properties for this paragraph level (defRPr)
    default_run_properties: "RunProperties | None" = None


@dataclass
class Paragraph:
    text_runs: list[TextRun] = field(default_factory=list)
    properties: ParagraphProperties = field(default_factory=ParagraphProperties)


@dataclass
class TextFrame:
    paragraphs: list[Paragraph] = field(default_factory=list)
    # Vertical alignment properties from <a:bodyPr>
    anchor: str | None = None  # t (top), ctr (center), b (bottom), just, dist
    anchor_ctr: bool = False  # horizontal centering
    left_inset: int = 0  # lIns - left inset
    top_inset: int = 0  # tIns - top inset
    right_inset: int = 0  # rIns - right inset
    bottom_inset: int = 0  # bIns - bottom inset


@dataclass
class Hyperlink:
    type: str
    target: str


@dataclass
class CommonSlideData:
    background_color: str | None = None
    background_gradient_fill: GradientFill | None = None
    cx: int = 0
    cy: int = 0


@dataclass
class Picture:
    id: str | None = None
    name: str | None = None
    path: str = ""
    transform: Transform = field(default_factory=Transform)
    blip_fill: BlipFill | None = None
    ph_type: str | None = None
    ph_idx: int | None = None


@dataclass
class GroupShape:
    id: str | None = None
    name: str | None = None
    transform: Transform = field(default_factory=Transform)
    children: list[Any] = field(
        default_factory=list
    )  # Can contain Shape, Picture, GroupShape
    is_flex_container: bool = False


@dataclass
class GraphicFrame:
    id: str | None = None
    name: str | None = None
    transform: Transform = field(default_factory=Transform)


@dataclass
class Shape:
    type: str
    id: str | None = None
    name: str | None = None
    transform: Transform = field(default_factory=Transform)
    prst_geom: str | None = None
    fill: Fill | None = None
    line: Line | None = None
    text_frame: TextFrame | None = None
    ph_type: str | None = None
    ph_idx: int | None = None
    ph_orient: str | None = None
    ph_sz: str | None = None


@dataclass
class LayoutPlaceholder:
    ph_type: str | None = None
    ph_idx: int | None = None
    transform: Transform = field(default_factory=Transform)
    # Text frame properties from layout XML
    anchor: str | None = None  # Vertical alignment: t, ctr, b, just, dist
    anchor_ctr: bool = False  # Horizontal centering of bounding box
    # Text insets
    left_inset: int | None = None
    top_inset: int | None = None
    right_inset: int | None = None
    bottom_inset: int | None = None
    # Paragraph alignment from layout lstStyle
    paragraph_align: str | None = (
        None  # Horizontal text alignment: l, r, ctr, just, dist
    )


@dataclass
class SlideLayout:
    name: str | None = None
    type: str | None = None  # e.g., 'title', 'picTx', 'secHead', 'tx'
    placeholders: list[LayoutPlaceholder] = field(default_factory=list)
    list_styles: dict[int, ParagraphProperties] = field(default_factory=dict)


@dataclass
class Slide:
    slide_number: int
    common_slide_data: CommonSlideData = field(default_factory=CommonSlideData)
    shapes: list[Shape] = field(default_factory=list)
    pictures: list[Picture] = field(default_factory=list)
    group_shapes: list[GroupShape] = field(default_factory=list)
    graphic_frames: list[GraphicFrame] = field(default_factory=list)
    hyperlinks: list[Hyperlink] = field(default_factory=list)
    slide_layout: SlideLayout | None = None


# Simplified JSON-friendly data models
@dataclass
class JsonElement:
    type: str
    text: str | None = None
    style: dict[str, Any] | None = None
    items: list[dict[str, Any]] | None = None
    src: str | None = None
    alt: str | None = None
    attribution: str | None = None
    description: str | None = None
    group: str | None = None  # For bullet-list grouping


@dataclass
class JsonSlide:
    id: str
    layout: str
    elements: list[JsonElement] = field(default_factory=list)


@dataclass
class JsonPresentation:
    id: str
    title: str
    slides: list[JsonSlide] = field(default_factory=list)


@dataclass
class JsonPresentationWrapper:
    presentation: JsonPresentation
