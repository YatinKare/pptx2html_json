## Project Tasks

This file tracks the high-level tasks and sub-tasks for building the LearnX PowerPoint Parser.

## 📋 Gemini Workflow Overview (Revised)

### ❗️ Start Here: Setup + Planning Phase (Completed)

### 🔹 Phase 1: Advanced Property Resolution (Core)
**Goal**: Implement a robust mechanism to resolve inherited properties for slide elements.

*   [ ] **Task: `understand_pptx_inheritance_model`**
    *   [ ] Sub-task: Review ECMA-376 Part 1 (Section 19.3.1.16 `p:ph` and 19.3.1.17 `p:spPr`) and other relevant sections for property inheritance rules (e.g., from slide master, slide layout, theme).
    *   [ ] Sub-task: Identify key XML files involved in inheritance: `theme*.xml`, `slideLayout*.xml`, `slideMaster*.xml`, `presProps.xml`, `viewProps.xml`.
    *   [ ] Sub-task: Document the inheritance hierarchy for common properties (position, size, font, color) in `docs/inheritance_model.md`.
*   [ ] **Task: `implement_style_resolver_base`**
    *   [ ] Sub-task: Create `src/learnx_parser/style_resolver.py`.
    *   [ ] Sub-task: Implement a base `StyleResolver` class that can load and store properties from XML elements.
    *   [ ] Sub-task: Add methods to merge properties based on a defined inheritance order.
    *   [ ] Sub-task: Write unit tests for `StyleResolver`'s property merging logic.
*   [ ] **Task: `extract_theme_properties`**
    *   [ ] Sub-task: Modify `StyleResolver` to parse `ppt/theme/theme*.xml` to extract default text styles, colors, and other theme-level properties.
    *   [ ] Sub-task: Write unit tests to verify theme property extraction.
*   [ ] **Task: `extract_master_properties`**
    *   [ ] Sub-task: Modify `StyleResolver` to parse `ppt/slideMasters/slideMaster*.xml` to extract master slide properties, including placeholders and their default styles.
    *   [ ] Sub-task: Write unit tests to verify master property extraction and merging with master/theme properties.
*   [x] **Task: `extract_layout_properties`**
    *   [x] Sub-task: Modify `StyleResolver` to parse `ppt/slideLayouts/slideLayout*.xml` to extract layout-specific properties and placeholder information.
    *   [x] Sub-task: Write unit tests to verify layout property extraction and merging with master/theme properties.
*   [x] **Task: `integrate_property_lookup`**
    *   [x] Sub-task: Modify `SlideParser` to accept `StyleResolver` instance.
    *   [x] Sub-task: Update `SlideParser.extract_shapes_and_text` to use `StyleResolver` to look up effective properties for each shape and text run, considering inheritance from slide, layout, and master.
    *   [x] Sub-task: Update `SlideParser.extract_media` to use `StyleResolver` for image positioning if defined by placeholders.
    *   [x] Sub-task: Update `tests/test_slide_parser.py` to reflect the new property extraction.

### 🔹 Phase 2: Enhanced Slide Content Extraction
**Goal**: Integrate the property resolution into the `SlideParser` to extract a richer set of data.

*   [ ] **Task: `extract_full_text_properties`**
    *   [ ] Sub-task: Enhance `SlideParser` to extract more text properties: font family (`a:font`), color (`a:solidFill`, `a:schemeClr`), alignment (`a:pPr algn`), line spacing (`a:lnSpc`), paragraph indentation (`a:pPr marL`).
    *   [ ] Sub-task: Update `tests/test_slide_parser.py` to assert these new properties.
*   [ ] **Task: `extract_shape_geometry`**
    *   [ ] Sub-task: Ensure `SlideParser` accurately extracts shape geometry (position and size) from `p:spPr/a:xfrm` and resolves inherited values.
    *   [ ] Sub-task: Update `tests/test_slide_parser.py` to verify accurate geometry extraction.
*   [ ] **Task: `extract_slide_background`**
    *   [ ] Sub-task: Modify `SlideParser` to extract slide background properties (solid fill, gradient fill, picture fill) from `p:bg` elements, considering inheritance.
    *   [ ] Sub-task: Update `tests/test_slide_parser.py` to verify background extraction.

### 🔹 Phase 3: Comprehensive HTML Generation
**Goal**: Update the `HtmlWriter` to utilize the richer extracted data to produce visually accurate HTML.

*   [x] **Task: `render_accurate_text_styles`**
    *   [x] Sub-task: Modify `HtmlWriter` to apply all extracted text properties (font family, color, alignment, line spacing, etc.) to the generated HTML.
    *   [x] Sub-task: Update `tests/test_html_writer.py` to verify these styles.
*   [ ] **Task: `render_accurate_shape_positions`**
    *   [ ] Sub-task: Modify `HtmlWriter` to use the resolved `x`, `y`, `cx`, `cy` values for positioning and sizing HTML elements, ensuring accurate layout.
    *   [ ] Sub-task: Update `tests/test_html_writer.py` to verify accurate positioning.
*   [ ] **Task: `render_slide_background`**
    *   [ ] Sub-task: Modify `HtmlWriter` to render the extracted slide background (e.g., using CSS for solid colors or gradients, or `<img>` for background images).
    *   [ ] Sub-task: Update `tests/test_html_writer.py` to verify background rendering.
*   [ ] **Task: `improve_html_layout`**
    *   **Goal:** Improve the HTML layout to accurately reflect the positioning and arrangement of elements in the original PowerPoint presentation, specifically addressing the vertical stacking issue.
    *   [x] **Sub-task: `review_openxml_layout_docs`**
        *   **Description:** Re-examine relevant OpenXML documentation (`13_PresentationML.txt`, `20_DrawingML_Framework.txt`, etc.) for properties related to element positioning, text box flow, and multi-column layouts.
    *   [ ] **Sub-task: `analyze_galaxy_slide_xml_for_layout`**
        *   **Description:** Analyze `slide23.xml` and its associated layout (`slideLayout26.xml`) to identify specific XML attributes that define the horizontal arrangement of elements, especially for the "Agenda" slide.
    *   [ ] **Sub-task: `propose_css_layout_strategy`**
        *   **Description:** Based on the OpenXML analysis, develop a detailed CSS strategy (e.g., using Flexbox or Grid) to achieve the desired horizontal layout, considering how elements are grouped and positioned in PowerPoint.
    *   [ ] **Sub-task: `implement_css_layout_in_html_writer`**
        *   **Description:** Modify `src/learnx_parser/html_writer.py` to apply the new CSS layout strategy. This may involve changes to the `slide-container` styles and how individual elements are rendered.
    *   [ ] **Sub-task: `test_html_layout_accuracy`**
        *   **Description:** Write/update unit tests in `tests/test_html_writer.py` to specifically verify the accuracy of the new HTML layout, ensuring elements are positioned correctly relative to each other.
    *   [ ] **Sub-task: `visual_verify_html_output`**
        *   **Description:** Manually verify the generated HTML output (`output_presentation/slide2/slide2.html`) against the PowerPoint screenshot to confirm visual accuracy of the layout.

### 🔹 Phase 4: Refactoring and Modularity
**Goal**: Review the codebase for further modularization and adherence to best practices.

*   [ ] **Task: `refactor_xml_parsing_helpers`**
    *   [ ] Sub-task: Create a utility module (e.g., `src/learnx_parser/xml_utils.py`) for common XML parsing patterns (e.g., finding elements with namespaces, getting attributes safely).
    *   [ ] Sub-task: Refactor `SlideParser`, `PresentationParser`, and `StyleResolver` to use these utilities.
    *   [ ] Sub-task: Ensure existing tests still pass.
*   [ ] **Task: `centralize_constants`**
    *   [ ] Sub-task: Create a `src/learnx_parser/constants.py` module for OpenXML namespaces, relationship types, and other magic strings.
    *   [ ] Sub-task: Replace hardcoded strings with constants across the codebase.
    *   [ ] Sub-task: Ensure existing tests still pass.

### 🔹 Phase 5: Visual Verification & Refinement
**Goal**: Implement automated or semi-automated visual testing and refine the parsing/rendering.

*   [ ] **Task: `implement_visual_comparison_tool`**
    *   [ ] Sub-task: Research Python libraries for image comparison (e.g., `Pillow`, `scikit-image`).
    *   [ ] Sub-task: Develop a script that takes a generated HTML file, renders it to an image (e.g., using `selenium` with a headless browser), and compares it to a reference screenshot.
    *   [ ] Sub-task: Integrate this into the testing workflow (perhaps as a separate `uv run visual_test` command).
*   [ ] **Task: `refine_rendering_based_on_visuals`**
    *   [ ] Sub-task: Analyze visual discrepancies identified by the comparison tool.
    *   [ ] Sub-task: Iteratively refine `SlideParser` and `HtmlWriter` to address these discrepancies (e.g., font rendering, spacing, exact positioning).
    *   [ ] Sub-task: Update tests as necessary.
