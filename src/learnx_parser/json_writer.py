import json
import os
from dataclasses import asdict, is_dataclass

from learnx_parser.data_models import Slide, Transform, SlideLayout, LayoutPlaceholder


class DataclassJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if is_dataclass(obj):
            return asdict(obj)
        return json.JSONEncoder.default(self, obj)


class JsonWriter:
    def __init__(self, output_directory="./output"):
        # Directory where the generated JSON output will be saved
        self.output_directory = output_directory

    

    def _process_slide_for_json(self, slide: Slide) -> dict:
        processed_elements = []
        used_element_ids = set()

        slide_cx = slide.common_slide_data.cx
        slide_cy = slide.common_slide_data.cy

        # Create a dictionary to quickly look up slide elements by their ID
        slide_elements_by_id = {el.id: el for el in slide.shapes + slide.pictures + slide.group_shapes + slide.graphic_frames if el.id is not None}

        if slide.slide_layout:
            for layout_ph in slide.slide_layout.placeholders:
                found_element = None
                for el_id, element in slide_elements_by_id.items():
                    if hasattr(element, 'ph_type') and element.ph_type == layout_ph.ph_type and \
                       (layout_ph.ph_idx is None or (hasattr(element, 'ph_idx') and element.ph_idx == layout_ph.ph_idx)):
                        found_element = element
                        break

                if found_element:
                    element_dict = asdict(found_element)
                    if found_element.transform and found_element.transform.rot != 0:
                        element_dict["transform"] = {
                            "rotation": found_element.transform.rot / 60000.0,
                        }
                    else:
                        element_dict["transform"] = {}

                    processed_elements.append({
                        "type": "placeholder_container",
                        "ph_type": layout_ph.ph_type,
                        "ph_idx": layout_ph.ph_idx,
                        "transform": {
                            "rotation": layout_ph.transform.rot / 60000.0,
                        } if layout_ph.transform and layout_ph.transform.rot != 0 else {},
                        "children": [element_dict]
                    })
                    used_element_ids.add(found_element.id)

        all_slide_elements = slide.shapes + slide.pictures + slide.group_shapes + slide.graphic_frames
        for element in all_slide_elements:
            if element.id is not None and element.id not in used_element_ids:
                element_dict = asdict(element)
                if element.transform and element.transform.rot != 0:
                    element_dict["transform"] = {
                        "rotation": element.transform.rot / 60000.0,
                    }
                else:
                    element_dict["transform"] = {}
                processed_elements.append(element_dict)

        # Remove raw EMU values from common_slide_data
        processed_common_slide_data = asdict(slide.common_slide_data)
        del processed_common_slide_data['cx']
        del processed_common_slide_data['cy']

        processed_slide_layout = None
        if slide.slide_layout:
            processed_slide_layout = asdict(slide.slide_layout)
            if "placeholders" in processed_slide_layout:
                for placeholder in processed_slide_layout["placeholders"]:
                    if "transform" in placeholder:
                        # Create a Transform object from the dictionary
                        transform_obj = Transform(**placeholder["transform"])
                        placeholder["transform"] = {
                            "rotation": transform_obj.rot / 60000.0,
                        } if transform_obj.rot != 0 else {}

        return {
            "slide_number": slide.slide_number,
            "common_slide_data": processed_common_slide_data,
            "slide_layout": processed_slide_layout,
            "elements": processed_elements
        }

    def write_slide_json(self, slide_data, slide_number):
        processed_slide_data = self._process_slide_for_json(slide_data)
        slide_output_directory = os.path.join(self.output_directory, f"slide{slide_number}")
        os.makedirs(slide_output_directory, exist_ok=True)

        output_file_path = os.path.join(slide_output_directory, f"slide{slide_number}.json")
        with open(output_file_path, "w", encoding="utf-8") as f:
            json.dump(processed_slide_data, f, indent=4, cls=DataclassJSONEncoder)
        return output_file_path