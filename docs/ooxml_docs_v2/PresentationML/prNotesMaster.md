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

# PresentationML Slides - Notes Master

The notes master slide is the template upon which notes slides are built. It specifies the shapes and objects as placeholders for content on notes slides, as well as the formatting of the content within the placeholders. Of course the content and formatting specified on a notes master can be altered by the notes slides themselves, but absent such overrides, the notes master establishes the overall look and feel of the notes slides. See [Slides - Overview](prSlide.php) for more on placeholders. A notes slide is very similar to any other slide, except that it will have a placeholder (of type 'body') for the notes.

The notes master is a separate part within a notesMasters directory. There can be only one notes master. The presentation part (presentation.xml) references the notes master from within the <p:notesMasterIdLst> element, which is a child of <p:presentation>.

<p:presentation . .. >

<p:notesMasterIdLst>

<p:notesMasterId r:id="rId4"/>

</p:notesMasterIdLst>

Within the presentation.xml.rels is the relationship: <Relationship Id="rId4" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/notesMaster" Target="/notesMasters/notesMaster1.xml"/>

Each notes slide has a relationship with the notes master. So within the .rels file for a notes slide is a relationship that specifies the notes master slide. For example, in the notesSlide2.xml.rels file for the second notes slide is the following relationship: <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/notesMaster" Target="../notesMasters/notesMaster1.xml"/>.

The root element of a notes master is the <p:notesMaster> element. Below is a table showing the possible children of the root element.

### Elements:

| Element | Description |
| --- | --- |
| <p:clrMap> | Specifies the color scheme. For details, see [Slide Properties - Color Scheme](prSlide-color.php). |
| <p:cSld> | Specifies the slide content. For details, see [Slides - Common Slide Data](prCommonSlideData.php). |
| <p:hf> | Specifies header and footer information for a slide. For details, see [Properties - Headers and Footers](prSlide-footer.php). |
| <p:notesStyle> | Specifies the text styles within notes slides. For details, see [Properties - Text Styles](prSlide-styles-textStyles.php). |

  

Footer