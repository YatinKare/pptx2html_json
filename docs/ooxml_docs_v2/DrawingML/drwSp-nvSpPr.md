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

Non-Visual Properties

The <nvSpPr> element within the <sp> element specifies the non-visual
properties of a shape. The actual properties are within child elements - <cNvPr> (for Id, name, title, and
description and hidden) and <cNvSpPr> (locking properties and text box).
Presentations also have a third child element <nvPr> (for multimedia associated with a shape and for placeholders within slide layouts and slide masters).

Note that the non-visual properties are in different namespaces, depending on the document type.
The examples show the spreadsheet drawingML namespace with prefix 'xdr'. For presentations the non-visual properties are in the main presentationML
namespace with prefix 'p'.

<xdr:sp macro="" textlink="">

<xdr:nvSpPr>

<xdr:cNvPr id="2" name="Rounded Rectangle 1"/>

<xdr:cNvSpPr/>

</xdr:nvSpPr>

. . .

</xdr:sp>

Reference: ECMA-376, 3rd Edition (June, 2011), Fundamentals and Markup Language Reference § 19.3.1.34 (presentations) and § 20.5.2.23 (spreadsheets).

## Id, Name, Title and Description

An id, name, title and description for a picture can be specified with attributes on the <cNvPr> element: <cNvPr id="222" name="Rounded Rectangle 1" title="My Shape" descr="This is the description"/>. The id is an integer and specifies a unique identifier. The name is a string. The title is a string that specifies the caption. The descr is alternative text used for assistive technologies which do not display the object. Finally, note that <cNvPr> can have child elements <hlinkClick> and <hlinkhover> for links that are not covered here.

Reference: ECMA-376, 3rd Edition (June, 2011), Fundamentals and Markup Language Reference § 19.3.1.12 (presentations) and § 20.5.2.8 (spreadsheets).

## Hidden

A shape can be hidden by specifying the hidden attribute on the <cNvPr> element: <cNvPr hidden="true">. However, note that an application can have settings that allow the object to be displayed.

## Shape Resizing, Cropping, Rotating, Changing Aspect Ratio, Moving, Selecting

The locking properties of a shape are specified with the <spLocks> element within the <cNvSpPr> element. Various aspects of a shape's size can be specified with attributes on <spLocks>. If the attributes are not specified, then it is assumed that the properties can be changed. For example, to disallow changing the aspect ratio, specify the noChangeAspect attribute as true.

The following are the most useful attributes:

* noAdjustHandles (the application should not show adjust handles)
* noChangeArrowHandles (the application should not allow arrowhead changes)
* noChangeAspect
* noChangeShapeType
* noEditPoints (the application should not allow shape point changes)
* noGrp (disallow shape grouping)
* noMove
* noResize
* noRot (no rotation)
* noSelect
* noTextEdit

Reference: ECMA-376, 3rd Edition (June, 2011), Fundamentals and Markup Language Reference § 19.3.1.13 (presentations) and § 20.5.2.9 (spreadsheets).

## Text Boxes

The <cNvSpPr> element has a txBox attribute which specifies that the shape is a text box. The value is a boolean. However, it is important to note that a shape can still have text attached to it even if this attribute is not specified as true. A text box is just a specialized shape with specific properties.

## Multimedia in Presentations

Multimedia can be associated with an object using child elements of <nvPr>. The various media types specified in child elements include <audioCd>, <audioFile>, <quickTimeFile>, <videoFile>, <waveAudioFile>. The details for these media types are not covered here.

  

[About this site](aboutThisSite.php) | [Contact us](contactUs.php)
  
Copyright © 2023. All Rights Reserved.