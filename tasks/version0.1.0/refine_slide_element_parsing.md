## Log: Refactor HtmlWriter - Extract _render_shape_html, _render_picture_html, _render_group_shape_html, _render_graphic_frame_html, _get_shape_style_css, _get_paragraph_style_css, and _get_run_style_css

### What I did:
1.  Extracted the HTML rendering logic for `Shape` elements from `write_slide_html` into a new private method `_render_shape_html`. The `write_slide_html` method now calls this new helper method when it encounters a `Shape` element.
2.  Extracted the HTML rendering logic for `Picture` elements from `write_slide_html` into a new private method `_render_picture_html`. The `write_slide_html` method now calls this new helper method when it encounters a `Picture` element.
3.  Extracted the HTML rendering logic for `GroupShape` elements from `write_slide_html` into a new private method `_render_group_shape_html`. The `write_slide_html` method now calls this new helper method when it encounters a `GroupShape` element.
4.  Extracted the HTML rendering logic for `GraphicFrame` elements from `write_slide_html` into a new private method `_render_graphic_frame_html`. The `write_slide_html` method now calls this new helper method when it encounters a `GraphicFrame` element.
5.  Extracted the CSS styling logic for `Shape` elements from `_render_shape_html` into a new private method `_get_shape_style_css`. The `_render_shape_html` method now calls this new helper method to get the shape style CSS.
6.  Extracted the CSS styling logic for `Paragraph` elements from `_render_shape_html` into a new private method `_get_paragraph_style_css`. The `_render_shape_html` method now calls this new helper method to get the paragraph style CSS.
7.  Extracted the CSS styling logic for `Run` elements from `_render_shape_html` into a new private method `_get_run_style_css`. The `_render_shape_html` method now calls this new helper method to get the run style CSS.

### How I did it:
1.  Identified the block of code within `write_slide_html` responsible for rendering `Shape` elements.
2.  Moved this code into a new method `_render_shape_html` within the `HtmlWriter` class, which takes a `Shape` object as an argument.
3.  Modified `write_slide_html` to call `self._render_shape_html(element)` when `element` is an instance of `Shape`.
4.  Identified the block of code within `write_slide_html` responsible for rendering `Picture` elements.
5.  Moved this code into a new method `_render_picture_html` within the `HtmlWriter` class, which takes a `Picture` object as an argument.
6.  Modified `write_slide_html` to call `self._render_picture_html(element)` when `element` is an instance of `Picture`.
7.  Identified the block of code within `write_slide_html` responsible for rendering `GroupShape` elements.
8.  Moved this code into a new method `_render_group_shape_html` within the `HtmlWriter` class, which takes a `GroupShape` object as an argument.
9.  Modified `write_slide_html` to call `self._render_group_shape_html(element)` when `element` is an instance of `GroupShape`.
10. Identified the block of code within `write_slide_html` responsible for rendering `GraphicFrame` elements.
11. Moved this code into a new method `_render_graphic_frame_html` within the `HtmlWriter` class, which takes a `GraphicFrame` object as an argument.
12. Modified `write_slide_html` to call `self._render_graphic_frame_html(element)` when `element` is an instance of `GraphicFrame`.
13. Identified the block of code within `_render_shape_html` responsible for generating shape style CSS.
14. Moved this code into a new method `_get_shape_style_css` within the `HtmlWriter` class, which takes a `Shape` object as an argument.
15. Modified `_render_shape_html` to call `self._get_shape_style_css(element)` and assign the returned CSS string to `shape_style`.
16. Identified the block of code within `_render_shape_html` responsible for generating paragraph style CSS.
17. Moved this code into a new method `_get_paragraph_style_css` within the `HtmlWriter` class, which takes a `Paragraph` object as an argument.
18. Modified `_render_shape_html` to call `self._get_paragraph_style_css(paragraph)` and assign the returned CSS string to `paragraph_style`.
19. Identified the block of code within `_render_shape_html` responsible for generating run style CSS.
20. Moved this code into a new method `_get_run_style_css` within the `HtmlWriter` class, which takes a `TextRun` object as an argument.
21. Modified `_render_shape_html` to call `self._get_run_style_css(run)` and assign the returned CSS string to `run_style`.
22. Ran existing unit tests (`uv run pytest tests/test_html_writer.py`) to ensure no regressions were introduced.

### What was challenging:
None for this step.

### Future work:
Continue refactoring `html_writer.py` to improve modularity and readability.