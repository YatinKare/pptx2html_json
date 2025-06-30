# Task 1.2.5: Update calls to rendering functions in `write_slide_html` to pass `0, 0` for top-level elements

**Status:** Completed

**Description:**
Modified the `write_slide_html` method in `src/learnx_parser/html_writer.py` to pass `0` for both `parent_x` and `parent_y` when calling the rendering functions for top-level elements (shapes, pictures, group shapes, graphic frames). This ensures that top-level elements are positioned absolutely relative to the slide container.
