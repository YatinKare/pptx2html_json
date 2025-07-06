"""
Main HTML writer that coordinates slide rendering.
This module contains the main HtmlWriter class that orchestrates HTML generation.
"""

import os

from learnx_parser.models.core import Slide
from learnx_parser.writers.css_utils import emu_to_px, get_gradient_css
from learnx_parser.writers.layout_handlers import render_slide_content


class HtmlWriter:
    """Main HTML writer class that coordinates slide rendering to HTML."""

    def __init__(self, output_directory="./output", pptx_unpacked_path=None):
        """Initialize the HTML writer.

        Args:
            output_directory: Directory where HTML files will be saved
            pptx_unpacked_path: Path to unpacked PPTX for resolving media files
        """
        self.output_directory = output_directory
        self.pptx_unpacked_path = pptx_unpacked_path

    def write_slide_html(self, slide: Slide, slide_number: int):
        """Write a slide to an HTML file.

        Args:
            slide: Slide object containing the slide data
            slide_number: The slide number for file naming
        """
        # Determine the layout class for the slide container
        layout_class = ""
        if slide.slide_layout and slide.slide_layout.type:
            layout_class = f" {slide.slide_layout.type}-layout"

        # Get slide dimensions
        slide_width = emu_to_px(slide.common_slide_data.cx)
        slide_height = emu_to_px(slide.common_slide_data.cy)

        # Generate background CSS
        background_css = self._get_background_css(slide)

        # Generate the HTML structure
        html_content = f"""<!DOCTYPE html>
<html>
<head>
    <title>Slide {slide_number}</title>
    <style>
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
    </style>
</head>
<body>
    <div class="slide-container{layout_class}">
"""

        # Render the slide content
        html_content += render_slide_content(slide, self)

        # Close the HTML structure
        html_content += """
    </div>
</body>
</html>"""

        # Create output directory and write file
        slide_output_directory = os.path.join(
            self.output_directory, f"slide{slide_number}"
        )
        os.makedirs(slide_output_directory, exist_ok=True)

        output_file_path = os.path.join(
            slide_output_directory, f"slide{slide_number}.html"
        )
        with open(output_file_path, "w", encoding="utf-8") as f:
            f.write(html_content)
        return output_file_path

    def _get_background_css(self, slide: Slide) -> str:
        """Generate CSS for slide background.

        Args:
            slide: Slide object

        Returns:
            str: CSS for slide background
        """
        background_css = ""

        # Add solid background color
        if slide.common_slide_data.background_color:
            background_css += (
                f"background-color: #{slide.common_slide_data.background_color};"
            )

        # Add gradient background
        if slide.common_slide_data.background_gradient_fill:
            gradient_css = get_gradient_css(
                slide.common_slide_data.background_gradient_fill
            )
            if gradient_css:
                background_css += f" {gradient_css}"

        return background_css
