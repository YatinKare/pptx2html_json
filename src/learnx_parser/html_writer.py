import os
import shutil
from learnx_parser.data_models import (
    Slide, Shape, Picture, GroupShape, GraphicFrame, TextFrame, Paragraph, TextRun,
    Transform, SolidFill, GradientFill, BlipFill, PatternFill, Line, RunProperties, ParagraphProperties, Hyperlink
)

class HtmlWriter:
    def __init__(self, output_directory="./output", pptx_unpacked_path=None):
        # Directory where the generated HTML and associated media files will be saved
        self.output_directory = output_directory
        # Path to the unpacked PowerPoint presentation, used for resolving media file paths
        self.pptx_unpacked_path = pptx_unpacked_path

    def _emu_to_px(self, emu):
        # Convert English Metric Units (EMU) to pixels. 1 inch = 914400 EMUs = 96 pixels (standard DPI).
        # Therefore, 1 EMU = 96 / 914400 pixels = 1 / 9525 pixels.
        return round(emu / 9525)

    def _get_gradient_css(self, gradient_fill: GradientFill):
        # Generate CSS for a linear gradient background
        if not gradient_fill or not gradient_fill.stops:
            return ""

        # PowerPoint rotation is in 60000ths of a degree. CSS uses degrees, where 0deg is to bottom.
        # Adjust angle to CSS standard (0deg is bottom, 90deg is right) if necessary.
        angle = gradient_fill.angle if gradient_fill.angle is not None else 0
        css_angle = (angle + 90) % 360

        color_stops = []
        # Iterate through each gradient stop to format color and position
        for stop in gradient_fill.stops:
            color = f"#{stop.color}"
            # Convert stop position (0-100000) to percentage (0-100%)
            position = f"{stop.pos * 100}%" 
            color_stops.append(f"{color} {position}")

        # Return the complete linear-gradient CSS property
        return f"background: linear-gradient({css_angle}deg, {', '.join(color_stops)});"

    def _get_transform_css(self, transform: Transform):
        # Initialize a list to hold CSS transform properties
        css_transforms = []
        # Apply rotation if present. PowerPoint rotation is in 60000ths of a degree.
        # CSS rotate() expects degrees.
        if transform.rot != 0:
            css_transforms.append(f"rotate({transform.rot / 60000:.2f}deg)")
        # Apply horizontal flip if present
        if transform.flipH:
            css_transforms.append("scaleX(-1)")
        # Apply vertical flip if present
        if transform.flipV:
            css_transforms.append("scaleY(-1)")
        # Join all transform properties into a single CSS string
        return "transform: " + " ".join(css_transforms) + ";" if css_transforms else ""

    def _get_image_crop_css(self, blip_fill: BlipFill):
        # Generate CSS for image cropping using clip-path property
        # Cropping values (src_rect_t, b, l, r) are in 1000ths of a percentage.
        # For example, 50000 means 50%.
        if blip_fill and (blip_fill.src_rect_t is not None or
                          blip_fill.src_rect_b is not None or
                          blip_fill.src_rect_l is not None or
                          blip_fill.src_rect_r is not None):
            # Convert 1000ths of a percentage to CSS percentage string
            top = f"{blip_fill.src_rect_t / 1000:.2f}%" if blip_fill.src_rect_t is not None else "0%"
            bottom = f"{blip_fill.src_rect_b / 1000:.2f}%" if blip_fill.src_rect_b is not None else "0%"
            left = f"{blip_fill.src_rect_l / 1000:.2f}%" if blip_fill.src_rect_l is not None else "0%"
            right = f"{blip_fill.src_rect_r / 1000:.2f}%" if blip_fill.src_rect_r is not None else "0%"
            # Return the clip-path CSS property
            return f"clip-path: inset({top} {right} {bottom} {left});"

    def _get_shape_style_css(self, element: Shape) -> str:
        # Generate CSS for shape fill and line properties
        shape_style = ""
        # Apply fill properties (solid color or gradient)
        if element.fill:
            if isinstance(element.fill, SolidFill):
                shape_style += f"background-color: #{element.fill.color};"
            elif isinstance(element.fill, GradientFill):
                shape_style += self._get_gradient_css(element.fill)
        # Apply line (border) properties
        if element.line:
            shape_style += f"border: {self._emu_to_px(element.line.width)}px solid #{element.line.color};"
        return shape_style

    def _get_paragraph_style_css(self, paragraph: Paragraph) -> str:
        # Generate CSS for paragraph properties like text alignment and indentation
        paragraph_style = ""
        # Apply text alignment if specified
        if paragraph.properties and paragraph.properties.align:
            paragraph_style += f"text-align: {paragraph.properties.align};"
        # Apply padding-left for indentation if specified
        if paragraph.properties and paragraph.properties.indent is not None:
            paragraph_style += f"padding-left: {self._emu_to_px(paragraph.properties.indent)}px;"
        return paragraph_style

    def _get_run_style_css(self, run: TextRun) -> str:
        # Generate CSS for text run properties like font size, weight, style, color, and font face
        run_style = ""
        if run.properties:
            # Apply font size if specified, converting EMUs to pixels
            if run.properties.font_size:
                run_style += f"font-size: {self._emu_to_px(run.properties.font_size)}px;"
            # Apply bold font weight
            if run.properties.bold:
                run_style += "font-weight: bold;"
            # Apply italic font style
            if run.properties.italic:
                run_style += "font-style: italic;"
            # Apply underline text decoration
            if run.properties.underline:
                run_style += "text-decoration: underline;"
            # Apply explicit color if specified
            if run.properties.color:
                run_style += f"color: #{run.properties.color};"
            # Apply scheme color if specified (using CSS variables for theming)
            elif run.properties.scheme_color:
                run_style += f"color: var(--{run.properties.scheme_color}-color, black);"
            # Apply font family if specified
            if run.properties.font_face:
                run_style += f"font-family: '{run.properties.font_face}';"
        return run_style

    def _get_flex_properties_from_name(self, name: str) -> str:
        # Generate Flexbox CSS properties based on a given name string.
        # This allows for dynamic application of Flexbox styles based on element names.
        flex_style = ""
        # Check for row direction
        if "flex-row" in name:
            flex_style += "flex-direction: row;"
        # Check for column direction
        if "flex-col" in name:
            flex_style += "flex-direction: column;"
        # Check for center justification
        if "justify-center" in name:
            flex_style += "justify-content: center;"
        # Check for space-between justification
        if "justify-between" in name:
            flex_style += "justify-content: space-between;"
        # Check for center alignment
        if "items-center" in name:
            flex_style += "align-items: center;"
        return flex_style

    def _render_graphic_frame_html(self, element: GraphicFrame, parent_x: int = 0, parent_y: int = 0) -> str:
        # Calculate the absolute position and size of the graphic frame in pixels
        x = self._emu_to_px(element.transform.x - parent_x)
        y = self._emu_to_px(element.transform.y - parent_y)
        cx = self._emu_to_px(element.transform.cx)
        cy = self._emu_to_px(element.transform.cy)
        # Return an HTML div element representing the graphic frame with absolute positioning
        return f"""
        <div class="graphic-frame" style="left: {x}px; top: {y}px; width: {cx}px; height: {cy}px;">
            <!-- Graphic Frame content (e.g., charts, tables) would go here -->
        </div>
"""

    def _render_group_shape_html(self, element: GroupShape, parent_x: int = 0, parent_y: int = 0) -> str:
        # Calculate the relative position and size of the group shape in pixels
        # These are relative to its parent container (if any), hence parent_x and parent_y are subtracted.
        relative_x = self._emu_to_px(element.transform.x - parent_x)
        relative_y = self._emu_to_px(element.transform.y - parent_y)
        cx = self._emu_to_px(element.transform.cx)
        cy = self._emu_to_px(element.transform.cy)

        group_style = ""
        # If the group shape is designated as a flex container, apply display: flex and other flex properties
        if element.is_flex_container:
            group_style += "display: flex; "
            group_style += self._get_flex_properties_from_name(element.name)

        children_html = ""
        # Render HTML for all child shapes, pictures, nested group shapes, and graphic frames
        # The children's positions are calculated relative to the current group shape's transform.
        for child in element.children[0]: # shapes
            children_html += self._render_shape_html(child, element.transform.x, element.transform.y)
        for child in element.children[1]: # pictures
            children_html += self._render_picture_html(child, element.transform.x, element.transform.y)
        for child in element.children[2]: # group_shapes
            children_html += self._render_group_shape_html(child, element.transform.x, element.transform.y)
        for child in element.children[3]: # graphic_frames
            children_html += self._render_graphic_frame_html(child, element.transform.x, element.transform.y)

        # Return an HTML div element representing the group shape with its styles and rendered children
        return f"""
        <div class="group-shape" style="left: {relative_x}px; top: {relative_y}px; width: {cx}px; height: {cy}px; {group_style}">
            {children_html}
        </div>
"""

    def _render_picture_html(self, element: Picture, parent_x: int = 0, parent_y: int = 0, parent_cx: int = 0, parent_cy: int = 0, use_absolute_pos: bool = True) -> str:
        # Calculate the position and size of the picture in pixels, relative to its parent
        x = self._emu_to_px(element.transform.x - parent_x)
        y = self._emu_to_px(element.transform.y - parent_y)
        cx = self._emu_to_px(element.transform.cx)
        cy = self._emu_to_px(element.transform.cy)
        # Construct the image source path, assuming media files are in a 'media' subdirectory
        image_src = os.path.join("media", os.path.basename(element.blip_fill.path))
        
        style_attributes = []
        # If absolute positioning is enabled, add left, top, width, and height styles
        if use_absolute_pos:
            style_attributes.append(f"left: {x}px;")
            style_attributes.append(f"top: {y}px;")
            style_attributes.append(f"width: {cx}px;")
            style_attributes.append(f"height: {cy}px;")

        # Add transform (rotation, flip) and image crop (clip-path) CSS properties
        style_attributes.append(self._get_transform_css(element.transform))
        style_attributes.append(self._get_image_crop_css(element.blip_fill))
        
        # Join all collected style attributes into a single string
        style_string = " ".join(filter(None, style_attributes))

        # Return an HTML img tag representing the picture with its styles
        return f"""
        <img class="image" src="{image_src}" style="{style_string}" />
"""

    def _render_shape_html(self, element: Shape, parent_x: int = 0, parent_y: int = 0, parent_cx: int = 0, parent_cy: int = 0, use_absolute_pos: bool = True) -> str:
        # Calculate the position and size of the shape in pixels, relative to its parent
        x = self._emu_to_px(element.transform.x - parent_x)
        y = self._emu_to_px(element.transform.y - parent_y)
        cx = self._emu_to_px(element.transform.cx)
        cy = self._emu_to_px(element.transform.cy)

        # Get the base CSS style for the shape (fill, line)
        shape_style = self._get_shape_style_css(element)
        
        style_attributes = []
        # If absolute positioning is enabled, add left, top, width, and height styles
        if use_absolute_pos:
            style_attributes.append(f"left: {x}px;")
            style_attributes.append(f"top: {y}px;")
            style_attributes.append(f"width: {cx}px;")
            style_attributes.append(f"height: {cy}px;")

        # Add shape-specific styles and transform (rotation, flip) CSS properties
        style_attributes.append(shape_style)
        style_attributes.append(self._get_transform_css(element.transform))

        # Join all collected style attributes into a single string
        style_string = " ".join(filter(None, style_attributes))

        text_content_html = ""
        # If the shape contains a text frame, render its paragraphs and text runs
        if element.text_frame:
            for paragraph in element.text_frame.paragraphs:
                paragraph_style = self._get_paragraph_style_css(paragraph)

                text_runs_html = ""
                for run in paragraph.text_runs:
                    run_style = self._get_run_style_css(run)

                    text_runs_html += f"<span style=\"{run_style}\">{run.text}</span>"
                text_content_html += f"<p style=\"{paragraph_style}\">{text_runs_html}</p>"

        # Return an HTML div element representing the shape with its styles and text content
        return f"""
        <div class="shape" id="shape-{element.id}" style="{style_string}">
            <div class="text-content">{text_content_html}</div>
        </div>
"""

    def _render_slide_content(self, slide: Slide) -> str:
        content_html = ""
        slide_elements_by_id = {el.id: el for el in slide.shapes + slide.pictures + slide.group_shapes + slide.graphic_frames if el.id is not None}
        used_element_ids = set()

        placeholder_elements = {}
        if slide.slide_layout:
            for layout_ph in slide.slide_layout.placeholders:
                for element_id, element in slide_elements_by_id.items():
                    if hasattr(element, 'ph_type') and element.ph_type == layout_ph.ph_type and (layout_ph.ph_idx is None or (hasattr(element, 'ph_idx') and element.ph_idx == layout_ph.ph_idx)):
                        placeholder_elements[layout_ph.ph_type] = element
                        break

        layout_type = slide.slide_layout.type if slide.slide_layout else None

        layout_handlers = {
            "picTx": self._render_picTx_layout,
            "tx": self._render_tx_layout,
            "obj": self._render_obj_layout,
            "titleOnly": self._render_titleOnly_layout,
            "blank": self._render_blank_layout,
            "title": self._render_title_layout,
            "titlePic": self._render_titlePic_layout,
        }

        handler = layout_handlers.get(layout_type, self._render_generic_layout)
        handler_html, handler_used_element_ids = handler(slide, placeholder_elements)
        content_html += handler_html
        used_element_ids.update(handler_used_element_ids)

        # Add any remaining elements that were not part of any specific layout
        all_slide_elements = slide.shapes + slide.pictures + slide.group_shapes + slide.graphic_frames
        for element in all_slide_elements:
            if element.id is not None and element.id not in used_element_ids:
                if isinstance(element, Shape):
                    content_html += self._render_shape_html(element, 0, 0)
                elif isinstance(element, Picture):
                    content_html += self._render_picture_html(element, 0, 0)
                elif isinstance(element, GroupShape):
                    content_html += self._render_group_shape_html(element, 0, 0)
                elif isinstance(element, GraphicFrame):
                    content_html += self._render_graphic_frame_html(element, 0, 0)

        return content_html

    def _render_picTx_layout(self, slide: Slide, placeholder_elements: dict) -> tuple[str, set]:
        content_html = ""
        used_element_ids = set()

        title_element = placeholder_elements.get("title")
        pic_element = placeholder_elements.get("pic")
        body_element = placeholder_elements.get("body")

        if title_element:
            content_html += f'''
    <div class="title-container">
        {self._render_shape_html(title_element, use_absolute_pos=False)}
    </div>
'''
            used_element_ids.add(title_element.id)

        if pic_element and body_element:
            content_html += f'''
    <div class="content-flex-container">
        {self._render_picture_html(pic_element, use_absolute_pos=False)}
        {self._render_shape_html(body_element, use_absolute_pos=False)}
    </div>
'''
            used_element_ids.add(pic_element.id)
            used_element_ids.add(body_element.id)

        return content_html, used_element_ids

    def _render_tx_layout(self, slide: Slide, placeholder_elements: dict) -> tuple[str, set]:
        content_html = ""
        used_element_ids = set()

        title_element = placeholder_elements.get("title")
        body_element = placeholder_elements.get("body")

        if title_element:
            content_html += f'''
    <div class="title-container">
        {self._render_shape_html(title_element, use_absolute_pos=False)}
    </div>
'''
            used_element_ids.add(title_element.id)

        if body_element:
            content_html += f'''
    <div class="content-flex-container">
        {self._render_shape_html(body_element, use_absolute_pos=False)}
    </div>
'''
            used_element_ids.add(body_element.id)

        return content_html, used_element_ids

    def _render_obj_layout(self, slide: Slide, placeholder_elements: dict) -> tuple[str, set]:
        return self._render_tx_layout(slide, placeholder_elements) # Same as tx

    def _render_titleOnly_layout(self, slide: Slide, placeholder_elements: dict) -> tuple[str, set]:
        content_html = ""
        used_element_ids = set()

        title_element = placeholder_elements.get("title") or placeholder_elements.get("ctrTitle")

        if title_element:
            content_html += f'''
    <div class="title-container">
        {self._render_shape_html(title_element, use_absolute_pos=False)}
    </div>
'''
            used_element_ids.add(title_element.id)

        return content_html, used_element_ids

    def _render_blank_layout(self, slide: Slide, placeholder_elements: dict) -> tuple[str, set]:
        return "", set()

    def _render_title_layout(self, slide: Slide, placeholder_elements: dict) -> tuple[str, set]:
        content_html = ""
        used_element_ids = set()

        title_element = placeholder_elements.get("ctrTitle")
        subtitle_element = placeholder_elements.get("subTitle")

        if title_element:
            content_html += f'''
    <div class="title-container">
        {self._render_shape_html(title_element, use_absolute_pos=False)}
    </div>
'''
            used_element_ids.add(title_element.id)

        if subtitle_element:
            content_html += f'''
    <div class="content-flex-container">
        {self._render_shape_html(subtitle_element, use_absolute_pos=False)}
    </div>
'''
            used_element_ids.add(subtitle_element.id)

        return content_html, used_element_ids

    def _render_titlePic_layout(self, slide: Slide, placeholder_elements: dict) -> tuple[str, set]:
        content_html = ""
        used_element_ids = set()

        title_element = placeholder_elements.get("title") or placeholder_elements.get("ctrTitle")
        pic_element = placeholder_elements.get("pic")
        body_element = placeholder_elements.get("body")

        if title_element:
            content_html += f'''
    <div class="title-container">
        {self._render_shape_html(title_element, use_absolute_pos=False)}
    </div>
'''
            used_element_ids.add(title_element.id)

        # Create a flex container for the picture and body elements
        content_html += f'''
    <div class="content-flex-container">
'''
        if pic_element:
            content_html += f'''
        {self._render_picture_html(pic_element, use_absolute_pos=False)}
'''
            used_element_ids.add(pic_element.id)

        if body_element:
            content_html += f'''
        {self._render_shape_html(body_element, use_absolute_pos=False)}
'''
            used_element_ids.add(body_element.id)

        content_html += f'''
    </div>
'''

        return content_html, used_element_ids

    def _render_generic_layout(self, slide: Slide, placeholder_elements: dict) -> tuple[str, set]:
        content_html = ""
        used_element_ids = set()

        all_slide_elements = slide.shapes + slide.pictures + slide.group_shapes + slide.graphic_frames

        for element in all_slide_elements:
            if element.id is not None and element.id not in used_element_ids:
                content_html += f'''
    <div class="generic-container" style="display: flex; justify-content: center; align-items: center;">
'''
                if isinstance(element, Shape):
                    content_html += self._render_shape_html(element, use_absolute_pos=False)
                elif isinstance(element, Picture):
                    content_html += self._render_picture_html(element, use_absolute_pos=False)
                elif isinstance(element, GroupShape):
                    content_html += self._render_group_shape_html(element, use_absolute_pos=False)
                elif isinstance(element, GraphicFrame):
                    content_html += self._render_graphic_frame_html(element, use_absolute_pos=False)
                content_html += f'''
    </div>
'''
                used_element_ids.add(element.id)

        return content_html, used_element_ids

    def write_slide_html(self, slide: Slide, slide_number: int):
        # Determine the layout class for the slide container based on the slide layout type
        layout_class = f" {slide.slide_layout.type}-layout" if slide.slide_layout and slide.slide_layout.type else ""
        # Construct the initial HTML structure including DOCTYPE, head, title, and basic styles
        html_content = f"""<!DOCTYPE html>
<html>
<head>
    <title>Slide {slide_number}</title>
    <style>
        body {{ margin: 0; padding: 0; font-family: sans-serif; overflow: hidden; }}
        .slide-container {{ position: relative; width: {self._emu_to_px(slide.common_slide_data.cx)}px; height: {self._emu_to_px(slide.common_slide_data.cy)}px; background-color: #fff; display: flex; flex-direction: column; }}
        .shape, .image, .graphic-frame, .group-shape, .placeholder-container {{ box-sizing: border-box; }}
        .text-content {{ white-wrap: pre-wrap; word-wrap: break-word; }}

        /* Layout-specific CSS */
        .slide-container.picTx-layout .content-flex-container {{ display: flex; flex-direction: row; justify-content: space-around; align-items: center; flex: 1; }}
        .slide-container.tx-layout .content-flex-container {{ display: flex; flex-direction: column; justify-content: center; align-items: center; flex: 1; }}
        .slide-container.titlePic-layout .content-flex-container {{ display: flex; flex-direction: row; justify-content: space-around; align-items: center; flex: 1; }}
        .title-container {{ display: flex; justify-content: center; align-items: center; flex: 0 0 auto; }}
        .content-flex-container {{ display: flex; flex: 1; }}
    </style>
</head>
<body>
    <div class="slide-container{layout_class}">
"""

        # Render the actual content of the slide (shapes, pictures, etc.) and append to the HTML
        html_content += self._render_slide_content(slide)

        # Close the HTML structure
        html_content += """
    </div>
</body>
</html>"""

        # Construct the output directory for the current slide
        slide_output_directory = os.path.join(self.output_directory, f"slide{slide_number}")
        # Create the slide-specific output directory if it doesn't exist
        os.makedirs(slide_output_directory, exist_ok=True)

        # Define the full path for the output HTML file
        output_file_path = os.path.join(slide_output_directory, f"slide{slide_number}.html")
        # Write the generated HTML content to the file
        with open(output_file_path, "w", encoding="utf-8") as f:
            f.write(html_content)
        return output_file_path
