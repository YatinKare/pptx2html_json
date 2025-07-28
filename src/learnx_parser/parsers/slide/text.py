from learnx_parser.models.core import (
    Paragraph,
    ParagraphProperties,
    RunProperties,
    SlideLayout,
    TextFrame,
    TextRun,
)


def extract_text_frame_properties(
    parser_instance,
    shape_element,
    slide_layout_obj: SlideLayout | None,
    ph_type: str | None = None,
    style_resolver=None,
) -> TextFrame:
    # Initialize an empty TextFrame object to store parsed text data
    text_frame = TextFrame()

    # Parse bodyPr element according to OpenXML inheritance standards
    body_pr_element = shape_element.find(
        ".//a:bodyPr", namespaces=parser_instance.nsmap
    )

    # Parse anchor (vertical alignment) with proper inheritance
    text_frame.anchor = _parse_anchor_with_inheritance(
        body_pr_element, slide_layout_obj, ph_type
    )

    # Parse anchorCtr (horizontal centering) with proper inheritance
    text_frame.anchor_ctr = _parse_anchor_ctr_with_inheritance(
        body_pr_element, slide_layout_obj, ph_type
    )

    # Parse insets with OpenXML defaults (45720 EMUs = 0.05 inches)
    text_frame.left_inset = _parse_inset_with_inheritance(body_pr_element, "lIns")
    text_frame.top_inset = _parse_inset_with_inheritance(body_pr_element, "tIns")
    text_frame.right_inset = _parse_inset_with_inheritance(body_pr_element, "rIns")
    text_frame.bottom_inset = _parse_inset_with_inheritance(body_pr_element, "bIns")

    # Iterate through all paragraph elements (a:p) within the shape
    for paragraph_element in shape_element.findall(
        ".//a:p", namespaces=parser_instance.nsmap
    ):
        # Extract properties for the current paragraph
        paragraph_object = extract_paragraph_properties(
            parser_instance, paragraph_element, slide_layout_obj, ph_type, style_resolver
        )
        # Only add the paragraph to the text frame if it contains actual text runs
        if paragraph_object.text_runs:
            text_frame.paragraphs.append(paragraph_object)
    return text_frame


def extract_paragraph_properties(
    parser_instance,
    paragraph_element,
    slide_layout_obj: SlideLayout | None,
    ph_type: str | None = None,
    style_resolver=None,
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

    # Use StyleResolver if available, otherwise fall back to old logic
    if style_resolver:
        # Use the new centralized StyleResolver
        paragraph_object.properties = style_resolver.resolve_paragraph_properties(
            paragraph_element, slide_layout_obj, ph_type, current_level
        )
        
        # Override with any direct properties from the paragraph's XML
        if paragraph_properties_element is not None:
            if paragraph_properties_element.get("algn") is not None:
                paragraph_object.properties.align = paragraph_properties_element.get("algn")
            if paragraph_properties_element.get("indent") is not None:
                paragraph_object.properties.indent = int(
                    paragraph_properties_element.get("indent")
                )
            if paragraph_properties_element.get("lvl") is not None:
                paragraph_object.properties.level = int(paragraph_properties_element.get("lvl"))

    # Iterate through all run elements (a:r) within the paragraph
    for run_element in paragraph_element.findall(
        ".//a:r", namespaces=parser_instance.nsmap
    ):
        # Find the text element (a:t) within the run
        run_text_element = run_element.find(".//a:t", namespaces=parser_instance.nsmap)
        # If text content exists, extract it and its properties
        if run_text_element is not None and run_text_element.text is not None:
            text_content = run_text_element.text
            # Pass slide layout and placeholder type for inheritance
            run_properties = extract_run_properties(
                parser_instance,
                run_element,
                slide_layout_obj,
                ph_type,
                current_level,
                paragraph_properties_element,
                paragraph_object.properties,  # Pass resolved paragraph properties
                style_resolver,
            )
            # Append a new TextRun object to the paragraph's text runs
            paragraph_object.text_runs.append(
                TextRun(text=text_content, properties=run_properties)
            )
    return paragraph_object


def extract_run_properties(
    parser_instance,
    run_element,
    slide_layout_obj: SlideLayout | None = None,
    ph_type: str | None = None,
    paragraph_level: int | None = None,
    paragraph_properties_element=None,
    resolved_paragraph_properties: ParagraphProperties | None = None,
    style_resolver=None,
) -> RunProperties:
    """Extract run properties from a text run element."""
    
    # Use StyleResolver if available, otherwise fall back to old logic
    if (style_resolver and resolved_paragraph_properties):
        
        # Extract the run properties element from XML
        run_properties_element = run_element.find(".//a:rPr", namespaces=parser_instance.nsmap)
        
        # Use the new centralized StyleResolver
        run_properties = style_resolver.resolve_run_properties(
            run_properties_element, resolved_paragraph_properties, slide_layout_obj, paragraph_level
        )
        
        return run_properties











def _extract_layout_default_run_properties(
    parser_instance, slide_layout_obj: SlideLayout, ph_type: str
) -> dict:
    """Extract default run properties from slide layout XML without hard-coded defaults.

    This parses the actual slide layout XML to find default run properties,
    following proper OpenXML inheritance hierarchy without placeholder type assumptions.
    """
    # For now, return empty dict as layout-level run property parsing
    # would require significant additional XML parsing infrastructure.
    # The inheritance hierarchy will fall back to master and presentation defaults.
    #
    # TODO: To fully implement this, we would need to:
    # 1. Parse slide layout XML files for each placeholder's lstStyle
    # 2. Extract defRPr (default run properties) from lvlXpPr elements
    # 3. Store these in the SlideLayout object during layout parsing
    # 4. Return those parsed values here instead of an empty dict
    return {}


def _get_master_paragraph_alignment_default(
    slide_layout_obj: SlideLayout, ph_type: str
) -> str | None:
    """Get master slide default paragraph alignment from parsed list styles.

    Uses the layout's list_styles which contain master slide text style defaults.
    This follows proper OpenXML inheritance without hard-coded layout name matching.

    Args:
        slide_layout_obj: Slide layout object containing parsed master styles
        ph_type: Placeholder type (title, body, ctrTitle, etc.)

    Returns:
        str: Master slide default alignment or None if not found
    """
    if not slide_layout_obj or not ph_type:
        return None

    # Check master slide list styles for level 0 (most common level)
    if slide_layout_obj.list_styles and 0 in slide_layout_obj.list_styles:
        level_0_props = slide_layout_obj.list_styles[0]
        if level_0_props and level_0_props.align:
            return level_0_props.align

    # No explicit master alignment found
    return None


def _parse_anchor_with_inheritance(
    body_pr_element, slide_layout_obj: SlideLayout | None, ph_type: str | None
) -> str:
    """Parse anchor (vertical alignment) following OpenXML inheritance hierarchy.

    Follows the exact hierarchy:
    1. Slide Level: anchor attribute in <a:bodyPr> on the shape
    2. Layout Level: anchor attribute in <a:bodyPr> in slide layout placeholder
    3. Master Level: anchor attribute in <a:bodyPr> in slide master placeholder
    4. Application Default: top
    """
    # 1. Slide Level: anchor attribute in <a:bodyPr> on the shape
    if body_pr_element is not None:
        anchor = body_pr_element.get("anchor")
        if anchor:
            return anchor

    # 2. Layout Level: anchor attribute in <a:bodyPr> in slide layout placeholder
    if slide_layout_obj and ph_type:
        layout_anchor = _get_layout_bodypr_anchor_from_xml(slide_layout_obj, ph_type)
        if layout_anchor:
            return layout_anchor

    # 3. Master Level: anchor attribute in <a:bodyPr> in slide master placeholder
    master_anchor = _get_master_bodypr_anchor(slide_layout_obj, ph_type)
    if master_anchor:
        return master_anchor

    # 4. Application Default: top
    return "t"


def _parse_anchor_ctr_with_inheritance(
    body_pr_element, slide_layout_obj: SlideLayout | None, ph_type: str | None
) -> bool:
    """Parse anchorCtr (horizontal centering) with OpenXML inheritance."""
    # 1. Check slide-level bodyPr element
    if body_pr_element is not None:
        anchor_ctr = body_pr_element.get("anchorCtr")
        if anchor_ctr is not None:
            return anchor_ctr == "1"

    # 2. Layout and master inheritance (can be enhanced later)
    # For now, use OpenXML default

    # 3. OpenXML default
    return False  # False is the default


def _parse_inset_with_inheritance(body_pr_element, inset_attr: str) -> int:
    """Parse text inset with OpenXML inheritance and defaults.

    OpenXML default: 45720 EMUs (0.05 inches) if not specified
    """
    # 1. Check slide-level bodyPr element
    if body_pr_element is not None:
        inset = body_pr_element.get(inset_attr)
        if inset is not None:
            return int(inset)

    # 2. Layout and master inheritance (can be enhanced later)
    # For now, use OpenXML default

    # 3. OpenXML default: 45720 EMUs (0.05 inches)
    return 45720


def _get_layout_bodypr_anchor_from_xml(
    slide_layout_obj: SlideLayout, ph_type: str
) -> str | None:
    """Get bodyPr anchor value from parsed layout placeholders.

    Now uses the anchor values extracted during layout parsing.
    """
    if not slide_layout_obj or not ph_type:
        return None

    # Find the placeholder with matching type
    for placeholder in slide_layout_obj.placeholders:
        if placeholder.ph_type == ph_type:
            return placeholder.anchor

    return None


def _get_layout_paragraph_align_from_placeholders(
    slide_layout_obj: SlideLayout, ph_type: str
) -> str | None:
    """Get paragraph alignment from parsed layout placeholders.

    Uses the paragraph_align value extracted during layout parsing.
    """
    if not slide_layout_obj or not ph_type:
        return None

    # Find the placeholder with matching type and return its paragraph alignment
    for placeholder in slide_layout_obj.placeholders:
        if placeholder.ph_type == ph_type:
            return placeholder.paragraph_align

    return None


def _get_presentation_default_alignment(
    parser_instance, level: int | None
) -> str | None:
    """Get presentation-level default alignment from p:defaultTextStyle.

    This implements step 4 of the OpenXML inheritance hierarchy.

    Args:
        parser_instance: Slide parser instance with presentation_defaults
        level: Paragraph level (0-based indexing)

    Returns:
        str: Presentation default alignment or None if not found
    """
    if (
        not hasattr(parser_instance, "presentation_defaults")
        or not parser_instance.presentation_defaults
    ):
        return None

    # Use level 0 if no specific level provided
    effective_level = level if level is not None else 0

    # Check if we have defaults for this level
    if effective_level in parser_instance.presentation_defaults:
        level_props = parser_instance.presentation_defaults[effective_level]
        if level_props and level_props.align:
            return level_props.align

    # Fallback to level 0 if specific level not found
    if effective_level != 0 and 0 in parser_instance.presentation_defaults:
        level_0_props = parser_instance.presentation_defaults[0]
        if level_0_props and level_0_props.align:
            return level_0_props.align

    return None


def _get_master_bodypr_anchor(
    slide_layout_obj: SlideLayout, ph_type: str
) -> str | None:
    """Get anchor value from master slide bodyPr for given placeholder type.

    This implements step 3 of the vertical alignment inheritance hierarchy.
    Currently returns None as master slide parsing is not yet implemented.

    Args:
        slide_layout_obj: Slide layout object
        ph_type: Placeholder type

    Returns:
        str: Master slide anchor value or None if not found
    """
    # TODO: Implement actual master slide bodyPr parsing
    # This would require:
    # 1. Loading the slide master XML file referenced by the layout
    # 2. Finding the matching placeholder by type
    # 3. Extracting the anchor attribute from its bodyPr element
    # For now, return None to fall back to application default
    return None


def _resolve_paragraph_alignment_intelligently(
    parser_instance,
    slide_layout_obj: SlideLayout | None,
    ph_type: str | None,
    level: int | None,
) -> str:
    """Intelligently resolve paragraph alignment using sophisticated PowerPoint-like logic.

    This function implements the sophisticated alignment resolution that PowerPoint uses,
    understanding the difference between layout-level "style variants" and master-level
    "primary styles". It avoids the naive "first found wins" approach.

    Args:
        parser_instance: Slide parser instance
        slide_layout_obj: Slide layout object
        ph_type: Placeholder type
        level: Paragraph level

    Returns:
        str: Resolved alignment (guaranteed to never be None)
    """
    # Collect alignment values from all hierarchy levels
    layout_align = None
    master_align = None
    theme_align = None

    if slide_layout_obj and ph_type:
        # 2. Layout Level: Check for layout placeholder alignment
        layout_align = _get_layout_paragraph_align_from_placeholders(
            slide_layout_obj, ph_type
        )

        # 3. Master Level: Check for master slide text style alignment
        master_align = _get_master_paragraph_alignment_default(
            slide_layout_obj, ph_type
        )

    # 4. Theme Level: Check for presentation default alignment
    theme_align = _get_presentation_default_alignment(parser_instance, level)

    # Apply sophisticated resolution logic:
    # Master-level "primary styles" often override layout-level "style variants"
    # This mimics PowerPoint's intelligent style resolution

    # If we have both layout and master alignments, prefer master for body text
    if layout_align and master_align:
        # For body/content placeholders, master "primary style" usually wins over layout "variant"
        if ph_type in ["body", "obj", "content"]:
            return master_align
        # For title placeholders, layout alignment often takes precedence
        elif ph_type in ["title", "ctrTitle"]:
            return layout_align
        else:
            # For other placeholder types, prefer master as the "primary style"
            return master_align

    # Standard inheritance hierarchy when no conflicts exist
    if layout_align:
        return layout_align
    elif master_align:
        return master_align
    elif theme_align:
        return theme_align
    else:
        # 5. Application Default: left
        return "l"


def _resolve_bullet_properties_intelligently(
    parser_instance,
    paragraph_object,
    paragraph_properties_element,
    slide_layout_obj: SlideLayout | None,
    ph_type: str | None,
    level: int | None,
):
    """Intelligently resolve bullet properties using proper OpenXML inheritance hierarchy.

    Follows the exact bullet hierarchy:
    1. Slide Level: Check <a:pPr> on the slide itself
    2. Layout Level: Check <a:pPr> of placeholder in slide layout
    3. Master Level: Check <a:lvlXpPr> in slide master text style
    4. Theme Level: Check <p:defaultTextStyle> in presentation
    5. Application Default: No bullet

    Args:
        parser_instance: Slide parser instance
        paragraph_object: Paragraph object to update
        paragraph_properties_element: XML element containing slide-level properties
        slide_layout_obj: Slide layout object
        ph_type: Placeholder type
        level: Paragraph level
    """

    # 1. Slide Level (Most Powerful): Check slide's <a:pPr> element
    slide_bullet_result = _check_bullet_properties_in_element(
        parser_instance, paragraph_properties_element
    )
    if slide_bullet_result is not None:
        _apply_bullet_result(paragraph_object, slide_bullet_result, parser_instance)
        return  # Slide level wins - stop here

    # 2. Layout Level: Check placeholder in slide layout
    if slide_layout_obj and ph_type:
        layout_bullet_result = _get_layout_bullet_properties(slide_layout_obj, ph_type)
        if layout_bullet_result is not None:
            _apply_bullet_result(
                paragraph_object, layout_bullet_result, parser_instance
            )
            return  # Layout level wins - stop here

    # 3. Master Level: Check slide master text style for this level
    if slide_layout_obj and level is not None:
        master_bullet_result = _get_master_bullet_properties(slide_layout_obj, level)
        if master_bullet_result is not None:
            _apply_bullet_result(
                paragraph_object, master_bullet_result, parser_instance
            )
            return  # Master level wins - stop here

    # 4. Theme Level: Check presentation defaults
    theme_bullet_result = _get_presentation_bullet_properties(parser_instance, level)
    if theme_bullet_result is not None:
        _apply_bullet_result(paragraph_object, theme_bullet_result, parser_instance)
        return  # Theme level wins - stop here

    # 5. Application Default: No bullet (leave bullet_type as None)
    # paragraph_object.properties.bullet_type remains None (no bullet)


def _check_bullet_properties_in_element(parser_instance, properties_element):
    """Check for bullet properties in a given XML element.

    Returns:
        dict: Bullet information if found, None if no definitive bullet info
    """
    if properties_element is None:
        return None

    # Check for buNone (no bullet) - this stops the search
    bu_none_element = properties_element.find(
        ".//a:buNone", namespaces=parser_instance.nsmap
    )
    if bu_none_element is not None:
        return {"type": "none"}

    # Check for buChar (character bullet)
    bu_char_element = properties_element.find(
        ".//a:buChar", namespaces=parser_instance.nsmap
    )
    if bu_char_element is not None:
        result = {"type": "char", "char": bu_char_element.get("char")}

        # Get additional char bullet properties
        bu_font_element = properties_element.find(
            ".//a:buFont", namespaces=parser_instance.nsmap
        )
        if bu_font_element is not None:
            result["font_face"] = bu_font_element.get("typeface")

        bu_sz_pct_element = properties_element.find(
            ".//a:buSzPct", namespaces=parser_instance.nsmap
        )
        if bu_sz_pct_element is not None:
            result["size_pct"] = int(bu_sz_pct_element.get("val"))

        bu_sz_pts_element = properties_element.find(
            ".//a:buSzPts", namespaces=parser_instance.nsmap
        )
        if bu_sz_pts_element is not None:
            result["size_pts"] = int(bu_sz_pts_element.get("val"))

        return result

    # Check for buAutoNum (auto numbering)
    bu_auto_num_element = properties_element.find(
        ".//a:buAutoNum", namespaces=parser_instance.nsmap
    )
    if bu_auto_num_element is not None:
        result = {"type": "autoNum", "auto_num_type": bu_auto_num_element.get("type")}
        if bu_auto_num_element.get("startAt") is not None:
            result["start_at"] = int(bu_auto_num_element.get("startAt"))
        return result

    # Check for buBlip (image bullet)
    bu_blip_element = properties_element.find(
        ".//a:buBlip", namespaces=parser_instance.nsmap
    )
    if bu_blip_element is not None:
        blip_element = bu_blip_element.find(
            ".//a:blip", namespaces=parser_instance.nsmap
        )
        if blip_element is not None:
            embed_id = blip_element.get(
                "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed"
            )
            if embed_id and embed_id in parser_instance.rels:
                return {"type": "blip", "image_path": parser_instance.rels[embed_id]}

    # No definitive bullet information found
    return None


def _apply_bullet_result(paragraph_object, bullet_result, parser_instance):
    """Apply bullet result to paragraph object."""
    if not bullet_result:
        return

    bullet_type = bullet_result.get("type")
    paragraph_object.properties.bullet_type = bullet_type

    if bullet_type == "char":
        paragraph_object.properties.bullet_char = bullet_result.get("char")
        paragraph_object.properties.bullet_font_face = bullet_result.get("font_face")
        paragraph_object.properties.bullet_size_pct = bullet_result.get("size_pct")
        paragraph_object.properties.bullet_size_pts = bullet_result.get("size_pts")
    elif bullet_type == "autoNum":
        paragraph_object.properties.bullet_auto_num_type = bullet_result.get(
            "auto_num_type"
        )
        paragraph_object.properties.bullet_start_at = bullet_result.get("start_at")
    elif bullet_type == "blip":
        paragraph_object.properties.bullet_image_path = bullet_result.get("image_path")


def _get_layout_bullet_properties(slide_layout_obj: SlideLayout, ph_type: str):
    """Get bullet properties from slide layout placeholder.

    Currently returns None as layout-level bullet parsing is not yet implemented.
    This would require parsing the slide layout XML for placeholder bullet properties.
    """
    # TODO: Implement layout-level bullet property parsing
    # This would involve parsing the slide layout XML files to extract
    # bullet properties from placeholder definitions
    return None


def _get_master_bullet_properties(slide_layout_obj: SlideLayout, level: int):
    """Get bullet properties from slide master text style for given level.

    Uses the list_styles which contain master slide text style defaults.
    """
    if not slide_layout_obj or level is None:
        return None

    # Check master slide list styles for this level
    if slide_layout_obj.list_styles and level in slide_layout_obj.list_styles:
        level_props = slide_layout_obj.list_styles[level]
        if level_props and level_props.bullet_type:
            result = {"type": level_props.bullet_type}

            if level_props.bullet_type == "char":
                result["char"] = level_props.bullet_char
                result["font_face"] = level_props.bullet_font_face
                result["size_pct"] = level_props.bullet_size_pct
                result["size_pts"] = level_props.bullet_size_pts
            elif level_props.bullet_type == "autoNum":
                result["auto_num_type"] = level_props.bullet_auto_num_type
                result["start_at"] = level_props.bullet_start_at
            elif level_props.bullet_type == "blip":
                result["image_path"] = level_props.bullet_image_path

            return result

    return None


def _get_presentation_bullet_properties(parser_instance, level: int | None):
    """Get bullet properties from presentation defaults.

    Uses presentation_defaults which contain parsed p:defaultTextStyle data.
    """
    if (
        not hasattr(parser_instance, "presentation_defaults")
        or not parser_instance.presentation_defaults
    ):
        return None

    # Use level 0 if no specific level provided
    effective_level = level if level is not None else 0

    # Check if we have defaults for this level
    if effective_level in parser_instance.presentation_defaults:
        level_props = parser_instance.presentation_defaults[effective_level]
        if level_props and level_props.bullet_type:
            result = {"type": level_props.bullet_type}

            if level_props.bullet_type == "char":
                result["char"] = level_props.bullet_char
                result["font_face"] = level_props.bullet_font_face
                result["size_pct"] = level_props.bullet_size_pct
                result["size_pts"] = level_props.bullet_size_pts
            elif level_props.bullet_type == "autoNum":
                result["auto_num_type"] = level_props.bullet_auto_num_type
                result["start_at"] = level_props.bullet_start_at
            elif level_props.bullet_type == "blip":
                result["image_path"] = level_props.bullet_image_path

            return result

    # Fallback to level 0 if specific level not found
    if effective_level != 0 and 0 in parser_instance.presentation_defaults:
        level_0_props = parser_instance.presentation_defaults[0]
        if level_0_props and level_0_props.bullet_type:
            result = {"type": level_0_props.bullet_type}

            if level_0_props.bullet_type == "char":
                result["char"] = level_0_props.bullet_char
                result["font_face"] = level_0_props.bullet_font_face
                result["size_pct"] = level_0_props.bullet_size_pct
                result["size_pts"] = level_0_props.bullet_size_pts
            elif level_0_props.bullet_type == "autoNum":
                result["auto_num_type"] = level_0_props.bullet_auto_num_type
                result["start_at"] = level_0_props.bullet_start_at
            elif level_0_props.bullet_type == "blip":
                result["image_path"] = level_0_props.bullet_image_path

            return result

    return None




def _get_layout_text_style_font_size(slide_layout_obj: SlideLayout, ph_type: str) -> int | None:
    """Get font size from layout text styles based on placeholder type.
    
    Args:
        slide_layout_obj: SlideLayout object with parsed text styles
        ph_type: Placeholder type (title, body, etc.)
        
    Returns:
        Font size in PowerPoint units or None if not found
    """
    if not slide_layout_obj:
        return None
    
    # Map placeholder types to text style properties
    if ph_type in ["title", "ctrTitle"]:
        text_style = slide_layout_obj.title_style
    elif ph_type in ["body", "obj", "content"]:
        text_style = slide_layout_obj.body_style
    else:
        text_style = slide_layout_obj.other_style
    
    # Extract font size from text style
    if (text_style and 
        text_style.default_run_properties and 
        text_style.default_run_properties.font_size is not None):
        return text_style.default_run_properties.font_size
    
    return None


def _get_master_text_style_font_size(slide_layout_obj: SlideLayout, ph_type: str) -> int | None:
    """Get font size from master text styles based on placeholder type.
    
    Args:
        slide_layout_obj: SlideLayout object that may reference a master
        ph_type: Placeholder type (title, body, etc.)
        
    Returns:
        Font size in PowerPoint units or None if not found
    """
    if not slide_layout_obj or not slide_layout_obj.slide_master:
        return None
    
    slide_master = slide_layout_obj.slide_master
    
    # Map placeholder types to master text style properties
    if ph_type in ["title", "ctrTitle"]:
        text_style = slide_master.title_style
    elif ph_type in ["body", "obj", "content"]:
        text_style = slide_master.body_style
    else:
        text_style = slide_master.other_style
    
    # Extract font size from master text style
    if (text_style and 
        text_style.default_run_properties and 
        text_style.default_run_properties.font_size is not None):
        return text_style.default_run_properties.font_size
    
    # Fallback to master list styles if text styles don't have font size
    if (slide_layout_obj.list_styles and 
        0 in slide_layout_obj.list_styles):
        level_0_props = slide_layout_obj.list_styles[0]
        if (level_0_props and 
            level_0_props.default_run_properties and 
            level_0_props.default_run_properties.font_size is not None):
            return level_0_props.default_run_properties.font_size
    
    return None


def _get_layout_text_style_font_info(slide_layout_obj: SlideLayout, ph_type: str) -> dict | None:
    """Get font information from layout text styles based on placeholder type.
    
    Args:
        slide_layout_obj: SlideLayout object containing text styles
        ph_type: Placeholder type (title, body, etc.)
        
    Returns:
        Dict with font_face or font_ref key, or None if not found
    """
    if not slide_layout_obj:
        return None
    
    # Map placeholder types to layout text style properties
    if ph_type in ["title", "ctrTitle"]:
        text_style = slide_layout_obj.title_style
    elif ph_type in ["body", "obj", "content"]:
        text_style = slide_layout_obj.body_style
    else:
        text_style = slide_layout_obj.other_style
    
    # Extract font information from layout text style
    if (text_style and text_style.default_run_properties):
        if text_style.default_run_properties.font_face:
            return {"font_face": text_style.default_run_properties.font_face}
        elif text_style.default_run_properties.font_ref:
            return {"font_ref": text_style.default_run_properties.font_ref}
    
    return None


def _get_master_text_style_font_info(slide_master, ph_type: str) -> dict | None:
    """Get font information from master text styles based on placeholder type.
    
    Args:
        slide_master: SlideMaster object containing text styles
        ph_type: Placeholder type (title, body, etc.)
        
    Returns:
        Dict with font_face or font_ref key, or None if not found
    """
    if not slide_master:
        return None
    
    # Map placeholder types to master text style properties
    if ph_type in ["title", "ctrTitle"]:
        text_style = slide_master.title_style
    elif ph_type in ["body", "obj", "content"]:
        text_style = slide_master.body_style
    else:
        text_style = slide_master.other_style
    
    # Extract font information from master text style
    if (text_style and text_style.default_run_properties):
        if text_style.default_run_properties.font_face:
            return {"font_face": text_style.default_run_properties.font_face}
        elif text_style.default_run_properties.font_ref:
            return {"font_ref": text_style.default_run_properties.font_ref}
    
    return None








