import json
import os
from dataclasses import asdict

from learnx_parser.models.core import (
    JsonElement,
    JsonPresentation,
    JsonPresentationWrapper,
    JsonSlide,
    Slide,
)


class JsonWriter:
    def __init__(self, output_directory="./output"):
        self.output_directory = output_directory

    def write_presentation_json(self, presentation_data: JsonPresentation):
        output_file_path = os.path.join(self.output_directory, "presentation.json")
        os.makedirs(self.output_directory, exist_ok=True)

        # Wrap presentation in v2 schema format
        wrapped_presentation = JsonPresentationWrapper(presentation=presentation_data)

        # Convert dataclass to dictionary and remove None values recursively
        def remove_none(obj):
            if isinstance(obj, dict):
                return {k: remove_none(v) for k, v in obj.items() if v is not None}
            elif isinstance(obj, list):
                return [remove_none(elem) for elem in obj if elem is not None]
            else:
                return obj

        cleaned_data = remove_none(asdict(wrapped_presentation))

        with open(output_file_path, "w", encoding="utf-8") as f:
            json.dump(cleaned_data, f, indent=2)

        return output_file_path

    def transform_to_json_presentation(
        self, slides: list[Slide], presentation_id: str, presentation_title: str
    ) -> JsonPresentation:
        json_slides = []
        for slide in slides:
            json_slides.append(self._transform_slide_to_json_slide(slide))

        return JsonPresentation(
            id=presentation_id, title=presentation_title, slides=json_slides
        )

    def _transform_slide_to_json_slide(self, slide: Slide) -> JsonSlide:
        elements = []
        for shape in slide.shapes:
            if shape.ph_type == "ctrTitle" or shape.ph_type == "title":
                text_content = self._get_text_from_shape(shape)
                if text_content:
                    elements.append(JsonElement(type="title", text=text_content))
            elif shape.text_frame:
                current_bullet_items = []
                current_text_box_content = []

                for paragraph in shape.text_frame.paragraphs:
                    # Skip paragraphs with no text runs
                    if not paragraph.text_runs:
                        continue

                    paragraph_text = "".join([run.text for run in paragraph.text_runs])

                    paragraph_style = {}
                    first_run_properties = paragraph.text_runs[0].properties
                    if first_run_properties:  # Check if properties exist
                        if first_run_properties.bold:
                            paragraph_style["bold"] = True
                        if first_run_properties.italic:
                            paragraph_style["italic"] = True
                        if first_run_properties.font_size:
                            paragraph_style["fontSize"] = first_run_properties.font_size
                        if first_run_properties.underline:
                            paragraph_style["underline"] = True

                    # Enhanced bullet detection logic
                    is_bullet = self._is_bullet_paragraph(
                        paragraph, shape.text_frame.paragraphs
                    )

                    if is_bullet:
                        # If we were accumulating text box content, finalize it first
                        if current_text_box_content:
                            text_style = self._get_text_style(
                                current_text_box_content, shape.text_frame.paragraphs
                            )
                            text_element = JsonElement(
                                type="text-box",
                                text="\n".join(current_text_box_content),
                            )
                            if text_style:
                                text_element.style = text_style
                            elements.append(text_element)
                            current_text_box_content = []

                        item_data = {"text": paragraph_text}
                        if paragraph_style:
                            item_data["style"] = {
                                k: v
                                for k, v in paragraph_style.items()
                                if v is not None
                            }
                        current_bullet_items.append(item_data)
                    else:
                        # If we were accumulating bullet items, finalize them first
                        if current_bullet_items:
                            elements.append(
                                JsonElement(
                                    type="bullet-list", items=current_bullet_items
                                )
                            )
                            current_bullet_items = []

                        # Accumulate text box content
                        current_text_box_content.append(paragraph_text)

                # After iterating through all paragraphs, finalize any remaining content
                if current_bullet_items:
                    elements.append(
                        JsonElement(type="bullet-list", items=current_bullet_items)
                    )
                elif current_text_box_content:
                    text_style = self._get_text_style(
                        current_text_box_content, shape.text_frame.paragraphs
                    )
                    text_element = JsonElement(
                        type="text-box", text="\n".join(current_text_box_content)
                    )
                    if text_style:
                        text_element.style = text_style
                    elements.append(text_element)

        for picture in slide.pictures:
            if picture.path:
                elements.append(JsonElement(type="image", src=picture.path))

        # Filter out elements with no meaningful content (e.g., empty text boxes)
        elements = [
            el for el in elements if el.text or el.src or el.items or el.description
        ]

        # Map PowerPoint layout to semantic layout names
        layout = self._map_layout_to_semantic_name(slide, elements)

        return JsonSlide(
            id=f"slide-{slide.slide_number}", layout=layout, elements=elements
        )

    def _get_text_from_shape(self, shape) -> str:
        if not shape.text_frame:
            return ""
        return "\n".join(
            [
                "".join([run.text for run in p.text_runs])
                for p in shape.text_frame.paragraphs
            ]
        )

    def _is_bullet_paragraph(self, paragraph, all_paragraphs) -> bool:
        """Enhanced bullet detection logic"""
        # Check explicit bullet properties
        if (
            paragraph.properties.bullet_type is not None
            and paragraph.properties.bullet_type != "none"
        ):
            return True

        # Check if paragraph has level > 0
        if paragraph.properties.level is not None and paragraph.properties.level > 0:
            return True

        # Enhanced heuristic: detect list-like patterns
        paragraph_text = "".join([run.text for run in paragraph.text_runs]).strip()

        # Skip empty paragraphs
        if not paragraph_text:
            return False

        # If this is in a multi-paragraph shape with similar content, check for list patterns
        if len(all_paragraphs) > 1:
            # Get all non-empty paragraph texts
            all_texts = [
                "".join([run.text for run in p.text_runs]).strip()
                for p in all_paragraphs
                if "".join([run.text for run in p.text_runs]).strip()
            ]

            # If all paragraphs are short and similar in structure, treat as bullets
            if len(all_texts) > 1:
                # Check if texts are list-like (short, similar length)
                avg_length = sum(len(text) for text in all_texts) / len(all_texts)
                if avg_length < 50:  # Short items are likely bullets
                    # Check if they start with similar patterns (Topic, etc.)
                    starts_with_topic = any(
                        text.startswith("Topic") for text in all_texts
                    )
                    if starts_with_topic and len(all_texts) >= 3:
                        return True

        return False

    def _get_text_style(self, text_content_list, all_paragraphs) -> dict | None:
        """Extract text style from paragraphs"""
        if not all_paragraphs:
            return None

        # Get style from first paragraph with text runs
        for paragraph in all_paragraphs:
            if paragraph.text_runs:
                first_run_properties = paragraph.text_runs[0].properties
                # !!! IMPORTANT: Check if the properties object exists before using it.
                if first_run_properties:
                    style = {}
                    if first_run_properties.bold:
                        style["bold"] = True
                    if first_run_properties.italic:
                        style["italic"] = True
                    if first_run_properties.font_size:
                        style["fontSize"] = first_run_properties.font_size
                    if first_run_properties.underline:
                        style["underline"] = True

                    # Only return a style dictionary if it's not empty
                    return style if style else None

        return None

    def _map_layout_to_semantic_name(self, slide, elements) -> str:
        """Map PowerPoint layout names to JSON Schema v2 compliant layout names"""
        if not slide.slide_layout:
            return "blank"

        ppt_layout = slide.slide_layout.type

        # Count element types
        title_count = sum(1 for el in elements if el.type == "title")
        text_box_count = sum(1 for el in elements if el.type == "text-box")
        bullet_list_count = sum(1 for el in elements if el.type == "bullet-list")
        image_count = sum(1 for el in elements if el.type == "image")

        # Detect if this is a title slide (first slide with title + subtitle pattern)
        if (
            slide.slide_number == 1
            and title_count >= 1
            and (text_box_count > 0 or len(elements) <= 2)
        ):
            return "title-slide"

        # Map based on PowerPoint layout and content (v2 compliant names only)
        if ppt_layout == "titleOnly":
            if title_count == 1 and len(elements) == 1:
                return "title-only"
            elif title_count == 1 and (bullet_list_count > 0 or text_box_count > 0):
                return "title-and-content"
            else:
                return "title-only"

        elif ppt_layout == "picTx":
            if image_count > 0 and (bullet_list_count > 0 or text_box_count > 0):
                return "two-content"  # Side-by-side content
            else:
                return "title-and-content"

        elif ppt_layout == "titlePic":
            if image_count > 0 and title_count > 0:
                if text_box_count > 0 or bullet_list_count > 0:
                    return "title-and-content"
                else:
                    return "content-with-caption"  # Image with title as caption
            else:
                return "title-and-content"

        elif ppt_layout == "title":
            if bullet_list_count > 0 or text_box_count > 0:
                return "title-and-content"
            else:
                return "title-only"

        elif ppt_layout == "obj":
            return "title-only"

        elif ppt_layout == "blank":
            return "blank"

        # Default mapping for unknown layouts (v2 compliant)
        if title_count == 1 and len(elements) == 1:
            return "title-only"
        elif title_count >= 1 and (bullet_list_count > 0 or text_box_count > 0):
            return "title-and-content"
        elif image_count > 0 and (text_box_count > 0 or bullet_list_count > 0):
            return "content-with-caption"
        elif len(elements) == 0:
            return "blank"
        else:
            return "title-and-content"
