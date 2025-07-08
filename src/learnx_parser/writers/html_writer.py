"""
Main HTML writer that coordinates slide rendering.
This module contains the main HtmlWriter class that orchestrates HTML generation.
"""

import os

from htpy import body, div, head, html, style, title
from markupsafe import Markup

from learnx_parser.models.core import Slide
from learnx_parser.writers.css_utils import (
    PositioningConfig,
    emu_to_px,
    get_gradient_css,
)
from learnx_parser.writers.layout_handlers import render_slide_content


class HtmlWriter:
    """Main HTML writer class that coordinates slide rendering to HTML."""

    def __init__(self, output_directory="./output", pptx_unpacked_path=None, 
                 positioning_mode="responsive"):
        """Initialize the HTML writer.

        Args:
            output_directory: Directory where HTML files will be saved
            pptx_unpacked_path: Path to unpacked PPTX for resolving media files
            positioning_mode: Positioning mode ('responsive', 'absolute', 'hybrid')
        """
        self.output_directory = output_directory
        self.pptx_unpacked_path = pptx_unpacked_path
        self.positioning_config = PositioningConfig(positioning_mode)

    def write_slide_html(self, slide: Slide, slide_number: int):
        """Write a slide to an HTML file.

        Args:
            slide: Slide object containing the slide data
            slide_number: The slide number for file naming
        """
        if self.positioning_config.mode == PositioningConfig.ABSOLUTE:
            return self._write_slide_absolute(slide, slide_number)
        else:
            return self._write_slide_responsive(slide, slide_number)

    def _write_slide_responsive(self, slide: Slide, slide_number: int):
        """Write a slide using responsive positioning (original method).

        Args:
            slide: Slide object containing the slide data
            slide_number: The slide number for file naming
        """
        # Determine the layout class for the slide container
        layout_classes = ["slide-container"]
        if slide.slide_layout and slide.slide_layout.type:
            layout_classes.append(f"{slide.slide_layout.type}-layout")

        # Get slide dimensions
        slide_width = emu_to_px(slide.common_slide_data.cx)
        slide_height = emu_to_px(slide.common_slide_data.cy)

        # Generate background CSS
        background_css = self._get_background_css(slide)

        # Create CSS content
        css_content = f"""
        body {{ margin: 0; padding: 0; font-family: sans-serif; overflow: hidden; }}
        .slide-container {{ 
            position: relative; 
            width: {slide_width}px; 
            height: {slide_height}px; 
            background-color: #fff; 
            display: flex; 
            flex-direction: column;
            {background_css}
        }}
        .shape, .image, .graphic-frame, .group-shape, .placeholder-container {{ 
            box-sizing: border-box; 
        }}
        .text-content {{ 
            white-space: pre-wrap; 
            word-wrap: break-word; 
        }}

        /* Layout-specific CSS */
        .slide-container.picTx-layout .content-flex-container {{ 
            display: flex; 
            flex-direction: row; 
            justify-content: space-around; 
            align-items: center; 
            flex: 1; 
        }}
        .slide-container.tx-layout .content-flex-container {{ 
            display: flex; 
            flex-direction: column; 
            justify-content: center; 
            align-items: center; 
            flex: 1; 
        }}
        .slide-container.titlePic-layout .content-flex-container {{ 
            display: flex; 
            flex-direction: row; 
            justify-content: space-around; 
            align-items: center; 
            flex: 1; 
        }}
        .title-container {{ 
            display: flex; 
            justify-content: center; 
            align-items: center; 
            flex: 0 0 auto; 
        }}
        .content-flex-container {{ 
            display: flex; 
            flex: 1; 
        }}
        """

        # Render the slide content
        slide_content = render_slide_content(slide, self)

        # Generate the HTML structure using htpy
        html_doc = html[
            head[
                title[f"Slide {slide_number}"],
                style[Markup(css_content)]
            ],
            body[
                div(class_=" ".join(layout_classes))[
                    Markup(slide_content)
                ]
            ]
        ]

        # Create output directory and write file
        slide_output_directory = os.path.join(
            self.output_directory, f"slide{slide_number}"
        )
        os.makedirs(slide_output_directory, exist_ok=True)

        output_file_path = os.path.join(
            slide_output_directory, f"slide{slide_number}.html"
        )
        with open(output_file_path, "w", encoding="utf-8") as f:
            f.write(str(html_doc))
        return output_file_path

    def _write_slide_absolute(self, slide: Slide, slide_number: int):
        """Write a slide using absolute positioning.

        Args:
            slide: Slide object containing the slide data
            slide_number: The slide number for file naming
        """
        # Use fixed slide dimensions for absolute positioning
        slide_width = self.positioning_config.slide_width
        slide_height = self.positioning_config.slide_height

        # Generate background CSS
        background_css = self._get_background_css(slide)

        # Create CSS content for absolute positioning (HTML5Point-inspired)
        css_content = f"""
        body {{ 
            position: absolute;
            height: 100%;
            width: 100%;
            overflow: hidden;
            margin: 0px;
            padding: 0;
            font-family: sans-serif;
        }}
        
        #player {{
            position: relative;
            height: 100%;
            width: 100%;
            overflow: hidden;
        }}
        
        #player canvas, #player div, #player iframe, #player img {{
            position: absolute;
        }}
        
        #resizer {{ 
            left: 0px;
            top: 0px;
            height: {slide_height}px;
            width: {slide_width}px;
            overflow: hidden;
            -moz-transform-origin: 0 0;
            -o-transform-origin: 0 0;
            -webkit-transform-origin: 0 0;
            -ms-transform-origin: 0 0;
            transform-origin: 0 0;
            position: absolute;
            left: 50%;
            top: 50%;
            margin-left: -{slide_width//2}px;
            margin-top: -{slide_height//2}px;
            {background_css}
        }}
        
        .shape {{
            position: absolute;
            box-sizing: border-box;
        }}
        
        .image {{
            position: absolute;
        }}
        
        /* Auto-scaling based on window size */
        @media all {{
            #resizer {{
                transform: scale(min(calc(100vw / {slide_width}), calc(100vh / {slide_height})));
            }}
        }}
        """

        # Render the slide content with absolute positioning
        slide_content = self._render_slide_content_absolute(slide)

        # Generate the HTML structure using htpy (HTML5Point-inspired)
        html_doc = html[
            head[
                title[f"Slide {slide_number}"],
                style[Markup(css_content)]
            ],
            body[
                div(id="player")[
                    div(id="resizer")[
                        Markup(slide_content)
                    ]
                ]
            ]
        ]

        # Create output directory and write file
        slide_output_directory = os.path.join(
            self.output_directory, f"slide{slide_number}"
        )
        os.makedirs(slide_output_directory, exist_ok=True)

        output_file_path = os.path.join(
            slide_output_directory, f"slide{slide_number}.html"
        )
        with open(output_file_path, "w", encoding="utf-8") as f:
            f.write(str(html_doc))
        return output_file_path

    def _render_slide_content_absolute(self, slide: Slide) -> str:
        """Render slide content with absolute positioning.
        
        Args:
            slide: Slide object containing elements to render
            
        Returns:
            str: HTML content for the slide with absolute positioning
        """
        from learnx_parser.writers.element_renderers import (
            render_graphic_frame_html,
            render_group_shape_html,
            render_picture_html,
            render_shape_html,
        )
        
        html_parts = []
        
        # Render all shapes with absolute positioning
        for shape in slide.shapes:
            try:
                shape_html = render_shape_html(shape, use_absolute_pos=True)
                html_parts.append(shape_html)
            except Exception as e:
                # Fallback rendering if element renderer fails
                print(f"Warning: Failed to render shape {getattr(shape, 'id', 'unknown')}: {e}")
                if shape.transform:
                    from learnx_parser.writers.css_utils import CoordinateConverter
                    position = CoordinateConverter.extract_position(shape.transform)
                    if position:
                        css = CoordinateConverter.generate_absolute_css(position, 100)
                        fallback_html = f'<div class="shape-fallback" style="{css} background: lightcoral; border: 1px solid #999;">Shape (fallback)</div>'
                        html_parts.append(fallback_html)
        
        # Render all pictures with absolute positioning  
        for picture in slide.pictures:
            try:
                picture_html = render_picture_html(picture, use_absolute_pos=True)
                html_parts.append(picture_html)
            except Exception as e:
                # Fallback rendering if element renderer fails
                print(f"Warning: Failed to render picture {getattr(picture, 'id', 'unknown')}: {e}")
                if picture.transform:
                    from learnx_parser.writers.css_utils import CoordinateConverter
                    position = CoordinateConverter.extract_position(picture.transform)
                    if position:
                        css = CoordinateConverter.generate_absolute_css(position, 300)
                        fallback_html = f'<div class="picture-fallback" style="{css} background: lightblue; border: 1px solid #666;">Picture (fallback)</div>'
                        html_parts.append(fallback_html)
        
        # Render all group shapes with absolute positioning
        for group_shape in slide.group_shapes:
            try:
                group_html = render_group_shape_html(group_shape, use_absolute_pos=True)
                html_parts.append(group_html)
            except Exception as e:
                # Fallback rendering if element renderer fails
                print(f"Warning: Failed to render group shape {getattr(group_shape, 'id', 'unknown')}: {e}")
                if group_shape.transform:
                    from learnx_parser.writers.css_utils import CoordinateConverter
                    position = CoordinateConverter.extract_position(group_shape.transform)
                    if position:
                        css = CoordinateConverter.generate_absolute_css(position, 100)
                        fallback_html = f'<div class="group-fallback" style="{css} background: lightgreen; border: 1px solid #333;">Group (fallback)</div>'
                        html_parts.append(fallback_html)
        
        # Render all graphic frames with absolute positioning
        for graphic_frame in slide.graphic_frames:
            try:
                frame_html = render_graphic_frame_html(graphic_frame)
                html_parts.append(frame_html)
            except Exception as e:
                # Fallback rendering if element renderer fails
                print(f"Warning: Failed to render graphic frame {getattr(graphic_frame, 'id', 'unknown')}: {e}")
                if graphic_frame.transform:
                    from learnx_parser.writers.css_utils import CoordinateConverter
                    position = CoordinateConverter.extract_position(graphic_frame.transform)
                    if position:
                        css = CoordinateConverter.generate_absolute_css(position, 100)
                        fallback_html = f'<div class="frame-fallback" style="{css} background: lightyellow; border: 1px solid #444;">Frame (fallback)</div>'
                        html_parts.append(fallback_html)
        
        # If no elements, show placeholder
        if not html_parts:
            html_parts.append('<div class="element-absolute" style="left: 100px; top: 100px; width: 200px; height: 50px; background: lightgray; z-index: 1; border: 1px dashed #ccc;">No elements found</div>')
        
        return ''.join(html_parts)

    def _get_background_css(self, slide: Slide) -> str:
        """Generate CSS for slide background.

        Args:
            slide: Slide object

        Returns:
            str: CSS for slide background
        """
        background_css_parts = []

        # Add solid background color
        if slide.common_slide_data.background_color:
            background_css_parts.append(
                f"background-color: #{slide.common_slide_data.background_color};"
            )

        # Add gradient background
        if slide.common_slide_data.background_gradient_fill:
            gradient_css = get_gradient_css(
                slide.common_slide_data.background_gradient_fill
            )
            if gradient_css:
                background_css_parts.append(gradient_css)

        return " ".join(background_css_parts)
