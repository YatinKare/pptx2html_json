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
    get_gradient_css,
)
from learnx_parser.writers.theme_resolver import ThemeResolver


class HtmlWriter:
    """Main HTML writer class that coordinates slide rendering to HTML."""

    def __init__(
        self,
        output_directory="./output",
        pptx_unpacked_path=None,
    ):
        """Initialize the HTML writer.

        Args:
            output_directory: Directory where HTML files will be saved
            pptx_unpacked_path: Path to unpacked PPTX for resolving media files
        """
        self.output_directory = output_directory
        self.pptx_unpacked_path = pptx_unpacked_path
        self.positioning_config = PositioningConfig(PositioningConfig.ABSOLUTE)

        # Initialize theme resolver for background and color resolution
        self.theme_resolver = None
        if pptx_unpacked_path:
            try:
                self.theme_resolver = ThemeResolver(pptx_unpacked_path)
                # Load slide master color map
                slide_master_path = os.path.join(
                    pptx_unpacked_path, "ppt", "slideMasters"
                )
                if os.path.exists(slide_master_path):
                    for master_file in os.listdir(slide_master_path):
                        if master_file.endswith(".xml"):
                            master_full_path = os.path.join(
                                slide_master_path, master_file
                            )
                            self.theme_resolver.load_slide_master_color_map(
                                master_full_path
                            )
                            break  # Use first slide master found
            except Exception as e:
                print(f"Warning: Could not initialize theme resolver: {e}")
                self.theme_resolver = None

    def write_slide_html(self, slide: Slide, slide_number: int):
        """Write a slide to an HTML file using absolute positioning.

        Args:
            slide: Slide object containing the slide data
            slide_number: The slide number for file naming
        """
        return self._write_slide_absolute(slide, slide_number)

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
            margin-left: -{slide_width // 2}px;
            margin-top: -{slide_height // 2}px;
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
            head[title[f"Slide {slide_number}"], style[Markup(css_content)]],
            body[div(id="player")[div(id="resizer")[Markup(slide_content)]]],
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
                slide_bg_color = self._get_slide_background_color(slide)
                shape_html = render_shape_html(
                    shape,
                    theme_resolver=self.theme_resolver,
                    slide_background_color=slide_bg_color,
                )
                html_parts.append(shape_html)
            except Exception as e:
                # Fallback rendering if element renderer fails
                print(
                    f"Warning: Failed to render shape {getattr(shape, 'id', 'unknown')}: {e}"
                )
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
                picture_html = render_picture_html(picture)
                html_parts.append(picture_html)
            except Exception as e:
                # Fallback rendering if element renderer fails
                print(
                    f"Warning: Failed to render picture {getattr(picture, 'id', 'unknown')}: {e}"
                )
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
                group_html = render_group_shape_html(group_shape)
                html_parts.append(group_html)
            except Exception as e:
                # Fallback rendering if element renderer fails
                print(
                    f"Warning: Failed to render group shape {getattr(group_shape, 'id', 'unknown')}: {e}"
                )
                if group_shape.transform:
                    from learnx_parser.writers.css_utils import CoordinateConverter

                    position = CoordinateConverter.extract_position(
                        group_shape.transform
                    )
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
                print(
                    f"Warning: Failed to render graphic frame {getattr(graphic_frame, 'id', 'unknown')}: {e}"
                )
                if graphic_frame.transform:
                    from learnx_parser.writers.css_utils import CoordinateConverter

                    position = CoordinateConverter.extract_position(
                        graphic_frame.transform
                    )
                    if position:
                        css = CoordinateConverter.generate_absolute_css(position, 100)
                        fallback_html = f'<div class="frame-fallback" style="{css} background: lightyellow; border: 1px solid #444;">Frame (fallback)</div>'
                        html_parts.append(fallback_html)

        # If no elements, show placeholder
        if not html_parts:
            html_parts.append(
                '<div class="element-absolute" style="left: 100px; top: 100px; width: 200px; height: 50px; background: lightgray; z-index: 1; border: 1px dashed #ccc;">No elements found</div>'
            )

        return "".join(html_parts)

    def _get_background_css(self, slide: Slide) -> str:
        """Generate CSS for slide background with Goal 1 integration.
        
        This method implements the background image priority system for Goal 1:
        Background as a Single Image. It prioritizes generated background images
        over legacy CSS-based background generation to ensure perfect visual fidelity.
        
        Priority order:
        1. Generated background images (Goal 1) - highest priority
        2. Theme-resolved background CSS - medium priority
        3. Direct background properties (fallback) - lowest priority
        
        For Goal 1 implementation, when a slide has a generated_background_path,
        this method generates CSS with background-image, background-size: cover,
        background-position: center, and background-repeat: no-repeat to ensure
        the PNG background image displays correctly at all screen sizes.

        Args:
            slide (Slide): Slide object containing background properties and 
                potentially a generated_background_path from Goal 1 processing

        Returns:
            str: CSS background properties string. For generated images, returns
                complete background-image CSS. For legacy slides, returns 
                background-color or gradient CSS. Empty string if no background.
                
        Example generated CSS:
            "background-image: url('media/background_1.png'); background-size: cover; 
             background-position: center; background-repeat: no-repeat;"
        """
        # Check for generated background image first (Goal 1: Background as Single Image)
        if slide.generated_background_path:
            return f"background-image: url('{slide.generated_background_path}'); background-size: cover; background-position: center; background-repeat: no-repeat;"
        
        # Fallback to old background generation for slides without generated images
        background_css_parts = []

        # Try to resolve background from slide hierarchy (slide -> layout -> master)
        resolved_background = self._resolve_slide_background(slide)
        if resolved_background:
            background_css_parts.append(resolved_background)

        # Fallback to existing slide background data
        if not background_css_parts:
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

    def _resolve_slide_background(self, slide: Slide) -> str:
        """Resolve slide background from theme system.

        Args:
            slide: Slide object

        Returns:
            str: CSS background property or empty string
        """
        if not self.theme_resolver:
            return ""

        # Look for slide-level background first
        slide_bg = self._parse_slide_background_xml(slide)
        if slide_bg:
            return slide_bg

        # Fallback to layout-level background
        layout_bg = self._parse_layout_background_xml(slide)
        if layout_bg:
            return layout_bg

        # Fallback to master-level background
        master_bg = self._parse_master_background_xml()
        if master_bg:
            return master_bg

        return ""

    def _parse_slide_background_xml(self, slide: Slide) -> str:
        """Parse slide-level background from slide XML.

        Args:
            slide: Slide object

        Returns:
            str: CSS background property or empty string
        """
        if not self.pptx_unpacked_path:
            return ""

        slide_xml_path = None
        try:
            # Look for slide XML file - need to map slide number to actual slide file
            slide_xml_path = self._find_slide_xml_path(slide.slide_number)
            if not slide_xml_path or not os.path.exists(slide_xml_path):
                return ""

            import xml.etree.ElementTree as ET

            tree = ET.parse(slide_xml_path)
            root = tree.getroot()

            # Define namespaces
            ns = {
                "p": "http://schemas.openxmlformats.org/presentationml/2006/main",
                "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
                "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
            }

            # Look for background element in slide
            bg_elem = root.find(".//p:bg", ns)
            if bg_elem is not None:
                return self._process_background_element(bg_elem, slide_xml_path, ns)

            # Look for background images in slide content (pictures with specific positioning)
            pics = root.findall(".//p:pic", ns)
            for pic in pics:
                # Check if this picture might be a background image
                if self._is_background_image(pic, ns):
                    return self._process_background_image(pic, slide_xml_path, ns)

        except Exception as e:
            if slide_xml_path:
                print(
                    f"Warning: Error parsing slide background from {slide_xml_path}: {e}"
                )
            else:
                print(
                    f"Warning: Error parsing slide background for slide {slide.slide_number}: {e}"
                )

        return ""

    def _find_slide_xml_path(self, slide_number):
        """Find the XML file path for a given slide number.

        Args:
            slide_number: Slide number (1-based)

        Returns:
            str: Path to slide XML file or None
        """
        if not self.pptx_unpacked_path:
            return None

        try:
            # Parse presentation.xml to get slide order
            presentation_path = os.path.join(
                self.pptx_unpacked_path, "ppt", "presentation.xml"
            )
            if not os.path.exists(presentation_path):
                return None

            import xml.etree.ElementTree as ET

            tree = ET.parse(presentation_path)
            root = tree.getroot()

            # Find slide ID list
            sld_id_lst = root.find(
                ".//p:sldIdLst",
                {"p": "http://schemas.openxmlformats.org/presentationml/2006/main"},
            )
            if sld_id_lst is None:
                return None

            # Get slide IDs in order
            slide_ids = []
            for sld_id in sld_id_lst.findall(
                "p:sldId",
                {"p": "http://schemas.openxmlformats.org/presentationml/2006/main"},
            ):
                r_id = sld_id.get(
                    "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id"
                )
                if r_id:
                    slide_ids.append(r_id)

            # Check if slide number is valid
            if not (1 <= slide_number <= len(slide_ids)):
                return None

            # Get the relationship ID for this slide
            target_r_id = slide_ids[slide_number - 1]

            # Parse presentation relationships to get slide file
            rels_path = os.path.join(
                self.pptx_unpacked_path, "ppt", "_rels", "presentation.xml.rels"
            )
            if not os.path.exists(rels_path):
                return None

            tree = ET.parse(rels_path)
            root = tree.getroot()

            # Find the target slide file
            for rel in root.findall(
                ".//{http://schemas.openxmlformats.org/package/2006/relationships}Relationship"
            ):
                if rel.get("Id") == target_r_id and rel.get("Type", "").endswith(
                    "/slide"
                ):
                    target = rel.get("Target")
                    if target:
                        # Convert relative path to absolute path
                        if target.startswith("/"):
                            return os.path.join(self.pptx_unpacked_path, target[1:])
                        else:
                            return os.path.join(self.pptx_unpacked_path, "ppt", target)

        except Exception as e:
            print(
                f"Warning: Error finding slide XML path for slide {slide_number}: {e}"
            )

        return None

    def _process_background_element(self, bg_elem, slide_xml_path, ns):
        """Process background element from slide XML.

        Args:
            bg_elem: Background XML element
            slide_xml_path: Path to slide XML file
            ns: XML namespaces

        Returns:
            str: CSS background property or empty string
        """
        # Look for background reference
        bg_ref = bg_elem.find(".//p:bgRef", ns)
        if bg_ref is not None:
            idx = int(bg_ref.get("idx", "0"))

            # Look for scheme color
            scheme_clr = bg_ref.find(".//a:schemeClr", ns)
            scheme_color = None
            if scheme_clr is not None:
                scheme_color = scheme_clr.get("val")

            # Resolve background through theme resolver
            if self.theme_resolver:
                background_css = self.theme_resolver.get_background_css(
                    idx, scheme_color
                )
                return background_css

        return ""

    def _is_background_image(self, pic_elem, ns):
        """Check if a picture element is likely a background image.

        Args:
            pic_elem: Picture XML element
            ns: XML namespaces

        Returns:
            bool: True if likely a background image
        """
        # For now, return False - picture elements in slides are typically content, not backgrounds
        # True background images would be defined in slide layouts or masters using <p:bg> elements
        # Content images (even when they span the slide) should be handled as regular images
        return False

    def _process_background_image(self, pic_elem, slide_xml_path, ns):
        """Process background image from slide XML.

        Args:
            pic_elem: Picture XML element
            slide_xml_path: Path to slide XML file
            ns: XML namespaces

        Returns:
            str: CSS background property or empty string
        """
        try:
            # Look for blip reference
            blip_elem = pic_elem.find(".//a:blip", ns)
            if blip_elem is not None:
                r_embed = blip_elem.get(
                    "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed"
                )
                if r_embed:
                    # Resolve the relationship to get the image path
                    image_path = self._resolve_image_relationship(
                        r_embed, slide_xml_path
                    )
                    if image_path:
                        # Copy image to output directory and return CSS
                        return self._generate_background_image_css(image_path)

        except Exception as e:
            print(f"Warning: Error processing background image: {e}")

        return ""

    def _resolve_image_relationship(self, r_embed, slide_xml_path):
        """Resolve image relationship to get the actual image path.

        Args:
            r_embed: Relationship ID
            slide_xml_path: Path to slide XML file

        Returns:
            str: Path to image file or None
        """
        try:
            # Get the relationships file for this slide
            slide_dir = os.path.dirname(slide_xml_path)
            slide_name = os.path.basename(slide_xml_path)
            rels_path = os.path.join(slide_dir, "_rels", f"{slide_name}.rels")

            if not os.path.exists(rels_path):
                return None

            import xml.etree.ElementTree as ET

            tree = ET.parse(rels_path)
            root = tree.getroot()

            # Find the relationship
            for rel in root.findall(
                ".//{http://schemas.openxmlformats.org/package/2006/relationships}Relationship"
            ):
                if rel.get("Id") == r_embed:
                    target = rel.get("Target")
                    if target:
                        # Convert relative path to absolute path
                        if target.startswith("/"):
                            return os.path.join(self.pptx_unpacked_path, target[1:])
                        else:
                            return os.path.join(self.pptx_unpacked_path, "ppt", target)

        except Exception as e:
            print(f"Warning: Error resolving image relationship {r_embed}: {e}")

        return None

    def _generate_background_image_css(self, image_path):
        """Generate CSS for background image.

        Args:
            image_path: Path to the image file

        Returns:
            str: CSS background property
        """
        try:
            if not os.path.exists(image_path):
                return ""

            # Copy image to output directory
            image_filename = os.path.basename(image_path)
            output_image_path = os.path.join(
                self.output_directory, "media", image_filename
            )

            # Create media directory if it doesn't exist
            media_dir = os.path.dirname(output_image_path)
            os.makedirs(media_dir, exist_ok=True)

            # Copy the image file
            import shutil

            shutil.copy2(image_path, output_image_path)

            # Generate CSS with relative path
            relative_image_path = f"../media/{image_filename}"
            return f"background-image: url('{relative_image_path}'); background-size: cover; background-position: center; background-repeat: no-repeat;"

        except Exception as e:
            print(f"Warning: Error generating background image CSS: {e}")

        return ""

    def _parse_layout_background_xml(self, slide: Slide) -> str:
        """Parse layout-level background from slide layout XML.

        Args:
            slide: Slide object

        Returns:
            str: CSS background property or empty string
        """
        if not self.pptx_unpacked_path:
            return ""

        slide_xml_path = None
        try:
            # Find the slide XML path first
            slide_xml_path = self._find_slide_xml_path(slide.slide_number)
            if not slide_xml_path or not os.path.exists(slide_xml_path):
                return ""

            # Get the slide layout relationship
            slide_dir = os.path.dirname(slide_xml_path)
            slide_name = os.path.basename(slide_xml_path)
            rels_path = os.path.join(slide_dir, "_rels", f"{slide_name}.rels")

            if not os.path.exists(rels_path):
                return ""

            import xml.etree.ElementTree as ET

            # Parse slide relationships to find layout
            tree = ET.parse(rels_path)
            root = tree.getroot()

            layout_path = None
            for rel in root.findall(
                ".//{http://schemas.openxmlformats.org/package/2006/relationships}Relationship"
            ):
                if rel.get("Type", "").endswith("/slideLayout"):
                    target = rel.get("Target")
                    if target:
                        # Convert relative path to absolute path
                        if target.startswith("/"):
                            layout_path = os.path.join(
                                self.pptx_unpacked_path, target[1:]
                            )
                        else:
                            layout_path = os.path.join(
                                self.pptx_unpacked_path, "ppt", target
                            )
                        break

            if not layout_path or not os.path.exists(layout_path):
                return ""

            # Parse layout XML for background
            tree = ET.parse(layout_path)
            root = tree.getroot()

            # Define namespaces
            ns = {
                "p": "http://schemas.openxmlformats.org/presentationml/2006/main",
                "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
            }

            # Look for background element
            bg_elem = root.find(".//p:bg", ns)
            if bg_elem is not None:
                return self._process_layout_background(bg_elem, ns)

        except Exception as e:
            if slide_xml_path:
                print(
                    f"Warning: Error parsing layout background for slide {slide.slide_number}: {e}"
                )
            else:
                print(
                    f"Warning: Error parsing layout background for slide {slide.slide_number}: {e}"
                )

        return ""

    def _process_layout_background(self, bg_elem, ns):
        """Process layout background element.

        Args:
            bg_elem: Background XML element
            ns: XML namespaces

        Returns:
            str: CSS background property or empty string
        """
        try:
            # Look for background properties
            bg_pr = bg_elem.find(".//p:bgPr", ns)
            if bg_pr is None:
                return ""

            # Check for gradient fill
            grad_fill = bg_pr.find(".//a:gradFill", ns)
            if grad_fill is not None:
                return self._process_gradient_background(grad_fill, ns)

            # Check for solid fill
            solid_fill = bg_pr.find(".//a:solidFill", ns)
            if solid_fill is not None:
                return self._process_solid_background(solid_fill, ns)

        except Exception as e:
            print(f"Warning: Error processing layout background: {e}")

        return ""

    def _process_gradient_background(self, grad_fill, ns):
        """Process gradient background fill.

        Args:
            grad_fill: Gradient fill XML element
            ns: XML namespaces

        Returns:
            str: CSS background gradient property
        """
        try:
            # Get gradient stops
            gs_list = grad_fill.find(".//a:gsLst", ns)
            if gs_list is None:
                return ""

            stops = []
            for gs in gs_list.findall("a:gs", ns):
                pos = int(gs.get("pos", "0")) / 1000  # Convert to percentage

                # Get color
                scheme_clr = gs.find(".//a:schemeClr", ns)
                if scheme_clr is not None:
                    color_name = scheme_clr.get("val")
                    if self.theme_resolver:
                        color_hex = self.theme_resolver.resolve_scheme_color(color_name)
                        stops.append((pos, f"#{color_hex}"))
                    else:
                        # Fallback colors for accent2 and accent4
                        if color_name == "accent2":
                            stops.append((pos, "#243FFF"))
                        elif color_name == "accent4":
                            stops.append((pos, "#FF9022"))
                        else:
                            stops.append((pos, "#FFFFFF"))

            # Sort stops by position and format for CSS
            stops.sort(key=lambda x: x[0])
            formatted_stops = [f"{color} {pos}%" for pos, color in stops]

            if len(stops) < 2:
                return ""

            # Get gradient angle
            lin_elem = grad_fill.find(".//a:lin", ns)
            angle = 0
            if lin_elem is not None:
                # PowerPoint angle is in 60,000ths of a degree
                ppt_angle = int(lin_elem.get("ang", "0"))
                # Convert to CSS degrees (0 is to right, 90 is down)
                angle = (ppt_angle / 60000) % 360
                # Convert PowerPoint angle to CSS angle and negate for vertical flip
                css_angle = (90 + angle) % 360

            # Generate CSS gradient
            gradient_str = ", ".join(formatted_stops)
            return f"background: linear-gradient({css_angle}deg, {gradient_str});"

        except Exception as e:
            print(f"Warning: Error processing gradient background: {e}")

        return ""

    def _process_solid_background(self, solid_fill, ns):
        """Process solid background fill.

        Args:
            solid_fill: Solid fill XML element
            ns: XML namespaces

        Returns:
            str: CSS background color property
        """
        try:
            scheme_clr = solid_fill.find(".//a:schemeClr", ns)
            if scheme_clr is not None:
                color_name = scheme_clr.get("val")
                if self.theme_resolver:
                    color_hex = self.theme_resolver.resolve_scheme_color(color_name)
                    return f"background-color: #{color_hex};"

        except Exception as e:
            print(f"Warning: Error processing solid background: {e}")

        return ""

    def _parse_master_background_xml(self) -> str:
        """Parse master-level background from slide master XML.

        Returns:
            str: CSS background property or empty string
        """
        if not self.theme_resolver or not self.pptx_unpacked_path:
            return ""

        try:
            # Parse slide master XML for background reference
            slide_master_path = os.path.join(
                self.pptx_unpacked_path, "ppt", "slideMasters"
            )
            if not os.path.exists(slide_master_path):
                return ""

            for master_file in os.listdir(slide_master_path):
                if master_file.endswith(".xml"):
                    master_full_path = os.path.join(slide_master_path, master_file)
                    return self._extract_master_background(master_full_path)

        except Exception as e:
            print(f"Warning: Error parsing master background: {e}")

        return ""

    def _extract_master_background(self, master_path: str) -> str:
        """Extract background from slide master XML.

        Args:
            master_path: Path to slide master XML file

        Returns:
            str: CSS background property or empty string
        """
        try:
            import xml.etree.ElementTree as ET

            tree = ET.parse(master_path)
            root = tree.getroot()

            # Define namespaces
            ns = {
                "p": "http://schemas.openxmlformats.org/presentationml/2006/main",
                "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
            }

            # Look for background element
            bg_elem = root.find(".//p:bg", ns)
            if bg_elem is not None:
                # Look for background reference
                bg_ref = bg_elem.find(".//p:bgRef", ns)
                if bg_ref is not None:
                    idx = int(bg_ref.get("idx", "0"))

                    # Look for scheme color
                    scheme_clr = bg_ref.find(".//a:schemeClr", ns)
                    scheme_color = None
                    if scheme_clr is not None:
                        scheme_color = scheme_clr.get("val")

                    # Resolve background through theme resolver
                    background_css = self.theme_resolver.get_background_css(
                        idx, scheme_color
                    )
                    return background_css

        except Exception as e:
            print(
                f"Warning: Error extracting master background from {master_path}: {e}"
            )

        return ""

    def _get_slide_background_color(self, slide: Slide) -> str | None:
        """Extract the dominant background color from slide for contrast calculations.
        
        This function has been updated for Goal 1 compatibility. Instead of parsing CSS
        (which now contains background-image URLs), it directly accesses the slide's
        background data and resolves theme colors properly.

        Args:
            slide: Slide object

        Returns:
            Optional[str]: Hex color string without # prefix, or None if not determinable
        """
        # Try to extract from solid background colors first
        if slide.common_slide_data.background_color:
            return slide.common_slide_data.background_color

        # Check for gradient - analyze gradient for overall darkness
        if (
            slide.common_slide_data.background_gradient_fill
            and slide.common_slide_data.background_gradient_fill.stops
        ):
            gradient = slide.common_slide_data.background_gradient_fill
            # For gradient backgrounds, determine the overall darkness by examining all stops
            total_luminance = 0
            valid_stops = 0
            
            for stop in gradient.stops:
                stop_color = None
                if stop.color:
                    stop_color = stop.color
                elif stop.scheme_color and self.theme_resolver:
                    resolved = self.theme_resolver.resolve_scheme_color(stop.scheme_color)
                    if resolved:
                        stop_color = resolved
                
                if stop_color:
                    # Calculate luminance for this stop
                    try:
                        r = int(stop_color[0:2], 16)
                        g = int(stop_color[2:4], 16)
                        b = int(stop_color[4:6], 16)
                        luminance = (0.2126 * r + 0.7152 * g + 0.0722 * b) / 255
                        total_luminance += luminance
                        valid_stops += 1
                    except (ValueError, IndexError):
                        continue
            
            if valid_stops > 0:
                avg_luminance = total_luminance / valid_stops
                # Return a representative color based on average luminance
                # If average luminance is dark (< 0.5), assume dark background needing white text
                if avg_luminance < 0.5:
                    return "000000"  # Dark background - will trigger white text
                else:
                    return "FFFFFF"  # Light background - will trigger black text
            
            # Fallback to first stop if analysis fails
            first_stop = gradient.stops[0]
            if first_stop.color:
                return first_stop.color
            if first_stop.scheme_color and self.theme_resolver:
                resolved_color = self.theme_resolver.resolve_scheme_color(first_stop.scheme_color)
                if resolved_color:
                    return resolved_color

        # Handle background references (theme-based backgrounds)
        if slide.common_slide_data.background_reference:
            bg_ref = slide.common_slide_data.background_reference
            if bg_ref.scheme_color and self.theme_resolver:
                resolved_color = self.theme_resolver.resolve_scheme_color(bg_ref.scheme_color)
                if resolved_color:
                    return resolved_color
            
            # Galaxy theme defaults for common scheme colors
            galaxy_defaults = {
                "bg1": "000000",  # Black background
                "bg2": "FFFFFF",  # White background  
                "accent2": "243FFF",  # Blue accent
                "accent4": "FF9022",  # Orange accent
            }
            
            if bg_ref.scheme_color in galaxy_defaults:
                return galaxy_defaults[bg_ref.scheme_color]

        # Default for slides without explicit background - assume white background
        return "FFFFFF"
