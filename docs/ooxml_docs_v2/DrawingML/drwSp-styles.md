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

Styles

The style information for a shape is specified with the <p:style> element within the <p:Sp>. Note at the outset that the <p:style> element is not within the main drawingML namespace; instead it is either in the presentationML main namespace (prefix p) or in the spreadsheetDrawing namespace (prefix xdr). Four characteristics of a shape are specified with this element: the type of fill, the type of outline, the effects to be applied, and the font. None of the style characteristics are actually defined within the <p:style> element, however. Instead, the element only contains references to the style details found within the theme part. The corresponding elements containing the references are within the main drawingML namespace and are: <a:effectRef>, <a:fillRef>, <a:fontRef>, and <a:lnRef>. Each of these reference elements contains an idx attribute, which is an index to the corresponding lists of properties within the theme part. So it is important to first understand a bit about the theme part.

The core of the theme part is the <a:themeElements> element,which contains most of the style information for the theme in three child elements: <a:clrScheme>, <a:fmtScheme>, and <a:fontScheme>. The <a:fmtScheme> contains four child elements: <a:bgFillStyleLst>, <a:effectStyleLst>, <a:fillStyleLst>, and <a:lnStyleLst>. The four ref child elements within <p:style> refer to the child elements of the <a:themeElements> element within the theme part. Below is first a sample <p:style> element within a shape definition in a presentation slide, followed by an outline of the theme part. The colors indicate reference relationships.

<p:style>

<a:lnRef idx="2">

<a:schemeClr val="accent1">

<a:shade val="50000"/>

</a:schemeClr>

</a:lnRef>

  

<a:fillRef idx="1">

</a:fillRef>

  

<a:effectRef idx="0">

<a:schemeClr val="accent2"/>

</a:effectRef>

  

<a:fontRef idx="minor">

<a:srgbClr val="00B0F0"/>

</a:fontRef>

</p:style>

  

<a:theme xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" name="Office Theme">

<a:themeElements>

<a:clrScheme name="Office">

. . .

</a:clrScheme>

<a:fontScheme>

<a:majorFont>

. . .

</a:majorFont>

<a:minorFont>

. . .

</a:minorFont>

</a:fontScheme>

<a:fmtScheme>

<a:fillStyleLst>

. . .

</a:fillStyleLst>

<a:lnStyleLst>

. . .

</a:lnStyleLst>

<a:effectStyleLst>

. . .

</a:effectStyleLst>

<a:bgFillStyleLst>

. . .

</a:bgFillStyleLst>

</a:fmtScheme>

</a:themeElements>

. . .

</a:theme>

## Fill

As noted above, the fill style is specified by the <a:fillRef> element within the style element. The <a:fillRef> references a child element of either the <a:fillStyleLst> or <a:bgFillStyleLst> in the theme part. The particular child element is specified by an index as given in the idx attribute on <a:fillRef>. A value of 0 or 1000 indicates no background; values 1-999 refer to the index of a fill style in <a:fillStyleLst>; and values 1001 and above refer to the index of a background fill style within <a:bgFillStyleLst>. For example, in the sample above, we have <a:fillRef idx="1">, so it refers to the first fill style within the <a:fillStyleLst> of the theme part. Below is the corresponding <a:fillStyleLst> and shape. The first fill style is a solid fill using the theme color accent2, which is defined within the <a:clrScheme> of the theme part. (For more on fills, see [Shape Fill](drwSp-shapeFill.php).)

<a:theme xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" name="Office Theme">

<a:themeElements>

<a:clrScheme name="Office">

. . .

<a:accent2>

<a:srgbClr val="C0504D"/>

</a:accent2>

. . .

</a:clrScheme>

. . .

<a:fmtScheme>

<a:fillStyleLst>

<a:solidFill>

<a:schemeClr val="accent2"/>

</a:solidFill>

. . .

</a:fillStyleLst>

. . .

</a:fmtScheme>

</a:themeElements>

. . .

</a:theme>

![Shape with text - styles - fill](images/drwSp-text-style-fill1.gif)

## Line

The line style is specified by the <a:lnRef> element within the style element. The <a:lnRef> references a child element of the <a:lnStyleLst> element in the theme part. The particular child element is specified by an index as given in the idx attribute on <a:lnRef>. (For more on outlines, see [Shape Outline](drwSp-outline.php).) In the sample below, the shape references the second line style found within the theme: <a:lnRef idx="2">.

<a:theme xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" name="Office Theme">

<a:themeElements>

<a:clrScheme name="Office">

. . .

</a:clrScheme>

. . .

<a:fmtScheme>

. . .

<a:lnStyleLst>

<a:ln . . .>

. . .

</a:ln>

<a:ln w="254000" cap="flat" cmpd="dbl" algn="ctr">

<a:solidFill>

<a:srgbClr val="000000"/>

</a:solidFill>

<a:prstDash val="dot"/>

</a:ln>

. . .

</a:lnStyleLst>

. . .

</a:fmtScheme>

</a:themeElements>

. . .

</a:theme>

![Shape with text - styles - line](images/drwSp-text-style-ln1.gif)

## Effect

The effect style is specified by the <a:effectRef> element within the style element. The <a:effectRef> references a child element of the <a:effectStyleLst> element in the theme part. The particular child element is specified by an index as given in the idx attribute on <a:effectRef>. (For more on shape effects, see [Shape Effects](drwSp-effects.php).) In the sample below, the shape references the first effect style found within the theme: <a:effectRef idx="1">. It applies a blue shadow to the bottom of the shape.

<a:theme xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" name="Office Theme">

<a:themeElements>

<a:clrScheme name="Office">

. . .

</a:clrScheme>

. . .

<a:fmtScheme>

. . .

<a:effectStyleLst>

<a:effectStyle>

<a:effectLst>

<a:outerShdw blurRad="400000" dist="200000" dir="5400000" rotWithShape="0">

<a:srgbClr val="0000FF"/>

</a:outerShdw>

</a:effectLst>

</a:effectStyle>

. . .

</a:effectStyleLst>

. . .

</a:fmtScheme>

</a:themeElements>

. . .

</a:theme>

![Shape with text - styles - effect](images/drwSp-text-style-effect1.gif)

## Font

The font style is specified by the <a:fontRef> element within the style element. The <a:fontRef> references a child element of the <a:fontScheme> element in the theme part. The particular font is specified by an index as given in the idx attribute on <a:fontRef>. The <a:fontRef> element also specifies a choice of color. In the sample below, the shape references the minor latin font found within the theme, with the color white.

<p:style>

. . .

<a:fontRef idx="minor">

<a:srgbClr val="FFFFFF"/>

</a:fontRef>

</p:style>

  

<a:theme xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" name="Office Theme">

<a:themeElements>

. .

<a:fontScheme name="Office">

<a:majorFont>

. . .

</a:majorFont>

<a:minorFont>

<a:latin typeface="Courier"/>

. . .

</a:minorFont>

</a:fontScheme>

. . .

</a:themeElements>

. . .

</a:theme>

![Shape with text - styles - font](images/drwSp-text-style-font1.gif)

  

[About this site](aboutThisSite.php) | [Contact us](contactUs.php)
  
Copyright © 2023. All Rights Reserved.