# Task 1.1.2: Implement basic heuristic for "title + image-left + text-right" layout within `_render_slide_content`

**Status:** Completed

**Description:**
Implemented a basic layout inference heuristic within the `_render_slide_content` method in `src/learnx_parser/html_writer.py`. This heuristic identifies the title, main image, and body text based on their placeholder types and relative x-coordinates. If an image is to the left of the body text, a flexbox container is generated to arrange them side-by-side.
