"""
Presentation-level data model containing all shared resources.
"""

from dataclasses import dataclass, field

from learnx_parser.models.core import ParagraphProperties, SlideLayout, SlideMaster


@dataclass
class Presentation:
    """
    Container for all presentation-wide data needed for style inheritance.
    
    This centralizes slide masters, layouts, and presentation defaults
    so they can be passed through the parsing pipeline.
    """
    slide_masters: dict[str, SlideMaster] = field(default_factory=dict)
    slide_layouts: dict[str, SlideLayout] = field(default_factory=dict)
    presentation_defaults: dict[int, ParagraphProperties] = field(default_factory=dict)