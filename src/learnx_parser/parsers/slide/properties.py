"""
Property extraction functions for PowerPoint elements.
This module contains functions that extract properties like transforms, fills, and lines.
"""

from learnx_parser.models.core import (
    GradientFill,
    GradientStop,
    Line,
    SolidFill,
    Transform,
)


def extract_transform(parser_instance, element_root) -> Transform:
    """Extract transform properties (position, size, rotation, flip) from an element.

    Args:
        parser_instance: Parser instance with namespace map
        element_root: XML element containing transform information

    Returns:
        Transform: Transform object with extracted properties
    """
    # Initialize a Transform object with default values
    transform = Transform()
    # Find the shape properties element (p:spPr) which contains transform information for shapes
    shape_properties_element = None

    # Check if element_root is already p:spPr
    if (
        element_root.tag
        == "{http://schemas.openxmlformats.org/presentationml/2006/main}spPr"
    ):
        shape_properties_element = element_root
    else:
        shape_properties_element = element_root.find(
            "p:spPr", namespaces=parser_instance.nsmap
        )

    transform_element = None

    # Determine where the transform element (a:xfrm) is located based on the element type
    if shape_properties_element is not None:
        transform_element = shape_properties_element.find(
            "{http://schemas.openxmlformats.org/drawingml/2006/main}xfrm",
            namespaces=parser_instance.nsmap,
        )
    # For graphic frames, the transform element is directly under the graphicFrame element
    elif (
        element_root.tag
        == "{http://schemas.openxmlformats.org/presentationml/2006/main}graphicFrame"
    ):
        transform_element = element_root.find(
            "{http://schemas.openxmlformats.org/drawingml/2006/main}xfrm",
            namespaces=parser_instance.nsmap,
        )

    # If a transform element is found, extract its properties
    if transform_element is not None:
        # Extract offset (x, y position) information
        offset_element = transform_element.find(
            "{http://schemas.openxmlformats.org/drawingml/2006/main}off",
            namespaces=parser_instance.nsmap,
        )
        # Extract extent (width, height) information
        extent_element = transform_element.find(
            "{http://schemas.openxmlformats.org/drawingml/2006/main}ext",
            namespaces=parser_instance.nsmap,
        )
        if offset_element is not None:
            transform.x = int(offset_element.get("x", 0))
            transform.y = int(offset_element.get("y", 0))
        if extent_element is not None:
            transform.cx = int(extent_element.get("cx", 0))
            transform.cy = int(extent_element.get("cy", 0))

        # Extract rotation, horizontal flip, and vertical flip properties
        transform.rot = (
            int(transform_element.get("rot", 0))
            if transform_element.get("rot") is not None
            else 0
        )
        transform.flipH = transform_element.get("flipH", "0") == "1"
        transform.flipV = transform_element.get("flipV", "0") == "1"

    return transform


def extract_fill_properties(parser_instance, shape_properties_element):
    """Extract fill properties (solid, gradient) from a shape properties element.

    Args:
        parser_instance: Parser instance with namespace map
        shape_properties_element: XML element containing fill properties

    Returns:
        SolidFill or GradientFill or None: Fill object with extracted properties
    """
    # Initialize fill to None
    fill = None

    # Check if shape_properties_element is already a solid fill element
    if (
        shape_properties_element.tag
        == "{http://schemas.openxmlformats.org/drawingml/2006/main}solidFill"
    ):
        solid_fill_element = shape_properties_element
    else:
        # Find solid fill element (a:solidFill)
        solid_fill_element = shape_properties_element.find(
            "{http://schemas.openxmlformats.org/drawingml/2006/main}solidFill",
            namespaces=parser_instance.nsmap,
        )
    if solid_fill_element is not None:
        # If solid fill is found, create a SolidFill object
        fill = SolidFill()
        # Extract SRGB color value
        srgb_color_element = solid_fill_element.find(
            "{http://schemas.openxmlformats.org/drawingml/2006/main}srgbClr",
            namespaces=parser_instance.nsmap,
        )
        if srgb_color_element is not None:
            fill.color = srgb_color_element.get("val")
        else:
            # Extract scheme color value if SRGB color is not present
            scheme_color_element = solid_fill_element.find(
                "{http://schemas.openxmlformats.org/drawingml/2006/main}schemeClr",
                namespaces=parser_instance.nsmap,
            )
            if scheme_color_element is not None:
                fill.scheme_color = scheme_color_element.get("val")
    else:
        # If no solid fill, check for gradient fill
        gradient_fill_element = shape_properties_element.find(
            "{http://schemas.openxmlformats.org/drawingml/2006/main}gradFill",
            namespaces=parser_instance.nsmap,
        )
        if gradient_fill_element is not None:
            # If gradient fill is found, create a GradientFill object
            fill = GradientFill()
            # Extract linear gradient properties (angle, scaled)
            linear_element = gradient_fill_element.find(
                "{http://schemas.openxmlformats.org/drawingml/2006/main}lin",
                namespaces=parser_instance.nsmap,
            )
            if linear_element is not None:
                fill.angle = (
                    int(linear_element.get("ang", 0))
                    if linear_element.get("ang") is not None
                    else None
                )
                fill.scaled = linear_element.get("scaled", "0") == "1"

            # Extract gradient stop list
            gradient_stop_list_element = gradient_fill_element.find(
                "{http://schemas.openxmlformats.org/drawingml/2006/main}gsLst",
                namespaces=parser_instance.nsmap,
            )
            if gradient_stop_list_element is not None:
                # Iterate through each gradient stop
                for gradient_stop_element in gradient_stop_list_element.findall(
                    "{http://schemas.openxmlformats.org/drawingml/2006/main}gs",
                    namespaces=parser_instance.nsmap,
                ):
                    position = int(gradient_stop_element.get("pos", 0))
                    stop_color = None
                    stop_scheme_color = None
                    # Extract SRGB color for the stop
                    srgb_color_element = gradient_stop_element.find(
                        "{http://schemas.openxmlformats.org/drawingml/2006/main}srgbClr",
                        namespaces=parser_instance.nsmap,
                    )
                    if srgb_color_element is not None:
                        stop_color = srgb_color_element.get("val")
                    else:
                        # Extract scheme color for the stop
                        scheme_color_element = gradient_stop_element.find(
                            "{http://schemas.openxmlformats.org/drawingml/2006/main}schemeClr",
                            namespaces=parser_instance.nsmap,
                        )
                        if scheme_color_element is not None:
                            stop_scheme_color = scheme_color_element.get("val")
                    # Append the gradient stop to the list
                    fill.stops.append(
                        GradientStop(
                            pos=position,
                            color=stop_color,
                            scheme_color=stop_scheme_color,
                        )
                    )

    return fill


def extract_line_properties(parser_instance, shape_properties_element):
    """Extract line properties (border, outline) from a shape properties element.

    Args:
        parser_instance: Parser instance with namespace map
        shape_properties_element: XML element containing line properties

    Returns:
        Line or None: Line object with extracted properties
    """
    # Find line element (a:ln)
    line_element = shape_properties_element.find(
        "{http://schemas.openxmlformats.org/drawingml/2006/main}ln",
        namespaces=parser_instance.nsmap,
    )
    if line_element is not None:
        # If line is found, create a Line object
        line = Line()
        # Extract line width
        line.width = (
            int(line_element.get("w", 0)) if line_element.get("w") is not None else 0
        )
        # Extract line color
        solid_fill_element = line_element.find(
            "{http://schemas.openxmlformats.org/drawingml/2006/main}solidFill",
            namespaces=parser_instance.nsmap,
        )
        if solid_fill_element is not None:
            srgb_color_element = solid_fill_element.find(
                "{http://schemas.openxmlformats.org/drawingml/2006/main}srgbClr",
                namespaces=parser_instance.nsmap,
            )
            if srgb_color_element is not None:
                line.color = srgb_color_element.get("val")
        return line
    return None
