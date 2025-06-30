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

Text - Content

The text content of a shape is contained within one or more <a:p> elements. The content model for text in a shape is similar but not identical to that of content within a wordprocessingML document. Below are the permitted elements of a <a:p>.

### Elements:

| Element | Description |
| --- | --- |
| br | Specifies a line break. Note that within a wordprocessingML document, breaks are contained within runs (<a:r>). However, within shapes breaks are contained directly within the paragraph element. Breaks within shapes can have run properties specified by a <a:rPr> element. If text is later inserted where the break is, a new run can be generated with the specified formatting. See [Shapes - Text - Run Properties](drwSp-text-runProps.php) for more on the <a:rPr> element. |
| endParaRPr | Specifies the text run properties that are to be used if another run is inserted after the last run. If it is not specified, then the application can determine the properties to apply. See [Shapes - Text - Run Properties](drwSp-text-runProps.php) for the details. |
| r | Specifies a run of content within the paragraph. It is the lowest level of text separator that can have properties. If no properties are specified, then the properties specified in the default run properties element (<a:defRPr>) are used. A run can have run properties and text elements (<a:t>). See [Shapes - Text - Run Properties](drwSp-text-runProps.php) for details on run properties. |
| pPr | Specifies a set of properties for the paragraph. See [Shapes - Text - Paragraph Properties](drwSp-text-paraProps.php). Note that if no properties are specified, then the default properties specified in the <a:defPPr> element are used. See Shapes - Text - List Styles for more on default paragraph properties. |
| fld | Specifies a text field which contains generated text that the application updates periodically. The types of text are limited to dates and times or slide numbers. An id attribute for the fld element is generated by the application. A type attribute specifies the type of text. The reserved values are:   * slidenum * datetime (the default date time format for the application) * datetime1 (MM/DD/YYYY) * datetime2 (Day, Month DD YYYY) * datetime3 (MM/DD/YYYY) * datetime4 (MM/DD/YYYY) * datetime5 (MM/DD/YYYY) * datetime6 (MM/DD/YYYY) * datetime7 (MM/DD/YYYY) * datetime8 (MM/DD/YYYY) * datetime9 (MM/DD/YYYY) * datetime10 (MM/DD/YYYY) * datetime11 (MM/DD/YYYY) * datetime12 (MM/DD/YYYY) * datetime13 (MM/DD/YYYY)   The <a:fld> element can contain text (<a:t>) as well as paragraph and run property elements. See [Shapes - Text - Paragraph Properties](drwSp-text-paraProps.php) and [Shapes - Text - Run Properties](drwSp-text-runProps.php) for details. Below is a sample shape with a date field.  <p:txBody>  <a:bodyPr rtlCol="0" anchor="ctr"/>  <a:lstStyle/>  <a:p>  <a:pPr algn="ctr"/>  <a:r>  <a:rPr . . . >  . . .  </a:rPr>  <a:t>The time is </a:t>  </a:r>  <a:fld id="8DE09930-A1F0-4970-A755-490F150ACA4" type="datetime4">  <a:rPr lang="en-US" smtClean="0">  . . .  </a:rPr>  <a:t>  October 26, 2012  </a:t>  </a:fld  <a:endParaRPr . . .>  . . .  </a:endParaRPr>  </a:p>  </p:txBody>  Shape with text - rotation |

  

[About this site](aboutThisSite.php) | [Contact us](contactUs.php)
  
Copyright © 2023. All Rights Reserved.