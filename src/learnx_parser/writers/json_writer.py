import json
import os
from dataclasses import asdict

from learnx_parser.models.core import JsonElement, JsonPresentation, JsonSlide, Slide


class JsonWriter:
    def __init__(self, output_directory="./output"):
        self.output_directory = output_directory

    def write_presentation_json(self, presentation_data: JsonPresentation):
        output_file_path = os.path.join(self.output_directory, "presentation.json")
        os.makedirs(self.output_directory, exist_ok=True)

        # Convert dataclass to dictionary and remove None values recursively
        def remove_none(obj):
            if isinstance(obj, dict):
                return {k: remove_none(v) for k, v in obj.items() if v is not None}
            elif isinstance(obj, list):
                return [remove_none(elem) for elem in obj if elem is not None]
            else:
                return obj

        cleaned_data = remove_none(asdict(presentation_data))

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
                    paragraph_text = "".join([run.text for run in paragraph.text_runs])

                    paragraph_style = {}
                    if paragraph.text_runs:
                        first_run_properties = paragraph.text_runs[0].properties
                        if first_run_properties.bold:
                            paragraph_style["bold"] = True
                        if first_run_properties.italic:
                            paragraph_style["italic"] = True
                        if first_run_properties.font_size:
                            paragraph_style["fontSize"] = first_run_properties.font_size
                        if first_run_properties.underline:
                            paragraph_style["underline"] = True

                    is_bullet = (
                        paragraph.properties.bullet_type is not None
                        and paragraph.properties.bullet_type != "none"
                    ) or (
                        paragraph.properties.level is not None
                        and paragraph.properties.level > 0
                    )

                    if is_bullet:
                        # If we were accumulating text box content, finalize it first
                        if current_text_box_content:
                            elements.append(
                                JsonElement(
                                    type="text-box",
                                    text="\n".join(current_text_box_content),
                                )
                            )
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
                    elements.append(
                        JsonElement(
                            type="text-box", text="\n".join(current_text_box_content)
                        )
                    )

        for picture in slide.pictures:
            if picture.path:
                elements.append(JsonElement(type="image", src=picture.path))

        # Filter out elements with no meaningful content (e.g., empty text boxes)
        elements = [
            el for el in elements if el.text or el.src or el.items or el.description
        ]

        # This is a simplified layout mapping. You may need to adjust it based on your needs.
        layout = slide.slide_layout.type if slide.slide_layout else "custom"

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
