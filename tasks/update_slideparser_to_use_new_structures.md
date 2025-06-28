## Log: Update SlideParser to use new structures
- **Prompt**: Update `SlideParser` to use new data structures.
- **Issue**: Previous dictionary-based data structure was unwieldy.

### What I did:
- Updated `src/learnx_parser/slide_parser.py` to use the newly defined dataclasses (`Transform`, `SolidFill`, `Line`, `TextFrame`, `Paragraph`, `ParagraphProperties`, `TextRun`, `RunProperties`, `Shape`, `Picture`, `GroupShape`, `GraphicFrame`, `Hyperlink`, `CommonSlideData`, `Slide`).
- Modified `_parse_shape_tree` to return separate lists for different shape types (`shapes`, `pictures`, `group_shapes`, `graphic_frames`).
- Updated `parse_slide` to construct and return a `Slide` object.
- Updated `extract_hyperlinks` to return a list of `Hyperlink` objects.
- Initialized `prst_geom_val` to `None` to prevent `UnboundLocalError`.
- Corrected the return statement in `_parse_shape_tree` to return all four lists.
- Updated `tests/test_slide_parser.py` to use the new dataclass structure for assertions and removed the `background_color` assertion.

### How I did it:
- Refactored `SlideParser` methods to create and populate instances of the new dataclasses.
- Adjusted return types and variable assignments to match the new structure.
- Updated test assertions to access properties via dot notation on dataclass instances.

### What was challenging:
- Migrating from dictionary-based data to a structured dataclass model required careful refactoring across multiple methods.
- Ensuring all relevant data was correctly mapped to the new dataclass fields.

### Future work:
- **Subtask 1.1.4.1: Paragraph Properties (`a:pPr`)**: Extract alignment, indentation, spacing, and bullet/numbering properties.
- Continue with other subtasks in Phase 1, focusing on detailed property extraction.
- Update unit tests in `tests/test_slide_parser.py` for new parsing logic.
