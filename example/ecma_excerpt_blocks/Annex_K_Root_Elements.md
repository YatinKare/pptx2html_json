\n--- Page 4532 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
<a:rPr lang="en-US" dirty="0" smtClean="0"/>
<a:t>Shape 1</a:t>
</a:r>
<a:endParaRPr lang="en-US" dirty="0"/>
</a:p>
</p:txBody>
</p:sp>
<p:sp>
<p:nvSpPr>
<p:cNvPr id="8" name="TextBox 7" descr="Caption for
animations:&#xA;Blue rectangle of height 1.5 inches and width 2 inches with
text “Shape 1” is moving from bottom left of slide to top left of slide
while fading in over 3 seconds.&#xA;"
title=”Animation Close Caption”/>
<p:cNvSpPr txBox="1"/>
<p:nvPr/>
</p:nvSpPr>
<p:spPr>
<a:xfrm>…</a:xfrm>
<a:prstGeom prst="rect"><a:avLst/></a:prstGeom>
<a:noFill/>
</p:spPr>
<p:txBody>
<a:bodyPr wrap="square" rtlCol="0">
<a:spAutoFit/>
</a:bodyPr>
<a:lstStyle/>
<a:p>
<a:r>
<a:rPr lang="en-US" dirty="0" smtClean="0"/>
<a:t>Blue rectangle of height 1.5 inches and width 2 inches
with text “Shape 1” is moving from bottom left of slide to top left of
slide.</a:t>
</a:r>
<a:endParaRPr lang="en-US" dirty="0" smtClean="0"/>
</a:p>
</p:txBody>
</p:sp>
</p:spTree>
As the shape tree above shows, the animating shape has a shape ID of 5 and the closed caption text box
has a shape ID of 8. With both shapes in the shape tree, they can be added to the slide timeline.
4522 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 4533 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
<p:timing>
…
<p:bldLst>
<p:bldP spid="5" grpId="0" animBg="1"/>
<p:bldP spid="8" grpId="1"/>
<p:bldP spid="8" grpId="2"/>
</p:bldLst>
</p:timing>
There are three build steps in the timeline:
Animate the shape ( move across the slide )
Animate the text box ( appear )
Animation the text box ( disappear )
This approach can be used in even more complex animations by reusing the general principle of
associating a text box per animation.
J.5.4 Specifying Language to Enable Accessibility Tools
It is incredibly important for customers to always specify which language is being used to author a
document. The rationale behind this is that speech synthesizers and Braille devices can automatically
switch to the new language, making the document more accessible to multilingual users.
when an Office Open XML document uses different languages for text, a clear identification of the
language used and its country is provided. The <w:lang/> tag is generated which indicates the language
used in the paragraph and run.
<w:p>
<w:r w:rsidR="0008256F">
<w:t xml:space="preserve">multiple languages like </w:t>
</w:r>
<w:r w:rsidR="0008256F">
<w:t>سهلاشقش هيعشس ؤهلاشقش</w:t>
</w:r>
<w:r w:rsidR="0008256F">
<w:rPr>
<w:rFonts w:hint="cs"/>
<w:rtl/>
<w:lang w:bidi="ar-DZ"/>
</w:rPr>
<w:t>شهقثلمش ؤهلاشقش</w:t>
</w:r>
©ISO/IEC 2016 – All rights reserved 4523\n\n--- Page 4534 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
<w:r w:rsidR="0008256F">
<w:rPr>
<w:rFonts w:hint="cs"/>
<w:rtl/>
<w:lang w:bidi="ar-EG"/>
</w:rPr>
<w:t>فحغلث ؤهلاشقش</w:t>
</w:r>
</w:p>
J.5.5 Using Styles when Possible
Although most people associate styles usage only with the goal of making a document look visually
appealing, they can also be of particular use for those readers who are trying to read documents. If a
customer authors a document such that it uses styles, the transform a reader can do to accommodate a
visual impairment is substantially easier than the transform required for documents not based on a
style: in the style case, a styles optimized for visual impaired readers can be quickly applied; in the non-
style case, extensive direct formatting of the document must be done by the reader.
J.5.6 Techniques for Improving Document Navigation
It is highly desirable for customers to author their documents in such a way that there is predictability in
terms of navigation. The following describes the techniques that the customer can use to make use
built-in primitives in Office Open XML, as well as how such techniques change the underlying document
data, to achieve the desired outcome.
J.5.6.1 Navigating Shapes on Slides
In cases where a reader is navigating slides, navigation is complicated by the 2D-nature of the slide.
Office Open XML provides a remedy for this by allowing customers to define the reading order, or
navigation order, of shapes on a slide through the use of z-order.
Consider the case that a presentation author elects to construct a slide that contains five placeholders:
one for the title (A) , two for list headings (B, C) and two lists (D, E). Visually, this could be represented
as follows:
4524 ©ISO/IEC 2016 – All rights reserved\n