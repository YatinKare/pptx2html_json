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

### 🔹 Phase 3: Single Slide Parser Prototype
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

### 🔹 Phase 4: JSON Representation
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
  - ✅ `uv venv`, `uv pip install`, `uv add`, `uv run`, `uv test`
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
