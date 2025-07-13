"""
Element parsing functions for PowerPoint slide elements.
This module contains functions that parse individual elements like shapes, pictures, and groups.
"""

from learnx_parser.models.core import (
    BlipFill,
    GraphicFrame,
    GroupShape,
    Picture,
    Shape,
)
from learnx_parser.parsers.slide.properties import (
    extract_fill_properties,
    extract_line_properties,
    extract_transform,
)


def parse_shape_element(parser_instance, shape_element, slide_layout_obj) -> Shape:
    """Parse a shape element from XML to Shape object.

    Args:
        parser_instance: Parser instance with namespace map and relationships
        shape_element: XML element containing shape data
        slide_layout_obj: Slide layout object for inheritance

    Returns:
        Shape: Parsed shape object
    """
    # Extract the shape's ID and name from its properties
    shape_id = shape_element.find(
        "{http://schemas.openxmlformats.org/presentationml/2006/main}nvSpPr/{http://schemas.openxmlformats.org/presentationml/2006/main}cNvPr",
        namespaces=parser_instance.nsmap,
    ).get("id")
    shape_name = shape_element.find(
        "{http://schemas.openxmlformats.org/presentationml/2006/main}nvSpPr/{http://schemas.openxmlformats.org/presentationml/2006/main}cNvPr",
        namespaces=parser_instance.nsmap,
    ).get("name")

    # Extract placeholder information for shapes if it's a placeholder
    placeholder_element = shape_element.find(
        "{http://schemas.openxmlformats.org/presentationml/2006/main}nvSpPr/{http://schemas.openxmlformats.org/presentationml/2006/main}nvPr/{http://schemas.openxmlformats.org/presentationml/2006/main}ph",
        namespaces=parser_instance.nsmap,
    )
    ph_type = (
        placeholder_element.get("type") if placeholder_element is not None else None
    )
    ph_idx = (
        int(placeholder_element.get("idx"))
        if placeholder_element is not None
        and placeholder_element.get("idx") is not None
        else None
    )

    # Extract the transform properties (position, size, rotation, flip) of the shape
    transform = extract_transform(parser_instance, shape_element)

    # Extract shape properties (fill, line, geometry)
    shape_properties_element = shape_element.find(
        "{http://schemas.openxmlformats.org/presentationml/2006/main}spPr",
        namespaces=parser_instance.nsmap,
    )
    fill = None
    line = None
    prst_geom = None
    if shape_properties_element is not None:
        # Extract fill properties
        fill = extract_fill_properties(parser_instance, shape_properties_element)
        # Extract line properties
        line = extract_line_properties(parser_instance, shape_properties_element)
        # Extract preset geometry
        prst_geom_element = shape_properties_element.find(
            "{http://schemas.openxmlformats.org/drawingml/2006/main}prstGeom",
            namespaces=parser_instance.nsmap,
        )
        if prst_geom_element is not None:
            prst_geom = prst_geom_element.get("prst")

    # Extract text frame if present
    text_frame = None
    text_body_element = shape_element.find(
        "{http://schemas.openxmlformats.org/presentationml/2006/main}txBody",
        namespaces=parser_instance.nsmap,
    )
    if text_body_element is not None:
        from learnx_parser.parsers.slide.text import extract_text_frame_properties

        text_frame = extract_text_frame_properties(
            parser_instance, shape_element, slide_layout_obj, ph_type
        )

    return Shape(
        type="shape",
        id=shape_id,
        name=shape_name,
        ph_type=ph_type,
        ph_idx=ph_idx,
        transform=transform,
        fill=fill,
        line=line,
        prst_geom=prst_geom,
        text_frame=text_frame,
    )


def parse_picture_element(parser_instance, picture_element) -> Picture:
    """Parse a picture element from XML to Picture object.

    Args:
        parser_instance: Parser instance with namespace map and relationships
        picture_element: XML element containing picture data

    Returns:
        Picture: Parsed picture object
    """
    # Extract the picture's ID and name from its properties
    picture_id = picture_element.find(
        "{http://schemas.openxmlformats.org/presentationml/2006/main}nvPicPr/{http://schemas.openxmlformats.org/presentationml/2006/main}cNvPr",
        namespaces=parser_instance.nsmap,
    ).get("id")
    picture_name = picture_element.find(
        "{http://schemas.openxmlformats.org/presentationml/2006/main}nvPicPr/{http://schemas.openxmlformats.org/presentationml/2006/main}cNvPr",
        namespaces=parser_instance.nsmap,
    ).get("name")
    picture_path = ""

    # Extract placeholder information for pictures if it's a placeholder
    placeholder_element = picture_element.find(
        "{http://schemas.openxmlformats.org/presentationml/2006/main}nvPicPr/{http://schemas.openxmlformats.org/presentationml/2006/main}nvPr/{http://schemas.openxmlformats.org/presentationml/2006/main}ph",
        namespaces=parser_instance.nsmap,
    )
    ph_type = (
        placeholder_element.get("type") if placeholder_element is not None else None
    )
    ph_idx = (
        int(placeholder_element.get("idx"))
        if placeholder_element is not None
        and placeholder_element.get("idx") is not None
        else None
    )

    # Extract the transform properties (position, size, rotation, flip) of the picture
    transform = extract_transform(parser_instance, picture_element)

    # Find the blip element (a:blip) which contains the relationship ID to the image file
    blip_element = picture_element.find(
        ".//{http://schemas.openxmlformats.org/drawingml/2006/main}blip",
        namespaces=parser_instance.nsmap,
    )
    if blip_element is not None:
        embed_id = blip_element.get(
            "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed"
        )
        # Resolve the image path using the relationship ID
        if embed_id in parser_instance.rels:
            picture_path = parser_instance.rels[embed_id]

    # Find the blip fill element (p:blipFill) which contains image fill properties like cropping
    blip_fill_element = picture_element.find(
        "{http://schemas.openxmlformats.org/presentationml/2006/main}blipFill",
        namespaces=parser_instance.nsmap,
    )
    blip_fill_object = None
    if blip_fill_element is not None:
        # Extract whether the image rotates with the shape
        rotate_with_shape = blip_fill_element.get("rotWithShape", "0") == "1"
        blip_fill_object = BlipFill(path=picture_path, rot_with_shape=rotate_with_shape)

        # Extract source rectangle (cropping) information
        source_rectangle_element = blip_fill_element.find(
            "{http://schemas.openxmlformats.org/drawingml/2006/main}srcRect",
            namespaces=parser_instance.nsmap,
        )
        if source_rectangle_element is not None:
            blip_fill_object.src_rect_t = (
                int(source_rectangle_element.get("t"))
                if source_rectangle_element.get("t") is not None
                else None
            )
            blip_fill_object.src_rect_b = (
                int(source_rectangle_element.get("b"))
                if source_rectangle_element.get("b") is not None
                else None
            )
            blip_fill_object.src_rect_l = (
                int(source_rectangle_element.get("l"))
                if source_rectangle_element.get("l") is not None
                else None
            )
            blip_fill_object.src_rect_r = (
                int(source_rectangle_element.get("r"))
                if source_rectangle_element.get("r") is not None
                else None
            )

    return Picture(
        id=picture_id,
        name=picture_name,
        path=picture_path,
        ph_type=ph_type,
        ph_idx=ph_idx,
        transform=transform,
        blip_fill=blip_fill_object,
    )


def parse_group_shape_element(
    parser_instance, group_shape_element, slide_layout_obj
) -> GroupShape:
    """Parse a group shape element from XML to GroupShape object.

    Args:
        parser_instance: Parser instance with namespace map and relationships
        group_shape_element: XML element containing group shape data
        slide_layout_obj: Slide layout object for inheritance

    Returns:
        GroupShape: Parsed group shape object
    """
    # Extract the group shape's ID and name from its properties
    group_shape_id = group_shape_element.find(
        "{http://schemas.openxmlformats.org/presentationml/2006/main}nvGrpSpPr/{http://schemas.openxmlformats.org/presentationml/2006/main}cNvPr",
        namespaces=parser_instance.nsmap,
    ).get("id")
    group_shape_name = group_shape_element.find(
        "{http://schemas.openxmlformats.org/presentationml/2006/main}nvGrpSpPr/{http://schemas.openxmlformats.org/presentationml/2006/main}cNvPr",
        namespaces=parser_instance.nsmap,
    ).get("name")

    # Extract the transform properties of the group shape
    transform = extract_transform(parser_instance, group_shape_element)

    # Determine if this is a flex container by checking the name
    is_flex_container = "flex-container" in (group_shape_name or "").lower()

    return GroupShape(
        id=group_shape_id,
        name=group_shape_name,
        transform=transform,
        is_flex_container=is_flex_container,
        children=(
            [],
            [],
            [],
            [],
        ),  # Initialize empty children (shapes, pictures, group_shapes, graphic_frames)
    )


def parse_graphic_frame_element(parser_instance, graphic_frame_element) -> GraphicFrame:
    """Parse a graphic frame element from XML to GraphicFrame object.

    Args:
        parser_instance: Parser instance with namespace map and relationships
        graphic_frame_element: XML element containing graphic frame data

    Returns:
        GraphicFrame: Parsed graphic frame object
    """
    # Extract the graphic frame's ID and name
    graphic_frame_id = graphic_frame_element.find(
        "{http://schemas.openxmlformats.org/presentationml/2006/main}nvGraphicFramePr/{http://schemas.openxmlformats.org/presentationml/2006/main}cNvPr",
        namespaces=parser_instance.nsmap,
    ).get("id")
    graphic_frame_name = graphic_frame_element.find(
        "{http://schemas.openxmlformats.org/presentationml/2006/main}nvGraphicFramePr/{http://schemas.openxmlformats.org/presentationml/2006/main}cNvPr",
        namespaces=parser_instance.nsmap,
    ).get("name")

    # Extract the transform properties of the graphic frame
    transform = extract_transform(parser_instance, graphic_frame_element)

    return GraphicFrame(
        id=graphic_frame_id, name=graphic_frame_name, transform=transform
    )
