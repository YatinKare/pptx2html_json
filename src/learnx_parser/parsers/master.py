import os

from lxml import etree

from learnx_parser.models.core import (
    BackgroundReference,
    GradientFill,
    GradientStop,
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

    def parse_master(self) -> SlideMaster:
        master_name = None
        cSld_element = self.root.find(".//p:cSld", namespaces=self.nsmap)
        if cSld_element is not None:
            master_name = cSld_element.get("name")

        background_color, background_gradient_fill, background_reference = self._extract_background_properties()

        # For now, we're focusing on background properties only
        # Placeholder and list style parsing can be added later if needed
        return SlideMaster(
            name=master_name,
            background_color=background_color,
            background_gradient_fill=background_gradient_fill,
            background_reference=background_reference,
        )