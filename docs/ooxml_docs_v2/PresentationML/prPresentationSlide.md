![PresentationXML.com](images/PresentationMLBanner.png)

[Home](index.php) | [WordprocessingML (docx)](anatomyofOOXML.php) | [SpreadsheetML (xlsx)](anatomyofOOXML-xlsx.php)
| [DrawingML](drwOverview.php) | [PresentationML (pptx)](anatomyofOOXML-pptx.php)

* [Presentation](prPresentation.php)
* Shows
  + [Transitions](prSlide-transitions.php)
  + Animation and Timing
  + Custom Shows
* Presentation Properties
* View Properties
* Slides
  + [Overview](prSlide.php)
  + [Content (Common Slide Data)](prCommonSlideData.php)
    - [Shapes](prSlide-shapeTree.php)
    - [Tables](drwTable.php)
    - [Audio and Video](prSlide-multiMedia.php)
  + [Slide Master](prSlideMaster.php)
  + [Slide Layout](prSlideLayout.php)
  + [Slide](prPresentationSlide.php)
  + [Notes Master](prNotesMaster.php)
  + [Notes Slide](prNotesSlide.php)
  + Handout Master
* Slide Properties
  + [Size](prSlide-size.php)
  + [Background](prSlide-background.php)
  + [Headers and Footers](prSlide-footer.php)
  + Styles and Formatting
    - [Fill, Fonts, Outines, Effects](prSlide-styles-themes.php)
    - [Text Styles](prSlide-styles-textStyles.php)
  + [Color Scheme](prSlide-color.php)
  + Slide Number

# PresentationML Slides - Presentation Slide

A presentation contains at least one slide. A presentation slide contains the contents--text, shapes, charts, diagrams, etc. The slides of a presentation are each contained within a slide part (within the slides folder), each of which is a target of a relationship from the presentation part. That is, the slides are referenced explicitly by the presentation part in its presentation.xml.rels file. So, for example, there is a relationship to slide1.xml: <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slide" Target="../slides/slide1.xml"/>. (The presentation also lists the slides to be shown in a presenation within <p:sldIdLst>. See [Presentation](prPresentation.php).) A presentation slide will have a relationship to the layout slide that is applied to its content, and the relationship will be within the .rels file for that slide (i.e., within slide1.xml.rels for slide 1). The following is the relationship to the layout applied to the second slide: <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideLayout" Target="../slideLayouts/slideLayout2.xml"/>

The content model for a slide layout is similar to a master slide, except that it does not contain a text styles element, and it has a color map override rather than a color map. (And of course there is no slide layout list.) See [Slides - Overview](prSlide.php) for a comparison of the content models of the various slide types. The root element of a slide layout is the <p:sldLayout> element. Below is a table showing the possible children of the root element, followed by a table showing the attributes of the root <p:sldLayout> element.

### Elements:

| Element | Description |
| --- | --- |
| <p:clrMapOvr> | Specifies overrides of the color scheme that is specified in the master slide's <p:clrMap>. For details, see [Slide Properties - Color Scheme](prSlide-color.php). |
| <p:cSld> | Specifies the slide content. For details, see [Slides - Common Slide Data](prCommonSlideData.php). |
| <p:timing> | Specifies the timing information for animations and timed events within a slide. |
| <p:transition> | Specifies the kind of transition that should be used to transition to the current slide from the previous slide. For details, see [Properties - Transitions](prSlide-transitions.php). |

The attributes are:

### Attributes:

| Attribute | Description |
| --- | --- |
| matchingName | Specifies a name to be used in place of the name attribute on <p:cSld>. See [Slides - Common Slide Data](prCommonSlideData.php). It is used for layout matching. |
| preserve | Specifies whether the layout should be deleted when all slides that follow the layout are deleted. The default value is false, so that the layout is deleted if the attribute is unspecified. |
| showMasterPhAnim | Specifies whether to display animations on placeholders from the master slide. Values are booleans. |
| showMasterSp | Specifies whether shapes from the master should be displayed on slides or not. Values are booleans. |
| type | Specifies the layout type, which provides a high-level description of the content type and postitioning of placeholders on a slide. This information can be used by applications to aid in mapping between different layouts; the appliation can choose which, if any, to make available. A complate list of possible values can be found at ECMA-376, 3rd Edition (June, 2011), Fundamentals and Markup Language Reference § 19.7.15. Examples include blank, picTx (a title, picture and caption text), secHead (section header and subtitle text), title (title layout with centered title and subtitle placeholders), and tx (title and text). |
| userDrawn | Specifies whether the object has been drawn by the user and should therefore not be deleted. Values are booleans. |

  

Footer