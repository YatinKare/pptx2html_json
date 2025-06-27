import json
import os

class JsonWriter:
    def __init__(self, output_dir="./output"):
        self.output_dir = output_dir

    def write_slide_json(self, slide_data, slide_number):
        # Ensure output directory exists
        os.makedirs(self.output_dir, exist_ok=True)

        output_file_path = os.path.join(self.output_dir, f"slide{slide_number}.json")
        with open(output_file_path, "w", encoding="utf-8") as f:
            json.dump(slide_data, f, indent=4)
        return output_file_path
