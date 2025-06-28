## Log: Refactor _extract_text_frame_properties - Extract _extract_paragraph_properties

### What I did:
1.  Extracted the logic for parsing paragraph properties from `_extract_text_frame_properties` into a new private method `_extract_paragraph_properties`. The `_extract_text_frame_properties` method now calls this new helper method to get the paragraph object.

### How I did it:
1.  Identified the block of code within `_extract_text_frame_properties` responsible for extracting paragraph properties.
2.  Moved this code into a new method `_extract_paragraph_properties` within the `SlideParser` class, which takes the `p_tag` as an argument.
3.  Modified `_extract_text_frame_properties` to call `self._extract_paragraph_properties(p_tag)` and append the returned paragraph object to the `text_frame.paragraphs` list.
4.  Ran existing unit tests (`uv run pytest tests/test_slide_parser.py`) to ensure no regressions were introduced.

### What was challenging:
None for this step.

### Future work:
Continue refactoring `slide_parser.py` by extracting helper methods for parsing run properties.