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

# PresentationML Slides - Master Slide

The master slide is the template upon which presentation slides are built. It specifies the shapes and objects as placeholders for content on presentation slides, as well as the formatting of the content within the placeholders. Of course the content and formatting specified on a master slide can be altered by layout slides and the presentation slides themselves, but absent such overrides, the master slide establishes the overall look and feel of the presentation.

The master slide is a separate part within a slideMasters directory. There can be more than one master slide. The presentation part (presentation.xml) references the master slides from within the <p:sldMasterIdLst> element, which is a child of <p:presentation>.

<p:presentation . .. >

<p:sldMasterIdLst>

<p:sldMasterId id="2147483660" r:id="rId1"/>

</p:sldMasterIdLst>

Within the presentation.xml.rels is the relationship: <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideMaster" Target="/slideMasters/slideMaster1.xml"/>

Each slide layout has a relationship with a master slide. So within the .rels file for a slide layout is a relationship that specifies which master slide the layout references or to which it is related. For example, in the slideLayout1.xml.rels file for the first slide is the following relationship: <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideMaster" Target="../slideMasters/slideMaster1.xml"/>. The master slide also has relationships (within slideMaster1.xml.rels) to the slide layouts that are based upon it, as well as to the theme.

The root element of a master slide is the <p:sldMaster> element. Below is a table showing the possible children of the root element.

### Elements:

| Element | Description |
| --- | --- |
| <p:clrMap> | Specifies the color scheme. For details, see [Slide Properties - Color Scheme](prSlide-color.php). |
| <p:cSld> | Specifies the slide content. For details, see [Slides - Common Slide Data](prCommonSlideData.php). |
| <p:hf> | Specifies header and footer information for a slide. For details, see [Properties - Headers and Footers](prSlide-footer.php). |
| <p:sldLayoutLst> | Specifies the list of slide layouts used within the slide master. This element contains one or more <p:sldLayoutId> elements, each representing a slide layout and each having a relationship identifier uniquely identifying it with the master slide that uses it. Each also has a unique id that identifies it within the presentation. Below is a sample layout list:  <p:sldMaster . .. >  . . .  <p:sldLayoutIdLst>  <p:sldLayoutId id="2147483661" r:id="rId1"/>  <p:sldLayoutId id="2147483662" r:id="rId2"/>  . . .  </p:sldLayoutIdLst>  </p:sldMaster>  In the .rels file for the master slide (slideMaster1.xml.rels), the relationship with id = rId1 looks like this: <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideLayout" Target="../slideLayouts/slideLayout1.xml"/>. The .rels file for the first layout slide (slideLayout1.xml.rels) has a relationship to the master slide: <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideMaster" Target="../slideMasters/slideMaster1.xml"/>. |
| <p:timing> | Specifies the timing information for animatinos and timed events within a slide. For details, see [Animation and Timing](prAnimation.php). |
| <p:transition> | Specifies the kind of transition that should be used to transition to the current slide from the previous slide. For details, see [Properties - Transitions](prSlide-transitions.php). |
| <p:txStyles> | Specifies the text styles within a master slide, including stying for the title, body, and other text. For details, see [Properties - Text Styles](prSlide-styles-textStyles.php). |

  

Footer