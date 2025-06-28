## Log: Refactor _parse_shape_element - Extract _extract_fill_properties

### What I did:
Extracted the logic for parsing fill properties (solid and gradient fills) from `_parse_shape_element` into a new private method `_extract_fill_properties`. The `_parse_shape_element` method now calls this new helper method to get the fill object.

### How I did it:
1.  Identified the block of code within `_parse_shape_element` responsible for extracting fill properties.
2.  Moved this code into a new method `_extract_fill_properties` within the `SlideParser` class, which takes the `sp_pr_element` as an argument.
3.  Modified `_parse_shape_element` to call `self._extract_fill_properties(sp_pr)` and assign the returned fill object to the `fill` variable.
4.  Ran existing unit tests (`uv run pytest tests/test_slide_parser.py`) to ensure no regressions were introduced.

### What was challenging:
None for this step.

### Future work:
Continue refactoring `slide_parser.py` by extracting helper methods for parsing line properties, text frame properties, and run properties.