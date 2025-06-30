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

# DrawingML Pictures

Overview

A picture can be added to a word processing document, a spreadsheet, or a presentation.
Adding a picture to any of these document types requires two components--(1) information about the picture itself, and (2) information about its placement
within the document. The former is common to all document types, and much of the XML for this information is within the main drawingML namespace
(xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main").
The information regarding placement and positioning within a document, including the high-level elements and the non-visual properties, is
specified in separate namespaces and varies based upon the document type . See [DrawingML Overview](drwOverview.php) for more on the namespaces.

A picture is specified with a <pic> element. The namespace in wordprocessing documents is in the picture namespace of drawingML
xmlns:pic="http://schemas.openxmlformats.org/drawingml/2006/picture". This is what is used for most of the sample XML on these pages.
In spreadsheets, it is the spreadsheet drawingML namespace xmlns:xdr="http://schemas.openxmlformats.org/drawingml/2006/spreadsheetDrawing".
In presentations it is in the main presentation namespace xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main".

A picture can have such characteristics as border, resizing behavior, overlaid fills, and other effects.
A sample picture within a word processing document is shown below.

<pic:pic xmlns:pic="http://schemas.openxmlformats.org/drawingml/2006/picture">

<pic:nvPicPr>

<pic:cNvPr id="0" name="Blue hills.jpg"/>

<pic:cNvPicPr/>

</pic:nvPicPr>

<pic:blipFill>

<a:blip r:embed="rId4" cstate="print"/>

<a:stretch>

<a:fillRect/>

</a:stretch/>

</pic:blipFill>

<pic:spPr>

<a:xfrm>

<a:off x="0" y="0"/>

<a:ext cx="2438400" cy="1828800"/>

</a:xfrm>

<a:prstGeom rst="rect>

<a:avLst/>

</a:prstGeom>

</pic:spPr>

</pic:pic>

Reference: ECMA-376, 3rd Edition (June, 2011), Fundamentals and Markup Language Reference
§ 20.2.2.5 (word processing), § 20.5.2.25 (spreadsheets), and § 19.3.1.37 (presentations).

### Elements:

A picture has three basic components--the fill or content that fills up the picture rectangle, non-visual properties, and shape properties.
Spreadsheets and presentations also have associated styles. These components are specified with the elements below.

| Element | Description |
| --- | --- |
| blipFill [BLIP = binary large image or picture] | Specifies the type of picture fill that the picture has. A picture has a fill already, but if the picture has transparent pixels, it is possible to add another fill within the <spPr> element by specifying, for example, a gradient fill. See [Image Data](drwPic-ImageData.php), [Tile or Stretch Image to Fill](drwPic-tile.php), and [Effects](drwPic-effects.php) for details of blipFill.  Reference: ECMA-376, 3rd Edition (June, 2011), Fundamentals and Markup Language Reference § 20.2.2.1. |
| nvPicPr | Specifies non-visual properties of a picture, such as locking properties, name, id and title, and whether the picture is hidden. See [Non-Visual Properties](drwPic-nvPicPr.php) for details.  Reference: ECMA-376, 3rd Edition (June, 2011), Fundamentals and Markup Language Reference § 20.2.2.4. |
| spPr | Specifies the visual shape properties that can be applied to a picture. They are the same properties that can be applied to shapes. See [Shapes - Visual Properties](drwSp-SpPr.php) for more.  Reference: ECMA-376, 3rd Edition (June, 2011), Fundamentals and Markup Language Reference § 20.2.2.6. |
| style (only in spreadsheets and presentations) | Specifies the style that is applied to a picture or shape and the references for each of the style components, such as lines, fills, fonts, and effects. See [Shapes - Styles](drwSp-styles.php) for more.  Reference: ECMA-376, 3rd Edition (June, 2011), Fundamentals and Markup Language Reference § 19.3.1.46 and § 20.5.2.31. |

A <xrd:pic> element within a spreadsheet document can have the following attributes.

### Attributes:

| Attribute Value | Description |
| --- | --- |
| fPublished (spreadsheets only) | Indicates whether the picture should be published with the worksheet when sent to the server. |
| macro (spreadsheets only) | Specifies a function associated with the object. E.g., macro="DoWork()". |

---

---

# Related HTML/CSS Property:

There is no corresponding HTML property.

  

[About this site](aboutThisSite.php) | [Contact us](contactUs.php)
  
Copyright © 2023. All Rights Reserved.