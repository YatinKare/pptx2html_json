import os

from lxml import etree

from learnx_parser.models.core import (
    BackgroundReference,
    GradientFill,
    GradientStop,
    ParagraphProperties,
    RunProperties,
    SlideMaster,
)


class SlideMasterParser:
    def __init__(self, master_xml_path, pptx_unpacked_path=None):
        self.master_xml_path = master_xml_path
        self.pptx_unpacked_path = pptx_unpacked_path
        self.tree = etree.parse(self.master_xml_path)
        self.root = self.tree.getroot()
        self.nsmap = self.root.nsmap
        self.rels = self._parse_rels()  # Parse relationships for the master file

    def _parse_rels(self):
        relationships = {}
        master_rels_path = os.path.join(
            os.path.dirname(self.master_xml_path),
            "_rels",
            os.path.basename(self.master_xml_path) + ".rels",
        )
        if os.path.exists(master_rels_path):
            relationships_tree = etree.parse(master_rels_path)
            for relationship in relationships_tree.findall(
                "{http://schemas.openxmlformats.org/package/2006/relationships}Relationship"
            ):
                relationships[relationship.get("Id")] = relationship.get("Target")
        return relationships

    def _extract_background_properties(self) -> tuple[str | None, GradientFill | None, BackgroundReference | None]:
        """Extract background properties from slide master XML.
        
        Returns:
            Tuple of (background_color, background_gradient_fill, background_reference)
        """
        background_color = None
        background_gradient_fill = None
        background_reference = None
        
        # Look for background element in common slide data
        cSld_element = self.root.find(".//p:cSld", namespaces=self.nsmap)
        if cSld_element is not None:
            background_element = cSld_element.find(".//p:bg", namespaces=self.nsmap)
            if background_element is not None:
                # Check for background properties (p:bgPr)
                background_properties_element = background_element.find(".//p:bgPr", namespaces=self.nsmap)
                if background_properties_element is not None:
                    # Extract solid fill
                    solid_fill_element = background_properties_element.find(".//a:solidFill", namespaces=self.nsmap)
                    if solid_fill_element is not None:
                        srgb_color_element = solid_fill_element.find(".//a:srgbClr", namespaces=self.nsmap)
                        if srgb_color_element is not None:
                            background_color = srgb_color_element.get("val")
                    
                    # Extract gradient fill
                    gradient_fill_element = background_properties_element.find(".//a:gradFill", namespaces=self.nsmap)
                    if gradient_fill_element is not None:
                        gradient_stops = []
                        for gs_element in gradient_fill_element.findall(".//a:gs", namespaces=self.nsmap):
                            pos = int(gs_element.get("pos", "0"))
                            
                            # Extract color from gradient stop
                            color = None
                            scheme_color = None
                            srgb_color_element = gs_element.find(".//a:srgbClr", namespaces=self.nsmap)
                            if srgb_color_element is not None:
                                color = srgb_color_element.get("val")
                            else:
                                scheme_color_element = gs_element.find(".//a:schemeClr", namespaces=self.nsmap)
                                if scheme_color_element is not None:
                                    scheme_color = scheme_color_element.get("val")
                            
                            gradient_stops.append(GradientStop(pos=pos, color=color, scheme_color=scheme_color))
                        
                        if gradient_stops:
                            # Extract gradient direction/angle
                            angle = None
                            lin_element = gradient_fill_element.find(".//a:lin", namespaces=self.nsmap)
                            if lin_element is not None:
                                angle = int(lin_element.get("ang", "0"))
                            
                            background_gradient_fill = GradientFill(stops=gradient_stops, angle=angle)
                
                # Check for background reference (p:bgRef)
                background_reference_element = background_element.find(".//p:bgRef", namespaces=self.nsmap)
                if background_reference_element is not None:
                    idx = int(background_reference_element.get("idx", "0"))
                    scheme_color = None
                    scheme_color_element = background_reference_element.find(".//a:schemeClr", namespaces=self.nsmap)
                    if scheme_color_element is not None:
                        scheme_color = scheme_color_element.get("val")
                    background_reference = BackgroundReference(idx=idx, scheme_color=scheme_color)
        
        return background_color, background_gradient_fill, background_reference

    def _parse_text_styles(self) -> tuple[ParagraphProperties | None, ParagraphProperties | None, ParagraphProperties | None, dict[int, ParagraphProperties]]:
        """Parse text styles from <p:txStyles> element in slide master.
        
        Returns:
            Tuple of (title_style, body_style, other_style, list_styles)
        """
        title_style = None
        body_style = None
        other_style = None
        list_styles = {}
        
        # Look for txStyles element in slide master
        tx_styles_element = self.root.find(".//p:txStyles", namespaces=self.nsmap)
        if tx_styles_element is not None:
            # Parse title style
            title_style_element = tx_styles_element.find(".//p:titleStyle", namespaces=self.nsmap)
            if title_style_element is not None:
                title_style = self._parse_text_style_element(title_style_element)
            
            # Parse body style AND its level-specific list styles
            body_style_element = tx_styles_element.find(".//p:bodyStyle", namespaces=self.nsmap)
            if body_style_element is not None:
                body_style = self._parse_text_style_element(body_style_element)
                # Parse individual levels for bullet properties
                list_styles = self._parse_list_styles_from_body(body_style_element)
            
            # Parse other style
            other_style_element = tx_styles_element.find(".//p:otherStyle", namespaces=self.nsmap)
            if other_style_element is not None:
                other_style = self._parse_text_style_element(other_style_element)
        
        return title_style, body_style, other_style, list_styles

    def _parse_text_style_element(self, style_element) -> ParagraphProperties | None:
        """Parse a single text style element (titleStyle, bodyStyle, otherStyle).
        
        Args:
            style_element: XML element containing text style properties
            
        Returns:
            ParagraphProperties with default run properties containing font size
        """
        # Look for default paragraph properties (defPPr)
        def_p_pr_element = style_element.find(".//a:defPPr", namespaces=self.nsmap)
        if def_p_pr_element is not None:
            # Create ParagraphProperties object
            props = ParagraphProperties()
            
            # Parse paragraph-level properties
            if def_p_pr_element.get("algn") is not None:
                props.align = def_p_pr_element.get("algn")
            
            # Parse default run properties (defRPr) - this is where font size is usually defined
            def_rpr_element = def_p_pr_element.find(".//a:defRPr", namespaces=self.nsmap)
            if def_rpr_element is not None:
                props.default_run_properties = self._parse_default_run_properties(def_rpr_element)
            
            return props
        
        # Check for level 1 paragraph properties (lvl1pPr) - Galaxy presentation uses this structure
        lvl1_element = style_element.find(".//a:lvl1pPr", namespaces=self.nsmap)
        if lvl1_element is not None:
            props = ParagraphProperties()
            # Parse paragraph-level properties
            if lvl1_element.get("algn") is not None:
                props.align = lvl1_element.get("algn")
                
            # Parse default run properties (defRPr) - this is where font size is defined
            def_rpr_element = lvl1_element.find(".//a:defRPr", namespaces=self.nsmap)
            if def_rpr_element is not None:
                props.default_run_properties = self._parse_default_run_properties(def_rpr_element)
            
            return props
        
        # Also check for list style elements in text styles - sometimes font sizes are defined here
        list_style_element = style_element.find(".//a:lstStyle", namespaces=self.nsmap)
        if list_style_element is not None:
            # Look for level 0 paragraph properties
            lvl0_element = list_style_element.find(".//a:lvl1pPr", namespaces=self.nsmap)
            if lvl0_element is not None:
                props = ParagraphProperties()
                def_rpr_element = lvl0_element.find(".//a:defRPr", namespaces=self.nsmap)
                if def_rpr_element is not None:
                    props.default_run_properties = self._parse_default_run_properties(def_rpr_element)
                return props
        
        return None

    def _parse_default_run_properties(self, def_rpr_element) -> RunProperties:
        """Parse default run properties (defRPr) from a level element.

        This extracts font size and other run properties for the inheritance hierarchy.

        Args:
            def_rpr_element: XML element containing default run properties

        Returns:
            RunProperties: Parsed run properties with font size and other attributes
        """
        run_props = RunProperties()

        # Parse font size (sz attribute) - most important for hierarchy
        if def_rpr_element.get("sz") is not None:
            run_props.font_size = int(def_rpr_element.get("sz"))
        else:
            # No font size specified in this element
            pass

        # Parse other run properties that can be inherited
        if def_rpr_element.get("b") == "1":
            run_props.bold = True

        if def_rpr_element.get("i") == "1":
            run_props.italic = True

        if def_rpr_element.get("cap") is not None:
            run_props.cap = def_rpr_element.get("cap")

        # Parse font face (explicit font)
        latin_font_element = def_rpr_element.find(".//a:latin", namespaces=self.nsmap)
        if latin_font_element is not None:
            typeface = latin_font_element.get("typeface")
            if typeface in ["+mj-lt", "+mj-ea", "+mj-cs"]:
                # This is a major font reference
                run_props.font_ref = "major"
            elif typeface in ["+mn-lt", "+mn-ea", "+mn-cs"]:
                # This is a minor font reference
                run_props.font_ref = "minor"
            else:
                # This is a literal font face
                run_props.font_face = typeface

        # Parse font reference (theme-based font)
        font_ref_element = def_rpr_element.find(".//a:fontRef", namespaces=self.nsmap)
        if font_ref_element is not None:
            run_props.font_ref = font_ref_element.get("idx")  # "major" or "minor"

        # Parse color
        solid_fill_element = def_rpr_element.find(
            ".//a:solidFill", namespaces=self.nsmap
        )
        if solid_fill_element is not None:
            srgb_color_element = solid_fill_element.find(
                ".//a:srgbClr", namespaces=self.nsmap
            )
            if srgb_color_element is not None:
                run_props.color = srgb_color_element.get("val")
            else:
                scheme_color_element = solid_fill_element.find(
                    ".//a:schemeClr", namespaces=self.nsmap
                )
                if scheme_color_element is not None:
                    run_props.scheme_color = scheme_color_element.get("val")

        return run_props

    def _parse_list_styles_from_body(self, body_style_element) -> dict[int, ParagraphProperties]:
        """Parse individual level properties from bodyStyle to extract bullet information.
        
        Args:
            body_style_element: The <p:bodyStyle> XML element
            
        Returns:
            Dictionary mapping level (0-based) to ParagraphProperties with bullet info
        """
        list_styles = {}
        
        # Parse each level (lvl1pPr, lvl2pPr, etc.)
        for level in range(9):  # PowerPoint supports up to 9 levels
            if level == 0:
                level_element = body_style_element.find(".//a:lvl1pPr", namespaces=self.nsmap)
            else:
                level_element = body_style_element.find(f".//a:lvl{level+1}pPr", namespaces=self.nsmap)
            
            if level_element is not None:
                props = ParagraphProperties()
                
                # Parse paragraph-level properties
                if level_element.get("algn") is not None:
                    props.align = level_element.get("algn")
                if level_element.get("marL") is not None:
                    props.margin_left = int(level_element.get("marL"))
                if level_element.get("indent") is not None:
                    props.indent = int(level_element.get("indent"))
                
                # Parse bullet properties - this is the key part!
                props.bullet_type = self._extract_bullet_type(level_element)
                if props.bullet_type == "char":
                    props.bullet_char = self._extract_bullet_char(level_element)
                    props.bullet_font_face = self._extract_bullet_font(level_element)
                elif props.bullet_type == "autoNum":
                    props.bullet_auto_num_type = self._extract_bullet_auto_num_type(level_element)
                elif props.bullet_type == "none":
                    # Explicitly no bullet
                    pass
                
                # Parse default run properties for this level
                def_rpr_element = level_element.find(".//a:defRPr", namespaces=self.nsmap)
                if def_rpr_element is not None:
                    props.default_run_properties = self._parse_default_run_properties(def_rpr_element)
                
                list_styles[level] = props
        
        return list_styles
    
    def _extract_bullet_type(self, level_element) -> str | None:
        """Extract bullet type from a level element."""
        # Check for buNone (no bullet)
        if level_element.find(".//a:buNone", namespaces=self.nsmap) is not None:
            return "none"
        
        # Check for buChar (character bullet)
        if level_element.find(".//a:buChar", namespaces=self.nsmap) is not None:
            return "char"
        
        # Check for buAutoNum (auto numbering)
        if level_element.find(".//a:buAutoNum", namespaces=self.nsmap) is not None:
            return "autoNum"
        
        # Check for buBlip (image bullet)
        if level_element.find(".//a:buBlip", namespaces=self.nsmap) is not None:
            return "blip"
        
        # No bullet specified - could inherit from higher level
        return None
    
    def _extract_bullet_char(self, level_element) -> str | None:
        """Extract bullet character from buChar element."""
        bu_char_element = level_element.find(".//a:buChar", namespaces=self.nsmap)
        if bu_char_element is not None:
            return bu_char_element.get("char", "•")  # Default to bullet if no char specified
        return None
    
    def _extract_bullet_font(self, level_element) -> str | None:
        """Extract bullet font from buFont element."""
        bu_font_element = level_element.find(".//a:buFont", namespaces=self.nsmap)
        if bu_font_element is not None:
            return bu_font_element.get("typeface", "Arial")  # Default to Arial
        return None
    
    def _extract_bullet_auto_num_type(self, level_element) -> str | None:
        """Extract auto numbering type from buAutoNum element."""
        bu_auto_num_element = level_element.find(".//a:buAutoNum", namespaces=self.nsmap)
        if bu_auto_num_element is not None:
            return bu_auto_num_element.get("type", "arabicPeriod")  # Default
        return None

    def parse_master(self) -> SlideMaster:
        master_name = None
        cSld_element = self.root.find(".//p:cSld", namespaces=self.nsmap)
        if cSld_element is not None:
            master_name = cSld_element.get("name")

        background_color, background_gradient_fill, background_reference = self._extract_background_properties()
        title_style, body_style, other_style, list_styles = self._parse_text_styles()

        return SlideMaster(
            name=master_name,
            background_color=background_color,
            background_gradient_fill=background_gradient_fill,
            background_reference=background_reference,
            title_style=title_style,
            body_style=body_style,
            other_style=other_style,
            list_styles=list_styles,
        )