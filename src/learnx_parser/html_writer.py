import os
import shutil

class HtmlWriter:
    def __init__(self, output_dir="./output", pptx_unpacked_path=None):
        self.output_dir = output_dir
        self.pptx_unpacked_path = pptx_unpacked_path

    def _emu_to_px(self, emu):
        # 1 EMUs = 1/914400 inches, 1 inch = 96 pixels (standard for web)
        return round(emu / 914400 * 96)

    def write_slide_html(self, slide_data, slide_number):
        html_content = f"""<!DOCTYPE html>
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

        for shape in slide_data["shapes"]:
            if shape["text"]:
                x = self._emu_to_px(shape["x"])
                y = self._emu_to_px(shape["y"])
                cx = self._emu_to_px(shape["cx"])
                cy = self._emu_to_px(shape["cy"])

                text_runs_html = ""
                for run in shape["runs"]:
                    style = ""
                    if "font_size" in run["properties"]:
                        style += f"font-size: {self._emu_to_px(run['properties']['font_size'])}px;"
                    if run["properties"].get("bold"):
                        style += "font-weight: bold;"
                    if run["properties"].get("italic"):
                        style += "font-style: italic;"
                    text_runs_html += f"<span style=\"{style}\">{run['text']}</span>"

                html_content += f"""
        <div class="shape" style="left: {x}px; top: {y}px; width: {cx}px; height: {cy}px;">
            <div class="text-content">{text_runs_html}</div>
        </div>
"""

        # Copy media files and update paths
        media_output_dir = os.path.join(self.output_dir, "media")
        os.makedirs(media_output_dir, exist_ok=True)

        for media_item in slide_data["media"]:
            if media_item["type"] == "image":
                # Original path in the unpacked PPTX
                original_media_path = os.path.join(self.pptx_unpacked_path, media_item["path"].lstrip("/"))
                # Destination path in the output directory
                dest_media_path = os.path.join(media_output_dir, os.path.basename(media_item["path"]))

                if os.path.exists(original_media_path):
                    shutil.copy(original_media_path, dest_media_path)
                    # Update src to be relative to the HTML file
                    html_content += f"""
        <img class="image" src="media/{os.path.basename(media_item['path'])}" style="left: 0; top: 0; width: 100px; height: 100px;" />
"""
                else:
                    print(f"Warning: Media file not found: {original_media_path}")

        html_content += f"""
    </div>
</body>
</html>"""

        os.makedirs(self.output_dir, exist_ok=True)

        output_file_path = os.path.join(self.output_dir, f"slide{slide_number}.html")
        with open(output_file_path, "w", encoding="utf-8") as f:
            f.write(html_content)
        return output_file_path
