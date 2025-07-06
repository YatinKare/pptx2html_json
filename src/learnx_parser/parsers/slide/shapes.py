from learnx_parser.models.core import (
    BlipFill,
    GradientFill,
    GradientStop,
    GraphicFrame,
    GroupShape,
    Line,
    Picture,
    Shape,
    SlideLayout,
    SolidFill,
    TextFrame,
    Transform,
)


def extract_transform(parser_instance, element_root) -> Transform:
    # Initialize a Transform object with default values
    transform = Transform()
    # Find the shape properties element (p:spPr) which contains transform information for shapes
    shape_properties_element = None
    
    # Check if element_root is already p:spPr
    if element_root.tag == "{http://schemas.openxmlformats.org/presentationml/2006/main}spPr":
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
    # Initialize fill to None
    fill = None
    
    # Check if shape_properties_element is already a solid fill element
    if shape_properties_element.tag == "{http://schemas.openxmlformats.org/drawingml/2006/main}solidFill":
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
            gradient_fill = GradientFill()
            # Extract linear gradient properties (angle, scaled)
            linear_element = gradient_fill_element.find(
                "{http://schemas.openxmlformats.org/drawingml/2006/main}lin",
                namespaces=parser_instance.nsmap,
            )
            if linear_element is not None:
                gradient_fill.angle = (
                    int(linear_element.get("ang", 0))
                    if linear_element.get("ang") is not None
                    else None
                )
                gradient_fill.scaled = linear_element.get("scaled", "0") == "1"

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
                    gradient_fill.stops.append(
                        GradientStop(
                            pos=position,
                            color=stop_color,
                            scheme_color=stop_scheme_color,
                        )
                    )
            fill = gradient_fill
    return fill


def extract_line_properties(parser_instance, shape_properties_element):
    # Initialize line to None
    line = None
    # Find the line element (a:ln) within the shape properties
    line_element = shape_properties_element.find(
        "{http://schemas.openxmlformats.org/drawingml/2006/main}ln",
        namespaces=parser_instance.nsmap,
    )
    if line_element is not None:
        # If a line element is found, create a Line object
        line = Line()
        # Extract line width, cap type, compound type, and alignment
        line.width = int(line_element.get("w", 0))
        line.cap = line_element.get("cap")
        line.cmpd = line_element.get("cmpd")
        line.algn = line_element.get("algn")

        # Extract solid fill properties for the line (color)
        solid_fill_element = line_element.find(
            "{http://schemas.openxmlformats.org/drawingml/2006/main}solidFill",
            namespaces=parser_instance.nsmap,
        )
        if solid_fill_element is not None:
            # Extract SRGB color value
            srgb_color_element = solid_fill_element.find(
                "{http://schemas.openxmlformats.org/drawingml/2006/main}srgbClr",
                namespaces=parser_instance.nsmap,
            )
            if srgb_color_element is not None:
                line.color = srgb_color_element.get("val")
            else:
                # Extract scheme color value if SRGB color is not present
                scheme_color_element = solid_fill_element.find(
                    "{http://schemas.openxmlformats.org/drawingml/2006/main}schemeClr",
                    namespaces=parser_instance.nsmap,
                )
                if scheme_color_element is not None:
                    line.scheme_color = scheme_color_element.get("val")
    return line


def parse_shape_element(
    parser_instance, shape_element, slide_layout_obj: SlideLayout | None
) -> Shape:
    # Extract the shape's ID and name from its properties
    shape_id = shape_element.find(
        "{http://schemas.openxmlformats.org/presentationml/2006/main}nvSpPr/{http://schemas.openxmlformats.org/presentationml/2006/main}cNvPr",
        namespaces=parser_instance.nsmap,
    ).get("id")
    shape_name = shape_element.find(
        "{http://schemas.openxmlformats.org/presentationml/2006/main}nvSpPr/{http://schemas.openxmlformats.org/presentationml/2006/main}cNvPr",
        namespaces=parser_instance.nsmap,
    ).get("name")

    # Extract placeholder information if the shape is a placeholder
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
    ph_orient = (
        placeholder_element.get("orient") if placeholder_element is not None else None
    )
    ph_sz = placeholder_element.get("sz") if placeholder_element is not None else None

    # Extract the transform properties (position, size, rotation, flip) of the shape
    transform = extract_transform(parser_instance, shape_element)
    fill = None
    line = None
    text_frame = TextFrame()
    preset_geometry_value = None

    # Find the shape properties element (p:spPr) which contains fill, line, and geometry information
    shape_properties_element = shape_element.find(
        "{http://schemas.openxmlformats.org/presentationml/2006/main}spPr",
        namespaces=parser_instance.nsmap,
    )
    if shape_properties_element is not None:
        # Extract geometry information (e.g., rectangle, oval, custom shape)
        preset_geometry = shape_properties_element.find(
            "{http://schemas.openxmlformats.org/drawingml/2006/main}prstGeom",
            namespaces=parser_instance.nsmap,
        )
        if preset_geometry is not None:
            preset_geometry_value = preset_geometry.get("prst")

        # Extract fill properties (solid color, gradient, etc.)
        fill = extract_fill_properties(parser_instance, shape_properties_element)

        # Extract line properties (border, outline)
        line = extract_line_properties(parser_instance, shape_properties_element)

    # Extract text frame properties if the shape contains text
    from learnx_parser.parsers.slide.text import extract_text_frame_properties

    text_frame = extract_text_frame_properties(
        parser_instance, shape_element, slide_layout_obj
    )

    # Return a new Shape object populated with the extracted data
    return Shape(
        type="shape",
        id=shape_id,
        name=shape_name,
        transform=transform,
        prst_geom=preset_geometry_value,
        fill=fill,
        line=line,
        text_frame=text_frame,
        ph_type=ph_type,
        ph_idx=ph_idx,
        ph_orient=ph_orient,
        ph_sz=ph_sz,
    )


def parse_picture_element(parser_instance, picture_element) -> Picture:
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

    # Return a new Picture object populated with the extracted data
    return Picture(
        id=picture_id,
        name=picture_name,
        path=picture_path,
        transform=transform,
        blip_fill=blip_fill_object,
        ph_type=ph_type,
        ph_idx=ph_idx,
    )


def parse_group_shape_element(
    parser_instance, group_shape_element, slide_layout_obj: SlideLayout | None
) -> GroupShape:
    # Extract the group shape's ID and name
    group_id = group_shape_element.find(
        "{http://schemas.openxmlformats.org/presentationml/2006/main}nvGrpSpPr/{http://schemas.openxmlformats.org/presentationml/2006/main}cNvPr",
        namespaces=parser_instance.nsmap,
    ).get("id")
    group_name = group_shape_element.find(
        "{http://schemas.openxmlformats.org/presentationml/2006/main}nvGrpSpPr/{http://schemas.openxmlformats.org/presentationml/2006/main}cNvPr",
        namespaces=parser_instance.nsmap,
    ).get("name")

    # Determine if the group shape is a flex container based on its name
    is_flex_container = False
    if group_name and "flex-container" in group_name:
        is_flex_container = True

    # Extract the transform properties of the group shape
    transform = extract_transform(parser_instance, group_shape_element)
    # Recursively parse child shapes within the group shape
    shapes, pictures, group_shapes, graphic_frames = parse_shape_tree(
        parser_instance, group_shape_element, slide_layout_obj
    )
    # Return a new GroupShape object populated with the extracted data and its children
    return GroupShape(
        id=group_id,
        name=group_name,
        transform=transform,
        children=(shapes, pictures, group_shapes, graphic_frames),
        is_flex_container=is_flex_container,
    )


def parse_graphic_frame_element(parser_instance, graphic_frame_element) -> GraphicFrame:
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
    # Return a new GraphicFrame object populated with the extracted data
    return GraphicFrame(
        id=graphic_frame_id, name=graphic_frame_name, transform=transform
    )


def parse_shape_tree(
    parser_instance, shape_tree_root, slide_layout_obj: SlideLayout | None
):
    # Initialize lists to store different types of elements found in the shape tree
    shapes = []
    pictures = []
    group_shapes = []
    graphic_frames = []

    # Iterate through each child element within the shape tree root
    for child_element in shape_tree_root:
        # Check the tag of the child element to determine its type and parse accordingly
        if (
            child_element.tag
            == "{http://schemas.openxmlformats.org/presentationml/2006/main}sp"
        ):
            # Parse a regular shape element
            shape = parse_shape_element(
                parser_instance, child_element, slide_layout_obj
            )
            shapes.append(shape)

        elif (
            child_element.tag
            == "{http://schemas.openxmlformats.org/presentationml/2006/main}pic"
        ):
            # Parse a picture element
            picture = parse_picture_element(parser_instance, child_element)
            pictures.append(picture)

        elif (
            child_element.tag
            == "{http://schemas.openxmlformats.org/presentationml/2006/main}grpSp"
        ):
            # Parse a group shape element (which can contain other shapes)
            group_shape = parse_group_shape_element(
                parser_instance, child_element, slide_layout_obj
            )
            group_shapes.append(group_shape)

        elif (
            child_element.tag
            == "{http://schemas.openxmlformats.org/presentationml/2006/main}graphicFrame"
        ):
            # Parse a graphic frame element (e.g., charts, tables)
            graphic_frame = parse_graphic_frame_element(parser_instance, child_element)
            graphic_frames.append(graphic_frame)
    # Return the categorized lists of parsed elements
    return shapes, pictures, group_shapes, graphic_frames
