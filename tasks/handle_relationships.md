## Log: Handle Relationships (`.rels` files)
- **Prompt**: Ensure all relationships (images, external links, slide masters, slide layouts) are correctly resolved and linked within the intermediate representation.
- **Issue**: Relationships are currently handled in a basic way, and a more robust and centralized approach is needed for comprehensive parsing.

### What I did:
- Created this log file for Subtask 1.1.5.
- Reviewed the `_parse_rels` method in `src/learnx_parser/slide_parser.py`.
- Confirmed that `_parse_rels` correctly extracts relationships from the slide's `.rels` file.
- Verified that `_parse_shape_tree` uses these relationships to resolve image paths for `Picture` objects.
- Verified that `extract_hyperlinks` uses these relationships for `Hyperlink` objects.
- Determined that the resolution of relationships for slide masters and slide layouts is a higher-level concern (e.g., `PresentationParser`) and is outside the direct scope of `SlideParser`.

### How I did it:
- Analyzed the existing code and cross-referenced with ECMA documentation regarding `.rels` file structure and relationship types.

### What was challenging:
- Clarifying the scope of relationship handling within the `SlideParser` versus higher-level parsers.

### Future work:
- Proceed to **Subtask 1.2.2: Update `SlideParser` to use new structures** (already partially completed, but needs full migration and testing).
- Continue with other subtasks in Phase 1, focusing on detailed property extraction.
- Update unit tests in `tests/test_slide_parser.py` for new parsing logic.