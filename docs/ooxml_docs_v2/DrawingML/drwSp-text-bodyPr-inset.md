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

Text - Body Properties - Positioning and Insets

## Text Positioning or Anchoring:

The anchoring position of the text within a shape is specified with a anchor attribute on <a:bodyPr>. Possible values are:

* b (bottom of the bounding box)
* ctr (middle of the bounding box)
* dist (The text is distributed vertically. When text is horizontal, this spaces out the actual lines of text, which is identical to the value just below. When text is vertical, it distributes the letters vertically, which is different from just below because it always forces distribution of the words.)
* just (Text is justified vertically. When text is vertical, it justifies the letters vertically. This is different from dist above because in some cases, such as when there is very little text in a line, it does not justify.)
* t (top of the bounding box). This is the default.

Below is an example of positioning in the center (<a:bodyPr rtlCol="0" anchor="ctr" />), followed by positioning at the top (<a:bodyPr rtlCol="0" anchor="t" />).

![Shape with text - anchoring](images/drwSp-text-anchor1.gif)
![Shape with text - anchoring](images/drwSp-text-anchor2.gif)

Horizontal centering of the bounding box can be set using the anchorCtr attribute on <a:bodyPr>. Values are either true or false. This attribute causes the smallest possible bounding box for the text to be centered. It is different than paragraph alignment, which aligns the text within the bounding box. This attribute is appropriate for all the different vertical anchoring values. Below is a shape that has horizontal text, with paragraphs aligned right, vertical centering of the bounding box and no horizontal centering of the box.

<a:bodyPr vert="horz" rtlCol="0" anchor="ctr" anchorCtr="0"/>

![Shape with text - anchoring](images/drwSp-text-anchor3.gif)

Below is the same shape, but also with horizontal anchoring of the bounding box.

<a:bodyPr vert="horz" rtlCol="0" anchor="ctr" anchorCtr="1"/>

![Shape with text - anchoring](images/drwSp-text-anchor4.gif)

## Text Inset:

Insets of the bounding box are specified by four attributes on <a:bodyPr>, one for each side: bIns (bottom inset), tIns (top inset), lIns (left inset), and rIns (rightInset). Insets are used as internal margins for text boxes within shapes. The values of the attributes are specified either in EMUs or as a number immediately followed by the unit identifier--e.g., 0.5in. If an attribute is not specified for a side, a value of 45720 or 0.05 inches is implied.

Below is an example of a shape with inset at the bottom of .1 inch, .5 inch at the top, and none on the left and right.

<xdr:txBody>

<a:bodyPr rtlCol="0" anchor="ctr" bIns="91440" tIns="475200" lIns="0" rIns="0"/>

<a:lstStyle/>

. . .

</xdr:txBody>

![Shape with text - inset](images/drwSp-text-inset2.gif)

If the inset attributes are removed, we get the shape and text as shown below.

![Shape with text - inset](images/drwSp-text-inset1.gif)

  

[About this site](aboutThisSite.php) | [Contact us](contactUs.php)
  
Copyright © 2023. All Rights Reserved.