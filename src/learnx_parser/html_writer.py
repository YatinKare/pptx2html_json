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
        return round(emu / 9525)

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

    def _get_shape_style_css(self, element: Shape) -> str:
        shape_style = ""
        if element.fill:
            if isinstance(element.fill, SolidFill):
                shape_style += f"background-color: #{element.fill.color};"
            elif isinstance(element.fill, GradientFill):
                shape_style += self._get_gradient_css(element.fill)
        if element.line:
            shape_style += f"border: {self._emu_to_px(element.line.width)}px solid #{element.line.color};"
        return shape_style

    def _get_paragraph_style_css(self, paragraph: Paragraph) -> str:
        paragraph_style = ""
        if paragraph.properties and paragraph.properties.align:
            paragraph_style += f"text-align: {paragraph.properties.align};"
        if paragraph.properties and paragraph.properties.indent is not None:
            paragraph_style += f"padding-left: {self._emu_to_px(paragraph.properties.indent)}px;"
        return paragraph_style

    def _get_run_style_css(self, run: TextRun) -> str:
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
        return run_style

    def _get_flex_properties_from_name(self, name: str) -> str:
        flex_style = ""
        if "flex-row" in name:
            flex_style += "flex-direction: row;"
        if "flex-col" in name:
            flex_style += "flex-direction: column;"
        if "justify-center" in name:
            flex_style += "justify-content: center;"
        if "justify-between" in name:
            flex_style += "justify-content: space-between;"
        if "items-center" in name:
            flex_style += "align-items: center;"
        return flex_style

    def _render_graphic_frame_html(self, element: GraphicFrame, parent_x: int = 0, parent_y: int = 0) -> str:
        x = self._emu_to_px(element.transform.x - parent_x)
        y = self._emu_to_px(element.transform.y - parent_y)
        cx = self._emu_to_px(element.transform.cx)
        cy = self._emu_to_px(element.transform.cy)
        return f"""
        <div class="graphic-frame" style="left: {x}px; top: {y}px; width: {cx}px; height: {cy}px;">
            <!-- Graphic Frame content (e.g., charts, tables) would go here -->
        </div>
"""

    def _render_group_shape_html(self, element: GroupShape, parent_x: int = 0, parent_y: int = 0) -> str:
        relative_x = self._emu_to_px(element.transform.x - parent_x)
        relative_y = self._emu_to_px(element.transform.y - parent_y)
        cx = self._emu_to_px(element.transform.cx)
        cy = self._emu_to_px(element.transform.cy)

        group_style = ""
        if element.is_flex_container:
            group_style += "display: flex; "
            group_style += self._get_flex_properties_from_name(element.name)

        children_html = ""
        for child in element.children[0]: # shapes
            children_html += self._render_shape_html(child, element.transform.x, element.transform.y)
        for child in element.children[1]: # pictures
            children_html += self._render_picture_html(child, element.transform.x, element.transform.y)
        for child in element.children[2]: # group_shapes
            children_html += self._render_group_shape_html(child, element.transform.x, element.transform.y)
        for child in element.children[3]: # graphic_frames
            children_html += self._render_graphic_frame_html(child, element.transform.x, element.transform.y)

        return f"""
        <div class="group-shape" style="left: {relative_x}px; top: {relative_y}px; width: {cx}px; height: {cy}px; {group_style}">
            {children_html}
        </div>
"""

    def _render_picture_html(self, element: Picture, parent_x: int = 0, parent_y: int = 0) -> str:
        x = self._emu_to_px(element.transform.x - parent_x)
        y = self._emu_to_px(element.transform.y - parent_y)
        cx = self._emu_to_px(element.transform.cx)
        cy = self._emu_to_px(element.transform.cy)
        image_src = os.path.join("media", os.path.basename(element.blip_fill.path))
        return f"""
        <img class="image" src="{image_src}" style="left: {x}px; top: {y}px; width: {cx}px; height: {cy}px; {self._get_transform_css(element.transform)} {self._get_image_crop_css(element.blip_fill)}" />
"""

    def _render_shape_html(self, element: Shape, parent_x: int = 0, parent_y: int = 0) -> str:
        x = self._emu_to_px(element.transform.x - parent_x)
        y = self._emu_to_px(element.transform.y - parent_y)
        cx = self._emu_to_px(element.transform.cx)
        cy = self._emu_to_px(element.transform.cy)

        shape_style = self._get_shape_style_css(element)

        text_content_html = ""
        if element.text_frame:
            for paragraph in element.text_frame.paragraphs:
                paragraph_style = self._get_paragraph_style_css(paragraph)

                text_runs_html = ""
                for run in paragraph.text_runs:
                    run_style = self._get_run_style_css(run)

                    text_runs_html += f"<span style=\"{run_style}\">{run.text}</span>"
                text_content_html += f"<p style=\"{paragraph_style}\">{text_runs_html}</p>"

        return f"""
        <div class="shape" id="shape-{element.id}" style="left: {x}px; top: {y}px; width: {cx}px; height: {cy}px; {shape_style} {self._get_transform_css(element.transform)}">
            <div class="text-content">{text_content_html}</div>
        </div>
"""

    def _render_slide_content(self, slide: Slide) -> str:
        content_html = ""
        title_html = ""
        main_content_html = ""
        image_html = ""
        text_html = ""

        title_shape = None
        main_image = None
        body_shape = None

        # Identify elements based on placeholder types
        for shape in slide.shapes:
            if shape.ph_type == "title":
                title_shape = shape
            elif shape.ph_type == "body":
                body_shape = shape
        for picture in slide.pictures:
            if picture.ph_type == "pic":
                main_image = picture

        # Render title if present
        if title_shape:
            title_html = self._render_shape_html(title_shape, 0, 0) # Title is always absolute to slide

        # Determine layout for main content (image and body text)
        if main_image and body_shape:
            # Check if they are side-by-side (image on left, text on right)
            # This is a heuristic based on their x-coordinates
            if main_image.transform.x < body_shape.transform.x:
                # Image is on the left, text is on the right
                # Create a flex container for these two elements
                main_content_html += f"""
        <div class="flex-row-container" style="display: flex; position: absolute; left: {self._emu_to_px(min(main_image.transform.x, body_shape.transform.x))}px; top: {self._emu_to_px(min(main_image.transform.y, body_shape.transform.y))}px; width: {self._emu_to_px(max(main_image.transform.x + main_image.transform.cx, body_shape.transform.x + body_shape.transform.cx) - min(main_image.transform.x, body_shape.transform.x))}px; height: {self._emu_to_px(max(main_image.transform.y + main_image.transform.cy, body_shape.transform.y + body_shape.transform.cy) - min(main_image.transform.y, body_shape.transform.y))}px;">
            {self._render_picture_html(main_image, min(main_image.transform.x, body_shape.transform.x), min(main_image.transform.y, body_shape.transform.y))}
            {self._render_shape_html(body_shape, min(main_image.transform.x, body_shape.transform.x), min(main_image.transform.y, body_shape.transform.y))}
        </div>
"""
            else:
                # Default to absolute positioning if not a clear side-by-side
                image_html = self._render_picture_html(main_image, 0, 0)
                text_html = self._render_shape_html(body_shape, 0, 0)
                main_content_html += image_html + text_html
        elif main_image:
            image_html = self._render_picture_html(main_image, 0, 0)
            main_content_html += image_html
        elif body_shape:
            text_html = self._render_shape_html(body_shape, 0, 0)
            main_content_html += text_html

        # Add any other shapes or graphic frames that are not part of the main content
        for element in slide.shapes + slide.pictures + slide.group_shapes + slide.graphic_frames:
            if element != title_shape and element != main_image and element != body_shape:
                if isinstance(element, Shape):
                    content_html += self._render_shape_html(element, 0, 0)
                elif isinstance(element, Picture):
                    content_html += self._render_picture_html(element, 0, 0)
                elif isinstance(element, GroupShape):
                    content_html += self._render_group_shape_html(element, 0, 0)
                elif isinstance(element, GraphicFrame):
                    content_html += self._render_graphic_frame_html(element, 0, 0)

        return title_html + main_content_html + content_html

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
        html_content += self._render_slide_content(slide)

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
