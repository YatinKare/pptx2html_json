import json
import os

import json
import os
from dataclasses import asdict, is_dataclass

class DataclassJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if is_dataclass(obj):
            return asdict(obj)
        return json.JSONEncoder.default(self, obj)

class JsonWriter:
    def __init__(self, output_dir="./output"):
        self.output_dir = output_dir

    def write_slide_json(self, slide_data, slide_number):
        slide_output_dir = os.path.join(self.output_dir, f"slide{slide_number}")
        os.makedirs(slide_output_dir, exist_ok=True)

        output_file_path = os.path.join(slide_output_dir, f"slide{slide_number}.json")
        with open(output_file_path, "w", encoding="utf-8") as f:
            json.dump(slide_data, f, indent=4, cls=DataclassJSONEncoder)
        return output_file_path
