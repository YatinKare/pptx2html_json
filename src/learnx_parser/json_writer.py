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
    def __init__(self, output_dir="./output"):
        self.output_dir = output_dir

    def _process_slide_for_json(self, slide: Slide) -> dict:
        processed_elements = []
        used_element_ids = set()

        # Create a dictionary to quickly look up slide elements by their ID
        slide_elements_by_id = {el.id: el for el in slide.shapes + slide.pictures + slide.group_shapes + slide.graphic_frames if el.id is not None}

        # Define a root container for the slide, with 0,0 coordinates
        # The slide_root_transform itself will have absolute coordinates (0,0) and the slide's dimensions
        slide_root_transform = Transform(x=0, y=0, cx=slide.common_slide_data.cx, cy=slide.common_slide_data.cy)

        if slide.slide_layout:
            # Process elements based on slide layout placeholders
            for layout_ph in slide.slide_layout.placeholders:
                # Find the actual slide element corresponding to this placeholder
                found_element = None
                for el_id, element in slide_elements_by_id.items():
                    if hasattr(element, 'ph_type') and element.ph_type == layout_ph.ph_type and \
                       (layout_ph.ph_idx is None or (hasattr(element, 'ph_idx') and element.ph_idx == layout_ph.ph_idx)):
                        found_element = element
                        break

                if found_element:
                    # Calculate element's transform relative to the placeholder
                    relative_transform_to_ph = Transform(
                        x=found_element.transform.x - layout_ph.transform.x,
                        y=found_element.transform.y - layout_ph.transform.y,
                        cx=found_element.transform.cx,
                        cy=found_element.transform.cy,
                        rot=found_element.transform.rot,
                        flipH=found_element.transform.flipH,
                        flipV=found_element.transform.flipV
                    )
                    element_dict = asdict(found_element)
                    element_dict["transform"] = asdict(relative_transform_to_ph)
                    
                    # Calculate placeholder's transform relative to the slide root
                    relative_ph_transform_to_root = Transform(
                        x=layout_ph.transform.x - slide_root_transform.x,
                        y=layout_ph.transform.y - slide_root_transform.y,
                        cx=layout_ph.transform.cx,
                        cy=layout_ph.transform.cy,
                        rot=layout_ph.transform.rot,
                        flipH=layout_ph.transform.flipH,
                        flipV=layout_ph.transform.flipV
                    )

                    processed_elements.append({
                        "type": "placeholder_container",
                        "ph_type": layout_ph.ph_type,
                        "ph_idx": layout_ph.ph_idx,
                        "transform": asdict(relative_ph_transform_to_root), # Placeholder's transform relative to slide root
                        "children": [element_dict]
                    })
                    used_element_ids.add(found_element.id)

        # Add any elements not associated with a placeholder (these will retain their absolute positioning for now)
        all_slide_elements = slide.shapes + slide.pictures + slide.group_shapes + slide.graphic_frames
        for element in all_slide_elements:
            if element.id is not None and element.id not in used_element_ids:
                processed_elements.append(asdict(element))

        return {
            "slide_number": slide.slide_number,
            "common_slide_data": asdict(slide.common_slide_data),
            "slide_layout": asdict(slide.slide_layout) if slide.slide_layout else None,
            "elements": processed_elements
        }

    def write_slide_json(self, slide_data, slide_number):
        processed_slide_data = self._process_slide_for_json(slide_data)
        slide_output_dir = os.path.join(self.output_dir, f"slide{slide_number}")
        os.makedirs(slide_output_dir, exist_ok=True)

        output_file_path = os.path.join(slide_output_dir, f"slide{slide_number}.json")
        with open(output_file_path, "w", encoding="utf-8") as f:
            json.dump(processed_slide_data, f, indent=4, cls=DataclassJSONEncoder)
        return output_file_path
