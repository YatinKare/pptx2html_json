# Version 0.2.1 Plan: Relative Layout and Semantic Structure

## Phase 1: Research and Layout Identification

### Task 1.1: Re-examine OOXML documentation for slide layouts and placeholders.
- **Subtask 1.1.1:** Review `docs/ooxml_docs_v2/PresentationML/` for slide layout definitions.
- **Subtask 1.1.2:** Review `docs/ooxml_docs_v2/DrawingML/` for shape and text properties related to layout.
- **Subtask 1.1.3:** Cross-reference with `temp_pptx` (decompiled `Galaxy presentation.pptx`) to understand real-world examples of layouts.
- **Subtask 1.1.4:** Identify common slide layouts (e.g., Title, Title and Content, Two Content, Title Only, Blank) and their characteristic placeholder arrangements.

### Task 1.2: Define new data structures for semantic layout.
- **Subtask 1.2.1:** Create Python classes/dataclasses to represent inferred slide layouts (e.g., `SlideLayout`, `LayoutPlaceholder`).
- **Subtask 1.2.2:** Update `Slide` dataclass to include a reference to the inferred layout.

## Phase 2: Slide Layout Inference

### Task 2.1: Implement layout inference in `slide_layout_parser.py` (or a new module).
- **Subtask 2.1.1:** Develop logic to analyze placeholder types and positions on a slide.
- **Subtask 2.1.2:** Map identified patterns to predefined common slide layouts.
- **Subtask 2.1.3:** Handle custom layouts or unknown layouts gracefully.

### Task 2.2: Integrate layout inference into `SlideParser`.
- **Subtask 2.2.1:** Modify `SlideParser` to use the layout inference logic.
- **Subtask 2.2.2:** Populate the `Slide` object with the inferred layout information.

## Phase 3: Relative Positioning in JSON Output

### Task 3.1: Modify `JsonWriter` to use inferred layout for relative positioning.
- **Subtask 3.1.1:** Update `_process_slide_for_json` to leverage the new layout information.
- **Subtask 3.1.2:** Calculate and output relative `x`, `y`, `cx`, `cy` values for elements within layout containers.
- **Subtask 3.1.3:** Ensure the JSON output reflects the hierarchical structure of the inferred layout.

### Task 3.2: Test JSON output for relative positioning.
- **Subtask 3.2.1:** Create new unit tests for `JsonWriter` to verify relative coordinates for various inferred layouts.
- **Subtask 3.2.2:** Generate JSON for `Galaxy presentation.pptx` and manually inspect `slide2.json` and `slide5.json` for correct relative positioning.

## Phase 4: Relative Positioning in HTML Output

### Task 4.1: Modify `HtmlWriter` to use inferred layout for relative positioning.
- **Subtask 4.1.1:** Update `_render_slide_content` to leverage the new layout information.
- **Subtask 4.1.2:** Generate HTML/CSS using flexbox or grid for layout, avoiding absolute positioning where possible.
- **Subtask 4.1.3:** Ensure text is not squished and covers the whole page as requested.

### Task 4.2: Test HTML output for relative positioning.
- **Subtask 4.2.1:** Create new unit tests for `HtmlWriter` to verify the generated HTML structure and CSS.
- **Subtask 4.2.2:** Generate HTML for `Galaxy presentation.pptx` and manually inspect `slide2.html` and `slide5.html` for correct visual layout.

## Phase 5: Final Review and User Testing

### Task 5.1: User review of generated HTML and JSON.
