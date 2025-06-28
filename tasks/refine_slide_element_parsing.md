## Log: Refactor _parse_shape_element - Extract _extract_fill_properties and _extract_line_properties

### What I did:
1.  Extracted the logic for parsing fill properties (solid and gradient fills) from `_parse_shape_element` into a new private method `_extract_fill_properties`. The `_parse_shape_element` method now calls this new helper method to get the fill object.
2.  Extracted the logic for parsing line properties from `_parse_shape_element` into a new private method `_extract_line_properties`. The `_parse_shape_element` method now calls this new helper method to get the line object.

### How I did it:
1.  Identified the block of code within `_parse_shape_element` responsible for extracting fill properties.
2.  Moved this code into a new method `_extract_fill_properties` within the `SlideParser` class, which takes the `sp_pr_element` as an argument.
3.  Modified `_parse_shape_element` to call `self._extract_fill_properties(sp_pr)` and assign the returned fill object to the `fill` variable.
4.  Identified the block of code within `_parse_shape_element` responsible for extracting line properties.
5.  Moved this code into a new method `_extract_line_properties` within the `SlideParser` class, which takes the `sp_pr_element` as an argument.
6.  Modified `_parse_shape_element` to call `self._extract_line_properties(sp_pr)` and assign the returned line object to the `line` variable.
7.  Ran existing unit tests (`uv run pytest tests/test_slide_parser.py`) to ensure no regressions were introduced.

### What was challenging:
None for this step.

### Future work:
Continue refactoring `slide_parser.py` by extracting helper methods for parsing text frame properties and run properties.