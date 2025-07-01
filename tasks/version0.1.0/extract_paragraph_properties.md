## Log: Extract Paragraph Properties (`a:pPr`)
- **Prompt**: Extract alignment, indentation, spacing, and bullet/numbering properties from `a:pPr`.
- **Issue**: Paragraph properties are not yet fully extracted, leading to inaccurate text rendering.

### What I did:
- Created this log file for Subtask 1.1.4.1.
- Implemented logic to extract `algn` and `indent` from `a:pPr` elements within `a:txBody` in `src/learnx_parser/slide_parser.py`.
- Updated `RunProperties` dataclass in `src/learnx_parser/data_models.py` to include `color`, `scheme_color`, `font_face`, and `underline` fields.
- Implemented extraction of `font_size`, `bold`, `italic`, `color`, `scheme_color`, `font_face`, and `underline` for text runs (`a:rPr`).
- Updated `tests/test_slide_parser.py` to assert the presence and values of these properties, and adjusted assertions for `font_size` based on the sample `slide23.xml`.
- Debugged and fixed `AttributeError` by adding missing attributes to `RunProperties` dataclass.

### How I did it:
- Analyzed `20_DrawingML_Framework.txt` to understand the structure of `a:pPr` and `a:rPr`.
- Modified `_parse_shape_tree` to extract the relevant attributes.
- Updated dataclasses to reflect the new data being extracted.
- Iteratively ran tests and debugged until all tests passed.

### What was challenging:
- Ensuring all relevant attributes were extracted and correctly mapped to the dataclasses.
- Handling cases where attributes might not be explicitly present in the XML (e.g., font size for the "Agenda" shape).

### Future work:
- **Subtask 1.1.4.3: Placeholder Information (`p:ph`)**: Identify placeholders and their types (title, body, picture, etc.).
- Continue with other subtasks in Phase 1, focusing on detailed property extraction.
- Update unit tests in `tests/test_slide_parser.py` for new parsing logic.
