# `shapes.py` Documentation

This module contains functions responsible for parsing various shape-related elements within a PowerPoint slide, including shapes, pictures, group shapes, and graphic frames. It also handles the extraction of transform, fill, and line properties common to these elements.

## Functions

### `extract_transform(parser_instance, element_root) -> Transform`
Extracts the position, size, rotation, and flip transformations from an XML element. It takes a `parser_instance` to access `nsmap`.

### `extract_fill_properties(parser_instance, shape_properties_element)`
Extracts fill properties (solid, gradient) from a shape's properties element. It takes a `parser_instance` to access `nsmap`.

### `extract_line_properties(parser_instance, shape_properties_element)`
Extracts line (border) properties from a shape's properties element. It takes a `parser_instance` to access `nsmap`.

### `parse_shape_element(parser_instance, shape_element, slide_layout_obj: SlideLayout | None) -> Shape`
Parses a single shape element, extracting its ID, name, placeholder information, transform, fill, line, and text frame properties. It takes a `parser_instance` to access `nsmap` and other helper functions.

### `parse_picture_element(parser_instance, picture_element) -> Picture`
Parses a single picture element, extracting its ID, name, path, transform, and blip fill properties. It takes a `parser_instance` to access `nsmap` and `rels`.

### `parse_group_shape_element(parser_instance, group_shape_element) -> GroupShape`
Parses a group shape element, extracting its ID, name, transform, and recursively parsing its child elements. It takes a `parser_instance` to access `nsmap`.

### `parse_graphic_frame_element(parser_instance, graphic_frame_element) -> GraphicFrame`
Parses a graphic frame element, extracting its ID, name, and transform properties. It takes a `parser_instance` to access `nsmap`.

### `parse_shape_tree(parser_instance, shape_tree_root, slide_layout_obj: SlideLayout | None)`
Recursively parses the shape tree of a slide, categorizing and extracting all shapes, pictures, group shapes, and graphic frames. It takes a `parser_instance` to access `nsmap` and other helper functions.
