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

Text - Spacing, Indents and Margins

## Vertical Line Spacing within a Paragraph

Vertical spacing between lines within a paragraph of text in a shape is specified with the <a:lnSpc> element within the <a:pPr> element for the paragraph. Spacing can be specified as either a percentage or as point size. A percentage is specified using the <a:spcPct> as a child element of <a:lnSpc>). The percentage is based on the run that has the largest size in the paragraph. Spacing in terms of point size is specified using the <a:spcPts> as a child element of <a:lnSpc>), with 100 equal to 1 point and 1200 equal to 12 points. Both child elements specify the actual value within the val attribute. If line spacing is not specified, then the spacing is determined by the size of the largest piece of text in the line. Below is a sample shape with line spacing set to double spacing or 200%.

<a:pPr>

<a:lnSpc>

<a:spcPct val="200000"/>

</a:lnSpc>

</a:pPr>

![Shape with text - line spacing](images/drwSp-text-vertSpace1.gif)

## Space before and after a Paragraph

Spacing before and after paragaphs within a shape are specified with the elements <a:spcBef> and <a:spcAft>, respectively. Each may be specified as a percentage or in points using the child elements <a:spcPct> and <a:spcPts>. Below is a shape with two paragraphs and space after the paragraph specified as 12 points.

<a:pPr>

<a:spcAft>

<a:spcPts val="1200"/>

</a:spcAft>

</a:pPr>

![Shape with text - line spacing](images/drwSp-text-spcAft.gif)

## Margins

The left and right margins for a paragraph of text in a shape are specified with the marL and marR attributes on the <a:pPr> element, respectively. These margins are in addition to the text body inset. See [Text Body Properties - Positioning and Insets](drwSp-text-bodyPr-inset.php). The margin values are between 0 and 51206400. Below is a shape with two paragraphs; the first paragraph has a left margin set at 1/2 inch (marL="457200").

<a:pPr marL="457200">

<a:spcAft>

<a:spcPts val="1200"/>

</a:spcAft>

</a:pPr>

![Shape with text - margins](images/drwSp-text-margins.gif)

## Indent

Indentation for the first line of text in a paragraph is specified with the indent attribute on the <a:pPr> element. The value is specified in EMUs, and if the attribute is omitted, then a value of -342900 is implied. Below is the same shape and text as above, except that an indent of .3 inches has been applied to the first paragraph.

<a:pPr marL="457200" indent="274320">

<a:spcAft>

<a:spcPts val="1200"/>

</a:spcAft>

</a:pPr>

![Shape with text - margins](images/drwSp-text-indent.gif)

  

[About this site](aboutThisSite.php) | [Contact us](contactUs.php)
  
Copyright © 2023. All Rights Reserved.