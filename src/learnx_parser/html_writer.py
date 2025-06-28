import os
import shutil
from learnx_parser.data_models import (
    Slide, Shape, Picture, GroupShape, GraphicFrame, TextFrame, Paragraph, TextRun,
    Transform, SolidFill, GradientFill, BlipFill, PatternFill, Line, RunProperties, ParagraphProperties, Hyperlink
)

class HtmlWriter:
    def __init__(self, output_dir="./output", pptx_unpacked_path=None):
        self.output_dir = output_dir
        self.pptx_unpacked_path = pptx_unpacked_path

    def _emu_to_px(self, emu):
        # 1 EMUs = 1/914400 inches, 1 inch = 96 pixels (standard for web)
        return round(emu / 914400 * 96)

    def _get_gradient_css(self, gradient_fill: GradientFill):
        if not gradient_fill or not gradient_fill.stops:
            return ""

        # Assuming linear gradient for simplicity, angle is in degrees
        angle = gradient_fill.angle if gradient_fill.angle is not None else 0
        # Convert angle to CSS standard (0deg is bottom, 90deg is right)
        css_angle = (angle + 90) % 360

        color_stops = []
        for stop in gradient_fill.stops:
            color = f"#{stop.color}"
            position = f"{stop.pos * 100}%" # Corrected to use stop.pos
            color_stops.append(f"{color} {position}")

        return f"background: linear-gradient({css_angle}deg, {', '.join(color_stops)});"

    def _get_transform_css(self, transform: Transform):
        css_transforms = []
        if transform.rot != 0:
            # PowerPoint rotation is in 60000ths of a degree, CSS is in degrees
            css_transforms.append(f"rotate({transform.rot / 60000:.2f}deg)")
        if transform.flipH:
            css_transforms.append("scaleX(-1)")
        if transform.flipV:
            css_transforms.append("scaleY(-1)")
        return "transform: " + " ".join(css_transforms) + ";" if css_transforms else ""

    def _get_image_crop_css(self, blip_fill: BlipFill):
        if blip_fill and (blip_fill.src_rect_t is not None or
                          blip_fill.src_rect_b is not None or
                          blip_fill.src_rect_l is not None or
                          blip_fill.src_rect_r is not None):
            top = f"{blip_fill.src_rect_t / 1000:.2f}%" if blip_fill.src_rect_t is not None else "0%"
            bottom = f"{blip_fill.src_rect_b / 1000:.2f}%" if blip_fill.src_rect_b is not None else "0%"
            left = f"{blip_fill.src_rect_l / 1000:.2f}%" if blip_fill.src_rect_l is not None else "0%"
            right = f"{blip_fill.src_rect_r / 1000:.2f}%" if blip_fill.src_rect_r is not None else "0%"
            return f"clip-path: inset({top} {right} {bottom} {left});"
        return ""

    def write_slide_html(self, slide: Slide, slide_number: int):
        html_content = """<!DOCTYPE html>
<html>
<head>
    <title>Slide {slide_number}</title>
    <style>
        body {{ margin: 0; padding: 0; font-family: sans-serif; overflow: hidden; }}
        .slide-container {{ position: relative; width: 1280px; height: 720px; background-color: #fff; }}
        .shape {{ position: absolute; box-sizing: border-box; }}
        .text-content {{ white-space: pre-wrap; word-wrap: break-word; }}
        .image {{ position: absolute; }}
    </style>
</head>
<body>
    <div class="slide-container">
"""

        all_elements = []
        for shape in slide.shapes:
            all_elements.append(shape)
        for picture in slide.pictures:
            all_elements.append(picture)
        for group_shape in slide.group_shapes:
            all_elements.append(group_shape)
        for graphic_frame in slide.graphic_frames:
            all_elements.append(graphic_frame)

        # Sort elements by their y-coordinate to maintain some visual order
        all_elements.sort(key=lambda e: e.transform.y)

        for element in all_elements:
            x = self._emu_to_px(element.transform.x)
            y = self._emu_to_px(element.transform.y)
            cx = self._emu_to_px(element.transform.cx)
            cy = self._emu_to_px(element.transform.cy)

            if isinstance(element, Shape):
                shape_style = ""
                if element.fill:
                    if isinstance(element.fill, SolidFill):
                        shape_style += f"background-color: #{element.fill.color};"
                    elif isinstance(element.fill, GradientFill):
                        shape_style += self._get_gradient_css(element.fill)
                if element.line:
                    shape_style += f"border: {self._emu_to_px(element.line.width)}px solid #{element.line.color};"

                text_content_html = ""
                if element.text_frame:
                    for paragraph in element.text_frame.paragraphs:
                        paragraph_style = ""
                        if paragraph.properties and paragraph.properties.align:
                            paragraph_style += f"text-align: {paragraph.properties.align};"
                        if paragraph.properties and paragraph.properties.indent is not None:
                            paragraph_style += f"padding-left: {self._emu_to_px(paragraph.properties.indent)}px;"

                        text_runs_html = ""
                        for run in paragraph.text_runs:
                            run_style = ""
                            if run.properties:
                                if run.properties.font_size:
                                    run_style += f"font-size: {self._emu_to_px(run.properties.font_size)}px;"
                                if run.properties.bold:
                                    run_style += "font-weight: bold;"
                                if run.properties.italic:
                                    run_style += "font-style: italic;"
                                if run.properties.underline:
                                    run_style += "text-decoration: underline;"
                                if run.properties.color:
                                    run_style += f"color: #{run.properties.color};"
                                elif run.properties.scheme_color:
                                    run_style += f"color: var(--{run.properties.scheme_color}-color, black);"
                                if run.properties.font_face:
                                    run_style += f"font-family: '{run.properties.font_face}';"

                            text_runs_html += f"<span style=\"{run_style}\">{run.text}</span>"
                        text_content_html += f"<p style=\"{paragraph_style}\">{text_runs_html}</p>"

                html_content += f"""
        <div class="shape" style="left: {x}px; top: {y}px; width: {cx}px; height: {cy}px; {shape_style} {self._get_transform_css(element.transform)}">
            <div class="text-content">{text_content_html}</div>
        </div>
"""
            elif isinstance(element, Picture):
                image_src = os.path.join("media", os.path.basename(element.blip_fill.path))
                html_content += f"""
        <img class="image" src="{image_src}" style="left: {x}px; top: {y}px; width: {cx}px; height: {cy}px; {self._get_transform_css(element.transform)} {self._get_image_crop_css(element.blip_fill)}" />
"""
            elif isinstance(element, GroupShape):
                # For GroupShape, create a container div and recursively render its children
                # This is a simplified approach and might need more complex styling for accurate group rendering
                group_content_html = ""
                # Recursively render children - this would require a helper method or refactoring
                # For now, we'll just create a div for the group itself
                html_content += f"""
        <div class="group-shape" style="left: {x}px; top: {y}px; width: {cx}px; height: {cy}px;">
            <!-- Grouped elements would go here -->
        </div>
"""
            elif isinstance(element, GraphicFrame):
                html_content += f"""
        <div class="graphic-frame" style="left: {x}px; top: {y}px; width: {cx}px; height: {cy}px;">
            <!-- Graphic Frame content (e.g., charts, tables) would go here -->
        </div>
"""

        html_content += """
    </div>
</body>
</html>"""

        slide_output_dir = os.path.join(self.output_dir, f"slide{slide_number}")
        os.makedirs(slide_output_dir, exist_ok=True)

        output_file_path = os.path.join(slide_output_dir, f"slide{slide_number}.html")
        with open(output_file_path, "w", encoding="utf-8") as f:
            f.write(html_content)
        return output_file_path
