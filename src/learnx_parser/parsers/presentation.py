from lxml import etree

from learnx_parser.models.core import ParagraphProperties, RunProperties


class PresentationParser:
    def __init__(self, presentation_xml_path):
        self.presentation_xml_path = presentation_xml_path
        self.tree = etree.parse(self.presentation_xml_path)
        self.root = self.tree.getroot()
        self.nsmap = self.root.nsmap

    def get_slide_order(self):
        slide_ids = []
        # Find the slide ID list
        sld_id_lst = self.root.find(".//p:sldIdLst", namespaces=self.nsmap)
        if sld_id_lst is not None:
            for sld_id in sld_id_lst.findall(".//p:sldId", namespaces=self.nsmap):
                slide_ids.append(
                    sld_id.get(
                        "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id"
                    )
                )
        return slide_ids

    def get_slide_size(self):
        sld_sz = self.root.find(".//p:sldSz", namespaces=self.nsmap)
        if sld_sz is not None:
            cx = int(sld_sz.get("cx", 0))
            cy = int(sld_sz.get("cy", 0))
            return cx, cy
        return 0, 0

    def get_default_text_style(self):
        """Parse presentation-level default text style (p:defaultTextStyle).

        Returns dict mapping level -> ParagraphProperties for theme-level inheritance.
        This implements step 4 of the OpenXML inheritance hierarchy.
        """
        default_text_styles = {}

        # Find p:defaultTextStyle element
        default_text_style = self.root.find(
            ".//p:defaultTextStyle", namespaces=self.nsmap
        )
        if default_text_style is not None:
            # Parse each level (lvl1pPr through lvl9pPr)
            for level in range(1, 10):  # Levels 1-9
                level_element = default_text_style.find(
                    f".//a:lvl{level}pPr", namespaces=self.nsmap
                )
                if level_element is not None:
                    level_props = ParagraphProperties()

                    # Parse alignment (algn attribute)
                    if level_element.get("algn") is not None:
                        level_props.align = level_element.get("algn")

                    # Parse other properties as needed
                    if level_element.get("indent") is not None:
                        level_props.indent = int(level_element.get("indent"))

                    # Parse bullet properties at presentation level
                    self._parse_bullet_properties_for_level(level_element, level_props)

                    # Parse default run properties (defRPr) for font size inheritance
                    def_rpr_element = level_element.find(
                        ".//a:defRPr", namespaces=self.nsmap
                    )
                    if def_rpr_element is not None:
                        level_props.default_run_properties = (
                            self._parse_default_run_properties(def_rpr_element)
                        )

                    # Store using 0-based indexing (level 1 -> index 0)
                    default_text_styles[level - 1] = level_props

        return default_text_styles

    def _parse_bullet_properties_for_level(self, level_element, level_props):
        """Parse bullet properties from a presentation-level lvlXpPr element.

        Args:
            level_element: XML element containing level properties
            level_props: ParagraphProperties object to update
        """
        # Check for buNone (no bullet)
        bu_none_element = level_element.find(".//a:buNone", namespaces=self.nsmap)
        if bu_none_element is not None:
            level_props.bullet_type = "none"
            return

        # Check for buChar (character bullet)
        bu_char_element = level_element.find(".//a:buChar", namespaces=self.nsmap)
        if bu_char_element is not None:
            level_props.bullet_type = "char"
            level_props.bullet_char = bu_char_element.get("char")

            # Get additional char bullet properties
            bu_font_element = level_element.find(".//a:buFont", namespaces=self.nsmap)
            if bu_font_element is not None:
                level_props.bullet_font_face = bu_font_element.get("typeface")

            bu_sz_pct_element = level_element.find(
                ".//a:buSzPct", namespaces=self.nsmap
            )
            if bu_sz_pct_element is not None:
                level_props.bullet_size_pct = int(bu_sz_pct_element.get("val"))

            bu_sz_pts_element = level_element.find(
                ".//a:buSzPts", namespaces=self.nsmap
            )
            if bu_sz_pts_element is not None:
                level_props.bullet_size_pts = int(bu_sz_pts_element.get("val"))
            return

        # Check for buAutoNum (auto numbering)
        bu_auto_num_element = level_element.find(
            ".//a:buAutoNum", namespaces=self.nsmap
        )
        if bu_auto_num_element is not None:
            level_props.bullet_type = "autoNum"
            level_props.bullet_auto_num_type = bu_auto_num_element.get("type")
            if bu_auto_num_element.get("startAt") is not None:
                level_props.bullet_start_at = int(bu_auto_num_element.get("startAt"))
            return

        # Check for buBlip (image bullet)
        bu_blip_element = level_element.find(".//a:buBlip", namespaces=self.nsmap)
        if bu_blip_element is not None:
            level_props.bullet_type = "blip"
            # Note: For presentation-level defaults, we can't resolve relationship IDs
            # since we don't have access to slide relationships here
            # This would need to be handled differently if needed
            return

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
            run_props.font_face = latin_font_element.get("typeface")

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
