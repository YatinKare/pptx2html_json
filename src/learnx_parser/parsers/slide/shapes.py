"""
Main shape parsing module that coordinates element parsing.
This module contains the main parse_shape_tree function and imports from focused modules.
"""

from learnx_parser.parsers.slide.elements import (
    parse_graphic_frame_element,
    parse_group_shape_element,
    parse_picture_element,
    parse_shape_element,
)


def parse_shape_tree(parser_instance, shape_tree_root, slide_layout_obj, style_resolver):
    """Parse the shape tree to extract all shapes, pictures, group shapes, and graphic frames.

    Args:
        parser_instance: Parser instance with namespace map and relationships
        shape_tree_root: Root XML element of the shape tree
        slide_layout_obj: Slide layout object for inheritance
        style_resolver: StyleResolver instance for resolving text properties

    Returns:
        tuple: (shapes, pictures, group_shapes, graphic_frames)
    """
    shapes = []
    pictures = []
    group_shapes = []
    graphic_frames = []

    # Parse all child elements in the shape tree
    for element in shape_tree_root:
        element_tag = element.tag

        # Parse shape elements (p:sp)
        if (
            element_tag
            == "{http://schemas.openxmlformats.org/presentationml/2006/main}sp"
        ):
            shape = parse_shape_element(parser_instance, element, slide_layout_obj, style_resolver)
            shapes.append(shape)

        # Parse picture elements (p:pic)
        elif (
            element_tag
            == "{http://schemas.openxmlformats.org/presentationml/2006/main}pic"
        ):
            picture = parse_picture_element(parser_instance, element)
            pictures.append(picture)

        # Parse group shape elements (p:grpSp)
        elif (
            element_tag
            == "{http://schemas.openxmlformats.org/presentationml/2006/main}grpSp"
        ):
            group_shape = parse_group_shape_element(
                parser_instance, element, slide_layout_obj, style_resolver
            )

            # Recursively parse children of the group shape
            child_shape_tree = element
            child_shapes, child_pictures, child_group_shapes, child_graphic_frames = (
                parse_shape_tree(parser_instance, child_shape_tree, slide_layout_obj, style_resolver)
            )

            # Store children in the group shape
            group_shape.children = (
                child_shapes,
                child_pictures,
                child_group_shapes,
                child_graphic_frames,
            )
            group_shapes.append(group_shape)

        # Parse graphic frame elements (p:graphicFrame)
        elif (
            element_tag
            == "{http://schemas.openxmlformats.org/presentationml/2006/main}graphicFrame"
        ):
            graphic_frame = parse_graphic_frame_element(parser_instance, element)
            graphic_frames.append(graphic_frame)

    return shapes, pictures, group_shapes, graphic_frames
