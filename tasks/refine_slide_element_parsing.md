## Log: Refine Slide Element Parsing (Placeholder Inheritance & Image Transforms)
- **Prompt**: Continue editing and looking at the tasks. Address visual inaccuracies in HTML output, specifically for image cropping and element positioning.
- **Issue**: Initial HTML output for `slide23.xml` (rendered as `slide2.html`) showed incorrect positioning and sizing for text and images, and image cropping was not applied. This was due to placeholder elements in the slide XML not having explicit transform data, which is instead inherited from the slide layout. The `_extract_transform` function in `slide_parser.py` was also initializing `cx` and `cy` with non-zero defaults, preventing inherited transforms from being applied.

### What I did:
1.  **Identified the problem**: Realized that placeholder elements in `slide23.xml` inherit their transform properties (position, size) from the associated slide layout (`slideLayout26.xml`).
2.  **Created `slide_layout_parser.py`**: Implemented a new parser to extract placeholder transform data from slide layout XML files.
3.  **Modified `slide_parser.py`**:
    *   Updated `__init__` to accept `pptx_unpacked_path`.
    *   Modified `parse_slide` to identify the correct slide layout, instantiate `SlideLayoutParser`, and use it to retrieve inherited transform properties for shapes and pictures that are placeholders and lack their own explicit transforms.
    *   Corrected the `_extract_transform` function to initialize `cx` and `cy` to 0, ensuring that inherited values are correctly applied.
    *   Updated `_parse_shape_tree` to extract `ph_type` and `ph_idx` for `Picture` objects.
4.  **Modified `data_models.py`**: Added `ph_type` and `ph_idx` attributes to the `Picture` dataclass.
5.  **Modified `html_writer.py`**:
    *   Added `_get_transform_css` helper function to generate CSS `transform` properties (rotation, flipH, flipV).
    *   Added `_get_image_crop_css` helper function to generate CSS `clip-path` properties based on `src_rect` values.
    *   Applied these new CSS properties to shapes and images in the generated HTML.
6.  **Modified `main.py`**: Updated to unpack the PPTX and use the `PptxParser` to generate HTML.
7.  **Updated `test_slide_parser.py`**:
    *   Modified the `slide_parser` fixture to pass `pptx_unpacked_path`.
    *   Updated assertions for `text_shape.transform` and `picture_obj.transform` to reflect the correct inherited values from `slideLayout26.xml`.
    *   Added assertions for `picture_obj.ph_type` and `picture_obj.ph_idx`.
8.  **Updated `test_html_writer.py`**: Added a new test `test_image_transform_and_crop_css` to verify the generated `transform` and `clip-path` CSS for images. Corrected syntax errors in assertion messages.

### How I did it:
-   Used `read_file` to inspect XML structures (`slide23.xml`, `slideLayout26.xml`, `.rels` files).
-   Used `write_file` to create new files (`slide_layout_parser.py`) and `replace` to modify existing files (`slide_parser.py`, `data_models.py`, `html_writer.py`, `main.py`, `test_slide_parser.py`, `test_html_writer.py`).
-   Used `uv run pytest` to iteratively test and debug the parsing and rendering logic, using print statements for detailed inspection when tests failed.
-   Corrected `TypeError` and `AssertionError` by carefully examining the call stack and print output.

### What was challenging:
-   Accurately identifying the source of transform data (direct vs. inherited from layout).
-   Debugging the `replace` tool's behavior with complex string literals and f-strings, which led to switching to `write_file` for some modifications.
-   Ensuring correct `ph_type` and `ph_idx` extraction and usage for placeholder lookup.

### Future work:
-   Implement full inheritance for all properties (not just transforms) from slide layouts and masters.
-   Handle more complex shape geometries beyond basic rectangles.
-   Implement support for visual effects (shadows, reflections, glows) in CSS.
-   Refine text rendering to accurately match PowerPoint's text flow and wrapping.
-   Consider automated visual regression testing for HTML output.
