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

# DrawingML Shapes

Overview

A shape can appear in each of the document types. There is an important distinction to keep in mind, however, regarding shapes and document types. Shapes within wordprocessing documents are implemented differently from shapes within spreadsheets and presentations, and this is reflected in the ECMA specification. Shapes within spreadsheets are specified with a <xdr:sp> (shape) element as defined within the spreadsheetML drawingML specification at section 20.5 of the ECMA specification; the shape element is within the xmlns:xdr="http://schemas.openxmlformats.org/drawingml/2006/speadsheetDrawing" namespace. Similarly, shapes within presentations are specified with a <p:sp> (shape) element as defined within the presentation specification at section 19 of the ECMA specification; the shape element is within the xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" namespace. Each of these shapes is inserted into its respective document type using the placement method as discussed at [Placement within Spreadsheets](drwPicInSpread.php) and [Placement within Presentations](drwPicInPresentation.php). In short, spreadsheets put shapes within one of the three anchoring tags, and the entire drawingML object or shape is placed within a separate drawing part. Presentations put shapes inline with the other content for the slide, and they are contained within a <p:spTree> or <p:grpSp> element. For each of these document types, although the placement within the document varies by document type, the actual details of the shape itself are the same in most respects. Word processing documents implement shapes differently both with respect to placement within the document and to details of the shape.

In earlier versions of Microsoft Word, shapes are implemented with VML. With Word 2010 both VML and drawingML are included in the XML for the document, using <mc:AlternateContent> with a pair of child elements: <mc:Choice Requires="wps">, which contains the drawingML XML, and <mc:Fallback>, which contains the VML. The wps for the Requires attribute refers to the Microsoft namespace for word processing shapes: xmlns:wps="http://schemas.microsoft.com/office/word/2010/wordprocessingShape". So if the application supports that shapes namespace, then the drawingML XML is used; otherwise the VML is used. Within the drawingML choice there is a container <w:drawing> element. That is positioned within the document using the method outlined at [Positioning within a Word Processing Document](drwPicInWord.php), placing the object either inline or anchored at a particular position. The actual specification of the shape is contained within a <a:graphicData> element, which is a generic container for all sorts of possible graphic content. That element has a uri attribute which specifies the "server" that can process the data type. For shapes in Word, the uri value is the same as the wordprocessing shapes namespace shown above. So for newer versions of Word, shapes are positioned in the document just as pictures or images are positioned, but the actual details of the shape are in a namespace different from spreadsheets and presentations, and the details are specific to Microsoft (or any other vendor which supports shapes in word processing). For this reason, the discussion here will focus only on shapes within spreadsheets and presentations, since those are defined as part of the ECMA OOXML specification. Note, however, that the content model for shapes in Word seems to be close to the model for shapes in spreadsheets and presentations, with differences in the model relating to the text within shapes.

Shapes are specified with a <xdr:sp> or <p:sp> element. Shapes can be either based on a preset geometry or on a custom geometry. There are four basic components of a shape, corresponding to the four child elements:

1. <nvSpPr> - non-visual shape properties. See [Shapes - Non-Visual Properties](drwSp-nvSpPr.php).
2. <spPr> - shape properties. See [Shapes - Shape Properties](drwSp-SpPr.php).
3. <style> - shape styles. See [Shapes - Styles](drwSp-styles.php).
4. <txBody> - text within the shape. See [Shapes - Text](drwSp-text.php).

Below is an example of a shape within a spreadsheet document.

<xdr:sp macro="" textlink="">

  

<xdr:nvSpPr>

<xdr:cNvPr id="2" name="Rounded Rectangle 1"/>

<xdr:cNvSpPr/>

</xdr:nvSpPr>

  

<xdr:spPr>

<a:xfrm>

<a:off x="1371600" y="514350"/>

<a:ext cx="1038225" cy="542925"/>

</a:xfrm>

<a:prstGeom prst="roundRect">

<a:avLst/>

</a:prstGeom>

</xdr:spPr>

  

<xdr:style>

<a:lnRef idx="2">

<a:schemeClr val="accent1">

<a:shade val="50000"/>

</a:schemeClr>

</a:lnRef>

<a:fillRef idx="1">

<a:schemeClr val="accent1"/>

</a:fillRef>

<a:effectRef idx="0">

<a:schemeClr val="accent1"/>

</a:effectRef>

<a:fontRef idx="minor">

<a:schemeClr val="lt1"/>

</a:fontRef>

</xdr:style>

  

<xdr:txBody>

<a:bodyPr vertOverflow="clip" rtlCol="0" anchor="ctr"/>

<a:lstStyle/>

<a:p>

<a:pPr algn="ctr"/>

<a:endParaRPr lang="en-US" sz="1100"/>

</a:p>

</xdr:txBody>

  

</xdr:sp>

![Shape in spreadsheet](images/drwSp.gif)

Reference: ECMA-376, 3rd Edition (June, 2011), Fundamentals and Markup Language Reference § 19.3.1.43 (presentations) and § 20.5.2.29 (spreadsheets).

Shapes can have the following attributes.

| Attribute | Description |
| --- | --- |
| fLocksText (in spreadsheets only) | Indicates whether to allow text editing within the space when the worksheet is protected. |
| fPublished (in spreadsheets only) | Indicates whether the shape should be published with the worksheet when sent to the server. |
| macro (in spreadsheets only) | Specifies a custom function associated with the shape. E.g., macro="DoWork()". |
| textlink (in spreadsheets only) | Specifies a formula linking to spreadsheet cell data. |
| useBgFill (in presentations only) | Specifies that the shape fill should be the same as that of the slide background. Note that this does not set the shape to be transparent--it sets the fill to be the same as the portion of the background that is behind the shape. |

  

[About this site](aboutThisSite.php) | [Contact us](contactUs.php)
  
Copyright © 2023. All Rights Reserved.