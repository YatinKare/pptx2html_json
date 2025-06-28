## Log: Extract Placeholder Information (`p:ph`)
- **Prompt**: Identify placeholders and their types (title, body, picture, etc.).
- **Issue**: Placeholder information is not currently extracted, which is crucial for correct layout and content mapping.

### What I did:
- Created this log file for Subtask 1.1.4.3.
- Updated the `Shape` dataclass in `src/learnx_parser/data_models.py` to include `ph_type`, `ph_idx`, `ph_orient`, and `ph_sz` fields.
- Implemented logic in `_parse_shape_tree` within `src/learnx_parser/slide_parser.py` to extract these attributes from `p:nvPr/p:ph` elements.
- Updated the `Shape` constructor call to pass the extracted placeholder information.
- Updated `tests/test_slide_parser.py` to include assertions for these new placeholder properties, specifically for the "Agenda" shape.

### How I did it:
- Analyzed `20_DrawingML_Framework.txt` and `13_PresentationML.txt` to understand the structure and attributes of `p:ph`.
- Modified `_parse_shape_tree` to extract the relevant attributes.
- Updated dataclasses and test assertions to reflect the new data being extracted.
- Iteratively ran tests and debugged until all tests passed.

### What was challenging:
- Correctly handling optional attributes and ensuring `None` values are assigned when attributes are not present.

### Future work:
- **Subtask 1.1.5: Handle Relationships (`.rels` files)**: Ensure all relationships (images, external links, slide masters, slide layouts) are correctly resolved and linked within the intermediate representation.
- Continue with other subtasks in Phase 1, focusing on detailed property extraction.
- Update unit tests in `tests/test_slide_parser.py` for new parsing logic.
