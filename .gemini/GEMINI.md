# GEMINI.md

## Project Charter: LearnX PowerPoint Parser

### 🧠 Objective

Build a robust, fully-tested, importable Python package that:
- Parses `.pptx` files by manually reading the OpenXML structure
- Converts slides to cleanly structured HTML or JSON per slide
- Extracts and references media files (images, audio) with renamed, organized folders
- Preserves layout, text position, styling, and supports multilingual text
- Is installable via `uv add` and suitable for PyPI publication
- Will be used as a module in a larger application (not as a full app)

---

## 📋 Gemini Workflow Overview

### ❗️ Start Here: Setup + Planning Phase

Before generating any code:
1. **Unpack a sample `.pptx`** file and inspect all XML components
2. **Cross-reference each part with the ECMA-376 Part 1 PDF**
3. **Write a grounding doc**: `docs/schema_notes.md`, which includes:
   - Breakdown of slide elements from `ppt/slides/*.xml`
   - Mapping of tags like `<p:sp>`, `<a:t>`, `<p:pic>` to slide content
   - Explanation of how relationships resolve to media (`.rels` files)
   - Examples from the `.pptx` sample for each major element
4. Only begin writing code **after this is complete and saved**

---

## 🧠 Defined Project Workflow

### 🔹 Phase 1: Understanding & Grounding
**Goal**: Full comprehension of `.pptx` and XML schema.

Example Tasks:
- `inspect_pptx_structure`
- `map_xml_to_slide_elements`
- `cross_reference_with_ecma_pdf`
- `write_schema_notes`

Artifacts:
- `docs/schema_notes.md`
- `REMINDERS.md`
- `write_readme_and_usage_example`

---

### 🔹 Phase 2: Project Bootstrapping
**Goal**: Setup workspace, tooling, and environment.

Example Tasks:
- `init_uv_project`
- `setup_git_repo`
- `configure_pyproject.toml`
- `create_base_folders`: `src/`, `tests/`, `learnx_parser/`, etc.

---

### ✅ Phase 3: Single Slide Parser Prototype (Completed)
**Goal**: Parse 1 slide → HTML + media

Example Tasks:
- `parse_slide_xml`
- `extract_shapes_and_text`
- `extract_images_and_links`
- `write_html_output`
- `validate_media_extraction`

Artifacts:
- `learnx_parser/core/slide_parser.py`
- `learnx_parser/output/html_writer.py`
- `tests/test_slide_parser.py`

---

### ✅ Phase 4: JSON Representation (Completed)
**Goal**: Provide alternate JSON output for programmatic use.

Example Tasks:
- `json_writer_module`
- `test_json_output`

---

### 🔹 Phase 5: Scale to Full Presentation
**Goal**: Parse all slides in order.

Example Tasks:
- `parse_presentation_order`
- `iterate_over_all_slides`
- `batch_html_output`
- `batch_json_output`

---

### 🔹 Phase 6: API Layer
**Goal**: Provide clean API entrypoints.

Example Tasks:
- `define_parse_pptx_entrypoint`
- `validate_file_outputs_in_tests`
- `test_multilingual_text`

---

### 🔹 Phase 7: Publishing & Docs
**Goal**: Finalize for PyPI and external usage.

Example Tasks:
- `validate_uv_add_install`
- `publish_package (if needed)`

---

## 📦 Tooling Rules

- Use only `uv` CLI commands:
  - ✅ `uv venv`, `uv pip install`, `uv run`, `uv add`, `uv test`
  - ❌ Never run `python main.py`, `pip install`, `pytest`, etc.
- Maintain all dependencies and scripts in `pyproject.toml`

---

## 📁 Output Folder Example

```
lecture_output/
├── slide1/
│   ├── slide1.html or slide1.json
│   └── image1.png, shape2.png
├── slide2/
│   ├── slide2.html
│   └── image.jpg
```

---

## 📓 Task Journal Instructions

At the end of every task (whether code or planning), update:

```
tasks/<task_name>.md
```

### Template:
```
## Log: <task title>
- **Prompt**: <prompt you received>
- **Issue**: <issue or ambiguity>

### What I did:
...

### How I did it:
...

### What was challenging:
...

### Future work:
...
```

---

## Summary

Gemini, your job is to reason, research, and execute like a full-stack engineer. This includes documentation, planning, reflection, and improvement — not just outputting code.

Do not proceed to code until:
- ✅ The XML schema has been analyzed and documented
- ✅ Your understanding is grounded in both the sample `.pptx` and ECMA PDF

You're not just building a parser — you're building infrastructure.

Good luck.

---

## 🧠 Revised Project Workflow (Addressing Visual Inaccuracies)

### **Phase 1: Enhanced XML Parsing & Intermediate Representation**

**Goal:** Accurately parse all relevant PresentationML and DrawingML elements and convert them into a structured, easy-to-use Python object model. This will be the foundation for correct rendering.

*   **Task 1.1: Refine Slide Element Parsing (`parse_slide_elements`)**
    *   **Subtask 1.1.1: Parse Common Slide Data (`p:cSld`)**: Extract slide dimensions, background properties, and relationships to slide layouts/masters.
    *   **Subtask 1.1.2: Parse Shape Tree (`p:spTree`)**: Recursively parse all shapes (`p:sp`), group shapes (`p:grpSp`), graphic frames (`p:graphicFrame`), and pictures (`p:pic`).
    *   **Subtask 1.1.3: Extract Detailed Shape Properties (`p:spPr`)**:
        *   **Subtask 1.1.3.1: Geometry (`a:prstGeom`, `a:custGeom`)**: Understand and extract preset and custom shape geometries.
        *   **Subtask 1.1.3.2: Fills (`a:solidFill`, `a:gradFill`, `a:blipFill`, `a:pattFill`)**: Extract fill types (solid color, gradient, image, pattern) and their properties.
        *   **Subtask 1.1.3.3: Lines (`a:ln`)**: Extract line properties (width, color, dash, cap, join).
        *   **Subtask 1.1.3.4: Effects (`a:effectLst`, `a:effectDag`)**: Identify and extract visual effects (shadows, reflections, glows).
        *   **Subtask 1.1.3.5: Transforms (`a:xfrm`)**: Accurately extract position, size, rotation, and flip transformations.
    *   **Subtask 1.1.4: Extract Detailed Text Body Properties (`a:txBody`)**:
        *   **Subtask 1.1.4.1: Paragraph Properties (`a:pPr`)**: Extract alignment, indentation, spacing, and bullet/numbering properties.
        *   **Subtask 1.1.4.2: Run Properties (`a:rPr`)**: Extract font size, bold, italic, underline, color, font face, and other character-level formatting.
        *   **Subtask 1.1.4.3: Placeholder Information (`p:ph`)**: Identify placeholders and their types (title, body, picture, etc.).
    *   **Subtask 1.1.5: Handle Relationships (`.rels` files)**: Ensure all relationships (images, external links, slide masters, slide layouts) are correctly resolved and linked within the intermediate representation.

*   **Task 1.2: Define Intermediate Data Structures**
    *   **Subtask 1.2.1: Create Python Classes/Dataclasses**: Design classes (e.g., `Slide`, `Shape`, `TextFrame`, `Paragraph`, `TextRun`, `Image`, `Fill`, `Line`, `Effect`, `Transform`) to hold parsed data.
    *   **Subtask 1.2.2: Update `SlideParser` to use new structures**: Modify `SlideParser` to populate these new data structures instead of simple dictionaries.

---

### ✅ **Phase 2: Advanced HTML/CSS Rendering (Completed)**

**Goal:** Translate the rich intermediate representation into visually accurate HTML and CSS, addressing layout, styling, and complex elements.

*   **Task 2.1: Refine HTML Structure Generation**
    *   **Subtask 2.1.1: Implement Absolute Positioning**: Use `position: absolute` and calculated `top`, `left`, `width`, `height` based on EMUs for all elements.
    *   **Subtask 2.1.2: Apply Transformations**: Translate rotation, scaling, and flipping from `a:xfrm` into CSS `transform` properties.
*   **Task 2.2: Implement Comprehensive CSS Styling**
    *   **Subtask 2.2.1: Text Styling**: Generate CSS for font-size, font-family, color, bold, italic, underline, and other text decorations.
    *   **Subtask 2.2.2: Shape Styling**: Generate CSS for background fills (solid, gradient, image), borders, and basic shape geometries (rectangles, ovals).
    *   **Subtask 2.2.3: Advanced Effects (Initial Pass)**: Implement basic CSS for shadows and reflections if feasible with pure CSS. (More complex effects might require SVG or canvas).
*   **Task 2.3: Handle Slide Masters and Layouts in Rendering**
    *   **Subtask 2.3.1: Apply Master/Layout Properties**: Implement logic to inherit and override properties from slide masters and slide layouts.
    *   **Subtask 2.3.2: Placeholder Mapping**: Correctly map content from slide elements to their corresponding placeholders defined in the layout.

---

### ✅ **Phase 3: Media and External Resource Management (Completed)**

**Goal:** Ensure all media (images, audio) and external resources are correctly extracted, organized, and referenced in the HTML output.

*   **Task 3.1: Robust Media Extraction and Renaming**
    *   **Subtask 3.1.1: Extract All Media Types**: Ensure all image formats (PNG, JPG, GIF, etc.) are handled.
    *   **Subtask 3.1.2: Organize and Rename Media Files**: Implement a consistent naming convention and directory structure for extracted media.
*   **Task 3.2: Correct Media Referencing in HTML**
    *   **Subtask 3.2.1: Update Image Paths**: Ensure `<img>` tags correctly point to the extracted and renamed media files.
    *   **Subtask 3.2.2: Handle Image Fills**: Integrate extracted image fills into CSS `background-image` properties for shapes.

---

### ✅ **Phase 4: Testing and Validation (Completed)**

**Goal:** Implement comprehensive tests to ensure visual accuracy and functional correctness.

*   **Task 4.1: Unit Tests for New Parsing Logic**: Write detailed unit tests for each new parsing function and intermediate data structure.
*   **Task 4.2: Visual Regression Tests (Manual/Automated)**:
    *   **Subtask 4.2.1: Manual Visual Comparison**: Generate HTML for sample PPTX files and manually compare them against original PowerPoint screenshots.
    *   **Subtask 4.2.2: Automated Visual Diff (Future)**: Explore tools for automated visual comparison if manual testing becomes too cumbersome.
*   **Task 4.3: Integration Tests**: Test the entire pipeline from PPTX parsing to HTML generation.

---

### 🔹 Phase 5: Refinement and Modularity Improvements

**Goal:** Improve code structure, maintainability, and adherence to project conventions.

*   **Task 5.1: Refactor Existing Code**: Break down large functions, improve variable names, and add comments where necessary.
*   **Task 5.2: Modularize Components**: Ensure clear separation of concerns between parsing, data modeling, and rendering components.
*   **Task 5.3: Performance Optimization (If Needed)**: Address any performance bottlenecks identified during testing.
