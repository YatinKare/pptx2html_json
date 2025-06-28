## Log: Refactor _extract_paragraph_properties - Extract _extract_run_properties

### What I did:
1.  Extracted the logic for parsing run properties from `_extract_paragraph_properties` into a new private method `_extract_run_properties`. The `_extract_paragraph_properties` method now calls this new helper method to get the run properties object.

### How I did it:
1.  Identified the block of code within `_extract_paragraph_properties` responsible for extracting run properties.
2.  Moved this code into a new method `_extract_run_properties` within the `SlideParser` class, which takes the `r_tag` as an argument.
3.  Modified `_extract_paragraph_properties` to call `self._extract_run_properties(r_tag)` and assign the returned run properties object to the `run_properties` variable.
4.  Ran existing unit tests (`uv run pytest tests/test_slide_parser.py`) to ensure no regressions were introduced.

### What was challenging:
I initially attempted to replace the code before defining the new method, leading to a `replace` tool failure. I corrected this by first defining the `_extract_run_properties` method and then replacing the inline code with a call to it.

### Future work:
Continue refactoring `slide_parser.py` to improve modularity and readability.