# `text.py` Documentation

This module contains functions responsible for parsing text-related elements within a PowerPoint slide, specifically text frames, paragraphs, and text runs. It handles the extraction of text content and its associated formatting properties.

## Functions

### `extract_text_frame_properties(parser_instance, shape_element, slide_layout_obj: SlideLayout | None) -> TextFrame`
Extracts text frame properties from a shape element, including all paragraphs and their text runs. It takes a `parser_instance` to access `nsmap` and other helper functions.

### `extract_paragraph_properties(parser_instance, paragraph_element, slide_layout_obj: SlideLayout | None) -> Paragraph`
Extracts paragraph properties, including alignment, indentation, and bullet point information. It also handles inherited properties from slide layouts. It takes a `parser_instance` to access `nsmap` and `rels`.

### `extract_run_properties(parser_instance, run_element) -> RunProperties`
Extracts text run properties such as font size, bold, italic, color, and font face. It takes a `parser_instance` to access `nsmap`.
