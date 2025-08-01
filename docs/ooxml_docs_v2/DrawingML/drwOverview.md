![OfficeOpenXML.com](images/drawingMLbanner.png)

[Home](index.php) | [WordprocessingML (docx)](anatomyofOOXML.php) | [SpreadsheetML (xlsx)](anatomyofOOXML-xlsx.php) | [PresentationML (pptx)](anatomyofOOXML-pptx.php) | [DrawingML](drwOverview.php)

* [Overview](drwOverview.php)
* Pictures
  + [Overview](drwPic.php)
  + Image Properties
    - [Image Data](drwPic-ImageData.php)
    - [Tile or Stretch Image to Fill](drwPic-tile.php)
    - [Effects](drwPic-effects.php)
  + [Non-Visual Properties](drwPic-nvPicPr.php)
  + [Shape Properties](drwSp-SpPr.php)
* Shapes
  + [Overview](drwShape.php)
  + [Non-Visual Properties](drwSp-nvSpPr.php)
  + [Visual Properties](drwSp-SpPr.php)
    - [Size of Bounding Box](drwSp-size.php)
    - [Location of Bounding Box](drwSp-location.php)
    - Geometry
      * [Preset](drwSp-prstGeom.php)
      * [Custom](drwSp-custGeom.php)
    - [Shape Fill](drwSp-shapeFill.php)
      * [Solid Fill](drwSp-SolidFill.php)
      * [Picture Fill](drwSp-PictFill.php)
      * [Gradient Fill](drwSp-GradFill.php)
      * [Pattern Fill](drwSp-PattFill.php)
      * [Group Fill](drwSp-grpFill.php)
    - [Effects](drwSp-effects.php)
    - [Outline Style](drwSp-outline.php)
    - [2D Transforms](drwSp-rotate.php)
    - 3-D
      * [Shape Properties](drwSp-3dProps.php)
      * [Scene Properties](drwSp-3dScene.php)
  + [Styles](drwSp-styles.php)
  + [Text](drwSp-text.php)
    - [Text Body Properties](drwSp-text-bodyPr.php)
      * [Positioning and Insets](drwSp-text-bodyPr-inset.php)
      * [Fit, Wrap, Warp and 3D](drwSp-text-bodyPr-fit.php)
      * [Columns, Vertical Text and Rotation](drwSp-text-bodyPr-columns.php)
    - [Paragraphs](drwSp-text-paragraph.php)
      * [Paragraph Properties](drwSp-text-paraProps.php)
        + [Bullets and Numbering](drwSp-text-paraProps-numbering.php)
        + [Spacing, Indent and Margins](drwSp-text-paraProps-margins.php)
        + [Alignment, Tabs, Other](drwSp-text-paraProps-align.php)
      * [Run Properties](drwSp-text-runProps.php)
    - [List Properties](drwSp-text-lstPr.php)
* [Connectors](drwCxnSp.php)
  + [Non-Visual Properties](drwSp-nvCxnSpPr.php)
* [Text](drwSp-textbox.php)
* Charts
* Diagrams
* [Tables](drwTable.php)
  + [Defining Structure](drwTableGrid.php)
  + [Rows, Cells, Cell Content](drwTableRowAndCell.php)
  + Cell Properties
    - [Alignment, Margins, Direction](drwTableCellProperties-alignment.php)
    - [Borders and Fill](drwTableCellProperties-bordersFills.php)
  + [Table Styles and Properties](drwTableStyles.php)
* Placement within Docs
  + [Overview](drwPicInWord.php)
  + [Inline Objects](drwPicInline.php)
  + [Floating Objects](drwPicFloating.php)
    - [Positioning](drwPicFloating-position.php)
    - [Text Wrapping](drwPicFloating-textWrap.php)
* Placement within Spreadsheets
  + [Overview](drwPicInSpread.php)
  + [Absolute Anchoring](drwPicInSpread-absolute.php)
  + [One Cell Anchoring](drwPicInSpread-oneCell.php)
  + [Two Cell Anchoring](drwPicInSpread-twoCell.php)
* [Placement within Presentations](drwPicInPresentation.php)

# DrawingML Overview

DrawingML is the language for defining graphical objects such as pictures, shapes, charts, and diagrams within ooxml documents. It also specifies package-wide appearance characteristics, i.e., the package's theme. DrawingML is not a standalone markup language; it supports and appears within wordprocessingML, spreadsheetML, and presentationML documents. DrawingML is distinct from SVG and VML. SVG (scaleable vector graphics) is a graphics file format for two-dimensional graphics in XML. It is used mostly on the web and in desktop publishing. VML is a competing language for vector graphic files. It is now largely deprecated in favor of SVG. According to the ECMA OOXML specification, "The DrawingML format is a newer and richer format created with the goal of eventually replacing any uses of VML in the Office Open XML formats. VML is a transitional format; it is included in Office Open XML for legacy reasons only." VML is still used extensively within Microsoft Word for certain graphic comnponents, in particular for things as shapes and text boxes.

DrawingML is a sprawling, confusing set of specifications for a number of different visual components within office documents. It is composed of a number of different namespaces, and care must be taken to be sure you have the correct namespace and namespace prefix for a given element within a particular document type. One must also be mindful of the differences between specification of the object and placement of the object within the document. Sometimes the definition (and namespace) of the object is the same throughout the three document types and only the specification of placement varies from document type to document type. In other cases, both the object and placement are unique to each document type.

Below is a brief summary of the various object types within the three document types and their corresponding namespaces. DrawingML objects such as charts and diagrams in any document type are all placed within a <a:graphic> element, which in turn contains a <a:graphicData> element. These elements are part of the main drawingML namespace: xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main". The <a:graphicData> element is essentially undefined, so applications can support or not support the particular object that is defined within it. The element has a uri attribute which is used to specify the type of data and/or "server" that can process the contents of the element. For example, the uri for a picture within Word is "http://schemas.openxmlformats.org/drawingml/2006/picture". Microsoft Office supports a set of objects, including charts, diagrams, locked canvas, table, ole, etc. Other applications will have their own set of supported object types.

|  | WordProcessing |
| --- | --- |
| Pictures | The picture object is defined with other content in the content part, document.xml, within the <pic:pic> element. This is wrapped within a <w:drawing> element within the regular wordprocessing namespace: xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main".  The namespace for the picture definition is xmlns:pic="http://schemas.openxmlformats.org/drawingml/2006/picture".  The XML for placement of the picture (e.g., whether it is inline [<wp:inline>] or anchored [<wp:anchor>]) is within the wordprocessing drawingML namespace: xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing". |
| Shapes | See textboxes below. |
| Charts | A diagram is defined outside of the regular content (document.xml) part and is instead defined in a separate part (one for each chart), chart1.xml (or chart2.xml, etc.).  The chart is placed in the document.xml within a <a:graphicData> element, as noted above, by placing a reference to the chart part in an attribute of <a:graphicData>. The namespace (and uri attribute value of <a:graphicData>) for the diagram specification is xmlns:dgm="http://schemas.openxmlformats.org/drawingml/2006/chart".  The XML for placement of the chart (e.g., whether it is inline [<wp:inline>] or anchored [<wp:anchor>]) is within the wordprocessing drawingML namespace: xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing". |
| Diagrams | A diagram is defined outside of the regular content (document.xml) part and is instead defined in a group of four separate parts (one group for each diagram): colors#.xml, data#.xml, layout#.xml, and quickStyle#.xml. There is also a fifth part, drawing#.xml, which Microsoft added as an extension for persisting diagram layout information.  The diagram is placed in the document.xml within a <a:graphicData> element, as noted above, by placing references to the diagram parts using a <dgm:relIds> element. The namespace (and uri attribute value of <a:graphicData>) for the diagram specification is xmlns:dgm="http://schemas.openxmlformats.org/drawingml/2006/diagram".  The XML for placement of the diagram (e.g., whether it is inline [<wp:inline>] or anchored [<wp:anchor>]) is within the wordprocessing drawingML namespace: xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing". |
| Textboxes | Shapes and textboxes in Microsoft Word 2003 and 2007 are implemented with VML, which has been largely deprecated and is not covered on this site. With Word 2010, Microsoft has moved toward using the same data structures that are used for diagrams and charts. Word 2010 includes both VML and drawingML in the XML for the document, using <mc:AlternateContent> with a pair of child elements: <mc:Choice Requires="wps">, which contains the drawingML xml, and <mc:Fallback>, which contains the VML. The wps for the Requires attribute refers to the new namespace word wordprocessing shapes (as well as to the uri attribute value of <a:graphicData>): xmlns:wps="http://schemas.microsoft.com/office/word/2010/wordprocessingShape".  Textboxes and shapes are inserted within the <a:graphicData> element, using a <wps:wsp> element. The extensions by Microsoft of drawingML for Word are not covered in detail here. Finally, note that text frames are similar to text boxes in many ways, but their underlying XML is very different. They are not part of drawingML. Instead they are within wordprocessingML and their specification is part of the specification of a paragraph. See [WordprocessingML - Text Frames](WPparagraph-textFrames.php). |
| Themes | Themes enable common styling across document types and are defined within the main drawingML namespace: xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main". They are defined in a separate theme1.xml part. |

|  | Spreadsheet |
| --- | --- |
| Pictures | A picture is placed within a worksheet by a <drawing> element, which merely references a separate drawing1.xml (or drawing2.xml, etc.) part. Placement or anchoring of the picture is specified with within the drawing part using the desired anchor (e.g., <xdr:twoCellAnchor> element). The drawing part contains the <xdr:pic> element, which defines the picture.  The namespace is xmlns:xdr="http://schemas.openxmlformats.org/drawingml/2006/spreadsheetDrawing". Note that it is is not within a <a:graphicData> element. |
||  |  |
| --- | --- |
| Shapes | A shape is placed within a worksheet by a <drawing> element, which merely references a separate drawing1.xml (or drawing2.xml, etc.) part. Placement or anchoring of the chart is specified with the desired anchor (e.g., <xdr:twoCellAnchor> element) within the drawing part using the xmlns:xdr="http://schemas.openxmlformats.org/drawingml/2006/speadsheetDrawing" namespace. The drawing part in turn contains an <xdr:sp> element which defines the shape. Note that it is is not within a <a:graphicData> element. |
| Charts | A chart is placed within a worksheet by a <drawing> element, which merely references a separate drawing1.xml (or drawing2.xml, etc.) part. Placement or anchoring of the chart is specified with the desired anchor (e.g., <xdr:twoCellAnchor> element) within the drawing part using the xmlns:xdr="http://schemas.openxmlformats.org/drawingml/2006/speadsheetDrawing" namespace.  The drawing part in turn contains the typical <a:graphicData> element noted above, which contains a <c:chart> element. That element references a separate part chart1.xml (or chart2.xml, etc) which defines the chart.  The namespace (and uri attribute value of <a:graphicData>) for the chart specification is xmlns:c="http://schemas.openxmlformats.org/drawingml/2006/chart". |
| Diagrams | A diagram is placed within a worksheet by a <drawing> element, which merely references a separate drawing1.xml (or drawing2.xml, etc.) part. Placement or anchoring of the diagram is specified with the desired anchor (e.g., <xdr:twoCellAnchor> element) within the drawing part using the xmlns:xdr="http://schemas.openxmlformats.org/drawingml/2006/speadsheetDrawing" namespace.  The drawing part in turn contains the typical <a:graphicData> element noted above, which contains a <dgm:relIds> element. That element references a group of four separate parts (one group for each diagram): colors#.xml, data#.xml, layout#.xml, and quickStyle#.xml which together define the diagram. There is also a fifth part, drawing#.xml, which Microsoft added as an extension for persisting diagram layout information.  The namespace (and uri attribute value of <a:graphicData>) for the diagram specification is xmlns:dgm="http://schemas.openxmlformats.org/drawingml/2006/diagram". |
| Textboxes | Textboxes are created by inserting text into shapes. See shapes in spreadsheets, above. |
| Themes | Themes enable common styling across document types and are defined within the main drawingML namespace: xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main". They are defined in a separate theme1.xml part. |

|  | Presentation |
| --- | --- |
| Pictures | The picture object is defined with other content for the slide in slide1.xml (or slide2.xml, etc.), within a <p:pic> element.  The namespace is xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main". Note that it is is not within a <a:graphicData> element. |
||  |  |
| --- | --- |
| Shapes | A shape is defined with other content for the slide in slide1.xml (or slide2.xml, etc.) in a <p:sp> element. The namespace is xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main". Note that it is is not within a <a:graphicData> element. |
| Charts | A chart is placed within a slide by a <p:graphicFrame> element, which in turn contains the typical <a:graphicData> element noted above, which contains a <c:chart> element. That element references a separate part chart1.xml (or chart2.xml, etc) which defines the chart.  The namespace (and uri attribute value of <a:graphicData>) for the chart specification is xmlns:c="http://schemas.openxmlformats.org/drawingml/2006/chart". |
| Diagrams | A diagram is placed within a slide by a <p:graphicFrame> element, which in turn contains the typical <a:graphicData> element noted above, which contains a <dgm:relIds> element. That element references a group of four separate parts (one group for each diagram): colors#.xml, data#.xml, layout#.xml, and quickStyle#.xml which together define the diagram. There is also a fifth part, drawing#.xml, which Microsoft added as an extension for persisting diagram layout information.  The namespace (and uri attribute value of <a:graphicData>) for the diagram specification is xmlns:dgm="http://schemas.openxmlformats.org/drawingml/2006/diagram". |
| Text | Text is created by inserting text into shapes. See shapes in presentations, above. |
| Tables | OOXML has three different table models--one for wordprocessing tables, on for spreadsheet tables, and one for presentations. This last one is part of drawingML. A table is placed within a slide by a <p:graphicFrame> element, which in turn contains the typical <a:graphicData> element noted above, which contains an <a:tbl> element. That element contains the data for the table inline--the table is NOT in a separate part.  The uri attribute value of <a:graphicData> is "http://schemas.openxmlformats.org/drawingml/2006/table". The namespace for the table specification is the drawingML main namespace xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main". |
| Themes | Themes enable common styling across document types and are defined within the main drawingML namespace: xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main". They are defined in a separate theme1.xml part. |

The ECMA OOXML specification (3rd edition) for drawingML is broken up into different sections, mostly to reflect the different namespaces.

![ECMA Specification TOC for DrawingML](images/ecmaSpecTOC.gif)

There is a section (20.1) on most of the main features in the namespace xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main", including shapes, non-visual properties, colors, and styles. A different section (201.1) covers the remaining parts of the main drawingML namespace, including text and text formatting, bullets and numbering, and tables, all used mostly within presentation documents. There is a separate section (20.2) on pictures generally; the namespace for a picture varies with the document type. Then there is a section (21.2) for the chart namespace (xmlns:c="http://schemas.openxmlformats.org/drawingml/2006/chart") and a section (21.4) for the diagram namespace (mlns:dgm="http://schemas.openxmlformats.org/drawingml/2006/diagram"). There is a section (20.4) for placement/positioning of drawingML objects within wordprocessing documents (xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing"), and a section (20.5) for placement/positioning of drawingML objects within spreadsheet documents (xmlns:xdr="http://schemas.openxmlformats.org/drawingml/2006/spreadsheetDrawing). Finally, there are separate sections on locked canvases (20.3, not covered here) and on drawings within charts (21.3) (xmlns:cdr="http://schemas.openxmlformats.org/drawingml/2006/chartDrawing).

  

[About this site](aboutThisSite.php) | [Contact us](contactUs.php)
  
Copyright © 2023. All Rights Reserved.