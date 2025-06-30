# Version 0.2.0 Plan: Layout Inference and Relative Positioning

## Phase 1: Layout Inference and Dynamic HTML Structure

### Task 1.1: Implement Layout Inference in HtmlWriter
- **Subtask 1.1.1:** Add `_render_slide_content(self, slide: Slide)` method to `html_writer.py`.
- **Subtask 1.1.2:** Implement basic heuristic for "title + image-left + text-right" layout within `_render_slide_content`.
- **Subtask 1.1.3:** Modify `write_slide_html` to call `_render_slide_content`.

### Task 1.2: Adjust Relative Positioning for Nested Elements
- **Subtask 1.2.1:** Modify `_render_graphic_frame_html` to accept `parent_x` and `parent_y` and calculate relative positions.
- **Subtask 1.2.2:** Modify `_render_group_shape_html` to accept `parent_x` and `parent_y` and calculate relative positions, and pass parent coordinates to its children.
- **Subtask 1.2.3:** Modify `_render_picture_html` to accept `parent_x` and `parent_y` and calculate relative positions.
- **Subtask 1.2.4:** Modify `_render_shape_html` to accept `parent_x` and `parent_y` and calculate relative positions.
- **Subtask 1.2.5:** Update calls to rendering functions in `write_slide_html` to pass `0, 0` for top-level elements.

### Task 1.3: Enhance Testing for Layout Inference
- **Subtask 1.3.1:** Add a new test case `test_nested_flexbox_layout_html_output` in `tests/test_flexbox_layout.py` to validate nested element rendering and relative positioning.
- **Subtask 1.3.2:** Fix `TypeError` in `tests/test_json_writer.py` by providing `pptx_unpacked_path` to `SlideParser`.
- **Subtask 1.3.3:** Fix `NameError` and `AttributeError` in `tests/test_flexbox_layout.py` by adding missing imports (`Picture`, `Shape`, `Slide`, `BlipFill`, `re`).
- **Subtask 1.3.4:** Adjust expected values in `test_flexbox_layout.py` and `test_html_writer.py` to account for rounding in `_emu_to_px`.

## Phase 2: Project Maintenance and Documentation

### Task 2.1: Update Project Metadata
- **Subtask 2.1.1:** Bump project version to 0.2.0 in `pyproject.toml`.

### Task 2.2: Update Documentation
- **Subtask 2.2.1:** Add comprehensive OOXML documentation files under `docs/ooxml_docs_v2/` and remove outdated documentation files.
- **Subtask 2.2.2:** Update `.gitignore` to exclude generated output directories and `requirements.txt`.

### Task 2.3: Final Review and User Testing
- **Subtask 2.3.1:** Generate HTML for `example/Galaxy presentation.pptx` and review `slide2.html` for correct layout.
- **Subtask 2.3.2:** User review of generated HTML.
