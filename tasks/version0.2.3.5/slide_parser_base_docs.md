# `base.py` Documentation

This module defines the core `SlideParser` class, responsible for orchestrating the parsing of a single PowerPoint slide. It handles the initialization, relationship parsing, and delegates specific parsing tasks to other modules.

## `SlideParser` Class

### `__init__(self, slide_xml_path, slide_rels_path, pptx_unpacked_path, slide_width, slide_height)`
- **`slide_xml_path`**: Absolute path to the slide's XML file.
- **`slide_rels_path`**: Absolute path to the slide's relationships XML file (can be `None`).
- **`pptx_unpacked_path`**: Root directory of the unpacked PPTX archive.
- **`slide_width`**: Width of the slide in EMUs.
- **`slide_height`**: Height of the slide in EMUs.

Initializes the parser, loads the slide XML, parses relationships, and sets up namespace maps.

### `_parse_rels(self)`
Parses the slide's `.rels` file to extract relationships (e.g., to media files, slide layouts).

### `_extract_common_slide_data(self) -> CommonSlideData`
Extracts common slide properties like background color/gradient and slide dimensions.

### `_get_slide_layout_obj(self) -> SlideLayout | None`
Resolves and parses the associated slide layout, returning a `SlideLayout` object if found.

### `_parse_slide_elements(self, slide_layout_obj: SlideLayout | None)`
Delegates to `parse_shape_tree` (from `shapes.py`) to extract all shapes, pictures, group shapes, and graphic frames from the slide.

### `_apply_inherited_transforms(self, shapes, pictures, slide_layout_object)`
Applies inherited transform properties from slide layout placeholders to corresponding slide elements if they don't have their own transforms.

### `parse_slide(self, slide_number: int) -> Slide`
Main method to parse a complete slide. It orchestrates the extraction of all slide data, applies inherited properties, and returns a `Slide` object.

### `extract_hyperlinks(self) -> list[Hyperlink]`
Extracts all hyperlinks present on the slide.
