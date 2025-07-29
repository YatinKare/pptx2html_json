from learnx_parser.models.core import (
    ParagraphProperties,
    PresentationDefaults,
    RunProperties,
    SlideLayout,
    SlideMaster,
)


class StyleResolver:
    def __init__(
        self,
        slide_master: SlideMaster,
        presentation_defaults: PresentationDefaults
    ):
        """
        Initializes the resolver with the highest-level style objects.

        Args:
            slide_master: The fully parsed SlideMaster object.
            presentation_defaults: The default text styles for the whole presentation.
        """
        self.slide_master = slide_master
        self.presentation_defaults = presentation_defaults

    def resolve_paragraph_properties(
        self, 
        p_element, 
        slide_layout: SlideLayout, 
        ph_type: str | None, 
        p_level: int | None
    ) -> ParagraphProperties:
        """
        Resolve paragraph properties using simplified 3-step logic.
        
        Args:
            p_element: The paragraph element containing direct <a:pPr> properties
            slide_layout: The slide layout containing layout-specific styles
            ph_type: Placeholder type (e.g., "title", "body", "ctrTitle", etc.)
            p_level: Paragraph level (0-based) for list styles
            
        Returns:
            ParagraphProperties with fully resolved bullet styles
        """
        # Step 1: Is it a list item?
        # Check if the paragraph has a lvl attribute (p_level is the parsed value)
        if p_level is None:
            # No lvl attribute = not a list item
            return ParagraphProperties(bullet_type=None)
        
        # Step 2: Does it have an explicit "no bullet" override?
        # Check if the paragraph's <a:pPr> has a <a:buNone/> tag
        if p_element is not None:
            nsmap = getattr(p_element, 'nsmap', {})
            p_pr_element = p_element.find(".//a:pPr", namespaces=nsmap)
            if p_pr_element is not None:
                if p_pr_element.find(".//a:buNone", namespaces=nsmap) is not None:
                    # List item with no visible bullet
                    return ParagraphProperties(bullet_type="none")
        
        # Step 3: Find the bullet style
        # Perform 4-level search: Paragraph -> Layout -> Master -> Defaults
        
        # 3a: Check paragraph level for bullet definitions
        if p_element is not None:
            nsmap = getattr(p_element, 'nsmap', {})
            p_pr_element = p_element.find(".//a:pPr", namespaces=nsmap)
            if p_pr_element is not None:
                # Check for <a:buChar>
                bu_char_element = p_pr_element.find(".//a:buChar", namespaces=nsmap)
                if bu_char_element is not None:
                    props = ParagraphProperties(bullet_type="char")
                    props.bullet_char = bu_char_element.get("char")
                    
                    # Get bullet font if present
                    bu_font_element = p_pr_element.find(".//a:buFont", namespaces=nsmap)
                    if bu_font_element is not None:
                        props.bullet_font_face = bu_font_element.get("typeface")
                    
                    return props
                
                # Check for <a:buAutoNum>
                bu_auto_num_element = p_pr_element.find(".//a:buAutoNum", namespaces=nsmap)
                if bu_auto_num_element is not None:
                    props = ParagraphProperties(bullet_type="autoNum")
                    props.bullet_auto_num_type = bu_auto_num_element.get("type")
                    if bu_auto_num_element.get("startAt") is not None:
                        props.bullet_start_at = int(bu_auto_num_element.get("startAt"))
                    return props
                
                # Check for <a:buBlip>
                bu_blip_element = p_pr_element.find(".//a:buBlip", namespaces=nsmap)
                if bu_blip_element is not None:
                    return ParagraphProperties(bullet_type="blip")
        
        # 3b: Check slide layout
        if slide_layout and slide_layout.list_styles and p_level in slide_layout.list_styles:
            layout_style = slide_layout.list_styles[p_level]
            if layout_style and layout_style.bullet_type:
                return self._merge_paragraph_properties(layout_style)
        
        # 3c: Check slide master
        if slide_layout and slide_layout.slide_master:
            # Check master's text style for placeholder type
            master_style = self._get_master_style_by_ph_type(ph_type)
            if master_style and hasattr(master_style, 'list_styles') and master_style.list_styles:
                if p_level in master_style.list_styles:
                    master_level_style = master_style.list_styles[p_level]
                    if master_level_style and master_level_style.bullet_type:
                        return self._merge_paragraph_properties(master_level_style)
            
            # Also check slide_master.list_styles directly
            if slide_layout.slide_master.list_styles and p_level in slide_layout.slide_master.list_styles:
                master_style = slide_layout.slide_master.list_styles[p_level]
                if master_style and master_style.bullet_type:
                    return self._merge_paragraph_properties(master_style)
        
        # 3d: Check presentation defaults
        if (self.presentation_defaults and 
            hasattr(self.presentation_defaults, 'list_styles') and 
            self.presentation_defaults.list_styles and 
            p_level in self.presentation_defaults.list_styles):
            default_style = self.presentation_defaults.list_styles[p_level]
            if default_style and default_style.bullet_type:
                return self._merge_paragraph_properties(default_style)
        
        # If no bullet definition found anywhere, use default bullet
        # This should rarely happen if the presentation is well-formed
        return ParagraphProperties(bullet_type="char", bullet_char="•")
    
    def _get_layout_style_by_ph_type(self, slide_layout: SlideLayout, ph_type: str | None) -> ParagraphProperties | None:
        """Get the appropriate style from slide layout based on placeholder type."""
        if ph_type in ["title", "ctrTitle"]:
            return slide_layout.title_style
        elif ph_type in ["body", "obj", "content"]:
            return slide_layout.body_style
        else:
            return slide_layout.other_style
    
    def _get_master_style_by_ph_type(self, ph_type: str | None) -> ParagraphProperties | None:
        """Get the appropriate style from slide master based on placeholder type."""
        if ph_type in ["title", "ctrTitle"]:
            return self.slide_master.title_style
        elif ph_type in ["body", "obj", "content"]:
            return self.slide_master.body_style
        else:
            return self.slide_master.other_style
    
    def _check_for_bullet_in_pPr(self, p_element) -> ParagraphProperties | None:
        """
        Check for bullet properties directly in the paragraph's <a:pPr> element.
        
        Args:
            p_element: The paragraph element to check
            
        Returns:
            ParagraphProperties if bullet property found, None otherwise
        """
        if p_element is None:
            return None
            
        # Look for pPr element within the paragraph
        nsmap = getattr(p_element, 'nsmap', {})
        p_pr_element = p_element.find(".//a:pPr", namespaces=nsmap)
        if p_pr_element is None:
            return None
            
        return self._extract_bullet_properties_from_element(p_pr_element)
    
    def _check_layout_list_style(self, slide_layout: SlideLayout, p_level: int | None) -> ParagraphProperties | None:
        """
        Check the slide layout's list style for the specified level.
        
        Args:
            slide_layout: The slide layout to check
            p_level: The paragraph level to look up
            
        Returns:
            ParagraphProperties if bullet property found, None otherwise
        """
        if not slide_layout or not slide_layout.list_styles or p_level is None:
            return None
            
        layout_level_style = slide_layout.list_styles.get(p_level)
        if layout_level_style and layout_level_style.bullet_type is not None:
            return self._merge_paragraph_properties(layout_level_style)
            
        return None
    
    def _check_master_text_style(self, slide_master: SlideMaster | None, ph_type: str | None, p_level: int | None) -> ParagraphProperties | None:
        """
        Check the slide master's text style for the specified placeholder type and level.
        
        Args:
            slide_master: The slide master to check
            ph_type: The placeholder type
            p_level: The paragraph level
            
        Returns:
            ParagraphProperties if bullet property found, None otherwise
        """
        if not slide_master:
            return None
            
        master_style = self._get_master_style_by_ph_type(ph_type)
        if master_style and master_style.bullet_type is not None:
            return self._merge_paragraph_properties(master_style)
            
        return None
    
    def _check_presentation_defaults(self, p_level: int | None) -> ParagraphProperties | None:
        """
        Check the presentation defaults for bullet properties.
        
        Args:
            p_level: The paragraph level
            
        Returns:
            ParagraphProperties if bullet property found, None otherwise
        """
        if (self.presentation_defaults.default_paragraph_properties and 
            self.presentation_defaults.default_paragraph_properties.bullet_type is not None):
            return self._merge_paragraph_properties(self.presentation_defaults.default_paragraph_properties)
            
        return None
    
    def _extract_bullet_properties_from_element(self, element) -> ParagraphProperties | None:
        """
        Extract bullet properties from a paragraph properties element.
        
        Args:
            element: XML element containing paragraph properties
            
        Returns:
            ParagraphProperties if bullet found, None otherwise
        """
        nsmap = getattr(element, 'nsmap', {})
        
        # Check for bullet elements in order of priority
        bu_none_element = element.find(".//a:buNone", namespaces=nsmap)
        if bu_none_element is not None:
            return ParagraphProperties(bullet_type="none")
            
        bu_char_element = element.find(".//a:buChar", namespaces=nsmap)
        if bu_char_element is not None:
            props = ParagraphProperties(bullet_type="char")
            props.bullet_char = bu_char_element.get("char")
            
            # Extract additional bullet properties
            bu_font_element = element.find(".//a:buFont", namespaces=nsmap)
            if bu_font_element is not None:
                props.bullet_font_face = bu_font_element.get("typeface")
                
            bu_sz_pct_element = element.find(".//a:buSzPct", namespaces=nsmap)
            if bu_sz_pct_element is not None:
                props.bullet_size_pct = int(bu_sz_pct_element.get("val"))
                
            bu_sz_pts_element = element.find(".//a:buSzPts", namespaces=nsmap)
            if bu_sz_pts_element is not None:
                props.bullet_size_pts = int(bu_sz_pts_element.get("val"))
                
            return props
            
        bu_auto_num_element = element.find(".//a:buAutoNum", namespaces=nsmap)
        if bu_auto_num_element is not None:
            props = ParagraphProperties(bullet_type="autoNum")
            props.bullet_auto_num_type = bu_auto_num_element.get("type")
            if bu_auto_num_element.get("startAt") is not None:
                props.bullet_start_at = int(bu_auto_num_element.get("startAt"))
            return props
            
        bu_blip_element = element.find(".//a:buBlip", namespaces=nsmap)
        if bu_blip_element is not None:
            props = ParagraphProperties(bullet_type="blip")
            # Handle image bullet extraction if needed
            return props
            
        return None
    
    def _merge_paragraph_properties(self, base_props: ParagraphProperties) -> ParagraphProperties:
        """
        Create a deep copy of paragraph properties to avoid modifying the original.
        """
        # Create a new ParagraphProperties with all values from base_props
        merged = ParagraphProperties(
            align=base_props.align,
            indent=base_props.indent,
            bullet_type=base_props.bullet_type,
            bullet_char=base_props.bullet_char,
            bullet_font_face=base_props.bullet_font_face,
            bullet_size_pct=base_props.bullet_size_pct,
            bullet_size_pts=base_props.bullet_size_pts,
            bullet_auto_num_type=base_props.bullet_auto_num_type,
            bullet_start_at=base_props.bullet_start_at,
            bullet_image_path=base_props.bullet_image_path,
            level=base_props.level,
            default_run_properties=base_props.default_run_properties
        )
        return merged

    def resolve_run_properties(
        self, 
        run_element, 
        paragraph_properties: ParagraphProperties,
        slide_layout: SlideLayout | None,
        list_level: int | None
    ) -> RunProperties:
        """
        Resolve run properties using the full 6-level OpenXML inheritance hierarchy.
        
        This implements the correct font size inheritance logic that was previously broken.
        The inheritance order is:
        1. Direct Run Properties: Check for properties on the run itself
        2. Paragraph-Level Default: Check for properties in paragraph's default settings
        3. List Style Level: Use list_level to check corresponding list style in slide_layout
        4. Layout/Master Style: Check titleStyle, bodyStyle, or otherStyle on slide_layout/master
        5. Presentation Default: Check presentation_defaults for default values
        6. Application Default: Use fallback value (1800 for 18pt font size)
        
        Args:
            run_element: XML element containing run-specific properties (<a:rPr>)
            paragraph_properties: Already resolved paragraph properties containing default run properties
            slide_layout: The slide layout for accessing layout/master styles
            list_level: Paragraph level (0-based) for looking up list styles
            
        Returns:
            RunProperties with fully resolved styles following the 6-level hierarchy
        """
        # Start with an empty RunProperties that we'll build up through the hierarchy
        resolved_run_props = RunProperties()
        
        # Level 6: Application Default (lowest priority)
        # Set default values that will be used if nothing else is found
        resolved_run_props.font_size = 1800  # 18pt default
        
        # Level 5: Presentation Default
        # Check if we have presentation defaults with font size information
        if (hasattr(self.presentation_defaults, 'default_run_properties') and 
            self.presentation_defaults.default_run_properties and
            self.presentation_defaults.default_run_properties.font_size):
            resolved_run_props.font_size = self.presentation_defaults.default_run_properties.font_size
        
        # For now, we'll assume presentation_defaults is the PresentationDefaults object
        # In a future update, we could access the dict structure if needed
        
        # Level 4: Layout/Master Style
        # Check slide layout and master text styles based on placeholder type
        if slide_layout:
            # First check layout styles
            layout_style = self._get_layout_style_by_ph_type(slide_layout, None)  # We don't have ph_type here
            if layout_style and layout_style.default_run_properties and layout_style.default_run_properties.font_size:
                resolved_run_props.font_size = layout_style.default_run_properties.font_size
            
            # Then check master styles through the layout
            if slide_layout.slide_master:
                master_style = self._get_master_style_by_ph_type(None)  # We don't have ph_type here
                if master_style and master_style.default_run_properties and master_style.default_run_properties.font_size:
                    resolved_run_props.font_size = master_style.default_run_properties.font_size
        
        # Level 3: List Style Level
        # Check the specific list level style in the slide layout
        if slide_layout and slide_layout.list_styles and list_level is not None:
            layout_level_style = slide_layout.list_styles.get(list_level)
            if (layout_level_style and 
                layout_level_style.default_run_properties and 
                layout_level_style.default_run_properties.font_size):
                resolved_run_props.font_size = layout_level_style.default_run_properties.font_size
        
        # Level 2: Paragraph-Level Default
        # Check for font size in the paragraph's default run properties
        if (paragraph_properties.default_run_properties and 
            paragraph_properties.default_run_properties.font_size):
            resolved_run_props.font_size = paragraph_properties.default_run_properties.font_size
        
        # Level 1: Direct Run Properties (highest priority)
        # Override with run-specific properties if they exist
        if run_element is not None:
            nsmap = getattr(run_element, 'nsmap', {})
            
            # Parse font size - this has the highest priority
            if run_element.get("sz") is not None:
                resolved_run_props.font_size = int(run_element.get("sz"))
            
            # Parse other run properties with the same inheritance logic
            # For now, we'll use the simpler approach for non-font-size properties
            
            # Parse bold
            if run_element.get("b") is not None:
                resolved_run_props.bold = run_element.get("b") == "1"
            elif (paragraph_properties.default_run_properties and 
                  paragraph_properties.default_run_properties.bold is not None):
                resolved_run_props.bold = paragraph_properties.default_run_properties.bold
            
            # Parse italic
            if run_element.get("i") is not None:
                resolved_run_props.italic = run_element.get("i") == "1"
            elif (paragraph_properties.default_run_properties and 
                  paragraph_properties.default_run_properties.italic is not None):
                resolved_run_props.italic = paragraph_properties.default_run_properties.italic
            
            # Parse underline
            if run_element.get("u") is not None:
                resolved_run_props.underline = run_element.get("u") != "none"
            elif (paragraph_properties.default_run_properties and 
                  paragraph_properties.default_run_properties.underline is not None):
                resolved_run_props.underline = paragraph_properties.default_run_properties.underline
            
            # Parse capitalization
            if run_element.get("cap") is not None:
                resolved_run_props.cap = run_element.get("cap")
            elif (paragraph_properties.default_run_properties and 
                  paragraph_properties.default_run_properties.cap is not None):
                resolved_run_props.cap = paragraph_properties.default_run_properties.cap
            
            # Parse font face from run element
            latin_font_element = run_element.find(".//a:latin", namespaces=nsmap)
            if latin_font_element is not None:
                typeface = latin_font_element.get("typeface")
                if typeface in ["+mj-lt", "+mj-ea", "+mj-cs"]:
                    resolved_run_props.font_ref = "major"
                elif typeface in ["+mn-lt", "+mn-ea", "+mn-cs"]:
                    resolved_run_props.font_ref = "minor"
                else:
                    resolved_run_props.font_face = typeface
            elif (paragraph_properties.default_run_properties and 
                  paragraph_properties.default_run_properties.font_face is not None):
                resolved_run_props.font_face = paragraph_properties.default_run_properties.font_face
            
            # Parse font reference
            font_ref_element = run_element.find(".//a:fontRef", namespaces=nsmap)
            if font_ref_element is not None:
                resolved_run_props.font_ref = font_ref_element.get("idx")
            elif (paragraph_properties.default_run_properties and 
                  paragraph_properties.default_run_properties.font_ref is not None):
                resolved_run_props.font_ref = paragraph_properties.default_run_properties.font_ref
            
            # Parse color from run element
            solid_fill_element = run_element.find(".//a:solidFill", namespaces=nsmap)
            if solid_fill_element is not None:
                srgb_color_element = solid_fill_element.find(".//a:srgbClr", namespaces=nsmap)
                if srgb_color_element is not None:
                    resolved_run_props.color = srgb_color_element.get("val")
                else:
                    scheme_color_element = solid_fill_element.find(".//a:schemeClr", namespaces=nsmap)
                    if scheme_color_element is not None:
                        resolved_run_props.scheme_color = scheme_color_element.get("val")
            elif (paragraph_properties.default_run_properties and 
                  paragraph_properties.default_run_properties.color is not None):
                resolved_run_props.color = paragraph_properties.default_run_properties.color
            elif (paragraph_properties.default_run_properties and 
                  paragraph_properties.default_run_properties.scheme_color is not None):
                resolved_run_props.scheme_color = paragraph_properties.default_run_properties.scheme_color
        
        # If run_element is None, still apply paragraph defaults for other properties
        elif paragraph_properties.default_run_properties:
            base_props = paragraph_properties.default_run_properties
            resolved_run_props.bold = base_props.bold
            resolved_run_props.italic = base_props.italic
            resolved_run_props.underline = base_props.underline
            resolved_run_props.cap = base_props.cap
            resolved_run_props.font_face = base_props.font_face
            resolved_run_props.font_ref = base_props.font_ref
            resolved_run_props.color = base_props.color
            resolved_run_props.scheme_color = base_props.scheme_color
        
        return resolved_run_props