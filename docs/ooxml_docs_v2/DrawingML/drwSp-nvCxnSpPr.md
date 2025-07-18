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

# DrawingML Connectors

Non-Visual Properties

The <nvCxnSpPr> element within the <cxnSp> element specifies the non-visual propeties of a connector. The actual properties are within child elements - <cNvPr> (for id, name, title, and description and hidden) and <cNvCxnSpPr> (locking properties and connector ends). Presentations also have a third child element <nvPr> (for multimedia associated with a connector).

<p:cxnSp>

<p:nvCxnSpPr>

<p:cNvPr id="9" name="Straight Arrow Connector 8"/>

<p:cNvCxnSpPr/>

<a:stCxn id="4" idx="3"/>

<a:endCxn id="5" idx="1"/>

</p:cNvCxnSpPr/>

</p:nvCxnSpPr>

. . .

</p:cxnSp>

Reference: ECMA-376, 3rd Edition (June, 2011), Fundamentals and Markup Language Reference § 19.3.1.29 (presentations) and § 20.5.2.19 (spreadsheets).

## Id, Name, Title and Description

An id, name, title and description for a connector can be specified with attributes on the <cNvPr> element: <cNvPr id="9" name="Straight Arrow Connector 8" title="My connector" descr="This is the description"/>. The id is an integer and specifies a unique identifier. The name is a string. The title is a string that specifies the caption. The descr is alternative text used for assistive technologies which do not display the object. Finally, note that <cNvPr> can have child elements <hlinkClick> and <hlinkhover> for links; these are not covered here.

Reference: ECMA-376, 3rd Edition (June, 2011), Fundamentals and Markup Language Reference § 19.3.1.12 (presentations) and § 20.5.2.8 (spreadsheets).

## Hidden

A connector can be hidden by specifying the hidden attribute on the <cNvPr> element: <cNvPr hidden="true">. However, note that an application can have settings that allow the object to be displayed.

## Shape Resizing, Cropping, Rotating, Changing Aspect Ratio, Moving, Selecting

The locking properties of a shape are specified with the <cxnSpLocks> element within the <cNvCxnSpPr> element. Various aspects of how a connector can be changed and edited are specified with attributes on <cxnSpLocks>. If the attributes are not specified, then it is assumed that the properties can be changed. For example, to disallow changing the aspect ratio, specify the noChangeAspect attribute as true.

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

## Connector Start and End Points

The <cNvCxnSpPr> element has child elements <stCxn> and <endCxn> which specify which shapes, and at what points on the shapes, the start and end points of the connector connect to. Both child elements have an id attribute and an idx attribute. The id attribute specifies the id of the shape to which the start or end point is attached. That is, each shape has an id specified by the id attribute on the <p:cNvPr> element within the <p:nvSpPr> element (assuming a presentation document). This is the attribute to which the id attribute of the stCxn or endCxn refers. So, for example, suppose I have three shapes with ids 4, 5, and 6 and one connector connecting shapes 4 and 5. The XML looks like the following.

<p:sp>

<p:nvSpPr>

<p:cNvPr id="4 name="Rounded Rectangle 3"/>

. . .

</p:nvSpPr>

. . .

</p:sp>

  

<p:sp>

<p:nvSpPr>

<p:cNvPr id="5" name="Rounded Rectangle 4"/>

. . .

</p:nvSpPr>

. . .

</p:sp>

  

<p:sp>

<p:nvSpPr>

<p:cNvPr id="6" name="Rounded Rectangle 5"/>

. . .

</p:nvSpPr>

. . .

</p:sp>

  

<p:cxnSp>

<p:nvCxnSpPr>

<p:cNvPr id="8" name="Straight Arrow Connector 7"/>

<p:cNvCxnSpPr>

<a:stCxn id="4" idx="3"/>

<a:endCxn id="5" idx="1"/>

</p:cNvCxnSpPr>

<p:nvPr/>

</p:nvCxnSpPr>

</p:cxnSp>

![Connector in a presentation](images/drwSp-connector2.gif)

To connect to the lower shape instead, which has an id=6, I change the XML as shown below.

<p:sp>

<p:nvSpPr>

<p:cNvPr id="4 name="Rounded Rectangle 3"/>

. . .

</p:nvSpPr>

. . .

</p:sp>

  

<p:sp>

<p:nvSpPr>

<p:cNvPr id="5" name="Rounded Rectangle 4"/>

. . .

</p:nvSpPr>

. . .

</p:sp>

  

<p:sp>

<p:nvSpPr>

<p:cNvPr id="6" name="Rounded Rectangle 5"/>

. . .

</p:nvSpPr>

. . .

</p:sp>

  

<p:cxnSp>

<p:nvCxnSpPr>

<p:cNvPr id="8" name="Straight Arrow Connector 7"/>

<p:cNvCxnSpPr>

<a:stCxn id="4" idx="3"/>

<a:endCxn id="6" idx="0"/>

</p:cNvCxnSpPr>

<p:nvPr/>

</p:nvCxnSpPr>

</p:cxnSp>

![Connector in a presentation](images/drwSp-connector3.gif)

The idx attribute on the start and end point elements specifies the index of the connection points on the shape. In the example above, the connector connects from shape 4 (at connection point 3) to shape 6, at connection point with index 0. If we change the value of idx for the end point to <a:endCxn id="6" idx="1"/>, we move the location on shape 6 where the connector attaches.

![Connector in a presentation](images/drwSp-connector4.gif)

Finally, recall that the type and style of the end points of a connector shape are determined by the <a:ln> element. See [Shapes - Outline](drwSp-outline.php) for details on these properties.

## Multimedia in Presentations

Multimedia can be associated with an object using child elements of <nvPr>. The various media types specified in child elements include <audioCd>, <audioFile>, <quickTimeFile>, <videoFile>, <waveAudioFile>. The details for these media types are not covered here.

  

[About this site](aboutThisSite.php) | [Contact us](contactUs.php)
  
Copyright © 2023. All Rights Reserved.