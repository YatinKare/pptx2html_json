# Project Tasks

This file tracks the high-level tasks and sub-tasks for building the LearnX PowerPoint Parser.

## Phase 1: Understanding & Grounding
**Goal**: Full comprehension of `.pptx` and XML schema.

*   [x] **Task: `inspect_pptx_structure`**
    *   [x] Sub-task: Obtain a sample `.pptx` file from the user.
    *   [x] Sub-task: Unzip the `.pptx` file into a temporary directory (`/tmp/pptx_unpacked`).
    *   [x] Sub-task: List the full directory structure of the unpacked content.
    *   [x] Sub-task: Document the high-level file/folder structure (e.g., `_rels`, `docProps`, `ppt`).
*   [x] **Task: `map_xml_to_slide_elements`**
    *   [x] Sub-task: Analyze the content of `ppt/presentation.xml` to understand presentation-level properties.
    *   [x] Sub-task: Analyze the content of `ppt/slides/_rels/slideX.xml.rels` to understand slide relationships.
    *   [x] Sub-task: Analyze the content of `ppt/slides/slideX.xml` to identify core shape, text, and image tags.
*   [x] **Task: `cross_reference_with_ecma_pdf`**
    *   [x] Sub-task: Search for the ECMA-376 Part 1 PDF online.
    *   [x] Sub-task: Download or link to the PDF for reference.
    *   [x] Sub-task: Correlate key XML tags (e.g., `<p:sp>`, `<a:t>`) with their definitions in the specification.
*   [x] **Task: `write_schema_notes`**
    *   [x] Sub-task: Create the `docs/` directory.
    *   [x] Sub-task: Create `docs/schema_notes.md`.
    *   [x] Sub-task: Synthesize findings into a structured document explaining the mapping from XML to slide content, with examples.

---

## Phase 2: Project Bootstrapping
**Goal**: Setup workspace, tooling, and environment.

*   [x] `init_uv_project`
*   [x] `setup_git_repo`
*   [x] `configure_pyproject.toml`
*   [x] `create_base_folders`

---

## Phase 3: Single Slide Parser Prototype
**Goal**: Parse 1 slide → HTML + media

*   [x] `parse_slide_xml`
*   [x] `extract_shapes_and_text`
*   [x] `extract_images_and_links`
*   [x] `write_html_output`
*   [x] `validate_media_extraction`

---

## Phase 4: JSON Representation
**Goal**: Provide alternate JSON output for programmatic use.

*   [x] `json_writer_module`
*   [x] `test_json_output`

---

## Phase 5: Scale to Full Presentation
**Goal**: Parse all slides in order.

*   [x] `parse_presentation_order`
*   [x] `iterate_over_all_slides`
*   [x] `batch_html_output`
*   [x] `batch_json_output`

---

## Phase 6: API Layer
**Goal**: Provide clean API entrypoints.

*   [x] `define_parse_pptx_entrypoint`
*   [x] `validate_file_outputs_in_tests`
*   [ ] `test_multilingual_text`

---

## Phase 7: Publishing & Docs
**Goal**: Finalize for PyPI and external usage.

*   [x] `validate_uv_add_install`
*   [x] `publish_package (if needed)`
*   [x] `write_readme_and_usage_example`
