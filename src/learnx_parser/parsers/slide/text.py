from learnx_parser.models.core import (
    Paragraph,
    ParagraphProperties,
    RunProperties,
    SlideLayout,
    TextFrame,
    TextRun,
)


def extract_text_frame_properties(
    parser_instance, shape_element, slide_layout_obj: SlideLayout | None
) -> TextFrame:
    # Initialize an empty TextFrame object to store parsed text data
    text_frame = TextFrame()
    # Iterate through all paragraph elements (a:p) within the shape
    for paragraph_element in shape_element.findall(
        ".//a:p", namespaces=parser_instance.nsmap
    ):
        # Extract properties for the current paragraph
        paragraph_object = extract_paragraph_properties(
            parser_instance, paragraph_element, slide_layout_obj
        )
        # Only add the paragraph to the text frame if it contains actual text runs
        if paragraph_object.text_runs:
            text_frame.paragraphs.append(paragraph_object)
    return text_frame


def extract_paragraph_properties(
    parser_instance, paragraph_element, slide_layout_obj: SlideLayout | None
) -> Paragraph:
    # Initialize a Paragraph object to store parsed paragraph data
    paragraph_object = Paragraph()

    # Extract level first, as it's needed for inherited properties
    paragraph_properties_element = paragraph_element.find(
        ".//a:pPr", namespaces=parser_instance.nsmap
    )

    current_level = None
    if (
        paragraph_properties_element is not None
        and paragraph_properties_element.get("lvl") is not None
    ):
        current_level = int(paragraph_properties_element.get("lvl"))
        paragraph_object.properties.level = current_level

    # Get inherited properties from slide layout if available
    if slide_layout_obj and current_level is not None:
        inherited_properties = slide_layout_obj.list_styles.get(current_level)
        if inherited_properties:
            # Create a new ParagraphProperties object by copying inherited properties
            # and then updating with any directly specified properties.
            # This ensures that direct properties override inherited ones.
            paragraph_object.properties = ParagraphProperties(
                align=inherited_properties.align,
                indent=inherited_properties.indent,
                bullet_type=inherited_properties.bullet_type,
                bullet_char=inherited_properties.bullet_char,
                bullet_font_face=inherited_properties.bullet_font_face,
                bullet_size_pct=inherited_properties.bullet_size_pct,
                bullet_size_pts=inherited_properties.bullet_size_pts,
                bullet_auto_num_type=inherited_properties.bullet_auto_num_type,
                bullet_start_at=inherited_properties.bullet_start_at,
                bullet_image_path=inherited_properties.bullet_image_path,
                level=inherited_properties.level,
            )

    # Apply direct properties from the current paragraph's XML, overriding inherited ones
    if paragraph_properties_element is not None:
        if paragraph_properties_element.get("algn") is not None:
            paragraph_object.properties.align = paragraph_properties_element.get("algn")
        if paragraph_properties_element.get("indent") is not None:
            paragraph_object.properties.indent = int(
                paragraph_properties_element.get("indent")
            )
        # Level is already set, no need to re-set it here unless it's explicitly overridden

        bu_none_element = paragraph_properties_element.find(
            ".//a:buNone", namespaces=parser_instance.nsmap
        )
        bu_char_element = paragraph_properties_element.find(
            ".//a:buChar", namespaces=parser_instance.nsmap
        )
        bu_auto_num_element = paragraph_properties_element.find(
            ".//a:buAutoNum", namespaces=parser_instance.nsmap
        )
        bu_blip_element = paragraph_properties_element.find(
            ".//a:buBlip", namespaces=parser_instance.nsmap
        )

        # Only set bullet_type if an explicit bullet element is found, overriding inherited
        if bu_none_element is not None:
            paragraph_object.properties.bullet_type = "none"
        elif bu_char_element is not None:
            paragraph_object.properties.bullet_type = "char"
            paragraph_object.properties.bullet_char = bu_char_element.get("char")
            bu_font_element = paragraph_properties_element.find(
                ".//a:buFont", namespaces=parser_instance.nsmap
            )
            if bu_font_element is not None:
                paragraph_object.properties.bullet_font_face = bu_font_element.get(
                    "typeface"
                )
            bu_sz_pct_element = paragraph_properties_element.find(
                ".//a:buSzPct", namespaces=parser_instance.nsmap
            )
            if bu_sz_pct_element is not None:
                paragraph_object.properties.bullet_size_pct = int(
                    bu_sz_pct_element.get("val")
                )
            bu_sz_pts_element = paragraph_properties_element.find(
                ".//a:buSzPts", namespaces=parser_instance.nsmap
            )
            if bu_sz_pts_element is not None:
                paragraph_object.properties.bullet_size_pts = int(
                    bu_sz_pts_element.get("val")
                )
        elif bu_auto_num_element is not None:
            paragraph_object.properties.bullet_type = "autoNum"
            paragraph_object.properties.bullet_auto_num_type = bu_auto_num_element.get(
                "type"
            )
            if bu_auto_num_element.get("startAt") is not None:
                paragraph_object.properties.bullet_start_at = int(
                    bu_auto_num_element.get("startAt")
                )
        elif bu_blip_element is not None:
            paragraph_object.properties.bullet_type = "blip"
            embed_id = bu_blip_element.find(
                ".//a:blip", namespaces=parser_instance.nsmap
            ).get(
                "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed"
            )
            if embed_id in parser_instance.rels:
                paragraph_object.properties.bullet_image_path = parser_instance.rels[
                    embed_id
                ]

    # Iterate through all run elements (a:r) within the paragraph
    for run_element in paragraph_element.findall(
        ".//a:r", namespaces=parser_instance.nsmap
    ):
        # Find the text element (a:t) within the run
        run_text_element = run_element.find(".//a:t", namespaces=parser_instance.nsmap)
        # If text content exists, extract it and its properties
        if run_text_element is not None and run_text_element.text is not None:
            text_content = run_text_element.text
            run_properties = extract_run_properties(parser_instance, run_element)
            # Append a new TextRun object to the paragraph's text runs
            paragraph_object.text_runs.append(
                TextRun(text=text_content, properties=run_properties)
            )
    return paragraph_object


def extract_run_properties(parser_instance, run_element) -> RunProperties:
    # Initialize a RunProperties object to store parsed run properties
    run_properties = RunProperties()
    # Find the run properties element (a:rPr)
    run_properties_element = run_element.find(
        ".//a:rPr", namespaces=parser_instance.nsmap
    )
    if run_properties_element is not None:
        # Extract font size
        if run_properties_element.get("sz") is not None:
            run_properties.font_size = int(run_properties_element.get("sz"))
        # Extract bold property
        if run_properties_element.get("b") == "1":
            run_properties.bold = True
        # Extract italic property
        if run_properties_element.get("i") == "1":
            run_properties.italic = True

        # Extract color
        solid_fill_element = run_properties_element.find(
            ".//a:solidFill", namespaces=parser_instance.nsmap
        )
        if solid_fill_element is not None:
            srgb_color_element = solid_fill_element.find(
                ".//a:srgbClr", namespaces=parser_instance.nsmap
            )
            if srgb_color_element is not None:
                run_properties.color = srgb_color_element.get("val")
            else:
                scheme_color_element = solid_fill_element.find(
                    ".//a:schemeClr", namespaces=parser_instance.nsmap
                )
                if scheme_color_element is not None:
                    run_properties.scheme_color = scheme_color_element.get("val")

        # Extract font face
        latin_font_element = run_properties_element.find(
            ".//a:latin", namespaces=parser_instance.nsmap
        )
        if latin_font_element is not None:
            run_properties.font_face = latin_font_element.get("typeface")

        # Extract underline
        underline_element = run_properties_element.find(
            ".//a:u", namespaces=parser_instance.nsmap
        )
        if underline_element is not None:
            run_properties.underline = True
    return run_properties
