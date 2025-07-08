\n--- Page 2515 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
640x480 (640 x 480 Resolution) Sets the target screen resolution to 640x480 pixels.
720x512 (720 x 512 Resolution) Sets the target screen resolution to 720x512 pixels.
800x600 (800 x 600 Resolution) Sets the target screen resolution to 800x600 pixels.
[Note: The W3C XML Schema definition of this simple type’s content model (ST_TargetScreenSize) is located in
§A.2. end note]
18.18.80 ST_TextHAlign (Comment Text Horizontal Alignment)
This simple type specifies the horizontal alignment of the text within a comment text field.
This simple type's contents are a restriction of the W3C XML Schema string datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
center (Center Alignment) Specifies that the text is centered horizontally.
distributed (Distributed Alignment) Specifies that the text is distributed horizontally.
justify (Justify Alignment) Specifies that the text is justified horizontally.
left (Left Alignment) Specifies that the text is left-aligned.
right (Right Alignment) Specifies that the text is right-aligned.
[Note: The W3C XML Schema definition of this simple type’s content model (ST_TextHAlign) is located in §A.2.
end note]
18.18.81 ST_TextVAlign (Comment Text Vertical Alignment)
This simple type specifies the vertical alignment of the text within a comment text field.
This simple type's contents are a restriction of the W3C XML Schema string datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
bottom (Bottom Alignment) Specifies that the text is bottom-aligned.
center (Center Alignment) Specifies that the text is centered vertically.
distributed (Distributed Alignment) Specifies that the text is distributed vertically.
justify (Justify Alignment) Specifies that the text is justified vertically.
top (Top Alignment) Specifies that the text is top-aligned.
©ISO/IEC 2016 – All rights reserved 2505\n\n--- Page 2516 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
[Note: The W3C XML Schema definition of this simple type’s content model (ST_TextVAlign) is located in §A.2.
end note]
18.18.82 ST_TimePeriod (Time Period Types)
Used in a "contains dates" conditional formatting rule. These are dynamic time periods, which change based on
the date the conditional formatting is refreshed / applied.
This simple type's contents are a restriction of the W3C XML Schema string datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
last7Days (Last 7 Days) A date in the last seven days.
lastMonth (Last Month) A date occuring in the last calendar month.
lastWeek (Last Week) A date occuring last week.
nextMonth (Next Month) A date occuring in the next calendar month.
nextWeek (Next Week) A date occuring next week.
thisMonth (This Month) A date occuring in this calendar month.
thisWeek (This Week) A date occuring this week.
today (Today) Today's date.
tomorrow (Tomorrow) Tomorrow's date.
yesterday (Yesterday) Yesterday's date.
[Note: The W3C XML Schema definition of this simple type’s content model (ST_TimePeriod) is located in §A.2.
end note]
18.18.83 ST_TotalsRowFunction (Totals Row Function Types)
An enumeration that specifies what function is used to aggregate the data in a column before it is displayed in
the totals row.
This simple type's contents are a restriction of the W3C XML Schema string datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
average (Average) Represents the arithmetic mean.
count (Non Empty Cell Count) Represents a count of the number of non-empty cells.
countNums (Count Numbers) Represents the number of cells that contain numbers.
custom (Custom Formula) Represents the formula provided in
totalsRowFormula.
max (Maximum) Represents the largest value.
2506 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2517 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
min (Minimum) Represents the smallest value.
none (None) No total row.
stdDev (StdDev) Represents the estimated standard deviation.
sum (Sum) Represents the arithmetic sum.
var (Var) Represents the estimated variance.
[Note: The W3C XML Schema definition of this simple type’s content model (ST_TotalsRowFunction) is located in
§A.2. end note]
18.18.84 ST_Type (Top N Evaluation Type)
This simple type defines the values for the Top N conditional formatting evaluation for the PivotTable. For more
information on Top N conditional formatting, see the Sheet (§18.3.1) reference material.
This simple type's contents are a restriction of the W3C XML Schema string datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
all (All) Indicates that Top N conditional formatting is
evaluated across the entire scope range.
column (Column Top N) Indicates that Top N conditional formatting is
evaluated for each column.
none (Top N None) Indicates that Top N conditional formatting is not
evaluated
row (Row Top N) Indicates that Top N conditional formatting is
evaluated for each row.
[Note: The W3C XML Schema definition of this simple type’s content model (ST_Type) is located in §A.2. end
note]
18.18.85 ST_UnderlineValues (Underline Types)
Represents the different types of possible underline formatting.
This simple type's contents are a restriction of the W3C XML Schema string datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
double (Double Underline) Double-line underlining under each character in the
cell. underlines are drawn through the descenders of
characters such as g and p.
©ISO/IEC 2016 – All rights reserved 2507\n\n--- Page 2518 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
doubleAccounting (Accounting Double Underline) Double-line accounting underlining under each
character in the cell. The underlines are drawn under
the descenders of characters such as g and p.
none (None) No underline.
single (Single Underline) Single-line underlining under each character in the cell.
The underline is drawn through the descenders of
characters such as g and p.
singleAccounting (Accounting Single Underline) Single-line accounting underlining under each
character in the cell. The underline is drawn under the
descenders of characters such as g and p.
[Note: The W3C XML Schema definition of this simple type’s content model (ST_UnderlineValues) is located in
§A.2. end note]
18.18.86 ST_UnsignedIntHex (Hex Unsigned Integer)
This simple type represents the Hex representation of an unsigned integer.
This simple type's contents are a restriction of the W3C XML Schema hexBinary datatype.
This simple type also specifies the following restrictions:
 This simple type's contents have a length of exactly 8 hexadecimal digit(s).
[Note: The W3C XML Schema definition of this simple type’s content model (ST_UnsignedIntHex) is located in
§A.2. end note]
18.18.87 ST_UpdateLinks (Update Links Behavior Types)
This simple type defines when the application updates links to other workbooks when the workbook is opened.
This simple type's contents are a restriction of the W3C XML Schema string datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
always (Always Update Links) Indicates that links to other workbooks are always
updated when the workbook is opened. The
application will not display an alert in the user
interface (UI).
2508 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2519 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
never (Never Update Links) Indicates that links to other workbooks are never
updated when the workbook is opened. The
application will not display an alert in the user
interface.
userSet (User Set) Indicates that the end-user specified whether they
receive an alert to update links to other workbooks
when the workbook is opened. [Example: The
application can expose this option in an application
settings dialog. end example]
[Note: The W3C XML Schema definition of this simple type’s content model (ST_UpdateLinks) is located in §A.2.
end note]
18.18.88 ST_VerticalAlignment (Vertical Alignment Types)
This enumeration value indicates the type of vertical alignment for a cell, i.e., whether it is aligned top, bottom,
vertically centered, justified or distributed.
This simple type's contents are a restriction of the W3C XML Schema string datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
bottom (Aligned To Bottom) The vertical alignment is aligned-to-bottom.
center (Centered Vertical Alignment) The vertical alignment is centered across the height of
the cell.
distributed (Distributed Vertical Alignment) When text direction is horizontal: the vertical
alignment of lines of text is distributed vertically,
where each line of text inside the cell is evenly
distributed across the height of the cell, with flush top
and bottom margins.
When text direction is vertical: behaves exactly as
distributed horizontal alignment. The first words in a
line of text (appearing at the top of the cell) are flush
with the top edge of the cell, and the last words of a
line of text are flush with the bottom edge of the cell,
and the line of text is distributed evenly from top to
bottom.
[Example: Horizontal text: this first example shows
four lines of text (read horizontally from left to right)
distributed vertically across the height of the cell. The
first line is "abc", the second line is "def", the third line
©ISO/IEC 2016 – All rights reserved 2509\n\n--- Page 2520 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
is "ghi" and the fourth line is "jkl".
Vertical text: this second example shows three lines of
text (read vertically from top to bottom) distributed
vertically across the height of the cell. The lines of text
are:
abcd efg hijklmnop qrs
tuv wx
yzabc defg hijk lmnop
The rendering looks like this:
end example]
justify (Justified Vertically) When text direction is horizontal: the vertical
alignment of lines of text is distributed vertically,
2510 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2521 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
where each line of text inside the cell is evenly
distributed across the height of the cell, with flush top
and bottom margins.
When text direction is vertical: similar behavior as
horizontal justification. The alignment is justified (flush
top and bottom in this case). For each line of text, each
line of the wrapped text in a cell is aligned to the top
and bottom (except the last line). If no single line of
text wraps in the cell, then the text is not justified.
[Example: Horizontal text: this first example shows
four lines of text (read horizontally from left to right)
justified vertically across the height of the cell. The
first line is "abc", the second line is "def", the third line
is "ghi" and the fourth line is "jkl".
Vertical text: this second example shows three lines of
text (read vertically from top to bottom) distributed
vertically across the height of the cell. The lines of text
are:
abcd efg hijklmnop qrs
tuv wx
yzabc defg hijk lmnop
The rendering looks like this:
©ISO/IEC 2016 – All rights reserved 2511\n\n--- Page 2522 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
end example]
top (Align Top) The vertical alignment is aligned-to-top.
[Note: The W3C XML Schema definition of this simple type’s content model (ST_VerticalAlignment) is located in
§A.2. end note]
18.18.89 ST_Visibility (Visibility Types)
This simple type defines the possible states for workbook window visibility.
This simple type's contents are a restriction of the W3C XML Schema string datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
hidden (Hidden) Indicates the workbook window is hidden, but can be
shown by the user via the user interface.
veryHidden (Very Hidden) Indicates the workbook window is hidden and cannot
be shown in the user interface (UI). This state is only
available programmatically.
visible (Visible) Indicates the workbook window is visible.
[Note: The W3C XML Schema definition of this simple type’s content model (ST_Visibility) is located in §A.2. end
note]
18.18.90 ST_VolDepType (Volatile Dependency Types)
This simple type defines the dependency types available for this workbook.
This simple type's contents are a restriction of the W3C XML Schema string datatype.
2512 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2523 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
olapFunctions (OLAP Formulas) Indicates that the type is Cube Functions.
realTimeData (Real Time Data) Indicates that the type is Real Time Data (RTD).
[Note: The W3C XML Schema definition of this simple type’s content model (ST_VolDepType) is located in §A.2.
end note]
18.18.91 ST_VolValueType (Volatile Dependency Value Types)
This simple type defines the data type of the values in the dependency cache.
This simple type's contents are a restriction of the W3C XML Schema string datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
b (Boolean) Indicates topic value is a boolean.
e (Error) Indicates topic value is an error.
n (Real Number) Indicates topic value is a real number.
s (String) Indicates topic value is a string.
[Note: The W3C XML Schema definition of this simple type’s content model (ST_VolValueType) is located in §A.2.
end note]
18.18.92 ST_WebSourceType (Web Source Type)
This is an enumeration of types of objects which can be selected from the workbook to be published as HTML.
For example, the entire sheet can be published, or a narrower set of objects on the sheet can be published, like
a chart or a range.
This simple type's contents are a restriction of the W3C XML Schema string datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
autoFilter (AutoFilter) Auto filter
chart (Chart) Chart
label (Label) Label
pivotTable (PivotTable) PivotTable
printArea (Print Area) Print area
query (QueryTable) Query Table
©ISO/IEC 2016 – All rights reserved 2513\n\n--- Page 2524 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
range (Range) Range of cells
sheet (All Sheet Content) All content of a sheet
[Note: The W3C XML Schema definition of this simple type’s content model (ST_WebSourceType) is located in
§A.2. end note]
18.18.93 ST_XmlDataType (XML Data Types)
Represents a W3C XML built-in datatype name (http://www.w3.org/TR/xmlschema-2/). The values permitted by
this type are the names of the simple datatypes defined by the XMLSchema Library,
http://www.w3.org/2001/XML-Schema-datatypes.
This simple type's contents are a restriction of the W3C XML Schema string datatype.
Note: The W3C XML Schema definition of this simple type’s content model (ST_XmlDataType) is located in §A.2.
end note]
18.18.94 ST_FontFamily (Font Family)
This simple type specifies a font family. A font family is a set of fonts having common stroke width and serif
characteristics. This is system-level font information.
This simple type's contents are a restriction of the W3C XML Schema unsignedInt datatype.
This simple type is restricted to the values listed in the following table:
Value Font Family
0 Not applicable.
1 Roman
2 Swiss
3 Modern
4 Script
5 Decorative
6 Reserved for future use
7 Reserved for future use
8 Reserved for future use
9 Reserved for future use
10 Reserved for future use
11 Reserved for future use
12 Reserved for future use
13 Reserved for future use
2514 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2525 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Value Font Family
14 Reserved for future use
[Note: The W3C XML Schema definition of this simple type’s content model (ST_FontFamily) is located in §A.2.
end note]
©ISO/IEC 2016 – All rights reserved 2515\n\n--- Page 2526 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
19. PresentationML Reference Material
[Note: For further information on the mapping of elements and attributes to OPC parts, see the Bibliography
entry, “Information on elements, attributes, and OPC parts in ISO/IEC 29500 (OOXML)”. end note]
The subordinate subclauses specify the semantics for the XML markup comprising a PresentationML document,
as defined by §13 of this Part of ISO/IEC 29500.
19.1 Table of Contents
This subclause is informative.
19.2 Presentation............................................................................................................................... 2522
19.2.1 Presentation Properties ................................................................................................................... 2522
19.2.1.1 bold (Bold Embedded Font) ..................................................................................................... 2522
19.2.1.2 boldItalic (Bold Italic Embedded Font) .................................................................................... 2523
19.2.1.3 browse (Browse Slide Show Mode) ......................................................................................... 2524
19.2.1.4 clrMru (Color MRU) ................................................................................................................. 2524
19.2.1.5 custShow (Custom Show) ........................................................................................................ 2525
19.2.1.6 custShow (Custom Show) ........................................................................................................ 2526
19.2.1.7 custShowLst (List of Custom Shows) ....................................................................................... 2526
19.2.1.8 defaultTextStyle (Presentation Default Text Style) ................................................................. 2526
19.2.1.9 embeddedFont (Embedded Font) ........................................................................................... 2527
19.2.1.10 embeddedFontLst (Embedded Font List) ................................................................................ 2527
19.2.1.11 ext (Extension) ......................................................................................................................... 2527
19.2.1.12 extLst (Extension List) .............................................................................................................. 2528
19.2.1.13 font (Embedded Font Name) ................................................................................................... 2528
19.2.1.14 handoutMasterId (Handout Master ID) .................................................................................. 2531
19.2.1.15 handoutMasterIdLst (List of Handout Master IDs) .................................................................. 2532
19.2.1.16 italic (Italic Embedded Font) .................................................................................................... 2532
19.2.1.17 kinsoku (Kinsoku Settings) ....................................................................................................... 2533
19.2.1.18 kiosk (Kiosk Slide Show Mode) ................................................................................................ 2533
19.2.1.19 modifyVerifier (Modification Verifier) ..................................................................................... 2534
19.2.1.20 notesMasterId (Notes Master ID) ............................................................................................ 2537
19.2.1.21 notesMasterIdLst (List of Notes Master IDs) ........................................................................... 2538
19.2.1.22 notesSz (Notes Slide Size) ........................................................................................................ 2538
19.2.1.23 penClr (Pen Color for Slide Show) ........................................................................................... 2539
19.2.1.24 photoAlbum (Photo Album Information) ................................................................................ 2539
19.2.1.25 present (Presenter Slide Show Mode) ..................................................................................... 2540
19.2.1.26 presentation (Presentation) .................................................................................................... 2541
19.2.1.27 presentationPr (Presentation-wide Properties) ...................................................................... 2543
19.2.1.28 prnPr (Printing Properties) ...................................................................................................... 2543
19.2.1.29 regular (Regular Embedded Font) ........................................................................................... 2544
19.2.1.30 showPr (Presentation-wide Show Properties) ........................................................................ 2545
2516 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2527 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
19.2.1.31 sld (Presentation Slide) ............................................................................................................ 2545
19.2.1.32 sldAll (All Slides) ....................................................................................................................... 2546
19.2.1.33 sldId (Slide ID) .......................................................................................................................... 2546
19.2.1.34 sldIdLst (List of Slide IDs) ......................................................................................................... 2547
19.2.1.35 sldLst (List of Presentation Slides) ........................................................................................... 2547
19.2.1.36 sldMasterId (Slide Master ID) .................................................................................................. 2547
19.2.1.37 sldMasterIdLst (List of Slide Master IDs) ................................................................................. 2548
19.2.1.38 sldRg (Slide Range) .................................................................................................................. 2548
19.2.1.39 sldSz (Presentation Slide Size) ................................................................................................. 2549
19.2.1.40 smartTags (Smart Tags) ........................................................................................................... 2550
19.2.2 View Properties ............................................................................................................................... 2551
19.2.2.1 cSldViewPr (Common Slide View Properties) .......................................................................... 2551
19.2.2.2 cViewPr (Common View Properties) ....................................................................................... 2551
19.2.2.3 gridSpacing (Grid Spacing) ....................................................................................................... 2552
19.2.2.4 guide (A Guide) ........................................................................................................................ 2553
19.2.2.5 guideLst (List of Guides) .......................................................................................................... 2553
19.2.2.6 normalViewPr (Normal View Properties) ................................................................................ 2553
19.2.2.7 notesTextViewPr (Notes Text View Properties) ...................................................................... 2555
19.2.2.8 notesViewPr (Notes View Properties) ..................................................................................... 2555
19.2.2.9 origin (View Origin) .................................................................................................................. 2555
19.2.2.10 outlineViewPr (Outline View Properties) ................................................................................ 2556
19.2.2.11 restoredLeft (Normal View Restored Left Properties) ............................................................ 2556
19.2.2.12 restoredTop (Normal View Restored Top Properties)............................................................. 2556
19.2.2.13 scale (View Scale) .................................................................................................................... 2557
19.2.2.14 sld (Presentation Slide) ............................................................................................................ 2557
19.2.2.15 sldLst (List of Presentation Slides) ........................................................................................... 2558
19.2.2.16 slideViewPr (Slide View Properties) ........................................................................................ 2558
19.2.2.17 sorterViewPr (Slide Sorter View Properties) ........................................................................... 2558
19.2.2.18 viewPr (Presentation-wide View Properties) .......................................................................... 2559
19.3 Slides ......................................................................................................................................... 2559
19.3.1 Slides ................................................................................................................................................ 2559
19.3.1.1 bg (Slide Background) .............................................................................................................. 2559
19.3.1.2 bgPr (Background Properties) ................................................................................................. 2560
19.3.1.3 bgRef (Background Style Reference) ....................................................................................... 2560
19.3.1.4 blipFill (Picture Fill) .................................................................................................................. 2561
19.3.1.5 bodyStyle (Slide Master Body Text Style) ................................................................................ 2564
19.3.1.6 clrMap (Color Scheme Map) .................................................................................................... 2564
19.3.1.7 clrMapOvr (Color Scheme Map Override) ............................................................................... 2566
19.3.1.8 cNvCxnSpPr (Non-Visual Connector Shape Drawing Properties) ............................................ 2566
19.3.1.9 cNvGraphicFramePr (Non-Visual Graphic Frame Drawing Properties) ................................... 2566
19.3.1.10 cNvGrpSpPr (Non-Visual Group Shape Drawing Properties) ................................................... 2567
19.3.1.11 cNvPicPr (Non-Visual Picture Drawing Properties) ................................................................. 2567
19.3.1.12 cNvPr (Non-Visual Drawing Properties) .................................................................................. 2568
19.3.1.13 cNvSpPr (Non-Visual Drawing Properties for a Shape) ........................................................... 2570
19.3.1.14 contentPart (Content Part) ...................................................................................................... 2571
19.3.1.15 controls (List of controls) ......................................................................................................... 2574
19.3.1.16 cSld (Common Slide Data) ....................................................................................................... 2574
©ISO/IEC 2016 – All rights reserved 2517\n\n--- Page 2528 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
19.3.1.17 custData (Customer Data) ....................................................................................................... 2575
19.3.1.18 custDataLst (Customer Data List) ............................................................................................ 2575
19.3.1.19 cxnSp (Connection Shape) ....................................................................................................... 2575
19.3.1.20 extLst (Extension List with Modification Flag) ......................................................................... 2576
19.3.1.21 graphicFrame (Graphic Frame) ................................................................................................ 2577
19.3.1.22 grpSp (Group Shape) ............................................................................................................... 2577
19.3.1.23 grpSpPr (Group Shape Properties) .......................................................................................... 2578
19.3.1.24 handoutMaster (Handout Master) .......................................................................................... 2579
19.3.1.25 hf (Header/Footer information for a slide master) ................................................................. 2579
19.3.1.26 notes (Notes Slide) .................................................................................................................. 2580
19.3.1.27 notesMaster (Notes Master) ................................................................................................... 2580
19.3.1.28 notesStyle (Notes Text Style) ................................................................................................... 2581
19.3.1.29 nvCxnSpPr (Non-Visual Properties for a Connection Shape) .................................................. 2581
19.3.1.30 nvGraphicFramePr (Non-Visual Properties for a Graphic Frame) ........................................... 2581
19.3.1.31 nvGrpSpPr (Non-Visual Properties for a Group Shape) ........................................................... 2581
19.3.1.32 nvPicPr (Non-Visual Properties for a Picture) .......................................................................... 2581
19.3.1.33 nvPr (Non-Visual Properties) ................................................................................................... 2582
19.3.1.34 nvSpPr (Non-Visual Properties for a Shape) ............................................................................ 2582
19.3.1.35 otherStyle (Slide Master Other Text Style) .............................................................................. 2582
19.3.1.36 ph (Placeholder Shape) ............................................................................................................ 2583
19.3.1.37 pic (Picture) .............................................................................................................................. 2583
19.3.1.38 sld (Presentation Slide) ............................................................................................................ 2584
19.3.1.39 sldLayout (Slide Layout) ........................................................................................................... 2585
19.3.1.40 sldLayoutId (Slide Layout Id) .................................................................................................... 2586
19.3.1.41 sldLayoutIdLst (List of Slide Layouts) ....................................................................................... 2586
19.3.1.42 sldMaster (Slide Master) ......................................................................................................... 2586
19.3.1.43 sp (Shape) ................................................................................................................................ 2587
19.3.1.44 spPr (Shape Properties) ........................................................................................................... 2587
19.3.1.45 spTree (Shape Tree) ................................................................................................................. 2588
19.3.1.46 style (Shape Style) ................................................................................................................... 2589
19.3.1.47 tags (Customer Data Tags) ....................................................................................................... 2590
19.3.1.48 timing (Slide Timing Information for a Slide Layout) ............................................................... 2590
19.3.1.49 titleStyle (Slide Master Title Text Style) .................................................................................. 2591
19.3.1.50 transition (Slide Transition for a Slide Layout) ........................................................................ 2591
19.3.1.51 txBody (Shape Text Body) ........................................................................................................ 2592
19.3.1.52 txStyles (Slide Master Text Styles) ........................................................................................... 2592
19.3.1.53 xfrm (2D Transform for Graphic Frame) .................................................................................. 2592
19.3.2 Embedded Objects .......................................................................................................................... 2593
19.3.2.1 control (Embedded Control) .................................................................................................... 2594
19.3.2.2 embed (Embedded Object or Control) .................................................................................... 2594
19.3.2.3 link (Linked Object or Control) ................................................................................................ 2595
19.3.2.4 oleObj (Global Element for Embedded objects and Controls) ................................................ 2595
19.3.3 Programmable Tags ......................................................................................................................... 2596
19.3.3.1 tag (Programmable Extensibility Tag)...................................................................................... 2596
19.3.3.2 tagLst (Programmable Tab List) ............................................................................................... 2596
19.4 Comments .................................................................................................................................. 2597
19.4.1 cm (Comment) ................................................................................................................................. 2597
2518 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2529 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
19.4.2 cmAuthor (Comment Author) ......................................................................................................... 2598
19.4.3 cmAuthorLst (List of Comment Authors) ......................................................................................... 2599
19.4.4 cmLst (Comment List) ...................................................................................................................... 2599
19.4.5 pos (Comment Position) .................................................................................................................. 2600
19.4.6 text (Comment's Text Content) ....................................................................................................... 2601
19.5 Animation .................................................................................................................................. 2601
19.5.1 anim (Animate) ................................................................................................................................ 2602
19.5.2 animClr (Animate Color Behavior) ................................................................................................... 2603
19.5.3 animEffect (Animate Effect) ............................................................................................................ 2604
19.5.4 animMotion (Animate Motion) ....................................................................................................... 2610
19.5.5 animRot (Animate Rotation) ........................................................................................................... 2611
19.5.6 animScale (Animate Scale) .............................................................................................................. 2612
19.5.7 attrName (Attribute Name) ............................................................................................................. 2613
19.5.8 attrNameLst (Attribute Name List) .................................................................................................. 2614
19.5.9 audio (Audio) ................................................................................................................................... 2615
19.5.10 bg (Background)............................................................................................................................... 2616
19.5.11 bldAsOne (Build As One) ................................................................................................................. 2616
19.5.12 bldDgm (Build Diagram) .................................................................................................................. 2616
19.5.13 bldGraphic (Build Graphics) ............................................................................................................. 2617
19.5.14 bldLst (Build List) ............................................................................................................................. 2618
19.5.15 bldOleChart (Build Embedded Chart) .............................................................................................. 2619
19.5.16 bldP (Build Paragraph) ..................................................................................................................... 2620
19.5.17 bldSub (Build Sub Elements) ............................................................................................................ 2622
19.5.18 blinds (Blinds Slide Transition)......................................................................................................... 2622
19.5.19 boolVal (Boolean Variant) ............................................................................................................... 2623
19.5.20 by (By) .............................................................................................................................................. 2624
19.5.21 by (By) .............................................................................................................................................. 2624
19.5.22 cBhvr (Common Behavior)............................................................................................................... 2625
19.5.23 charRg (Character Range) ................................................................................................................ 2626
19.5.24 checker (Checker Slide Transition) .................................................................................................. 2627
19.5.25 childTnLst (Children Time Node List) ............................................................................................... 2628
19.5.26 circle (Circle Slide Transition) .......................................................................................................... 2629
19.5.27 clrVal (Color Value) .......................................................................................................................... 2629
19.5.28 cmd (Command) .............................................................................................................................. 2630
19.5.29 cMediaNode (Common Media Node Properties) ............................................................................ 2632
19.5.30 comb (Comb Slide Transition) ......................................................................................................... 2633
19.5.31 cond (Condition) .............................................................................................................................. 2633
19.5.32 cover (Cover Slide Transition) .......................................................................................................... 2634
19.5.33 cTn (Common Time Node Properties) ............................................................................................. 2636
19.5.34 cut (Cut Slide Transition) ................................................................................................................. 2639
19.5.35 diamond (Diamond Slide Transition) ............................................................................................... 2640
19.5.36 dissolve (Dissolve Slide Transition) .................................................................................................. 2640
19.5.37 endCondLst (End Conditions List) .................................................................................................... 2641
19.5.38 endSnd (Stop Sound Action) ............................................................................................................ 2642
19.5.39 endSync (EndSync) ........................................................................................................................... 2642
19.5.40 excl (Exclusive) ................................................................................................................................. 2643
19.5.41 fade (Fade Slide Transition) ............................................................................................................. 2643
©ISO/IEC 2016 – All rights reserved 2519\n\n--- Page 2530 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
19.5.42 fltVal (Float Value) ........................................................................................................................... 2644
19.5.43 from (From) ..................................................................................................................................... 2645
19.5.44 from (From) ..................................................................................................................................... 2645
19.5.45 graphicEl (Graphic Element) ............................................................................................................ 2646
19.5.46 hsl (HSL) ........................................................................................................................................... 2647
19.5.47 inkTgt (Ink Target)............................................................................................................................ 2647
19.5.48 intVal (Integer) ................................................................................................................................. 2648
19.5.49 iterate (Iterate) ................................................................................................................................ 2648
19.5.50 newsflash (Newsflash Slide Transition) ........................................................................................... 2649
19.5.51 nextCondLst (Next Conditions List) ................................................................................................. 2650
19.5.52 oleChartEl (Embedded Chart Element) ........................................................................................... 2650
19.5.53 par (Parallel Time Node) .................................................................................................................. 2651
19.5.54 plus (Plus Slide Transition) ............................................................................................................... 2652
19.5.55 prevCondLst (Previous Conditions List) ........................................................................................... 2653
19.5.56 pRg (Paragraph Text Range) ............................................................................................................ 2653
19.5.57 progress (Progress) .......................................................................................................................... 2654
19.5.58 pull (Pull Slide Transition) ................................................................................................................ 2654
19.5.59 push (Push Slide Transition) ............................................................................................................ 2656
19.5.60 random (Random Slide Transition) .................................................................................................. 2658
19.5.61 randomBar (Random Bar Slide Transition) ...................................................................................... 2658
19.5.62 rCtr (Rotation Center) ...................................................................................................................... 2659
19.5.63 rgb (RGB).......................................................................................................................................... 2660
19.5.64 rtn (Runtime Node Trigger Choice) ................................................................................................. 2661
19.5.65 seq (Sequence Time Node) .............................................................................................................. 2661
19.5.66 set (Set Time Node Behavior) .......................................................................................................... 2663
19.5.67 sldTgt (Slide Target) ......................................................................................................................... 2664
19.5.68 snd (Sound) ...................................................................................................................................... 2664
19.5.69 sndAc (Sound Action) ...................................................................................................................... 2665
19.5.70 sndTgt (Sound Target) ..................................................................................................................... 2666
19.5.71 split (Split Slide Transition) .............................................................................................................. 2666
19.5.72 spTgt (Shape Target) ........................................................................................................................ 2668
19.5.73 stCondLst (Start Conditions List) ..................................................................................................... 2668
19.5.74 strips (Strips Slide Transition) .......................................................................................................... 2669
19.5.75 strVal (String Value) ......................................................................................................................... 2670
19.5.76 stSnd (Start Sound Action) ............................................................................................................... 2671
19.5.77 subSp (Subshape) ............................................................................................................................ 2671
19.5.78 subTnLst (Sub-TimeNodes List) ....................................................................................................... 2672
19.5.79 tav (Time Animate Value) ................................................................................................................ 2672
19.5.80 tavLst (Time Animated Value List) ................................................................................................... 2677
19.5.81 tgtEl (Target Element)...................................................................................................................... 2678
19.5.82 tmAbs (Time Absolute) .................................................................................................................... 2678
19.5.83 tmPct (Time Percentage) ................................................................................................................. 2679
19.5.84 tmpl (Template Effects) ................................................................................................................... 2679
19.5.85 tmplLst (Template effects) .............................................................................................................. 2680
19.5.86 tn (Time Node) ................................................................................................................................. 2680
19.5.87 tnLst (Time Node List) ...................................................................................................................... 2681
19.5.88 to (To) .............................................................................................................................................. 2682
19.5.89 to (To) .............................................................................................................................................. 2682
2520 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2531 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
19.5.90 to (To) .............................................................................................................................................. 2683
19.5.91 txEl (Text Element) .......................................................................................................................... 2683
19.5.92 val (Value) ........................................................................................................................................ 2684
19.5.93 video (Video) ................................................................................................................................... 2684
19.5.94 wedge (Wedge Slide Transition) ...................................................................................................... 2685
19.5.95 wheel (Wheel Slide Transition) ........................................................................................................ 2686
19.5.96 wipe (Wipe Slide Transition)............................................................................................................ 2688
19.5.97 zoom (Zoom Slide Transition) .......................................................................................................... 2689
19.6 Slide Synchronization Data ......................................................................................................... 2690
19.6.1 sldSyncPr (Slide Synchronization Properties) .................................................................................. 2690
19.7 Simple Types .............................................................................................................................. 2691
19.7.1 ST_BookmarkIdSeed (Bookmark ID Seed) ....................................................................................... 2691
19.7.2 ST_Direction (Direction) .................................................................................................................. 2691
19.7.3 ST_Index (Index) .............................................................................................................................. 2691
19.7.4 ST_IterateType (Iterate Type) .......................................................................................................... 2692
19.7.5 ST_Name (Name string) ................................................................................................................... 2692
19.7.6 ST_OleObjectFollowColorScheme (Embedded object to Follow Color Scheme) ............................ 2692
19.7.7 ST_PhotoAlbumFrameShape (Photo Album Shape for Photo Mask) .............................................. 2693
19.7.8 ST_PhotoAlbumLayout (Photo Album Layout Definition) ............................................................... 2694
19.7.9 ST_PlaceholderSize (Placeholder Size) ............................................................................................ 2695
19.7.10 ST_PlaceholderType (Placeholder IDs) ............................................................................................ 2696
19.7.11 ST_PrintColorMode (Print Color Mode) .......................................................................................... 2697
19.7.12 ST_PrintWhat (Default print output) ............................................................................................... 2697
19.7.13 ST_SlideId (Slide Identifier) .............................................................................................................. 2698
19.7.14 ST_SlideLayoutId (Slide Layout ID) .................................................................................................. 2698
19.7.15 ST_SlideLayoutType (Slide Layout Type) ......................................................................................... 2698
19.7.16 ST_SlideMasterId (Slide Master ID) ................................................................................................. 2702
19.7.17 ST_SlideSizeCoordinate (Slide Size Coordinate) .............................................................................. 2702
19.7.18 ST_SlideSizeType (Slide Size Type) .................................................................................................. 2702
19.7.19 ST_SplitterBarState (Splitter Bar State) ........................................................................................... 2703
19.7.20 ST_TLAnimateBehaviorCalcMode (Time List Animate Behavior Calculate Mode).......................... 2703
19.7.21 ST_TLAnimateBehaviorValueType (Time List Animate Behavior Value Types) ............................... 2704
19.7.22 ST_TLAnimateColorDirection (Time List Animate Color Direction) ................................................. 2704
19.7.23 ST_TLAnimateColorSpace (Time List Animate Color Space)............................................................ 2704
19.7.24 ST_TLAnimateEffectTransition (Time List Animate Effect Transition)............................................. 2705
19.7.25 ST_TLAnimateMotionBehaviorOrigin (Time List Animate Motion Behavior Origin) ....................... 2705
19.7.26 ST_TLAnimateMotionPathEditMode (Time List Animate Motion Path Edit Mode)........................ 2705
19.7.27 ST_TLBehaviorAccumulateType (Behavior Accumulate Type) ........................................................ 2706
19.7.28 ST_TLBehaviorAdditiveType (Behavior Additive Type) ................................................................... 2706
19.7.29 ST_TLBehaviorOverrideType (Behavior Override Type) .................................................................. 2707
19.7.30 ST_TLBehaviorTransformType (Behavior Transform Type) ............................................................. 2707
19.7.31 ST_TLChartSubelementType (Chart Subelement Type) .................................................................. 2707
19.7.32 ST_TLCommandType (Command Type) .......................................................................................... 2708
19.7.33 ST_TLDiagramBuildType (Diagram Build Types) .............................................................................. 2708
19.7.34 ST_TLNextActionType (Next Action Type) ....................................................................................... 2709
19.7.35 ST_TLOleChartBuildType (Embedded Chart Build Type) ................................................................. 2709
19.7.36 ST_TLParaBuildType (Paragraph Build Type) ................................................................................... 2710
©ISO/IEC 2016 – All rights reserved 2521\n\n--- Page 2532 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
19.7.37 ST_TLPreviousActionType (Previous Action Type) .......................................................................... 2710
19.7.38 ST_TLTime (Time) ............................................................................................................................ 2711
19.7.39 ST_TLTimeAnimateValueTime (Animation Time) ............................................................................ 2711
19.7.40 ST_TLTimeIndefinite (Indefinite Time Declaration) ......................................................................... 2711
19.7.41 ST_TLTimeNodeFillType (Time Node Fill Type) ............................................................................... 2711
19.7.42 ST_TLTimeNodeID (Time Node ID) .................................................................................................. 2712
19.7.43 ST_TLTimeNodeMasterRelation (Time Node Master Relation) ...................................................... 2712
19.7.44 ST_TLTimeNodePresetClassType (Time Node Preset Class Type) ................................................... 2712
19.7.45 ST_TLTimeNodeRestartType (Time Node Restart Type) ................................................................. 2713
19.7.46 ST_TLTimeNodeSyncType (Time Node Sync Type) .......................................................................... 2713
19.7.47 ST_TLTimeNodeType (Time Node Type) ......................................................................................... 2714
19.7.48 ST_TLTriggerEvent (Trigger Event) .................................................................................................. 2714
19.7.49 ST_TLTriggerRuntimeNode (Trigger RunTime Node) ...................................................................... 2715
19.7.50 ST_TransitionCornerDirectionType (Transition Corner Direction Type) ......................................... 2715
19.7.51 ST_TransitionEightDirectionType (Transition Eight Direction) ........................................................ 2716
19.7.52 ST_TransitionInOutDirectionType (Transition In/Out Direction Type) ........................................... 2716
19.7.53 ST_TransitionSideDirectionType (Transition Side Direction Type) .................................................. 2716
19.7.54 ST_TransitionSpeed (Transition Speed) ........................................................................................... 2717
19.7.55 ST_ViewType (List of View Types) ................................................................................................... 2717
End of informative text.
19.2 Presentation
The Presentation portion of the PresentationML framework houses a set of elements that describe the storing of
presentation-wide and view-specific properties. The presentation-wide properties are those that pertain to the
entire presentation. The view-specific properties assist the generating application and viewing application by
storing parameters that pertain to the final delivery of the presentation.
19.2.1 Presentation Properties
This section contains all presentation-level properties that pertain to a presentation document:
19.2.1.1 bold (Bold Embedded Font)
This element specifies a bold embedded font that is linked to a parent typeface. Once specified, this bold version
of the given typeface name is available for use within the presentation. The actual font data is referenced using
a relationships file that contains links to all fonts available. This font data contains font information for each of
the characters to be made available.
[Example: Consider the following embedded font with a bold version specified.
<p:embeddedFont>
<p:font typeface="MyFont" pitchFamily="34" charset="0"/>
<p:bold r:id="rId2"/>
</p:embeddedFont>
end example]
2522 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2533 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
[Note: Not all characters for a typeface must be stored. It is up to the generating application to determine which
characters are to be stored in the corresponding font data files. end note]
Attributes Description
id (Relationship Specifies the relationship identifier that is used in conjunction with a corresponding
Identifier) relationship file to resolve the location of this embedded font that is referenced in a
presentation.
Namespace:
http://purl.oclc.or The possible values for this attribute are defined by the ST_RelationshipId simple type
g/ooxml/officeDoc (§22.8.2.1).
ument/relationshi
ps
[Note: The W3C XML Schema definition of this element’s content model (CT_EmbeddedFontDataId) is located in
§A.3. end note]
19.2.1.2 boldItalic (Bold Italic Embedded Font)
This element specifies a bold italic embedded font that is linked to a parent typeface. Once specified, this bold
italic version of the given typeface name is available for use within the presentation. The actual font data is
referenced using a relationships file that contains links to all fonts available. This font data contains font
information for each of the characters to be made available.
[Example: Consider the following embedded font with a bold italic version specified.
<p:embeddedFont>
<p:font typeface="MyFont" pitchFamily="34" charset="0"/>
<p:boldItalic r:id="rId2"/>
</p:embeddedFont>
end example]
[Note: Not all characters for a typeface must be stored. It is up to the generating application to determine which
characters are to be stored in the corresponding font data files. end note]
Attributes Description
id (Relationship Specifies the relationship identifier that is used in conjunction with a corresponding
Identifier) relationship file to resolve the location of this embedded font that is referenced in a
presentation.
Namespace:
http://purl.oclc.or The possible values for this attribute are defined by the ST_RelationshipId simple type
g/ooxml/officeDoc (§22.8.2.1).
ument/relationshi
ps
©ISO/IEC 2016 – All rights reserved 2523\n\n--- Page 2534 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
[Note: The W3C XML Schema definition of this element’s content model (CT_EmbeddedFontDataId) is located in
§A.3. end note]
19.2.1.3 browse (Browse Slide Show Mode)
This element specifies that the presentation slide show should be viewed in a single window or browse mode,
instead of full screen.
[Example: Consider the following presentation that is to be viewed in a browse mode.
<p:presentationPr xmlns:a="…" xmlns:r="…" xmlns:p="…">
<p:showPr>
…
<p:browse showScrollbar="0"/>
…
</p:showPr>
</p:presentationPr>
end example]
Attributes Description
showScrollbar Specifies whether to show the scroll bar in the viewing window.
(Show Scroll Bar in
Window) The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
[Note: The W3C XML Schema definition of this element’s content model (CT_ShowInfoBrowse) is located in
§A.3. end note]
19.2.1.4 clrMru (Color MRU)
This specifies the most recently used user-selected colors within the presentation. This list contains custom
user-selected colors outside the presentation's theme colors, enabling the application to expose these
additional color choices for easy reuse. The first item in the list is the most recently used color.
[Example: Consider the following presentation with two user-selected colors in the color MRU list.
<p:presentationPr xmlns:a="…" xmlns:r="…" xmlns:p="…">
…
<p:clrMru>
<a:srgbClr val="5361EB"/>
<a:srgbClr val="CCECFF"/>
</p:clrMru>
…
</p:presentationPr>
2524 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2535 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
end example]
[Note: The W3C XML Schema definition of this element’s content model (CT_ColorMRU) is located in §A.4.1. end
note]
19.2.1.5 custShow (Custom Show)
This element specifies a custom show which is an ordered list of a group of slides that are contained within the
presentation. The custom show element allows for the specification of a presentation order that is different
from the order in which the slides themselves are stored.
[Example: Consider the following custom show list that outlines a couple custom shows for a given set of slides.
<p:custShowLst>
<p:custShow name="Custom Show 1" id="0">
<p:sldLst>
<p:sld r:id="rId4"/>
<p:sld r:id="rId3"/>
<p:sld r:id="rId2"/>
<p:sld r:id="rId5"/>
</p:sldLst>
</p:custShow>
<p:custShow name="Custom Show 2" id="1">
<p:sldLst>
<p:sld r:id="rId4"/>
<p:sld r:id="rId5"/>
</p:sldLst>
</p:custShow>
</p:custShowLst>
In the above example there are two custom shows specified. The first specifies to present the slides in the order
of 4, 3, 2 then 5 while the second specifies to play only slide 4 then 5. end example]
Attributes Description
id (Custom Show This attribute specifies the custom show identification number. This is a number given
Identifier) that should be unique within the presentation document.
The possible values for this attribute are defined by the W3C XML Schema unsignedInt
datatype.
[Note: The W3C XML Schema definition of this element’s content model (CT_CustomShowId) is located in §A.3.
end note]
©ISO/IEC 2016 – All rights reserved 2525\n\n--- Page 2536 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
19.2.1.6 custShow (Custom Show)
This element specifies a custom show that defines a specific slide sequence that the slides are displayed in. This
allows for many variants of the same set of slides to be presented.
[Example: Consider the following custom show using three slides.
<p:custShow name="Custom Show 1" id="0">
<p:sldLst>
<p:sld r:id="rId5"/>
<p:sld r:id="rId2"/>
<p:sld r:id="rId4"/>
</p:sldLst>
</p:custShow>
Notice here that the custom show specifies a show, or presentation, where slide 5 is shown first, then slide 2
and finally slide 4. end example]
Attributes Description
id (Custom Show ID) Specifies the identification number for this custom show. This should be unique among
all the custom shows within the corresponding presentation.
The possible values for this attribute are defined by the W3C XML Schema unsignedInt
datatype.
name (Custom Specifies a name for the custom show.
Show Name)
The possible values for this attribute are defined by the ST_Name simple type (§19.7.5).
[Note: The W3C XML Schema definition of this element’s content model (CT_CustomShow) is located in §A.3.
end note]
19.2.1.7 custShowLst (List of Custom Shows)
This element specifies a list of all custom shows that are available within the corresponding presentation. A
custom show is a defined slide sequence that allows for the displaying of the slides with the presentation in any
arbitrary order.
[Note: The W3C XML Schema definition of this element’s content model (CT_CustomShowList) is located in §A.3.
end note]
19.2.1.8 defaultTextStyle (Presentation Default Text Style)
This element specifies the default text styles that are to be used within the presentation. The text style defined
here can be referenced when inserting a new slide if that slide is not associated with a master slide or if no
styling information has been otherwise specified for the text within the presentation slide.
2526 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2537 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
[Note: The W3C XML Schema definition of this element’s content model (CT_TextListStyle) is located in §A.4.1.
end note]
19.2.1.9 embeddedFont (Embedded Font)
This element specifies an embedded font. Once specified, this font is available for use within the presentation.
Within a font specification there can be regular, bold, italic and boldItalic versions of the font specified. The
actual font data for each of these is referenced using a relationships file that contains links to all available fonts.
This font data contains font information for each of the characters to be made available in each version of the
font.
[Example: Consider the following embedded font.
<p:embeddedFont>
<p:font typeface="MyFont" pitchFamily="34" charset="0"/>
<p:regular r:id="rId2"/>
</p:embeddedFont>
end example]
[Note: Not all characters for a typeface must be stored. It is up to the generating application to determine which
characters are to be stored in the corresponding font data files. end note]
[Note: The W3C XML Schema definition of this element’s content model (CT_EmbeddedFontListEntry) is located
in §A.3. end note]
19.2.1.10 embeddedFontLst (Embedded Font List)
This element specifies a list of fonts that are embedded within the corresponding presentation. The font data for
these fonts is stored alongside the other document parts within the document container. The actual font data is
referenced within the embeddedFont element.
[Note: The W3C XML Schema definition of this element’s content model (CT_EmbeddedFontList) is located in
§A.3. end note]
19.2.1.11 ext (Extension)
This element specifies an extension that is used for future extensions to the current version of DrawingML. This
allows for the specifying of currently unknown elements for later versions of generating applications.
[Note: This element is not intended to reintroduce transitional schema into the strict conformance class. end
note]
Attributes Description
uri (Uniform This attribute specifies the URI, or uniform resource identifier that represents the data
Resource Identifier) stored under this tag. The URI is used to identify the correct 'server' that can process
the contents of this tag.
©ISO/IEC 2016 – All rights reserved 2527\n\n--- Page 2538 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
The possible values for this attribute are defined by the W3C XML Schema token
datatype.
[Note: The W3C XML Schema definition of this element’s content model (CT_Extension) is located in §A.3. end
note]
19.2.1.12 extLst (Extension List)
This element specifies the extension list within which all future extensions of element type ext are defined. The
extension list along with corresponding future extensions is used to extend the storage capabilities of the
PresentationML framework. This allows for various new kinds of data to be stored natively within the
framework.
[Note: The W3C XML Schema definition of this element’s content model (CT_ExtensionList) is located in §A.3.
end note]
19.2.1.13 font (Embedded Font Name)
This element specifies specific properties describing an embedded font. Once specified, this font is available for
use within the presentation. Within a font specification there can be regular, bold, italic and boldItalic versions
of the font specified. The actual font data for each of these is referenced using a relationships file that contains
links to all available fonts. This font data contains font information for each of the characters to be made
available in each version of the font.
[Example: Consider the following embedded font.
<p:embeddedFont>
<p:font typeface="MyFont" pitchFamily="34" charset="0"/>
<p:regular r:id="rId2"/>
</p:embeddedFont>
end example]
Font Substitution Logic:
If the specified font is not available on a system being used for rendering, then the attributes of this element are
to be utilized in selecting an alternate font.
[Note: Not all characters for a typeface must be stored. It is up to the generating application to determine which
characters are to be stored in the corresponding font data files. end note]
If ambiguities exist between properties in the markup of a body of text that refers to an embedded font (such as
the latin element specified in §21.1.2.3.7) and properties in the markup of the corresponding instance of this
embedded font element, the determination whether to use that embedded font is application-dependent
behavior. If ambiguities exist between properties in the markup of an instance of this embedded font element
2528 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2539 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
and properties within the corresponding embedded Font part as specified in §15.2.13, the determination
whether to use that embedded font is application-dependent behavior.
Attributes Description
charset (Similar Character Set) Specifies the character set that is supported by the parent
font. This information can be used in font substitution logic to
locate an appropriate substitute font when this font is not
available. This information is determined by querying the font
when present and shall not be modified when the font is not
available.
The value of this attribute shall be interpreted as follows:
Value Description
0x00 Specifies the ANSI character set. (IANA name
iso-8859-1)
0x01 Specifies the default character set.
0x02 Specifies the Symbol character set. This value
specifies that the characters in the Unicode
private use area (U+FF00 to U+FFFF) of the font
should be used to display characters in the
range U+0000 to U+00FF.
0x4D Specifies a Macintosh (Standard Roman)
character set. (IANA name macintosh)
0x80 Specifies the JIS character set. (IANA name
shift_jis)
0x81 Specifies the Hangul character set. (IANA name
ks_c_5601-1987)
0x82 Specifies a Johab character set. (IANA name KS
C-5601-1992)
0x86 Specifies the GB-2312 character set. (IANA
name GBK)
0x88 Specifies the Chinese Big Five character set.
©ISO/IEC 2016 – All rights reserved 2529\n\n--- Page 2540 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
(IANA name Big5)
0xA1 Specifies a Greek character set. (IANA name
windows-1253)
0xA2 Specifies a Turkish character set. (IANA name
iso-8859-9)
0xA3 Specifies a Vietnamese character set. (IANA
name windows-1258)
0xB1 Specifies a Hebrew character set. (IANA name
windows-1255)
0xB2 Specifies an Arabic character set. (IANA name
windows-1256)
0xBA Specifies a Baltic character set. (IANA name
windows-1257)
0xCC Specifies a Russian character set. (IANA name
windows-1251)
0xDE Specifies a Thai character set. (IANA name
windows-874)
0xEE Specifies an Eastern European character set.
(IANA name windows-1250)
0xFF Specifies an OEM character set not defined by
ISO/IEC 29500.
Any Application-defined, can be ignored.
other
value
The possible values for this attribute are defined by the W3C
XML Schema byte datatype.
panose (Panose Setting) Specifies the Panose-1 classification number for the current
font using the mechanism defined in §4.2.7.17 of ISO/IEC
2530 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2541 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
14496-22:2007.
The possible values for this attribute are defined by the
ST_Panose simple type (§22.9.2.8).
pitchFamily (Similar Font Family) Specifies the font pitch as well as the font family for the
corresponding font.
This information is determined by querying the font when
present and shall not be modified when the font is not
available. This information can be used in font substitution
logic to locate an appropriate substitute font when this font is
not available.
The possible values for this attribute are defined by the
ST_PitchFamily simple type (§20.1.10.41).
typeface (Text Typeface) Specifies the typeface, or name of the font that is to be used.
The typeface is a string name of the specific font that should
Namespace: be used in rendering the presentation. If this font is not
http://purl.oclc.org/ooxml/drawingml/main available within the font list of the generating application than
font substitution logic should be utilized in order to select an
alternate font.
The possible values for this attribute are defined by the
ST_TextTypeface simple type (§20.1.10.81).
[Note: The W3C XML Schema definition of this element’s content model (CT_TextFont) is located in §A.4.1. end
note]
19.2.1.14 handoutMasterId (Handout Master ID)
This element specifies a handout master that is available within the corresponding presentation. A handout
master is a slide that is specifically designed for printing as a handout.
[Example: Consider the following specification of a handout master within a presentation
<p:presentation xmlns:a="…" xmlns:r="…" xmlns:p="…" embedTrueTypeFonts="1">
…
<p:handoutMasterIdLst>
<p:handoutMasterId r:id="rId8"/>
</p:handoutMasterIdLst>
…
</p:presentation>
end example]
©ISO/IEC 2016 – All rights reserved 2531\n\n--- Page 2542 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
id (Relationship Specifies the relationship identifier that is used in conjunction with a corresponding
Identifier) relationship file to resolve the location within a presentation of the handoutMaster
element defining this handout master.
Namespace:
http://purl.oclc.or The possible values for this attribute are defined by the ST_RelationshipId simple type
g/ooxml/officeDoc (§22.8.2.1).
ument/relationshi
ps
[Note: The W3C XML Schema definition of this element’s content model (CT_HandoutMasterIdListEntry) is
located in §A.3. end note]
19.2.1.15 handoutMasterIdLst (List of Handout Master IDs)
This element specifies a list of identification information for the handout master slides that are available within
the corresponding presentation. A handout master is a slide that is specifically designed for printing as a
handout.
[Note: The W3C XML Schema definition of this element’s content model (CT_HandoutMasterIdList) is located in
§A.3. end note]
19.2.1.16 italic (Italic Embedded Font)
This element specifies an italic embedded font that is linked to a parent typeface. Once specified, this italic
version of the given typeface name is available for use within the presentation. The actual font data is
referenced using a relationships file that contains links to all fonts available. This font data contains font
information for each of the characters to be made available.
[Example: Consider the following embedded font with a italic version specified.
<p:embeddedFont>
<p:font typeface="MyFont" pitchFamily="34" charset="0"/>
<p:italic r:id="rId2"/>
</p:embeddedFont>
end example]
[Note: Not all characters for a typeface must be stored. It is up to the generating application to determine which
characters are to be stored in the corresponding font data files. end note]
Attributes Description
id (Relationship Specifies the relationship identifier that is used in conjunction with a corresponding
Identifier) relationship file to resolve the location of this embedded font that is referenced in a
presentation.
Namespace:
2532 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2543 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
http://purl.oclc.or The possible values for this attribute are defined by the ST_RelationshipId simple type
g/ooxml/officeDoc (§22.8.2.1).
ument/relationshi
ps
[Note: The W3C XML Schema definition of this element’s content model (CT_EmbeddedFontDataId) is located in
§A.3. end note]
19.2.1.17 kinsoku (Kinsoku Settings)
This element specifies the presentation-wide kinsoku settings that define the line breaking behaviour of East
Asian text within the corresponding presentation.
Attributes Description
invalEndChars Specifies the characters that cannot end a line of text.
(Invalid Kinsoku End
Characters) The possible values for this attribute are defined by the W3C XML Schema string
datatype.
invalStChars Specifies the characters that cannot start a line of text.
(Invalid Kinsoku
Start Characters) The possible values for this attribute are defined by the W3C XML Schema string
datatype.
lang (Language) Specifies the corresponding East Asian language that these settings apply to.
The possible values for this attribute are defined by the W3C XML Schema string
datatype.
[Note: The W3C XML Schema definition of this element’s content model (CT_Kinsoku) is located in §A.3. end
note]
19.2.1.18 kiosk (Kiosk Slide Show Mode)
This element specifies that the presentation slide show should be viewed in a full-screen kiosk mode. A
presentation viewed in kiosk mode should have user input disabled and restarts after a specified interval.
[Example: Consider the following presentation that is set to be viewed in a looping kiosk mode.
<p:presentationPr xmlns:a="…" xmlns:r="…" xmlns:p="…">
<p:showPr loop="1" showNarration="1">
…
<p:kiosk/>
…
</p:showPr>
©ISO/IEC 2016 – All rights reserved 2533\n\n--- Page 2544 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
</p:presentationPr>
end example]
Attributes Description
restart (Restart Specifies the time length that the presentation should run until it is to be restarted. That
Show) is, the presentation should loop back to the first slide specified in the presentation or
custom show. This value is specified in 1/1000ths of a second and measured from the
most recent time the presentation started or restarted.
[Note: The counter is reset when a presentation is restarted due to automatic looping at
the end of a show, if specified by the loop attribute of showPr. end note]
The possible values for this attribute are defined by the W3C XML Schema unsignedInt
datatype.
[Note: The W3C XML Schema definition of this element’s content model (CT_ShowInfoKiosk) is located in §A.3.
end note]
19.2.1.19 modifyVerifier (Modification Verifier)
This element specifies the write protection settings which have been applied to a PresentationML document.
Write protection refers to a mode in which the document's contents should not be modified, and the document
should not be resaved using the same file name.
When present, the application shall require a password to enable modifications to the document. If the
supplied password does not match the hash value in this attribute, then write protection shall be enabled. If this
element is omitted, then no write protection shall be applied to the current document. Since this protection
does not encrypt the document, malicious applications might circumvent its use.
The password supplied to the algorithm is to be a UTF-16LE encoded string; strings longer than 510 octets are
truncated to 510 octets. If there is a leading BOM character (U+FEFF) in the encoded password it is removed
before hash calculation. The attributes of this element specify the algorithm to be used to verify the password
provided by the user.
[Example: Consider a PresentationML document that can only be opened in a write protected state unless a
password is provided, in which case the file would be opened in an editable state. This requirement would be
specified using the following PresentationML:
<p:modifyVerifier p:algorithmName="SHA-512" …
p:hashValue="9oN7nWkCAyEZib1RomSJTjmPpCY=" … />
…In order for the hosting application to enable edits to the document, the hosting application would have to be
provided with a password that the hosting application would then hash using the algorithm specified by the
2534 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2545 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
algorithm attributes and compare to the value of the hashValue attribute (9oN7nWkCAyEZib1RomSJTjmPpCY=).
If the two values matched, the file would be opened in an editable state. end example]
Attributes Description
algorithmName Specifies the specific cryptographic hashing algorithm which shall be used along with the
(Cryptographic salt attribute and input password in order to compute the hash value.
Algorithm Name)
The following values are reserved:
Value Algorithm
MD2 Specifies that the MD2 algorithm, as defined by RFC 1319, shall
be used.
[Note: It is recommended that applications should avoid using
this algorithm to store new hash values, due to publically known
breaks. end note]
MD4 Specifies that the MD4 algorithm, as defined by RFC 1320, shall
be used.
[Note: It is recommended that applications should avoid using
this algorithm to store new hash values, due to publically known
breaks. end note]
MD5 Specifies that the MD5 algorithm, as defined by RFC 1321, shall
be used.
[Note: It is recommended that applications should avoid using
this algorithm to store new hash values, due to publically known
breaks. end note]
RIPEMD-128 Specifies that the RIPEMD-128 algorithm, as defined by ISO/IEC
10118-3:2004 shall be used.
[Note: It is recommended that applications should avoid using
this algorithm to store new hash values, due to publically known
breaks. end note]
RIPEMD-160 Specifies that the RIPEMD-160 algorithm, as defined by ISO/IEC
10118-3:2004 shall be used.
SHA-1 Specifies that the SHA-1 algorithm, as defined by ISO/IEC 10118-
3:2004 shall be used.
SHA-256 Specifies that the SHA-256 algorithm, as defined by ISO/IEC
10118-3:2004 shall be used.
SHA-384 Specifies that the SHA-384 algorithm, as defined by ISO/IEC
10118-3:2004 shall be used.
SHA-512 Specifies that the SHA-512 algorithm, as defined by ISO/IEC
10118-3:2004 shall be used.
©ISO/IEC 2016 – All rights reserved 2535\n\n--- Page 2546 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
WHIRLPOOL Specifies that the WHIRLPOOL algorithm, as defined by ISO/IEC
10118-3:2004 shall be used.
[Example: Consider an Office Open XML document with the following information stored
in one of its protection elements:
< … algorithmName="SHA-1"
hashValue="9oN7nWkCAyEZib1RomSJTjmPpCY=" />
The algorithmName attribute value of “SHA-1” specifies that the SHA-1 hashing
algorithm must be used to generate a hash from the user-defined password. end
example]
The possible values for this attribute are defined by the W3C XML Schema string
datatype.
hashValue Specifies the hash value for the password required to edit this chartsheet. This value shall
(Password Hash be compared with the resulting hash value after hashing the user-supplied password
Value) using the algorithm specified by the preceding attributes and parent XML element, and if
the two values match, the protection shall no longer be enforced.
If this value is omitted, then the reservationPassword attribute shall contain the
password hash for the workbook.
[Example: Consider an Office Open XML document with the following information stored
in one of its protection elements:
<… algorithmName="SHA-1"
hashValue="9oN7nWkCAyEZib1RomSJTjmPpCY=" />
The hashValue attribute value of 9oN7nWkCAyEZib1RomSJTjmPpCY= specifies that the
user-supplied password must be hashed using the pre-processing defined by the parent
element (if any) followed by the SHA-1 algorithm (specified via the algorithmName
attribute value of SHA-1) and that the resulting has value must be
9oN7nWkCAyEZib1RomSJTjmPpCY= for the protection to be disabled. end example]
The possible values for this attribute are defined by the W3C XML Schema base64Binary
datatype.
saltValue (Salt Specifies the salt which was prepended to the user-supplied password before it was
Value for Password hashed using the hashing algorithm defined by the preceding attribute values to generate
Verifier) the hashValue attribute, and which shall also be prepended to the user-supplied
password before attempting to generate a hash value for comparison. A salt is a random
string which is added to a user-supplied password before it is hashed in order to prevent
a malicious party from pre-calculating all possible password/hash combinations and
simply using those pre-calculated values (often referred to as a "dictionary attack").
2536 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2547 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
If this attribute is omitted, then no salt shall be prepended to the user-supplied password
before it is hashed for comparison with the stored hash value.
[Example: Consider an Office Open XML document with the following information stored
in one of its protection elements:
<… saltValue="ZUdHa+D8F/OAKP3I7ssUnQ=="
hashValue="9oN7nWkCAyEZib1RomSJTjmPpCY=" />
The saltValue attribute value of ZUdHa+D8F/OAKP3I7ssUnQ== specifies that the user-
supplied password must have this value prepended before it is run through the specified
hashing algorithm to generate a resulting hash value for comparison. end example]
The possible values for this attribute are defined by the W3C XML Schema base64Binary
datatype.
spinValue Specifies the number of times the hashing function shall be iteratively run (runs using
(Iterations to Run each iteration's result plus a 4 byte value (0-based, little endian) containing the number
Hashing Algorithm) of the iteration as the input for the next iteration) when attempting to compare a user-
supplied password with the value stored in the hashValue attribute.
[Rationale: Running the algorithm many times increases the cost of exhaustive search
attacks correspondingly. Storing this value allows for the number of iterations to be
increased over time to accommodate faster hardware (and hence the ability to run more
iterations in less time). end rationale]
[Example: Consider an Office Open XML document with the following information stored
in one of its protection elements:
<… spinCount="100000"
hashValue="9oN7nWkCAyEZib1RomSJTjmPpCY=" />
The spinCount attribute value of 100000 specifies that the hashing function must be run
one hundred thousand times to generate a hash value for comparison with the
hashValue attribute. end example]
The possible values for this attribute are defined by the W3C XML Schema unsignedInt
datatype.
[Note: The W3C XML Schema definition of this element’s content model (CT_ModifyVerifier) is located in §A.3.
end note]
19.2.1.20 notesMasterId (Notes Master ID)
This element specifies a notes master that is available within the corresponding presentation. A notes master is
a slide that is specifically designed for the printing of the slide along with any attached notes.
©ISO/IEC 2016 – All rights reserved 2537\n\n--- Page 2548 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
[Example: Consider the following specification of a notes master within a presentation
<p:presentation xmlns:a="…" xmlns:r="…" xmlns:p="…" embedTrueTypeFonts="1">
…
<p:notesMasterIdLst>
<p:notesMasterId r:id="rId8"/>
</p:notesMasterIdLst>
…
</p:presentation>
end example]
Attributes Description
id (Relationship Specifies the relationship identifier that is used in conjunction with a corresponding
Identifier) relationship file to resolve the location within a presentation of the notesMaster element
defining this notes master.
Namespace:
http://purl.oclc.or The possible values for this attribute are defined by the ST_RelationshipId simple type
g/ooxml/officeDoc (§22.8.2.1).
ument/relationshi
ps
[Note: The W3C XML Schema definition of this element’s content model (CT_NotesMasterIdListEntry) is located
in §A.3. end note]
19.2.1.21 notesMasterIdLst (List of Notes Master IDs)
This element specifies a list of identification information for the notes master slides that are available within the
corresponding presentation. A notes master is a slide that is specifically designed for the printing of the slide
along with any attached notes.
[Note: The W3C XML Schema definition of this element’s content model (CT_NotesMasterIdList) is located in
§A.3. end note]
19.2.1.22 notesSz (Notes Slide Size)
This element specifies the size of slide surface used for notes slides and handout slides. Objects within a notes
slide can be specified outside these extents, but the notes slide has a background surface of the specified size
when presented or printed. This element is intended to specify the region to which content is fitted in any
special format of printout the application might choose to generate, such as an outline handout.
[Example: Consider the following specifying of the size of a notes slide.
<p:presentation xmlns:a="…" xmlns:r="…" xmlns:p="…" embedTrueTypeFonts="1">
…
<p:notesSz cx="9144000" cy="6858000"/>
2538 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2549 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
…
</p:presentation>
end example]
Attributes Description
cx (Extent Length) Specifies the length of the extents rectangle in EMUs. This rectangle shall dictate the size
of the object as displayed (the result of any scaling to the original object).
Namespace:
http://purl.oclc.or [Example: Consider a DrawingML object specified as follows:
g/ooxml/drawing
ml/main <… cx="1828800" cy="200000"/>
The cx attributes specifies that this object has a height of 1828800 EMUs (English Metric
Units). end example]
The possible values for this attribute are defined by the ST_PositiveCoordinate simple
type (§20.1.10.41).
cy (Extent Width) Specifies the width of the extents rectangle in EMUs. This rectangle shall dictate the size
of the object as displayed (the result of any scaling to the original object).
Namespace:
http://purl.oclc.or [Example: Consider a DrawingML object specified as follows:
g/ooxml/drawing
ml/main < … cx="1828800" cy="200000"/>
The cy attribute specifies that this object has a width of 200000 EMUs (English Metric
Units). end example]
The possible values for this attribute are defined by the ST_PositiveCoordinate simple
type (§20.1.10.41).
[Note: The W3C XML Schema definition of this element’s content model (CT_PositiveSize2D) is located in §A.4.1.
end note]
19.2.1.23 penClr (Pen Color for Slide Show)
This element specifies the pen color that should be used to make markings on the slides while in a presentation.
[Note: The W3C XML Schema definition of this element’s content model (CT_Color) is located in §A.4.1. end
note]
19.2.1.24 photoAlbum (Photo Album Information)
This element specifies that the corresponding presentation contains a photo album. A photo album specifies a
list of images within the presentation that spread across one or more slides, all of which share a consistent
layout. Each image in the album is formatted with a consistent style. This functionality enables the application
to manage all of the images together and modify their ordering, layout, and formatting as a set.
©ISO/IEC 2016 – All rights reserved 2539\n\n--- Page 2550 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
This element does not enforce the specified properties on individual photo album images; rather, it specifies
common settings that should be applied by default to all photo album images and their containing slides.
Images that are part of the photo album are identified by the presence of the isPhoto element in the definition
of the picture.
[Example: Consider the following presentation that has been specified as a photo album
<p:presentation xmlns:a="…" xmlns:r="…" xmlns:p="…" embedTrueTypeFonts="1">
…
<p:photoAlbum bw="1" layout="2pic"/>
…
</p:presentation>
end example]
Attributes Description
bw (Black and Specifies whether all pictures in the photo album are to be displayed as black and white.
White)
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
frame (Frame Type) Specifies the frame type that is to be used on all the pictures in the photo album.
The possible values for this attribute are defined by the ST_PhotoAlbumFrameShape
simple type (§19.7.7).
layout (Photo Specifies the layout that is to be used to arrange the pictures in the photo album on
Album Layout) individual slides.
The possible values for this attribute are defined by the ST_PhotoAlbumLayout simple
type (§19.7.8).
showCaptions Specifies whether to show captions for pictures in the photo album. Captions are text
(Show/Hide boxes grouped with each image, with the group set to not allow ungrouping.
Captions)
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
[Note: The W3C XML Schema definition of this element’s content model (CT_PhotoAlbum) is located in §A.3. end
note]
19.2.1.25 present (Presenter Slide Show Mode)
This element specifies that the presentation slide show should be viewed in a full-screen presenter mode. In
this mode, the presentation is displayed on one monitor while a different monitor displays notes and provides
navigation controls intended to be viewed only by the presenter.
[Example: Consider the following presentation that is set to be viewed in a present mode.
2540 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2551 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
<p:presentationPr xmlns:a="…" xmlns:r="…" xmlns:p="…">
<p:showPr>
…
<p:present/>
…
</p:showPr>
</p:presentationPr>
end example]
[Note: The W3C XML Schema definition of this element’s content model (CT_Empty) is located in §A.3. end note]
19.2.1.26 presentation (Presentation)
This element specifies within it fundamental presentation-wide properties.
[Example: Consider the following presentation with a single slide master and two slides. In addition to these
commonly used elements there can also be the specification of other properties such as slide size, notes size and
default text styles.
<p:presentation xmlns:a="…" xmlns:r="…" xmlns:p="…">
<p:sldMasterIdLst>
<p:sldMasterId id="2147483648" r:id="rId1"/>
</p:sldMasterIdLst>
<p:sldIdLst>
<p:sldId id="256" r:id="rId3"/>
<p:sldId id="257" r:id="rId4"/>
</p:sldIdLst>
<p:sldSz cx="9144000" cy="6858000" type="screen4x3"/>
<p:notesSz cx="6858000" cy="9144000"/>
<p:defaultTextStyle>
…
</p:defaultTextStyle>
</p:presentation>
end example]
Attributes Description
autoCompressPict Specifies whether the generating application should automatically compress all pictures
ures (Automatically for this presentation.
Compress Pictures)
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
bookmarkIdSeed Specifies a seed for generating bookmark IDs to ensure IDs remain unique across the
(Bookmark ID Seed) document. This value specifies the number to be used as the ID for the next new
bookmark created.
©ISO/IEC 2016 – All rights reserved 2541\n\n--- Page 2552 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
The possible values for this attribute are defined by the ST_BookmarkIdSeed simple
type (§19.7.1).
compatMode Specifies whether the generating application is to be in a compatibility mode which
(Compatibility serves to inform the user of any loss of content or functionality when working with older
Mode) formats.
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
conformance Specifies the conformance class (§2.1) to which the PresentationML document conforms.
(Document
Conformance Class) If this attribute is omitted, its default value is transitional.
[Example: Consider the following PresentationML Presentation part markup:
<p:presentation conformance="strict">
…
</p:presentation>
This document has a conformance attribute value of strict, therefore it conforms to
the PML Strict conformance class. end example]
The possible values for this attribute are defined by the ST_ConformanceClass simple
type (§22.9.2.2).
embedTrueTypeFo Specifies whether the generating application should automatically embed true type fonts
nts (Embed True or not.
Type Fonts)
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
firstSlideNum (First Specifies the first slide number in the presentation.
Slide Number)
The possible values for this attribute are defined by the W3C XML Schema int datatype.
removePersonalInf Specifies whether to automatically remove personal information when the presentation
oOnSave (Remove document is saved.
Personal
Information on The possible values for this attribute are defined by the W3C XML Schema boolean
Save) datatype.
rtl (Right-To-Left Specifies if the current view of the user interface is oriented right-to-left or left-to-right.
Views) The view is right-to-left is this value is set to true, and left-to-right otherwise.
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
saveSubsetFonts Specifies to save only the subset of characters used in the presentation when a font is
(Save Subset Fonts) embedded.
2542 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2553 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
serverZoom (Server Specifies the scaling to be used when the presentation is embedded in another
Zoom) document. The embedded slides are to be scaled by this percentage.
The possible values for this attribute are defined by the ST_Percentage simple type
(§20.1.10.40).
showSpecialPlsOn Specifies whether to show the header and footer placeholders on the title slides.
TitleSld (Show
Header and Footer The possible values for this attribute are defined by the W3C XML Schema boolean
Placeholders on datatype.
Titles)
strictFirstAndLastC Specifies whether to use strict characters for starting and ending lines of Japanese text.
hars (Strict First and
Last Characters) The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
[Note: The W3C XML Schema definition of this element’s content model (CT_Presentation) is located in §A.3.
end note]
19.2.1.27 presentationPr (Presentation-wide Properties)
This element functions as a parent element within which additional presentation-wide document properties are
contained. All properties and their corresponding settings are defined within the child elements.
[Note: The W3C XML Schema definition of this element’s content model (CT_PresentationProperties) is located
in §A.3. end note]
19.2.1.28 prnPr (Printing Properties)
This element specifies the default printing properties associated with this presentation document.
Attributes Description
clrMode (Print Specifies the color mode to be used when printing.
Color Mode)
The possible values for this attribute are defined by the ST_PrintColorMode simple type
(§19.7.11).
frameSlides (Frame Specifies whether slides should be framed when printing. When framed, an outline
slides when border is printed for each slide.
printing)
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
hiddenSlides (Print Specifies whether hidden slides should be printed.
©ISO/IEC 2016 – All rights reserved 2543\n\n--- Page 2554 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
Hidden Slides)
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
prnWhat (Print Specifies what the default print output is in terms of content layout.
Output)
The possible values for this attribute are defined by the ST_PrintWhat simple type
(§19.7.12).
scaleToFitPaper Specifies whether the print output should be scaled to fit the paper being used.
(Scale to Fit Paper
when printing) The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
[Note: The W3C XML Schema definition of this element’s content model (CT_PrintProperties) is located in §A.3.
end note]
19.2.1.29 regular (Regular Embedded Font)
This element specifies a regular embedded font that is linked to a parent typeface. Once specified, this regular
version of the given typeface name is available for use within the presentation. The actual font data is
referenced using a relationships file that contains links to all fonts available. This font data contains font
information for each of the characters to be made available.
[Example: Consider the following embedded font with a regular version specified.
<p:embeddedFont>
<p:font typeface="MyFont" pitchFamily="34" charset="0"/>
<p:regular r:id="rId2"/>
</p:embeddedFont>
end example]
[Note: Not all characters for a typeface must be stored. It is up to the generating application to determine which
characters are to be stored in the corresponding font data files. end note]
Attributes Description
id (Relationship Specifies the relationship identifier that is used in conjunction with a corresponding
Identifier) relationship file to resolve the location of this embedded font that is referenced in a
presentation.
Namespace:
http://purl.oclc.or The possible values for this attribute are defined by the ST_RelationshipId simple type
g/ooxml/officeDoc (§22.8.2.1).
ument/relationshi
ps
2544 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2555 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
[Note: The W3C XML Schema definition of this element’s content model (CT_EmbeddedFontDataId) is located in
§A.3. end note]
19.2.1.30 showPr (Presentation-wide Show Properties)
This element functions as a parent element within which all presentation-wide show properties are contained.
All properties and their corresponding settings are defined within the child elements.
Attributes Description
loop (Loop Slide Specifies whether the slide show should be set to loop at the end.
Show)
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
showAnimation Specifies whether slide show animation should be shown when presenting.
(Show Animation in
Slide Show) The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
showNarration Specifies whether slide show narration should be played when presenting.
(Show Narration in
Slide Show) The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
useTimings (Use Specifies whether slide transition timings should be used to advance slides when
Timings in Slide presenting.
Show)
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
[Note: The W3C XML Schema definition of this element’s content model (CT_ShowProperties) is located in §A.3.
end note]
19.2.1.31 sld (Presentation Slide)
This element specifies a slide within a slide list. The slide list is used to specify an ordering of slides.
[Example: Consider the following custom show with an ordering of slides.
<p:custShowLst>
<p:custShow name="Custom Show 1" id="0">
<p:sldLst>
<p:sld r:id="rId4"/>
<p:sld r:id="rId3"/>
<p:sld r:id="rId2"/>
<p:sld r:id="rId5"/>
</p:sldLst>
</p:custShow>
©ISO/IEC 2016 – All rights reserved 2545\n\n--- Page 2556 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
</p:custShowLst>
In the above example the order specified to present the slides is slide 4, then 3, 2 and finally 5. end example]
Attributes Description
id (Relationship ID) This attribute specifies the relationship id that is used to reference to the actual slide
XML file that contains all the information to the slide listed within the slide list.
Namespace:
http://purl.oclc.or The possible values for this attribute are defined by the ST_RelationshipId simple type
g/ooxml/officeDoc (§22.8.2.1).
ument/relationshi
ps
[Note: The W3C XML Schema definition of this element’s content model (CT_SlideRelationshipListEntry) is
located in §A.3. end note]
19.2.1.32 sldAll (All Slides)
This attribute specifies all slides instead of a given range of slides for use within the html publishing properties as
well as the show properties.
[Note: The W3C XML Schema definition of this element’s content model (CT_Empty) is located in §A.3. end note]
19.2.1.33 sldId (Slide ID)
This element specifies a presentation slide that is available within the corresponding presentation. A slide
contains the information that is specific to a single slide such as slide-specific shape and text information.
[Example: Consider the following specification of a slide master within a presentation
<p:presentation xmlns:a="…" xmlns:r="…" xmlns:p="…" embedTrueTypeFonts="1">
..
<p:sldIdLst>
<p:sldId id="256" r:id="rId3"/>
<p:sldId id="257" r:id="rId4"/>
<p:sldId id="258" r:id="rId5"/>
<p:sldId id="259" r:id="rId6"/>
<p:sldId id="260" r:id="rId7"/>
</p:sldIdLst>
..
</p:presentation>
end example]
Attributes Description
id (Relationship Specifies the relationship identifier that is used in conjunction with a corresponding
2546 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2557 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
Identifier) relationship file to resolve the location within a presentation of the sld element defining
this slide.
Namespace:
http://purl.oclc.or The possible values for this attribute are defined by the ST_RelationshipId simple type
g/ooxml/officeDoc (§22.8.2.1).
ument/relationshi
ps
id (Slide Identifier) Specifies the slide identifier that is to contain a value that is unique throughout the
presentation.
The possible values for this attribute are defined by the ST_SlideId simple type
(§19.7.13).
[Note: The W3C XML Schema definition of this element’s content model (CT_SlideIdListEntry) is located in §A.3.
end note]
19.2.1.34 sldIdLst (List of Slide IDs)
This element specifies a list of identification information for the slides that are available within the
corresponding presentation. A slide contains the information that is specific to a single slide such as slide-
specific shape and text information.
[Note: The W3C XML Schema definition of this element’s content model (CT_SlideIdList) is located in §A.3. end
note]
19.2.1.35 sldLst (List of Presentation Slides)
This element specifies a list of presentation slides. A presentation slide contains the information that is specific
to a single slide such as slide-specific shape and text information.
[Note: The W3C XML Schema definition of this element’s content model (CT_SlideRelationshipList) is located in
§A.3. end note]
19.2.1.36 sldMasterId (Slide Master ID)
This element specifies a slide master that is available within the corresponding presentation. A slide master is a
slide that is specifically designed to be a template for all related child layout slides.
[Example: Consider the following specification of a slide master within a presentation
<p:presentation xmlns:a="…" xmlns:r="…" xmlns:p="…" embedTrueTypeFonts="1">
…
<p:sldMasterIdLst>
<p:sldMasterId id="2147483648" r:id="rId1"/>
</p:sldMasterIdLst>
…
©ISO/IEC 2016 – All rights reserved 2547\n\n--- Page 2558 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
</p:presentation>
end example]
Attributes Description
id (Relationship Specifies the relationship identifier that is used in conjunction with a corresponding
Identifier) relationship file to resolve the location within a presentation of the sldMaster element
defining this slide master.
Namespace:
http://purl.oclc.or The possible values for this attribute are defined by the ST_RelationshipId simple type
g/ooxml/officeDoc (§22.8.2.1).
ument/relationshi
ps
id (Slide Master Specifies the slide master identifier that is to contain a value that is unique throughout
Identifier) the presentation.
The possible values for this attribute are defined by the ST_SlideMasterId simple type
(§19.7.16).
[Note: The W3C XML Schema definition of this element’s content model (CT_SlideMasterIdListEntry) is located in
§A.3. end note]
19.2.1.37 sldMasterIdLst (List of Slide Master IDs)
This element specifies a list of identification information for the slide master slides that are available within the
corresponding presentation. A slide master is a slide that is specifically designed to be a template for all related
child layout slides.
[Note: The W3C XML Schema definition of this element’s content model (CT_SlideMasterIdList) is located in
§A.3. end note]
19.2.1.38 sldRg (Slide Range)
This element specifies a slide range for use within the html publishing properties as well as the show properties.
[Note: The indexes used here correlate directly with the presentation slide numbers which they reference to.
That is the slide range must be greater than or equal to 1 and also less than or equal to the number of slides in
the presentation document. end note]
Attributes Description
end (End) This attribute defines the end of the index range.
The possible values for this attribute are defined by the ST_Index simple type (§19.7.3).
st (Start) This attribute defines the start of the index range.
The possible values for this attribute are defined by the ST_Index simple type (§19.7.3).
2548 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2559 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
[Note: The W3C XML Schema definition of this element’s content model (CT_IndexRange) is located in §A.3. end
note]
19.2.1.39 sldSz (Presentation Slide Size)
This element specifies the size of the presentation slide surface. Objects within a presentation slide can be
specified outside these extents, but this is the size of background surface that is shown when the slide is
presented or printed..
[Example: Consider the following specifying of the size of a presentation slide.
<p:presentation xmlns:a="…" xmlns:r="…" xmlns:p="…" embedTrueTypeFonts="1">
…
<p:sldSz cx="9144000" cy="6858000" type="screen4x3"/>
…
</p:presentation>
end example]
Attributes Description
cx (Extent Length) Specifies the length of the extents rectangle in EMUs. This rectangle shall dictate the size
of the object as displayed (the result of any scaling to the original object).
[Example: Consider a DrawingML object specified as follows:
<… cx="1828800" cy="200000"/>
The cx attributes specifies that this object has a height of 1828800 EMUs (English Metric
Units). end example]
The possible values for this attribute are defined by the ST_SlideSizeCoordinate simple
type (§19.7.17).
cy (Extent Width) Specifies the width of the extents rectangle in EMUs. This rectangle shall dictate the size
of the object as displayed (the result of any scaling to the original object).
[Example: Consider a DrawingML object specified as follows:
< … cx="1828800" cy="200000"/>
The cy attribute specifies that this object has a width of 200000 EMUs (English Metric
Units). end example]
The possible values for this attribute are defined by the ST_SlideSizeCoordinate simple
type (§19.7.17).
type (Type of Size) Specifies the kind of slide size that should be used. This identifies in particular the
©ISO/IEC 2016 – All rights reserved 2549\n\n--- Page 2560 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
expected delivery platform for this presentation.
The possible values for this attribute are defined by the ST_SlideSizeType simple type
(§19.7.18).
[Note: The W3C XML Schema definition of this element’s content model (CT_SlideSize) is located in §A.3. end
note]
19.2.1.40 smartTags (Smart Tags)
This element specifies that references to smart tags exist within this document. [Note: For a complete definition
of smart tags, which are semantically identical throughout Office Open XML, see §17.5.1. end note] To denote
the location of smart tags on individual runs of text, there smart tag identifier attributes are specified for each
run to which a smart tag applies. These are further specified in the run property attributes within DrawingML.
[Example: Consider the following PresentationML markup:
<p:presentation>
…
<p:smartTags r:id="rId1"/>
</p:presentation>
The presence of the smartTags element specifies that there is smart tag information within the PresentationML
package. Individual runs are then inspected for the value of the smtId attribute to determine where smart tags
might apply, for example:
<p:txBody>
<a:bodyPr/>
<a:lstStyle/>
<a:p>
<a:r>
<a:rPr lang="en-US" dirty="0" smtId="1"/>
<a:t>CNTS</a:t>
</a:r>
<a:endParaRPr lang="en-US" dirty="0"/>
</a:p>
</p:txBody>
In the sample above there is a smart tag identifier of 1 specified for this run of text to denote that the text
should be inspected for smart tag information. end example]
2550 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2561 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
id (Relationship Specifies the relationship identifier that is used in conjunction with a corresponding
Identifier) relationship file to resolve the location of this smart tag.
Namespace: The possible values for this attribute are defined by the ST_RelationshipId simple type
http://purl.oclc.or (§22.8.2.1).
g/ooxml/officeDoc
ument/relationshi
ps
[Note: The W3C XML Schema definition of this element’s content model (CT_SmartTags) is located in §A.3. end
note]
19.2.2 View Properties
This section contains all properties that pertain to the viewing of the presentation.
19.2.2.1 cSldViewPr (Common Slide View Properties)
This element functions as a container for slide view properties that are common across multiple view property
elements. The specific properties and associated values for these view properties reside within the child
elements and attributes.
Attributes Description
showGuides (Show Specifies whether to show guides when editing the presentation.
Guides in View)
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
snapToGrid (Snap Specifies whether objects should snap to underlying presentation grid when editing.
Objects to Grid)
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
snapToObjects Specifies whether objects should snap to other objects when editing the presentation.
(Snap Objects to
Objects) The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
[Note: The W3C XML Schema definition of this element’s content model (CT_CommonSlideViewProperties) is
located in §A.3. end note]
19.2.2.2 cViewPr (Common View Properties)
This element specifies the view properties that are common across multiple view property elements.
©ISO/IEC 2016 – All rights reserved 2551\n\n--- Page 2562 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
varScale (Variable Specifies that the view content should automatically scale to best fit the current window
Scale) size.
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
[Note: The W3C XML Schema definition of this element’s content model (CT_CommonViewProperties) is located
in §A.3. end note]
19.2.2.3 gridSpacing (Grid Spacing)
This element specifies the grid spacing that should be used for the grid underlying the presentation document.
The grid can be used to align objects on the slide and to display visual positioning cues.
Attributes Description
cx (Extent Length) Specifies the length of the extents rectangle in EMUs. This rectangle shall dictate the size
of the object as displayed (the result of any scaling to the original object).
Namespace:
http://purl.oclc.or [Example: Consider a DrawingML object specified as follows:
g/ooxml/drawing
ml/main <… cx="1828800" cy="200000"/>
The cx attributes specifies that this object has a height of 1828800 EMUs (English Metric
Units). end example]
The possible values for this attribute are defined by the ST_PositiveCoordinate simple
type (§20.1.10.41).
cy (Extent Width) Specifies the width of the extents rectangle in EMUs. This rectangle shall dictate the size
of the object as displayed (the result of any scaling to the original object).
Namespace:
http://purl.oclc.or [Example: Consider a DrawingML object specified as follows:
g/ooxml/drawing
ml/main < … cx="1828800" cy="200000"/>
The cy attribute specifies that this object has a width of 200000 EMUs (English Metric
Units). end example]
The possible values for this attribute are defined by the ST_PositiveCoordinate simple
type (§20.1.10.41).
[Note: The W3C XML Schema definition of this element’s content model (CT_PositiveSize2D) is located in §A.4.1.
end note]
2552 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2563 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
19.2.2.4 guide (A Guide)
This element specifies a guide within the presentation. Guides are lines used for arranging layouts and content
and never appear except as an aid in editing slides.
Attributes Description
orient (Guide Specifies the orientation for a guide.
Orientation)
The possible values for this attribute are defined by the ST_Direction simple type
(§19.7.2).
pos (Guide Position) Specifies the position information for a guide.
The possible values for this attribute are defined by the ST_Coordinate32 simple type
(§20.1.10.17).
[Note: The W3C XML Schema definition of this element’s content model (CT_Guide) is located in §A.3. end note]
19.2.2.5 guideLst (List of Guides)
This element specifies a list of guides for a particular view of the presentation.
[Note: The W3C XML Schema definition of this element’s content model (CT_GuideList) is located in §A.3. end
note]
19.2.2.6 normalViewPr (Normal View Properties)
This element specifies the view properties associated with the normal slide view (§19.7.55) mode. The normal
slide view consists of three content regions: the slide itself, a side content region, and a bottom content region.
The content of the side content region and bottom content region is determined by the generating application.
Properties pertaining to the positioning of the different content regions are stored in this element. This
information allows the application to save its view state to the file, so that when reopened the view is in the
same state as when the presentation was last saved.
A vertical splitter bar separates the slide from the side content region. A horizontal splitter bar separates the
slide from the content region below the slide. If the presentation is set to left-to-right, the side content region is
to the left of the slide. If the presentation is set to right-to-left, the side content region is to the right of the
slide.
©ISO/IEC 2016 – All rights reserved 2553\n\n--- Page 2564 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
horzBarState (State Specifies the state that the horizontal splitter bar should be in when in normal slide view
of the Horizontal mode (§19.7.55). The region to be maximized or minimized is the side content region.
Splitter Bar)
The possible values for this attribute are defined by the ST_SplitterBarState simple type
(§19.7.19).
preferSingleView Specifies whether the user prefers to see a full-window single-content region over the
(Prefer Single View) normal slide view(§19.7.55) with three content regions. If enabled, the application can
choose to display one of the content regions in the entire window.
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
showOutlineIcons Specifies whether the application should show icons if displaying outline content in any
(Show Outline Icons of the content regions of normal slide view mode (§19.7.55).
in Normal View)
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
snapVertSplitter Specifies whether the vertical splitter should snap to a minimized state when the side
(Snap Vertical region is sufficiently small. The specific parameters of this behaviour are left to the
Splitter) generating application.
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
vertBarState (State Specifies the state that the vertical splitter bar should be in when in normal slide view
of the Vertical mode (§19.7.55). The region to be maximized or minimized is the primary slide content
Splitter Bar) region.
The possible values for this attribute are defined by the ST_SplitterBarState simple type
(§19.7.19).
2554 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2565 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
[Note: The W3C XML Schema definition of this element’s content model (CT_NormalViewProperties) is located
in §A.3. end note]
19.2.2.7 notesTextViewPr (Notes Text View Properties)
This element functions as a parent element within which all properties associated with the notes text view are
contained. All properties are defined within the child elements.
[Note: The W3C XML Schema definition of this element’s content model (CT_NotesTextViewProperties) is
located in §A.3. end note]
19.2.2.8 notesViewPr (Notes View Properties)
This element functions as a parent element within which all view properties associated with notes are
contained. All properties are defined within the child elements.
[Note: The W3C XML Schema definition of this element’s content model (CT_NotesViewProperties) is located in
§A.3. end note]
19.2.2.9 origin (View Origin)
This element specifies the origin of the slide when it is being viewed with various scaling factors using the scale
element.
Attributes Description
x (X-Axis Specifies a coordinate on the x-axis. The origin point for this coordinate shall be specified
Coordinate) by the parent XML element.
Namespace: [Example: Consider the following point on a basic wrapping polygon for a DrawingML
http://purl.oclc.or object:
g/ooxml/drawing
ml/main <… x="0" y="100" />
The x attribute defines an x-coordinate of 0. end example]
The possible values for this attribute are defined by the ST_Coordinate simple type
(§20.1.10.16).
y (Y-Axis Specifies a coordinate on the x-axis. The origin point for this coordinate shall be specified
Coordinate) by the parent XML element.
Namespace: [Example: Consider the following point on a basic wrapping polygon for a DrawingML
http://purl.oclc.or object:
g/ooxml/drawing
ml/main <… x="0" y="100" />
The y attribute defines a y-coordinate of 100. end example]
The possible values for this attribute are defined by the ST_Coordinate simple type
©ISO/IEC 2016 – All rights reserved 2555\n\n--- Page 2566 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
(§20.1.10.16).
[Note: The W3C XML Schema definition of this element’s content model (CT_Point2D) is located in §A.4.1. end
note]
19.2.2.10 outlineViewPr (Outline View Properties)
This element functions as a parent element within which all view properties associated with the outline view
(§19.7.55) mode are contained. All properties are defined within the child elements.
Outline view displays only the textual content of a presentation. The presentation is formatted as an outline,
with slide titles as the first level of the outline. Body text on slides is indented below the slide title.
[Note: The W3C XML Schema definition of this element’s content model (CT_OutlineViewProperties) is located
in §A.3. end note]
19.2.2.11 restoredLeft (Normal View Restored Left Properties)
This element specifies the sizing of the side content region of the normal slide view (§19.7.55), when the region
is of a variable restored size (neither minimized nor maximized).
Attributes Description
autoAdjust (Auto Specifies whether the size of the side content region should compensate for the new size
Adjust Normal when resizing the window containing the view within the application.
View)
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
sz (Normal View Specifies the size of the slide region (width when a child of restoredTop, height when a
Dimension Size) child of restoredLeft).
The possible values for this attribute are defined by the ST_PositiveFixedPercentage
simple type (§20.1.10.45).
[Note: The W3C XML Schema definition of this element’s content model (CT_NormalViewPortion) is located in
§A.3. end note]
19.2.2.12 restoredTop (Normal View Restored Top Properties)
This element specifies the sizing of the top slide region of the normal slide view (§19.7.55), when the region is of
a variable restored size (neither minimized nor maximized).
Attributes Description
autoAdjust (Auto Specifies whether the size of the side content region should compensate for the new size
Adjust Normal when resizing the window containing the view within the application.
2556 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2567 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
View)
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
sz (Normal View Specifies the size of the slide region (width when a child of restoredTop, height when a
Dimension Size) child of restoredLeft).
The possible values for this attribute are defined by the ST_PositiveFixedPercentage
simple type (§20.1.10.45).
[Note: The W3C XML Schema definition of this element’s content model (CT_NormalViewPortion) is located in
§A.3. end note]
19.2.2.13 scale (View Scale)
This element specifies the view scaling factors that the presentation was last viewed with.
[Note: The W3C XML Schema definition of this element’s content model (CT_Scale2D) is located in §A.4.1. end
note]
19.2.2.14 sld (Presentation Slide)
This element specifies a presentation slide and properties specific to the slide's appearance in outline view
(§19.7.55).
[Example: Consider the following presentation slide that has been collapsed in outline view.
<p:viewPr xmlns:a="…" xmlns:r="…" xmlns:p="…" lastView="outlineView">
…
<p:outlineViewPr>
…
<p:sldLst>
<p:sld r:id="rId1" collapse="1"/>
</p:sldLst>
…
</p:outlineViewPr>
…
</p:viewPr>
end example]
Attributes Description
collapse (Collapsed) Specifies whether this presentation slide is to be shown as collapsed within outline view.
That is, all text other than the slide title is not shown to the user.
©ISO/IEC 2016 – All rights reserved 2557\n\n--- Page 2568 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
id (Relationship Specifies the relationship identifier that is used in conjunction with a corresponding
Identifier) relationship file to resolve the location of this presentation slide within a presentation.
Namespace: The possible values for this attribute are defined by the ST_RelationshipId simple type
http://purl.oclc.or (§22.8.2.1).
g/ooxml/officeDoc
ument/relationshi
ps
[Note: The W3C XML Schema definition of this element’s content model (CT_OutlineViewSlideEntry) is located in
§A.3. end note]
19.2.2.15 sldLst (List of Presentation Slides)
This element specifies a list of presentation slides. A presentation slide contains the information that is specific
to a single slide such as slide-specific shape and text information.
[Note: The W3C XML Schema definition of this element’s content model (CT_OutlineViewSlideList) is located in
§A.3. end note]
19.2.2.16 slideViewPr (Slide View Properties)
This element functions as a parent element within which all view properties associated with the slide view mode
are contained. All properties are defined within the child elements.
[Note: The W3C XML Schema definition of this element’s content model (CT_SlideViewProperties) is located in
§A.3. end note]
19.2.2.17 sorterViewPr (Slide Sorter View Properties)
This element functions as a parent element within which all view properties associated with the slide sorter view
(§19.7.55) mode are contained. All properties are defined within the child elements.
The slide sorter view displays thumbnails of multiple slides at once; the number of slides and size of thumbnails
depends on the scaling factor of the view.
Attributes Description
showFormatting Specifies whether to show associated slide formatting when in slide sorter view mode.
(Show Formatting)
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
2558 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2569 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
[Note: The W3C XML Schema definition of this element’s content model (CT_SlideSorterViewProperties) is
located in §A.3. end note]
19.2.2.18 viewPr (Presentation-wide View Properties)
This element functions as a parent element within which all presentation-wide view properties are contained.
All properties and their corresponding settings are defined within the child elements.
Attributes Description
lastView (Last Specifies the view mode that was used when the presentation document was last saved.
View)
The possible values for this attribute are defined by the ST_ViewType simple type
(§19.7.55).
showComments Specifies whether the slide comments should be shown.
(Show Comments)
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
[Note: The W3C XML Schema definition of this element’s content model (CT_ViewProperties) is located in §A.3.
end note]
19.3 Slides
The Slides portion of the PresentationML framework stores all information pertaining specifically to slides of
various slide types. These slide types and corresponding parts can be broken down into three distinct parts,
namely slides, embedded objects, and programmable tags.
19.3.1 Slides
Being the main segment of this section of PresentationML, the slides elements encompass all data that is to be
contained within a slide. The best way to think of a slide is a container for all data that is to be on that slide. The
specific shapes, images and relations within a slide do not come into play here. The elements here pertain to the
six different slide types that can be described within PresentationML, namely slide, slide layout, slide master,
handout master, notes master and notes slide.
19.3.1.1 bg (Slide Background)
This element specifies the background appearance information for a slide. The slide background covers the
entire slide and is visible where no objects exist and as the background for transparent objects.
Attributes Description
bwMode (Black and Specifies that the background should be rendered using only black and white coloring.
White Mode) That is, the coloring information for the background should be converted to either black
or white when rendering the picture.
[Note: No gray is to be used in rendering this background, only stark black and stark
©ISO/IEC 2016 – All rights reserved 2559\n\n--- Page 2570 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
white. end note]
The possible values for this attribute are defined by the ST_BlackWhiteMode simple type
(§20.1.10.10).
[Note: The W3C XML Schema definition of this element’s content model (CT_Background) is located in §A.3. end
note]
19.3.1.2 bgPr (Background Properties)
This element specifies visual effects used to render the slide background. This includes any fill, image, or effects
that are to make up the background of the slide.
Attributes Description
shadeToTitle Specifies whether the background of the slide is of a shade to title background type. This
(Shade to Title) kind of gradient fill is on the slide background and changes based on the placement of
the slide title placeholder. An example is shown below.
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
[Note: The W3C XML Schema definition of this element’s content model (CT_BackgroundProperties) is located in
§A.3. end note]
19.3.1.3 bgRef (Background Style Reference)
This element specifies the slide background is to use a fill style defined in the style matrix. The idx attribute
refers to the index of a background fill style or fill style within the presentation's style matrix, defined by the
fmtScheme element. A value of 0 or 1000 indicates no background, values 1-999 refer to the index of a fill style
within the fillStyleLst element, and values 1001 and above refer to the index of a background fill style within
2560 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2571 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
the bgFillStyleLst element. The value 1001 corresponds to the first background fill style, 1002 to the second
background fill style, and so on.
[Example:
<p:bgRef idx="2">
<a:schemeClr val="bg2"/>
</p:bgRef>
The above code indicates a slide background with the style's second fill style using the second background color
of the color scheme.
end example]
[Example:
<p:bgRef idx="1001">
<a:schemeClr val="bg2"/>
</p:bgRef>
The above code indicates a slide background with the style's first background fill style using the second
background color of the color scheme.
end example]
Attributes Description
idx (Style Matrix Specifies the style matrix index of the style referred to.
Index)
The possible values for this attribute are defined by the ST_StyleMatrixColumnIndex
Namespace: simple type (§20.1.10.57).
http://purl.oclc.or
g/ooxml/drawing
ml/main
[Note: The W3C XML Schema definition of this element’s content model (CT_StyleMatrixReference) is located in
§A.4.1. end note]
19.3.1.4 blipFill (Picture Fill)
This element specifies the kind of picture fill that the picture object has. Because a picture has a picture fill
already by default, it is possible to have two fills specified for a picture object. An example of this is shown
below.
[Example: Consider the picture below that has a blip fill applied to it. The image used to fill this picture object
has transparent pixels instead of white pixels.
<p:pic>
©ISO/IEC 2016 – All rights reserved 2561\n\n--- Page 2572 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
…
<p:blipFill>
<a:blip r:embed="rId2"/>
<a:stretch>
<a:fillRect/>
</a:stretch>
</p:blipFill>
…
</p:pic>
The above picture object is shown as an example of this fill type. end example]
[Example: Consider now the same picture object but with an additional gradient fill applied within the shape
properties portion of the picture.
<p:pic>
…
<p:blipFill>
<a:blip r:embed="rId2"/>
<a:stretch>
<a:fillRect/>
</a:stretch>
</p:blipFill>
<p:spPr>
<a:gradFill>
<a:gsLst>
<a:gs pos="0">
<a:schemeClr val="tx2">
<a:shade val="50000"/>
</a:schemeClr>
</a:gs>
<a:gs pos="39999">
2562 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2573 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
<a:schemeClr val="tx2">
<a:tint val="20000"/>
</a:schemeClr>
</a:gs>
<a:gs pos="70000">
<a:srgbClr val="C4D6EB"/>
</a:gs>
<a:gs pos="100000">
<a:schemeClr val="bg1"/>
</a:gs>
</a:gsLst>
</a:gradFill>
</p:spPr>
…
</p:pic>
The above picture object is shown as an example of this double fill type. end example]
Attributes Description
dpi (DPI Setting) Specifies the DPI (dots per inch) used to calculate the size of the blip. If not present or
zero, the DPI in the blip is used.
Namespace:
http://purl.oclc.or [Note: This attribute is primarily used to keep track of the picture quality within a
g/ooxml/drawing document. There are different levels of quality needed for print than on-screen viewing
ml/main and thus a need to track this information. end note]
The possible values for this attribute are defined by the W3C XML Schema unsignedInt
datatype.
rotWithShape Specifies that the fill should rotate with the shape. That is, when the shape that has been
(Rotate With Shape) filled with a picture and the containing shape (say a rectangle) is transformed with a
rotation then the fill is transformed with the same rotation.
Namespace:
©ISO/IEC 2016 – All rights reserved 2563\n\n--- Page 2574 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
http://purl.oclc.or The possible values for this attribute are defined by the W3C XML Schema boolean
g/ooxml/drawing datatype.
ml/main
[Note: The W3C XML Schema definition of this element’s content model (CT_BlipFillProperties) is located in
§A.4.1. end note]
19.3.1.5 bodyStyle (Slide Master Body Text Style)
This element specifies the text formatting style for all body text within a master slide. This formatting is used on
all body text within presentation slides related to this master. The text formatting is specified by utilizing the
DrawingML framework just as within a regular presentation slide. Within the bodyStyle element there can be
many different style types defined as there are different kinds of text stored within the body of a slide.
[Note: The W3C XML Schema definition of this element’s content model (CT_TextListStyle) is located in §A.4.1.
end note]
19.3.1.6 clrMap (Color Scheme Map)
This element specifies the mapping layer that transforms one color scheme definition to another. Each attribute
represents a color name that can be referenced in this master, and the value is the corresponding color in the
theme.
[Example: Consider the following mapping of colors that applies to a slide master:
<p:clrMap bg1="dk1" tx1="lt1" bg2="dk2" tx2="lt2" accent1="accent1"
accent2="accent2" accent3="accent3" accent4="accent4" accent5="accent5"
accent6="accent6" hlink="hlink" folHlink="folHlink"/>
end example]
Attributes Description
accent1 (Accent 1) Specifies a color defined which is associated as the accent 1 color.
Namespace: The possible values for this attribute are defined by the ST_ColorSchemeIndex simple
http://purl.oclc.or type (§20.1.10.14).
g/ooxml/drawing
ml/main
accent2 (Accent 2) Specifies a color defined which is associated as the accent 2 color.
Namespace: The possible values for this attribute are defined by the ST_ColorSchemeIndex simple
http://purl.oclc.or type (§20.1.10.14).
g/ooxml/drawing
2564 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2575 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
ml/main
accent3 (Accent 3) Specifies a color defined which is associated as the accent 3 color.
Namespace: The possible values for this attribute are defined by the ST_ColorSchemeIndex simple
http://purl.oclc.or type (§20.1.10.14).
g/ooxml/drawing
ml/main
accent4 (Accent 4) Specifies a color defined which is associated as the accent 4 color.
Namespace: The possible values for this attribute are defined by the ST_ColorSchemeIndex simple
http://purl.oclc.or type (§20.1.10.14).
g/ooxml/drawing
ml/main
accent5 (Accent 5) Specifies a color defined which is associated as the accent 5 color.
Namespace: The possible values for this attribute are defined by the ST_ColorSchemeIndex simple
http://purl.oclc.or type (§20.1.10.14).
g/ooxml/drawing
ml/main
accent6 (Accent 6) Specifies a color defined which is associated as the accent 6 color.
Namespace: The possible values for this attribute are defined by the ST_ColorSchemeIndex simple
http://purl.oclc.or type (§20.1.10.14).
g/ooxml/drawing
ml/main
bg1 (Background 1) A color defined which is associated as the first background color.
Namespace: The possible values for this attribute are defined by the ST_ColorSchemeIndex simple
http://purl.oclc.or type (§20.1.10.14).
g/ooxml/drawing
ml/main
bg2 (Background 2) Specifies a color defined which is associated as the second background color.
Namespace: The possible values for this attribute are defined by the ST_ColorSchemeIndex simple
http://purl.oclc.or type (§20.1.10.14).
g/ooxml/drawing
ml/main
folHlink (Followed Specifies a color defined which is associated as the color for a followed hyperlink.
Hyperlink)
The possible values for this attribute are defined by the ST_ColorSchemeIndex simple
Namespace: type (§20.1.10.14).
http://purl.oclc.or
g/ooxml/drawing
ml/main
©ISO/IEC 2016 – All rights reserved 2565\n\n--- Page 2576 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
hlink (Hyperlink) Specifies a color defined which is associated as the color for a hyperlink.
Namespace: The possible values for this attribute are defined by the ST_ColorSchemeIndex simple
http://purl.oclc.or type (§20.1.10.14).
g/ooxml/drawing
ml/main
tx1 (Text 1) Specifies a color defined which is associated as the first text color.
Namespace: The possible values for this attribute are defined by the ST_ColorSchemeIndex simple
http://purl.oclc.or type (§20.1.10.14).
g/ooxml/drawing
ml/main
tx2 (Text 2) Specifies a color defined which is associated as the second text color.
Namespace: The possible values for this attribute are defined by the ST_ColorSchemeIndex simple
http://purl.oclc.or type (§20.1.10.14).
g/ooxml/drawing
ml/main
[Note: The W3C XML Schema definition of this element’s content model (CT_ColorMapping) is located in §A.4.1.
end note]
19.3.1.7 clrMapOvr (Color Scheme Map Override)
This element provides a mechanism with which to override the color schemes listed within the ClrMap element.
If the masterClrMapping element is present, the color scheme defined by the master is used. If the
overrideClrMapping element is present, it defines a new color scheme specific to the parent notes slide,
presentation slide, or slide layout.
[Note: The W3C XML Schema definition of this element’s content model (CT_ColorMappingOverride) is located
in §A.4.1. end note]
19.3.1.8 cNvCxnSpPr (Non-Visual Connector Shape Drawing Properties)
This element specifies the non-visual drawing properties specific to a connector shape. This includes
information specifying the shapes to which the connector shape is connected.
[Note: The W3C XML Schema definition of this element’s content model (CT_NonVisualConnectorProperties) is
located in §A.4.1. end note]
19.3.1.9 cNvGraphicFramePr (Non-Visual Graphic Frame Drawing Properties)
This element specifies the non-visual drawing properties for a graphic frame. These non-visual properties are
properties that the generating application would utilize when rendering the slide surface.
2566 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2577 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
[Note: The W3C XML Schema definition of this element’s content model (CT_NonVisualGraphicFrameProperties)
is located in §A.4.1. end note]
19.3.1.10 cNvGrpSpPr (Non-Visual Group Shape Drawing Properties)
This element specifies the non-visual drawing properties for a group shape. These non-visual properties are
properties that the generating application would utilize when rendering the slide surface.
[Note: The W3C XML Schema definition of this element’s content model
(CT_NonVisualGroupDrawingShapeProps) is located in §A.4.1. end note]
19.3.1.11 cNvPicPr (Non-Visual Picture Drawing Properties)
This element specifies the non-visual properties for the picture canvas. These properties are to be used by the
generating application to determine how certain properties are to be changed for the picture object in question.
[Example: Consider the following DrawingML.
<p:pic>
…
<p:nvPicPr>
<p:cNvPr id="4" name="Lilly_by_Lisher.jpg"/>
<p:cNvPicPr>
<a:picLocks noChangeAspect="1"/>
</p:cNvPicPr>
<p:nvPr/>
</p:nvPicPr>
…
</p:pic>
end example]
Attributes Description
preferRelativeResi Specifies if the user interface should show the resizing of the picture based on the
ze (Relative Resize picture's current size or its original size. If this attribute is set to true, then scaling is
Preferred) relative to the original picture size as opposed to the current picture size.
Namespace: [Example: Consider the case where a picture has been resized within a document and is
http://purl.oclc.or now 50% of the originally inserted picture size. Now if the user chooses to make a later
g/ooxml/drawing adjustment to the size of this picture within the generating application, then the value of
ml/main this attribute should be checked.
If this attribute is set to true then a value of 50% is shown. Similarly, if this attribute is set
to false, then a value of 100% should be shown because the picture has not yet been
resized from its current (smaller) size. end example]
The possible values for this attribute are defined by the W3C XML Schema boolean
©ISO/IEC 2016 – All rights reserved 2567\n\n--- Page 2578 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
datatype.
[Note: The W3C XML Schema definition of this element’s content model (CT_NonVisualPictureProperties) is
located in §A.4.1. end note]
19.3.1.12 cNvPr (Non-Visual Drawing Properties)
This element specifies non-visual canvas properties. This allows for additional information that does not affect
the appearance of the picture to be stored.
[Example: Consider the following DrawingML.
<p:pic>
…
<p:nvPicPr>
<p:cNvPr id="4" name="Lilly_by_Lisher.jpg"/>
</p:nvPicPr>
…
</p:pic>
end example]
Attributes Description
descr (Alternative Specifies alternative text for the current DrawingML object, for use by assistive
Text for Object) technologies or applications which do not display the current object.
Namespace: If this element is omitted, then no alternative text is present for the parent object.
http://purl.oclc.or
g/ooxml/drawing [Example: Consider a DrawingML object defined as follows:
ml/main
<… descr="A picture of a bowl of fruit">
The descr attribute contains alternative text which can be used in place of the actual
DrawingML object. end example]
The possible values for this attribute are defined by the W3C XML Schema string
datatype.
hidden (Hidden) Specifies whether this DrawingML object is displayed. When a DrawingML object is
displayed within a document, that object can be hidden (i.e., present, but not visible).
Namespace: This attribute determines whether the object is rendered or made hidden. [Note: An
http://purl.oclc.or application can have settings which allow this object to be viewed. end note]
g/ooxml/drawing
ml/main If this attribute is omitted, then the parent DrawingML object shall be displayed (i.e., not
hidden).
2568 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2579 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
[Example: Consider an inline DrawingML object which must be hidden within the
document's content. This setting would be specified as follows:
<… hidden="true" />
The hidden attribute has a value of true, which specifies that the DrawingML object is
hidden and not displayed when the document is displayed. end example]
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
id (Unique Specifies a unique identifier for the current DrawingML object within the current
Identifier) document. This ID can be used to assist in uniquely identifying this object so that it can
be referred to by other parts of the document.
Namespace:
http://purl.oclc.or If multiple objects within the same document share the same id attribute value, then the
g/ooxml/drawing document shall be considered non-conformant.
ml/main
[Example: Consider a DrawingML object defined as follows:
<… id="10" … >
The id attribute has a value of 10, which is the unique identifier for this DrawingML
object. end example]
The possible values for this attribute are defined by the ST_DrawingElementId simple
type (§20.1.10.21).
name (Name) Specifies the name of the object. [Note: Typically, this is used to store the original file
name of a picture object. end note]
Namespace:
http://purl.oclc.or [Example: Consider a DrawingML object defined as follows:
g/ooxml/drawing
ml/main < … name="foo.jpg" >
The name attribute has a value of foo.jpg, which is the name of this DrawingML object.
end example]
The possible values for this attribute are defined by the W3C XML Schema string
datatype.
title (Title) Specifies the title (caption) of the current DrawingML object.
Namespace: If this attribute is omitted, then no title text is present for the parent object.
http://purl.oclc.or
g/ooxml/drawing [Example: Consider a DrawingML object defined as follows:
ml/main
©ISO/IEC 2016 – All rights reserved 2569\n\n--- Page 2580 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
<… title="Process Flow Diagram">
end example]
The possible values for this attribute are defined by the W3C XML Schema string
datatype.
[Note: The W3C XML Schema definition of this element’s content model (CT_NonVisualDrawingProps) is located
in §A.4.1. end note]
19.3.1.13 cNvSpPr (Non-Visual Drawing Properties for a Shape)
This element specifies the non-visual drawing properties for a shape. These properties are to be used by the
generating application to determine how the shape should be dealt with
[Example: Consider the shape that has a shape lock applied to it.
<p:sp>
<p:nvSpPr>
<p:cNvPr id="2" name="Rectangle 1"/>
<p:cNvSpPr>
<a:spLocks noGrp="1"/>
</p:cNvSpPr>
</p:nvSpPr>
…
</p:sp>
This shape lock is stored within the non-visual drawing properties for this shape. end example]
Attributes Description
txBox (Text Box) Specifies that the corresponding shape is a text box and thus should be treated as such
by the generating application. If this attribute is omitted then it is assumed that the
Namespace: corresponding shape is not specifically a text box.
http://purl.oclc.or
g/ooxml/drawing [Note: Because a shape is not specified to be a text box does not mean that it cannot
ml/main have text attached to it. A text box is merely a specialized shape with specific properties.
end note]
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
[Note: The W3C XML Schema definition of this element’s content model (CT_NonVisualDrawingShapeProps) is
located in §A.4.1. end note]
2570 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2581 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
19.3.1.14 contentPart (Content Part)
This element specifies a reference to XML content in a format not defined by ISO/IEC 29500. [Note: This part
allows the native use of other commonly used interchange formats, such as:
 MathML (http://www.w3.org/TR/MathML2/)
 SMIL (http://www.w3.org/TR/REC-smil/)
 SVG (http://www.w3.org/TR/SVG11/)
end note]
The relationship type of the explicit relationship specified by this element shall be
http://purl.oclc.org/ooxml/officeDocument/relationships/customXml and have a TargetMode attribute value of
Internal. If an application cannot process content of the content type specified by the targeted part, then it
should continue to process the file. If possible, it should also provide some indication that unknown content was
not imported.
[Note: For better interoperability, only standard XML formats should be used. end note]
[Example: Consider a PresentationML document which includes the following SMIL markup in a part named
smil1.xml:
<!--
Copyright: Copyright 1998-2001 W3C (MIT, INRIA, Keio), All Rights
Reserved.
See http://www.w3.org/Consortium/Legal/.
Author: Aaron Cohen (Intel)
Version: February 7, 2001
Module: Animation Module
Feature: animation
File Name: animation-add-BE-05.smil
Media Components: none
Expected Behavior: Nine red rectangles numbered 1 to 9 shrink to squares
over 2s as follows:
at 2s #1 shrinks.
at 5s #2 shrinks, 1s after #1 completes
at 8s #3 shrinks.
#4 shrinks when it is clicked on.
#5 shrinks 1s after it is clicked on.
#6 shrinks 2s after it is clicked on.
#7 shrinks when the accesskey '1' is pressed.
#8 should be shrunk from 0s since it's wallclock time is in
the past.
#9 will not shrink unless a DOM call causes it to begin.
-->
©ISO/IEC 2016 – All rights reserved 2571\n\n--- Page 2582 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
<smil xmlns="http://www.w3.org/2001/SMIL20/Language">
<head>
<layout>
<root-layout width="640" height="480" backgroundColor="white"/>
<region id="whole" width="640" height="480" z-index="0"/>
<region id="rect1" top="50px" left="90px" height="50px" width="30px"
backgroundColor="red" z-index="1"/>
<region id="rect2" top="50px" left="234px" height="50px" width="30px"
backgroundColor="red" z-index="1"/>
<region id="rect4" top="160px" left="90px" height="50px" width="30px"
backgroundColor="transparent" z-index="1"/>
<region id="rect5" top="160px" left="234px" height="50px" width="30px"
backgroundColor="transparent" z-index="1"/>
<region id="rect6" top="160px" left="380px" height="50px" width="30px"
backgroundColor="transparent" z-index="1"/>
<region id="rect7" top="270px" left="90px" height="50px" width="30px"
backgroundColor="red" z-index="1"/>
<region id="rect8" top="270px" left="234px" height="50px" width="30px"
backgroundColor="red" z-index="1"/>
<region id="rect9" top="270px" left="380px" height="50px" width="30px"
backgroundColor="red" z-index="1"/>
</layout>
</head>
<!-- Copyright 1998-2001 W3C (MIT, INRIA, Keio), All Rights Reserved.
See http://www.w3.org/Consortium/Legal/. -->
<body>
<par dur="indefinite">
<img src="../images/animation-timing-BE-05.jpg" region="whole"/>
<animate id="anim1" targetElement="rect1" attributeName="height" from="50"
to="25" begin="2s" dur="2s" fill="freeze"/>
<animate id="anim2" targetElement="rect2" attributeName="height" from="50"
to="25" begin="anim1.end+1s" dur="2s" fill="freeze"/>
<brush id="brush4" color="red" region="rect4" height="50px" width="30px"/>
<animate id="anim4" targetElement="brush4" attributeName="height"
from="50" to="25" begin="brush4.activateEvent" dur="2s" fill="freeze"/>
<brush id="brush5" color="red" region="rect5" height="50px" width="30px"/>
<animate id="anim5" targetElement="brush5" attributeName="height"
from="50" to="25" begin="brush5.activateEvent+1s" dur="2s" fill="freeze"/>
<brush id="brush6" color="red" region="rect6" height="50px" width="30px"/>
<animate id="anim6a" targetElement="brush6" attributeName="width"
repeatCount="3" from="30" to="30" begin="brush6.activateEvent" dur="1s"
fill="freeze"/>
2572 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2583 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
<animate id="anim6b" targetElement="brush6" attributeName="height"
from="50" to="25" begin="anim6a.repeat(2)" dur="2s" fill="freeze"/>
<animate id="anim7" targetElement="rect7" attributeName="height" from="50"
to="25" begin="accesskey(1)" dur="2s" fill="freeze"/>
<animate id="anim8" targetElement="rect8" attributeName="height" from="50"
to="25" begin="wallclock(2000-01-01T00:00:00Z)" dur="2s" fill="freeze"/>
<animate id="anim9" targetElement="rect9" attributeName="width" from="30"
to="30" begin="indefinite" dur="1s" fill="freeze"/>
</par>
</body>
</smil>
A Slide Part would reference this content as follows:
<p:spTree>
…
<p:contentPart r:id="smil01"/>
…
</p:spTree>
The contentPart element specifies that the content targeted by the relationship with an ID of smil01 is part of
the PresentationML document. Examining the contents of the corresponding relationship part item, we can see
the targets for that relationship:
<Relationships … >
…
<Relationship Id="smil01" TargetMode="Internal"
Type="http://purl.oclc.org/ooxml/officeDocument/relationships/customXml"
Target="smil1.xml" />
…
</Relationships>
The corresponding relationship part item shows that the SMIL content is located next to the slide and is named
smil1.xml. end example]
ttributes Description
id (Relationship to Specifies the relationship ID to a content part.
Part)
[Example: Consider an XML element which has the following id attribute:
Namespace:
http://purl.oclc.or <… r:id="rId1" />
g/ooxml/officeDoc
ument/relationshi The markup specifies the associated relationship part with relationship ID rId1 contains
ps the corresponding relationship information for the parent XML element. end example]
©ISO/IEC 2016 – All rights reserved 2573\n\n--- Page 2584 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
ttributes Description
The possible values for this attribute are defined by the ST_RelationshipId simple type
(§22.8.2.1).
[Note: The W3C XML Schema definition of this element’s content model (CT_Rel) is located in §A.3. end note]
19.3.1.15 controls (List of controls)
This element specifies a list of embedded controls for the corresponding slide. Custom embedded controls can
be embedded on slides.
[Note: The W3C XML Schema definition of this element’s content model (CT_ControlList) is located in §A.3. end
note]
19.3.1.16 cSld (Common Slide Data)
This element specifies a container for slide information that is relevant to all of the slide types. All slides share a
common set of properties that is independent of the slide type; the description of these properties for any
particular slide is stored within the slide's cSld container. Slide data specific to the slide type indicated by the
parent element is stored elsewhere.
[Note: The actual data in cSld describe only the particular parent slide; it is only the kind of information stored
that is common across all slides. end note]
[Example: Consider the following PresentationML slide
<p:sld>
<p:cSld>
<p:spTree>
…
</p:spTree>
</p:cSld>
…
</p:sld>
As the above example shows, the shape tree of a slide (spTree) is a child element of cSld because all slide types
can contain a shape tree. Other slide properties specific to the slide type (such as transitions for sld slides) are
specified elsewhere. end example]
Attributes Description
name (Name) Specifies the slide name property that is used to further identify this unique configuration
of common slide data. This might be used to aid in distinguishing different slide layouts or
various other slide types.
The possible values for this attribute are defined by the W3C XML Schema string
2574 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2585 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
datatype.
[Note: The W3C XML Schema definition of this element’s content model (CT_CommonSlideData) is located in
§A.3. end note]
19.3.1.17 custData (Customer Data)
This element specifies customer data which allows for the specifying and persistence of customer specific data
within the presentation.
Attributes Description
id (Relationship ID) This attribute specifies the relationship id for referencing other resources outside the
scope of the current PresentationML file.
Namespace:
http://purl.oclc.or The possible values for this attribute are defined by the ST_RelationshipId simple type
g/ooxml/officeDoc (§22.8.2.1).
ument/relationshi
ps
[Note: The W3C XML Schema definition of this element’s content model (CT_CustomerData) is located in §A.3.
end note]
19.3.1.18 custDataLst (Customer Data List)
This element allows for the specifying of customer defined data within the PresentationML framework.
References to custom data or tags can be defined within this list.
[Note: The W3C XML Schema definition of this element’s content model (CT_CustomerDataList) is located in
§A.3. end note]
19.3.1.19 cxnSp (Connection Shape)
This element specifies a connection shape that is used to connect two sp elements. Once a connection is
specified using a cxnSp, it is left to the generating application to determine the exact path the connector takes.
That is the connector routing algorithm is left up to the generating application as the desired path might be
different depending on the specific needs of the application.
[Example: Consider the following connector shape that connects two regular shapes.
©ISO/IEC 2016 – All rights reserved 2575\n\n--- Page 2586 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
<p:spTree>
…
<p:sp>
<p:nvSpPr>
<p:cNvPr id="1" name="Rectangle 1"/>
<p:cNvSpPr/>
<p:nvPr/>
</p:nvSpPr>
…
</p:sp>
<p:sp>
<p:nvSpPr>
<p:cNvPr id="2" name="Rectangle 2"/>
<p:cNvSpPr/>
<p:nvPr/>
</p:nvSpPr>
…
</p:sp>
<p:cxnSp>
<p:nvCxnSpPr>
<p:cNvPr id="3" name="Elbow Connector 3"/>
<p:cNvCxnSpPr>
<a:stCxn id="1" idx="3"/>
<a:endCxn id="2" idx="1"/>
</p:cNvCxnSpPr>
<p:nvPr/>
</p:nvCxnSpPr>
…
</p:cxnSp>
</p:spTree>
end example]
[Note: The W3C XML Schema definition of this element’s content model (CT_Connector) is located in §A.3. end
note]
19.3.1.20 extLst (Extension List with Modification Flag)
This element specifies the extension list with modification ability within which all future extensions of element
type ext are defined. The extension list along with corresponding future extensions is used to extend the storage
capabilities of the PresentationML framework. This allows for various new kinds of data to be stored natively
within the framework.
[Note: Using this extLst element allows the generating application to store whether this extension property has
been modified. end note]
2576 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2587 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
mod (Modify) This attribute specifies whether the data contained within this element has been
modified and should thus be processed again by the generating application.
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
[Note: The W3C XML Schema definition of this element’s content model (CT_ExtensionListModify) is located in
§A.3. end note]
19.3.1.21 graphicFrame (Graphic Frame)
This element specifies the existence of a graphics frame. This frame contains a graphic that was generated by an
external source and needs a container in which to be displayed on the slide surface.
Attributes Description
bwMode (Black and Specifies how the graphical object should be rendered, using color, black or white,
White Mode) or grayscale.
Namespace: [Note: This does not mean that the graphical object itself is stored with only black
.../drawingml/2006/main and white or grayscale information. This attribute instead sets the rendering mode
that the graphical object uses. end note]
The possible values for this attribute are defined by the ST_BlackWhiteMode simple
type (§20.1.10.10).
[Note: The W3C XML Schema definition of this element’s content model (CT_GraphicalObjectFrame) is located in
§A.3. end note]
19.3.1.22 grpSp (Group Shape)
This element specifies a group shape that represents many shapes grouped together. This shape is to be treated
just as if it were a regular shape but instead of being described by a single geometry it is made up of all the
shape geometries encompassed within it. Within a group shape each of the shapes that make up the group are
specified just as they normally would. The idea behind grouping elements however is that a single transform can
apply to many shapes at the same time.
[Example: Consider the following group shape.
<p:grpSp>
<p:nvGrpSpPr>
<p:cNvPr id="10" name="Group 9"/>
<p:cNvGrpSpPr/>
<p:nvPr/>
</p:nvGrpSpPr>
©ISO/IEC 2016 – All rights reserved 2577\n\n--- Page 2588 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
<p:grpSpPr>
<a:xfrm>
<a:off x="838200" y="990600"/>
<a:ext cx="2426208" cy="978408"/>
<a:chOff x="838200" y="990600"/>
<a:chExt cx="2426208" cy="978408"/>
</a:xfrm>
</p:grpSpPr>
<p:sp>
…
</p:sp>
<p:sp>
…
</p:sp>
<p:sp>
…
</p:sp>
</p:grpSp>
In the above example we see three shapes specified within a single group. These three shapes have their
position and sizes specified just as they normally would within the shape tree. The generating application should
apply the transformation after the bounding box for the group shape has been calculated. end example]
[Note: The W3C XML Schema definition of this element’s content model (CT_GroupShape) is located in §A.3. end
note]
19.3.1.23 grpSpPr (Group Shape Properties)
This element specifies the properties that are to be common across all of the shapes within the corresponding
group. If there are any conflicting properties within the group shape properties and the individual shape
properties then the individual shape properties should take precedence.
Attributes Description
bwMode (Black and Specifies that the group shape should be rendered using only black and white coloring.
White Mode) That is the coloring information for the group shape should be converted to either black
or white when rendering the corresponding shapes.
Namespace:
http://purl.oclc.or No gray is to be used in rendering this image, only stark black and stark white.
g/ooxml/drawing
ml/main [Note: This does not mean that the group shapes themselves are stored with only black
and white color information. This attribute instead sets the rendering mode that the
shapes use when rendering. end note]
The possible values for this attribute are defined by the ST_BlackWhiteMode simple type
(§20.1.10.10).
2578 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2589 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
[Note: The W3C XML Schema definition of this element’s content model (CT_GroupShapeProperties) is located
in §A.4.1. end note]
19.3.1.24 handoutMaster (Handout Master)
This element specifies an instance of a handout master slide. Within a handout master slide are contained all
elements that describe the objects and their corresponding formatting for within a handout slide. Within a
handout master slide the cSld element specifies the common slide elements such as shapes and their attached
text bodies. There are other properties within a handout master slide but cSld encompasses the majority of the
intended purpose for a handoutMaster slide.
[Note: The W3C XML Schema definition of this element’s content model (CT_HandoutMaster) is located in §A.3.
end note]
19.3.1.25 hf (Header/Footer information for a slide master)
This element specifies the header and footer information for a slide. Headers and footers consist of
placeholders for text that should be consistent across all slides and slide types, such as a date and time, slide
numbering, and custom header and footer text.
Attributes Description
dt (Date/Time Specifies whether the Date/Time placeholder is enabled for this master. If this attribute is
Placeholder) not specified, a value of true should be assumed by the generating application.
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
ftr (Footer Specifies whether the Footer placeholder is enabled for this master. If this attribute is not
Placeholder) specified, a value of true should be assumed by the generating application.
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
hdr (Header Specifies whether the Header placeholder is enabled for this master. If this attribute is
Placeholder) not specified, a value of true should be assumed by the generating application.
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
sldNum (Slide Specifies whether the slide number placeholder is enabled. If this attribute is not
Number specified, a value of true should be assumed by the generating application.
Placeholder)
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
©ISO/IEC 2016 – All rights reserved 2579\n\n--- Page 2590 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
[Note: The W3C XML Schema definition of this element’s content model (CT_HeaderFooter) is located in §A.3.
end note]
19.3.1.26 notes (Notes Slide)
This element specifies the existence of a notes slide along with its corresponding data. Contained within a notes
slide are all the common slide elements along with addition properties that are specific to the notes element.
[Example: Consider the following PresentationML notes slide
<p:notes>
<p:cSld>
…
</p:cSld>
…
</p:notes>
In the above example a notes element specifies the existence of a notes slide with all of its parts. Notice the cSld
element, that specifies the common elements that can appear on any slide type and then any elements specify
additional non-common properties for this notes slide. end example]
Attributes Description
showMasterPhAni Specifies whether or not to display animations on placeholders from the master slide.
m (Show Master
Placeholder The possible values for this attribute are defined by the W3C XML Schema boolean
Animations) datatype.
showMasterSp Specifies if shapes on the master slide should be shown on slides or not.
(Show Master
Shapes)
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
[Note: The W3C XML Schema definition of this element’s content model (CT_NotesSlide) is located in §A.3. end
note]
19.3.1.27 notesMaster (Notes Master)
This element specifies an instance of a notes master slide. Within a notes master slide are contained all
elements that describe the objects and their corresponding formatting for within a notes slide. Within a notes
master slide the cSld element specifies the common slide elements such as shapes and their attached text
bodies. There are other properties within a notes master slide but cSld encompasses the majority of the
intended purpose for a notesMaster slide.
[Note: The W3C XML Schema definition of this element’s content model (CT_NotesMaster) is located in §A.3.
end note]
2580 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2591 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
19.3.1.28 notesStyle (Notes Text Style)
This element specifies the text formatting style for the all other text within a notes slide. This formatting is used
on all text within the corresponding notes slides. The text formatting is specified by utilizing the DrawingML
framework just as within a regular presentation slide. Within the notesStyle element there can be many
different style types defined as there are different kinds of text stored within a notes slide.
[Note: The W3C XML Schema definition of this element’s content model (CT_TextListStyle) is located in §A.4.1.
end note]
19.3.1.29 nvCxnSpPr (Non-Visual Properties for a Connection Shape)
This element specifies all non-visual properties for a connection shape. This element is a container for the non-
visual identification properties, shape properties and application properties that are to be associated with a
connection shape. This allows for additional information that does not affect the appearance of the connection
shape to be stored.
[Note: The W3C XML Schema definition of this element’s content model (CT_ConnectorNonVisual) is located in
§A.3. end note]
19.3.1.30 nvGraphicFramePr (Non-Visual Properties for a Graphic Frame)
This element specifies all non-visual properties for a graphic frame. This element is a container for the non-visual
identification properties, shape properties and application properties that are to be associated with a graphic
frame. This allows for additional information that does not affect the appearance of the graphic frame to be
stored.
[Note: The W3C XML Schema definition of this element’s content model (CT_GraphicalObjectFrameNonVisual) is
located in §A.3. end note]
19.3.1.31 nvGrpSpPr (Non-Visual Properties for a Group Shape)
This element specifies all non-visual properties for a group shape. This element is a container for the non-visual
identification properties, shape properties and application properties that are to be associated with a group
shape. This allows for additional information that does not affect the appearance of the group shape to be
stored.
[Note: The W3C XML Schema definition of this element’s content model (CT_GroupShapeNonVisual) is located
in §A.3. end note]
19.3.1.32 nvPicPr (Non-Visual Properties for a Picture)
This element specifies all non-visual properties for a picture. This element is a container for the non-visual
identification properties, shape properties and application properties that are to be associated with a picture.
This allows for additional information that does not affect the appearance of the picture to be stored.
[Example: Consider the following PresentationML.
<p:pic>
©ISO/IEC 2016 – All rights reserved 2581\n\n--- Page 2592 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
…
<p:nvPicPr>
…
</p:nvPicPr>
…
</p:pic>
end example]
[Note: The W3C XML Schema definition of this element’s content model (CT_PictureNonVisual) is located in
§A.3. end note]
19.3.1.33 nvPr (Non-Visual Properties)
This element specifies non-visual properties for objects. These properties include multimedia content associated
with an object and properties indicating how the object is to be used or displayed in different contexts.
Attributes Description
isPhoto (Is a Photo Specifies whether the picture belongs to a photo album and should thus be included
Album) when editing a photo album within the generating application.
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
userDrawn (Is User Specifies if the corresponding object has been drawn by the user and should thus not be
Drawn) deleted. This allows for the flagging of slides that contain user drawn data.
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
[Note: The W3C XML Schema definition of this element’s content model
(CT_ApplicationNonVisualDrawingProps) is located in §A.3. end note]
19.3.1.34 nvSpPr (Non-Visual Properties for a Shape)
This element specifies all non-visual properties for a shape. This element is a container for the non-visual
identification properties, shape properties and application properties that are to be associated with a shape.
This allows for additional information that does not affect the appearance of the shape to be stored.
[Note: The W3C XML Schema definition of this element’s content model (CT_ShapeNonVisual) is located in §A.3.
end note]
19.3.1.35 otherStyle (Slide Master Other Text Style)
This element specifies the text formatting style for the all other text within a master slide. This formatting is
used on all text not covered by the titleStyle or bodyStyle elements within related presentation slides. The text
formatting is specified by utilizing the DrawingML framework just as within a regular presentation slide. Within
2582 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2593 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
the otherStyle element there can be many different style types defined as there are different kinds of text
stored within a slide.
[Note: The otherStyle element is to be used for specifying the text formatting of text within a slide shape but
not within a text box. Text box styling is handled from within the bodyStyle element. end note]
[Note: The W3C XML Schema definition of this element’s content model (CT_TextListStyle) is located in §A.4.1.
end note]
19.3.1.36 ph (Placeholder Shape)
This element specifies that the corresponding shape should be represented by the generating application as a
placeholder. When a shape is considered a placeholder by the generating application it can have special
properties to alert the user that they can enter content into the shape. Different placeholder types are allowed
and can be specified by using the placeholder type attribute for this element.
Attributes Description
hasCustomPrompt Specifies whether the corresponding placeholder should have a custom prompt or not.
(Placeholder has
custom prompt) The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
idx (Placeholder Specifies the placeholder index. This is used when applying templates or changing
Index) layouts to match a placeholder on one template/master to another.
The possible values for this attribute are defined by the W3C XML Schema unsignedInt
datatype.
orient (Placeholder Specifies the orientation of a placeholder.
Orientation)
The possible values for this attribute are defined by the ST_Direction simple type
(§19.7.2).
sz (Placeholder Size) Specifies the size of a placeholder.
The possible values for this attribute are defined by the ST_PlaceholderSize simple type
(§19.7.9).
type (Placeholder Specifies what content type a placeholder is intended to contain.
Type)
The possible values for this attribute are defined by the ST_PlaceholderType simple type
(§19.7.10).
[Note: The W3C XML Schema definition of this element’s content model (CT_Placeholder) is located in §A.3. end
note]
19.3.1.37 pic (Picture)
This element specifies the existence of a picture object within the document.
©ISO/IEC 2016 – All rights reserved 2583\n\n--- Page 2594 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
[Example: Consider the following PresentationML that specifies the existence of a picture within a document.
This picture can have non-visual properties, a picture fill as well as shape properties attached to it.
<p:pic>
<p:nvPicPr>
<p:cNvPr id="4" name="lake.JPG" descr="Picture of a Lake" />
<p:cNvPicPr>
<a:picLocks noChangeAspect="1"/>
</p:cNvPicPr>
<p:nvPr/>
</p:nvPicPr>
<p:blipFill>
…
</p:blipFill>
<p:spPr>
…
</p:spPr>
</p:pic>
end example]
[Note: The W3C XML Schema definition of this element’s content model (CT_Picture) is located in §A.3. end
note]
19.3.1.38 sld (Presentation Slide)
This element is the root element of a Slide part (§13.3.8) and specifies an instance of a slide. Within a slide are
contained all elements that describe the objects and their corresponding formatting within a presentation slide.
Child elements describe the common slide elements such as shapes and their attached text bodies, transition
and timing specific to this slide and color information specific to this slide.
[Example: Consider the following basic slide.
<p:sld>
<p:cSld>
<p:spTree>
…
</p:spTree>
</p:cSld>
<p:clrMapOver>
…
</p:clrMapOver>
<p:transition>
…
</p:transition>
<p:timing>
2584 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2595 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
…
</p:timing>
</p:sld>
This example shows a slide with its content in the shape tree, a local color mapping override and a slide
transition with associated timing information. end example]
19.3.1.39 sldLayout (Slide Layout)
This element specifies an instance of a slide layout. The slide layout contains in essence a template slide design
that can be applied to any existing slide. When applied to an existing slide all corresponding content should be
mapped to the new slide layout.
Attributes Description
matchingName Specifies a name to be used in place of the name attribute within the cSld element. This
(Matching Name) is used for layout matching in response to layout changes and template applications.
The possible values for this attribute are defined by the W3C XML Schema string
datatype.
preserve (Preserve Specifies whether the corresponding slide layout is deleted when all the slides that follow
Slide Layout) that layout are deleted. If this attribute is not specified then a value of false should be
assumed by the generating application. This would mean that the slide would in fact be
deleted if no slides within the presentation were related to it.
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
showMasterPhAni Specifies whether or not to display animations on placeholders from the master slide.
m (Show Master
Placeholder The possible values for this attribute are defined by the W3C XML Schema boolean
Animations) datatype.
showMasterSp Specifies if shapes on the master slide should be shown on slides or not.
(Show Master
Shapes)
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
type (Slide Layout Specifies the slide layout type that is used by this slide.
Type)
The possible values for this attribute are defined by the ST_SlideLayoutType simple type
(§19.7.15).
userDrawn (Is User Specifies if the corresponding object has been drawn by the user and should thus not be
Drawn) deleted. This allows for the flagging of slides that contain user drawn data.
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
©ISO/IEC 2016 – All rights reserved 2585\n\n--- Page 2596 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
[Note: The W3C XML Schema definition of this element’s content model (CT_SlideLayout) is located in §A.3. end
note]
19.3.1.40 sldLayoutId (Slide Layout Id)
This element specifies the relationship information for each slide layout that is used within the slide master. The
slide master has relationship identifiers that it uses internally for determining the slide layouts that should be
used. Then, to resolve what these slide layouts should be the sldLayoutId elements in the sldLayoutIdLst are
utilized.
Attributes Description
id (ID Tag) Specifies the relationship id value that the generating application can use to resolve
which slide layout is used in the creation of the slide. This relationship id is used within
Namespace: the relationship file for the master slide to expose the location of the corresponding
http://purl.oclc.or layout file within the presentation.
g/ooxml/officeDoc
ument/relationshi The possible values for this attribute are defined by the ST_RelationshipId simple type
ps (§22.8.2.1).
id (ID Tag) Specifies the identification number that uniquely identifies this slide layout within the
presentation file.
The possible values for this attribute are defined by the ST_SlideLayoutId simple type
(§19.7.14).
[Note: The W3C XML Schema definition of this element’s content model (CT_SlideLayoutIdListEntry) is located in
§A.3. end note]
19.3.1.41 sldLayoutIdLst (List of Slide Layouts)
This element specifies the existence of the slide layout identification list. This list is contained within the slide
master and is used to determine which layouts are being used within the slide master file. Each layout within the
list of slide layouts has its own identification number and relationship identifier that uniquely identifies it within
both the presentation document and the particular master slide within which it is used.
[Note: The W3C XML Schema definition of this element’s content model (CT_SlideLayoutIdList) is located in §A.3.
end note]
19.3.1.42 sldMaster (Slide Master)
This element specifies an instance of a slide master slide. Within a slide master slide are contained all elements
that describe the objects and their corresponding formatting for within a presentation slide. Within a slide
master slide are two main elements. The cSld element specifies the common slide elements such as shapes and
their attached text bodies. Then the txStyles element specifies the formatting for the text within each of these
shapes. The other properties within a slide master slide specify other properties for within a presentation slide
such as color information, headers and footers, as well as timing and transition information for all corresponding
presentation slides.
2586 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2597 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
preserve (Preserve Specifies whether the corresponding slide layout is deleted when all the slides that follow
Slide Master) that layout are deleted. If this attribute is not specified then a value of false should be
assumed by the generating application. This would mean that the slide would in fact be
deleted if no slides within the presentation were related to it.
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
[Note: The W3C XML Schema definition of this element’s content model (CT_SlideMaster) is located in §A.3. end
note]
19.3.1.43 sp (Shape)
This element specifies the existence of a single shape. A shape can either be a preset or a custom geometry,
defined using the DrawingML framework. In addition to a geometry each shape can have both visual and non-
visual properties attached. Text and corresponding styling information can also be attached to a shape. This
shape is specified along with all other shapes within either the shape tree or group shape elements.
[Note: Shapes are the preferred mechanism for specifying text on a slide. end note]
Attributes Description
useBgFill (Use Specifies that the shape fill should be set to that of the slide background surface.
Background Fill)
[Note: This attribute does not set the fill of the shape to be transparent but instead sets it
to be filled with the portion of the slide background that is directly behind it. end note]
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
[Note: The W3C XML Schema definition of this element’s content model (CT_Shape) is located in §A.3. end note]
19.3.1.44 spPr (Shape Properties)
This element specifies the visual shape properties that can be applied to a shape. These properties include the
shape fill, outline, geometry, effects, and 3D orientation.
Attributes Description
bwMode (Black and Specifies that the picture should be rendered using only black and white coloring. That is
White Mode) the coloring information for the picture should be converted to either black or white
when rendering the picture.
Namespace:
http://purl.oclc.or No gray is to be used in rendering this image, only stark black and stark white.
g/ooxml/drawing
ml/main
©ISO/IEC 2016 – All rights reserved 2587\n\n--- Page 2598 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
[Note: This does not mean that the picture itself that is stored within the file is
necessarily a black and white picture. This attribute instead sets the rendering mode that
the picture has applied to when rendering. end note]
The possible values for this attribute are defined by the ST_BlackWhiteMode simple type
(§20.1.10.10).
[Note: The W3C XML Schema definition of this element’s content model (CT_ShapeProperties) is located in
§A.4.1. end note]
19.3.1.45 spTree (Shape Tree)
This element specifies all shape-based objects, either grouped or not, that can be referenced on a given slide. As
most objects within a slide are shapes, this represents the majority of content within a slide. Text and effects are
attached to shapes that are contained within the spTree element.
[Example: Consider the following PresentationML slide
<p:sld>
<p:cSld>
<p:spTree>
<p:nvGrpSpPr>
…
</p:nvGrpSpPr>
<p:grpSpPr>
…
</p:grpSpPr>
<p:sp>
…
</p:sp>
</p:spTree>
</p:cSld>
…
</p:sld>
In the above example the shape tree specifies all the shape properties for this slide. end example]
Each shape-based object within the shape tree, whether grouped or not, shall represent one unique level of z-
ordering on the slide. The z-order for each shape-based object shall be determined by the lexical ordering of
each shape-based object within the shape tree: the first shape-based object shall have the lowest z-order, while
the last shape-based object shall have the highest z-order.
2588 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2599 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
The z-ordering of shape-based objects within the shape tree shall also determine the navigation (tab) order of
the shape-based objects: the shape-based object with the lowest z-order (the first shape in lexical order) shall be
first in navigation order, with objects being navigated in ascending z-order.
[Example: Consider the following PresentationML slide with two shapes
<p:sld>
<p:cSld>
<p:spTree>
…
<p:sp>
<p:nvSpPr>
<p:cNvPr id="5" name="Oval 4" />
…
</p:nvSpPr>
…
</p:sp>
<p:sp>
<p:nvSpPr>
<p:cNvPr id="4" name="Isosceles Triangle 3" />
…
</p:nvSpPr>
…
</p:sp>
</p:spTree>
</p:cSld>
…
</p:sld>
In the above example the shape with name Oval 4 has the lowest z-order value since that shape is the first
shape in the shape tree. Oval 4 is also the first shape in navigation order. The shape with name Isosceles
Triangle 3 has the highest z positioning value since that shape is the last shape in the shape tree. Isosceles
Triangle 3 is also the last shape in navigation order. end example]
[Note: The W3C XML Schema definition of this element’s content model (CT_GroupShape) is located in §A.3. end
note]
19.3.1.46 style (Shape Style)
This element specifies the style information for a shape. This is used to define a shape's appearance in terms of
the preset styles defined by the style matrix for the theme.
[Example:
<p:style>
<a:lnRef idx="3">
©ISO/IEC 2016 – All rights reserved 2589\n\n--- Page 2600 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
<a:schemeClr val="lt1"/>
</a:lnRef>
<a:fillRef idx="1">
<a:schemeClr val="accent3"/>
</a:fillRef>
<a:effectRef idx="1">
<a:schemeClr val="accent3"/>
</a:effectRef>
<a:fontRef idx="minor">
<a:schemeClr val="lt1"/>
</a:fontRef>
</p:style>
The parent shape of the above code is to have an outline that uses the third line style defined by the theme, use
the first fill defined by the scheme, and be rendered with the first effect defined by the theme. Text inside the
shape is to use the minor font defined by the theme.
end example]
[Note: The W3C XML Schema definition of this element’s content model (CT_ShapeStyle) is located in §A.4.1.
end note]
19.3.1.47 tags (Customer Data Tags)
This element specifies the existence of customer data in the form of tags. This allows for the storage of customer
data within the PresentationML framework. While this is similar to the ext tag in that it can be used store
information, this tag mainly focuses on referencing to other parts of the presentation document. This is
accomplished via the relationship identification attribute that is required for all specified tags.
Attributes Description
id (Relationship ID) This attribute specifies the relationship identifier for the customer data tag. This allows
for a link to a resource that is external from the current XML document but still contained
Namespace: within the presentation document.
http://purl.oclc.or
g/ooxml/officeDoc The possible values for this attribute are defined by the ST_RelationshipId simple type
ument/relationshi (§22.8.2.1).
ps
[Note: The W3C XML Schema definition of this element’s content model (CT_TagsData) is located in §A.3. end
note]
19.3.1.48 timing (Slide Timing Information for a Slide Layout)
This element specifies the timing information for handling all animations and timed events within the
corresponding slide. This information is tracked via time nodes within the timing element. More information on
2590 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2601 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
the specifics of these time nodes and how they are to be defined can be found within the Animation section of
the PresentationML framework.
[Note: The W3C XML Schema definition of this element’s content model (CT_SlideTiming) is located in §A.3. end
note]
19.3.1.49 titleStyle (Slide Master Title Text Style)
This element specifies the text formatting style for the title text within a master slide. This formatting is used on
all title text within related presentation slides. The text formatting is specified by utilizing the DrawingML
framework just as within a regular presentation slide. Within a title style there can be many different style types
defined as there are different kinds of text stored within a slide title.
[Note: The W3C XML Schema definition of this element’s content model (CT_TextListStyle) is located in §A.4.1.
end note]
19.3.1.50 transition (Slide Transition for a Slide Layout)
This element specifies the kind of slide transition that should be used to transition to the current slide from the
previous slide. That is, the transition information is stored on the slide that appears after the transition is
complete.
Attributes Description
advClick (Advance Specifies whether a mouse click advances the slide or not. If this attribute is not specified
on Click) then a value of true is assumed.
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
advTm (Advance Specifies the time, in milliseconds, after which the transition should start. This setting can
after time) be used in conjunction with the advClick attribute. If this attribute is not specified then it
is assumed that no auto-advance occurs.
The possible values for this attribute are defined by the W3C XML Schema unsignedInt
datatype.
spd (Transition Specifies the transition speed that is to be used when transitioning from the current slide
Speed) to the next.
The possible values for this attribute are defined by the ST_TransitionSpeed simple type
(§19.7.54).
[Note: The W3C XML Schema definition of this element’s content model (CT_SlideTransition) is located in §A.3.
end note]
©ISO/IEC 2016 – All rights reserved 2591\n\n--- Page 2602 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
19.3.1.51 txBody (Shape Text Body)
This element specifies the existence of text to be contained within the corresponding shape. All visible text and
visible text related properties are contained within this element. There can be multiple paragraphs and within
paragraphs multiple runs of text.
[Note: The W3C XML Schema definition of this element’s content model (CT_TextBody) is located in §A.4.1. end
note]
19.3.1.52 txStyles (Slide Master Text Styles)
This element specifies the text styles within a slide master. Within this element is the styling information for title
text, the body text and other slide text as well. This element is only for use within the Slide Master and thus sets
the text styles for the corresponding presentation slides.
[Example: Consider the case where we would like to specify the title text for a master slide.
<p:txStyles>
<p:titleStyle>
<a:lvl1pPr algn="ctr" rtl="0" latinLnBrk="0">
<a:spcBef>
<a:spcPct val="0"/>
</a:spcBef>
<a:buNone/>
<a:defRPr sz="4400" kern="1200">
<a:solidFill>
<a:schemeClr val="tx1"/>
</a:solidFill>
<a:latin typeface="+mj-lt"/>
<a:ea typeface="+mj-ea"/>
<a:cs typeface="+mj-cs"/>
</a:defRPr>
</a:lvl1pPr>
</p:titleStyle>
</p:txStyles>
In the above example the title text is set according to the above formatting for all related slides within the
presentation. end example]
[Note: The W3C XML Schema definition of this element’s content model (CT_SlideMasterTextStyles) is located in
§A.3. end note]
19.3.1.53 xfrm (2D Transform for Graphic Frame)
This element specifies the transform to be applied to the corresponding graphic frame. This transformation is
applied to the graphic frame just as it would be for a shape or group shape.
2592 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2603 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
flipH (Horizontal Specifies a horizontal flip. When true, this attribute defines that the shape is flipped
Flip) horizontally about the center of its bounding box.
Namespace: [Example: The following illustrates the effect of a horizontal flip.
http://purl.oclc.or
g/ooxml/drawing
ml/main
end example]
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
flipV (Vertical Flip) Specifies a vertical flip. When true, this attribute defines that the group is flipped
vertically about the center of its bounding box.
Namespace:
http://purl.oclc.or [Example: The following illustrates the effect of a vertical flip.
g/ooxml/drawing
ml/main
end example]
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
rot (Rotation) Specifies the rotation of the Graphic Frame. The units for which this attribute is specified
in reside within the simple type definition referenced below.
Namespace:
http://purl.oclc.or The possible values for this attribute are defined by the ST_Angle simple type
g/ooxml/drawing (§20.1.10.3).
ml/main
[Note: The W3C XML Schema definition of this element’s content model (CT_Transform2D) is located in §A.4.1.
end note]
19.3.2 Embedded Objects
Within the slides portion of PresentationML, there are the embedded elements. These are objects that can be
embedded within a slide. As we defined a slide to be a container it can be seen that it does not just contain
shapes, pictures and text but embedded objects as well that are not necessarily native to the PresentationML
platform.
©ISO/IEC 2016 – All rights reserved 2593\n\n--- Page 2604 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
19.3.2.1 control (Embedded Control)
This element specifies the existence of an embedded control in the slide.
Attributes Description
id (Relationship ID) Specifies the relationship id that is used to identify this Embedded object from within a
slide.
Namespace:
http://purl.oclc.or The possible values for this attribute are defined by the ST_RelationshipId simple type
g/ooxml/officeDoc (§22.8.2.1).
ument/relationshi
ps
imgH (Image Specifies the height of the embedded control.
Height)
The possible values for this attribute are defined by the ST_PositiveCoordinate32 simple
type (§20.1.10.43).
imgW (Image Specifies the width of the embedded control.
Width)
The possible values for this attribute are defined by the ST_PositiveCoordinate32 simple
type (§20.1.10.43).
name (Embedded Specifies the identifying name class used by scripting languages. This name is also used to
Object Name) construct the clipboard name.
The possible values for this attribute are defined by the W3C XML Schema string
datatype.
showAsIcon (Show Specifies whether the Embedded object shows as an icon or using its native
Embedded Object representation.
As Icon)
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
[Note: The W3C XML Schema definition of this element’s content model (CT_Control) is located in §A.3. end
note]
19.3.2.2 embed (Embedded Object or Control)
This element specifies an Embedded object or Control that is embedded within the presentation.
Attributes Description
followColorScheme Specifies the Color Scheme Properties for the corresponding Embedded object being
(Color Scheme specified.
Properties for
Embedded object) The possible values for this attribute are defined by the
ST_OleObjectFollowColorScheme simple type (§19.7.6).
2594 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2605 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
[Note: The W3C XML Schema definition of this element’s content model (CT_OleObjectEmbed) is located in
§A.3. end note]
19.3.2.3 link (Linked Object or Control)
This element specifies a link to an external Embedded object or Control.
Attributes Description
updateAutomatic This attribute determines if linked embedded objects are automatically updated when
(Update Linked the presentation is opened or printed.
Embedded Objects
Automatically) The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
[Note: The W3C XML Schema definition of this element’s content model (CT_OleObjectLink) is located in §A.3.
end note]
19.3.2.4 oleObj (Global Element for Embedded objects and Controls)
This element specifies a global element to be used for an Embedded object and Control.
When the oleObject element contains a pic child element, the identifier specified by the
pic/nvPicPr/cNvPr@id attribute shall be ignored and the identifier specified by the
graphicFrame/nvGraphicFramePr/cNvPr@id attribute shall be used when deciding which identifier to use for
the OLE object.
Attributes Description
id (Relationship ID) Specifies the relationship id that is used to identify this Embedded object from within a
slide.
Namespace:
http://purl.oclc.or The possible values for this attribute are defined by the ST_RelationshipId simple type
g/ooxml/officeDoc (§22.8.2.1).
ument/relationshi
ps
imgH (Image Specifies the height of the embedded control.
Height)
The possible values for this attribute are defined by the ST_PositiveCoordinate32 simple
type (§20.1.10.43).
imgW (Image Specifies the width of the embedded control.
Width)
The possible values for this attribute are defined by the ST_PositiveCoordinate32 simple
type (§20.1.10.43).
name (Embedded Specifies the identifying name class used by scripting languages. This name is also used to
Object Name) construct the clipboard name.
©ISO/IEC 2016 – All rights reserved 2595\n\n--- Page 2606 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
The possible values for this attribute are defined by the W3C XML Schema string
datatype.
progId (Embedded Specifies the progid for an Embedded object.
Object ProgID)
The possible values for this attribute are defined by the W3C XML Schema string
datatype.
showAsIcon (Show Specifies whether the Embedded object shows as an icon or using its native
Embedded Object representation.
As Icon)
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
[Note: The W3C XML Schema definition of this element’s content model (CT_OleObject) is located in §A.3. end
note]
19.3.3 Programmable Tags
Within the slides portion of PresentationML there are the tag elements. These are extensibility names and
values that assist in the storage of legacy variables from older file formats.
19.3.3.1 tag (Programmable Extensibility Tag)
This element specifies a programmable extensibility tag to be used for storage of legacy variables.
Attributes Description
name (Name) Specifies the name associated with this specific programmable tag.
The possible values for this attribute are defined by the W3C XML Schema string
datatype.
val (Value) Specifies the value associated with this specific programmable tag.
The possible values for this attribute are defined by the W3C XML Schema string
datatype.
[Note: The W3C XML Schema definition of this element’s content model (CT_StringTag) is located in §A.3. end
note]
19.3.3.2 tagLst (Programmable Tab List)
This element specifies the list of programmable extensibility tags that are used to store variables from legacy file
formats.
[Note: The W3C XML Schema definition of this element’s content model (CT_TagList) is located in §A.3. end
note]
2596 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2607 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
19.4 Comments
A comment is a text note attached to a slide, with the primary purpose of allowing readers of a presentation to
provide feedback to the presentation author. Each comment contains an unformatted text string and
information about its author, and is attached to a particular location on a slide. Comments can be visible while
editing the presentation, but do not appear when a slide show is given. The displaying application decides when
to display comments and determines their visual appearance.
19.4.1 cm (Comment)
This element specifies a single comment attached to a slide. It contains the text of the comment, its position on
the slide, and attributes referring to its author and date.
[Example:
<p:cm authorId="0" dt="2006-08-28T17:26:44.129" idx="1">
<p:pos x="10" y="10"/>
<p:text>Add diagram to clarify.</p:text>
</p:cm>
end example]
Attributes Description
authorId (Comment This attribute specifies the author of the comment. It refers to the ID of an author in the
Author ID) comment author list for the document.
The possible values for this attribute are defined by the W3C XML Schema unsignedInt
datatype.
dt (Comment This attribute specifies the date and time this comment was last modified.
Date/Time)
The possible values for this attribute are defined by the W3C XML Schema dateTime
datatype.
idx (Comment This attribute specifies an identifier for this comment that is unique within a list of all
Index) comments by this author in this document. An author's first comment in a document
has index 1.
[Note: Because the index is unique only for the comment author, a document can contain
multiple comments with the same index created by different authors. end note]
The possible values for this attribute are defined by the ST_Index simple type (§19.7.3).
[Note: The W3C XML Schema definition of this element’s content model (CT_Comment) is located in §A.3. end
note]
©ISO/IEC 2016 – All rights reserved 2597\n\n--- Page 2608 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
19.4.2 cmAuthor (Comment Author)
This element specifies a single author with comments in the document. It contains a unique author ID, the
author's name and initials, the index of the author's last comment, and the index of a color associated with the
author.
[Example:
<p:cmAuthor id="0" name="Julie Lee" initials="JL" lastIdx="1" clrIdx="0"/>
end example]
Attributes Description
clrIdx (Comment This attribute specifies an index into the generating application's comments color table to
Author Color Index) allow for visual (color) differentiation of different author's comments. This color is used
for all comments by this author. If more authors exist than there are entries in the color
table, the color index wraps around to the beginning of the table.
[Note: It is left entirely up to the generating application to determine the amount of
colors used in the comments color table and in what order these are used when
rendering comments on a slide surface. end note]
The possible values for this attribute are defined by the W3C XML Schema unsignedInt
datatype.
id (Comment This attribute specifies a unique (within the document) zero-based identifier that refers
Author ID) to a single comment author.
[Note: The method of generating an author id is determined by the application and need
not be sequential, provided each id is unique within the list of comment authors for the
document. end note]
The possible values for this attribute are defined by the W3C XML Schema unsignedInt
datatype.
initials (Comment This attribute specifies a string that represents the initials of this particular author. The
Author Initials) value is not necessarily unique. It is intended for use by the application as an abbreviated
version of the comment author's name.
The possible values for this attribute are defined by the ST_Name simple type (§19.7.5).
lastIdx (Index of Index of the last comment added to this document by this author. New comments by this
Comment Author's author are counted starting with the value one greater than this index.
last comment)
[Note: The index of a deleted comment is not reused; therefore, this value is not an
accurate count of the total number of comments by the author. end note]
The possible values for this attribute are defined by the W3C XML Schema unsignedInt
datatype.
2598 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2609 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
name (Comment This attribute specifies the full name of this particular author. As a string, it has no
Author Name) security or authentication data. This value is not guaranteed to be unique across all
document authors.
The possible values for this attribute are defined by the ST_Name simple type (§19.7.5).
[Note: The W3C XML Schema definition of this element’s content model (CT_CommentAuthor) is located in
§A.3. end note]
19.4.3 cmAuthorLst (List of Comment Authors)
This element specifies a list of authors with comments in the current document. Each comment in a document
shall refer to an author in this list. No cmAuthor element in a cmAuthorLst shall have both the same name
attribute value and the same initials attribute value as any other cmAuthor element in the same cmAuthorLst.
[Example: A document contains comments left by two authors.
<p:cmAuthorLst>
<p:cmAuthor id="0" name="Julie Lee" initials="JL" lastIdx="1" clrIdx="0"/>
<p:cmAuthor id="1" name="Fred Jones" initials="FJ" lastIdx="2" clrIdx="1"/>
</p:cmAuthorLst>
end example]
[Note: The W3C XML Schema definition of this element’s content model (CT_CommentAuthorList) is located in
§A.3. end note]
19.4.4 cmLst (Comment List)
This element specifies a list of comments for a particular slide.
[Example: A slide contains two comments, each left by a different author. This example demonstrates that two
comments can have the same index if they are created by different authors.
<p:cmLst>
<p:cm authorId="0" dt="2006-08-28T17:26:44.129" idx="1">
<p:pos x="10" y="10"/>
<p:text>Add diagram to clarify.</p:text>
</p:cm>
<p:cm authorId="1" dt="2006-08-28T17:44:19.679" idx="1">
<p:pos x="1426" y="660"/>
<p:text>Clean up this text.</p:text>
</p:cm>
</p:cmLst>
©ISO/IEC 2016 – All rights reserved 2599\n\n--- Page 2610 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
end example]
[Note: The W3C XML Schema definition of this element’s content model (CT_CommentList) is located in §A.3.
end note]
19.4.5 pos (Comment Position)
This element specifies the positioning information for the placement of a comment on a slide surface. In LTR
versions of the generating application, this position information should refer to the upper left point of the
comment shape. In RTL versions of the generating application, this position information should refer to the
upper right point of the comment shape.
[Note: The anchoring point on the slide surface is unaffected by a right-to-left or left-to-right layout change. That
is the anchoring point remains the same for all language versions. end note]
[Note: Because there is no specified size or formatting for comments, this UI widget used to display a comment
can be any size and thus the lower right point of the comment shape is determined by how the viewing
application chooses to display comments. end note]
[Example:
<p:pos x="1426" y="660"/>
end example]
Attributes Description
x (X-Axis Specifies a coordinate on the x-axis. The origin point for this coordinate shall be specified
Coordinate) by the parent XML element.
Namespace: [Example: Consider the following point on a basic wrapping polygon for a DrawingML
http://purl.oclc.or object:
g/ooxml/drawing
ml/main <… x="0" y="100" />
The x attribute defines an x-coordinate of 0. end example]
The possible values for this attribute are defined by the ST_Coordinate simple type
(§20.1.10.16).
y (Y-Axis Specifies a coordinate on the y-axis. The origin point for this coordinate shall be specified
Coordinate) by the parent XML element.
Namespace: [Example: Consider the following point on a basic wrapping polygon for a DrawingML
http://purl.oclc.or object:
g/ooxml/drawing
ml/main <… x="0" y="100" />
The y attribute defines a y-coordinate of 100. end example]
2600 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2611 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
The possible values for this attribute are defined by the ST_Coordinate simple type
(§20.1.10.16).
[Note: The W3C XML Schema definition of this element’s content model (CT_Point2D) is located in §A.4.1. end
note]
19.4.6 text (Comment's Text Content)
This element specifies the content of a comment. This is the text with which the author has annotated the slide.
[Example:
<p:text>Add diagram to clarify.</p:text>
end example]
The possible values for this element are defined by the W3C XML Schema string datatype.
19.5 Animation
The Animation section of the PresentationML framework stores the movement and related information of
objects.
This schema is loosely based on the syntax and concepts from the Synchronized Multimedia Integration
Language (SMIL), a W3C Recommendation for describing multimedia presentations using XML.
The schema describes all the animations effects that reside on a slide and also the animation that occurs when
going from slide to slide (slide transition).
Animations on a slide are inherently time-based and consist of an animation effects on an object or text. Slide
transitions however do not follow this concept and always appear before any animation on a slide.
All elements described in this schema are contained within the slide XML file. More specifically they are in the
<transition> and the <timing> element as shown below:
<p:sld>
<p:cSld> … </p:cSld>
<p:clrMapOvr> … </p:clrMapOvr>
<p:transition> … </p:transition>
<p:timing> … </p:timing>
</p:sld>
©ISO/IEC 2016 – All rights reserved 2601\n\n--- Page 2612 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
19.5.1 anim (Animate)
This element is a generic animation element that requires little or no semantic understanding of the attribute
being animated. It can animate text within a shape or even the shape itself.
[Example: Consider trying to emphasize text within a shape by changing the size of its font by 150%. The
<anim> element should be used as follows:
<p:anim to="1.5" calcmode="lin" valueType="num">
<p:cBhvr override="childStyle">
<p:cTn id="1" dur="2000" fill="hold"/>
<p:tgtEl>
<p:spTgt spid="1">
<p:txEl>
<p:charRg st="1" end="4"/>
</p:txEl>
</p:spTgt>
</p:tgtEl>
<p:attrNameLst>
<p:attrName>style.fontSize</p:attrName>
</p:attrNameLst>
</p:cBhvr>
</p:anim>
end example]
Attributes Description
by (By) This attribute specifies a relative offset value for the animation with respect to its
position before the start of the animation.
The possible values for this attribute are defined by the W3C XML Schema string
datatype.
calcmode This attribute specifies the interpolation mode for the animation.
(Calculation Mode)
The possible values for this attribute are defined by the
ST_TLAnimateBehaviorCalcMode simple type (§19.7.20).
from (From) This attribute specifies the starting value of the animation.
The possible values for this attribute are defined by the W3C XML Schema string
datatype.
to (To) This attribute specifies the ending value for the animation as a percentage.
The possible values for this attribute are defined by the W3C XML Schema string
datatype.
2602 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2613 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
valueType (Value This attribute specifies the type of property value.
Type)
The possible values for this attribute are defined by the
ST_TLAnimateBehaviorValueType simple type (§19.7.21).
[Note: The W3C XML Schema definition of this element’s content model (CT_TLAnimateBehavior) is located in
§A.3. end note]
19.5.2 animClr (Animate Color Behavior)
This animation element is responsible for animating the color of an object.
[Example: Consider trying to emphasize a shape by changing its fill color to scheme color accent2. The
<animClr> element should be used as follows:
<p:animClr clrSpc="rgb">
<p:cBhvr>
<p:cTn id="1" dur="2000" fill="hold"/>
<p:tgtEl>
<p:spTgt spid="1"/>
</p:tgtEl>
<p:attrNameLst>
<p:attrName>fillcolor</p:attrName>
</p:attrNameLst>
</p:cBhvr>
<p:to>
<a:schemeClr val="accent2"/>
</p:to>
</p:animClr>
end example]
Attributes Description
clrSpc (Color Space) This attribute specifies the color space in which to interpolate the animation. Values for
example can be HSL & RGB.
The values for from/to/by/etc. can still be specified in any supported color format
without affecting the color space within which the animation happens.
The RGB color space is best used for doing animations between two different colors since
it doesn't require going through any other hues between the two colors specified. The
HSL space is useful for animating through a rainbow of colors or for modifying just the
saturation by 30% for example.
©ISO/IEC 2016 – All rights reserved 2603\n\n--- Page 2614 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
The possible values for this attribute are defined by the ST_TLAnimateColorSpace
simple type (§19.7.23).
dir (Direction) This attribute specifies which direction to cycle the hue around the color wheel. Values
are clockwise or counter clockwise. Default is clockwise.
The possible values for this attribute are defined by the ST_TLAnimateColorDirection
simple type (§19.7.22).
[Note: The W3C XML Schema definition of this element’s content model (CT_TLAnimateColorBehavior) is located
in §A.3. end note]
19.5.3 animEffect (Animate Effect)
This animation behavior provides the ability to do image transform/filter effects on elements. Some visual
effects are dynamic in nature and have a progress that animates from 0 to 1 over a period of time to do visual
transitions between hidden and visible states. Other filters are static and apply a effects like a blur or drop-
shadow which aren't inherently time-based.
[Example: Consider trying to emphasize a shape by creating an entrance animation using a "blinds" motion.
<p:animEffect transition="in" filter="blinds(horizontal)">
<p:cBhvr>
<p:cTn id="7" dur="500"/>
<p:tgtEl>
<p:spTgt spid="4"/>
</p:tgtEl>
</p:cBhvr>
</p:animEffect>
end example]
Attributes Description
filter (Filter)
This attribute specifies the animation types and subtypes to be used for the effect.
Multiple animations are allowed to be listed so that in the event that a superseding
animation (leftmost) cannot be rendered, a fallback animation is available. That is, the
rendering application parses the list from left to right until a supported animation is
found.
The syntax used for the filter attribute value is as follows: "type(subtype);type(subtype)".
Subtype can be a string value such as "fromLeft" or a numerical value depending on the
2604 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2615 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
type specified.
Reserved Animation Types(subtypes):
Value Description
blinds(horizontal)
blinds(vertical)
box(in)
box(out)
checkerboard(across)
checkerboard(down)
circle
diamond
dissolve
fade
©ISO/IEC 2016 – All rights reserved 2605\n\n--- Page 2616 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
slide(fromTop)
slide(fromBottom)
slide(fromLeft)
slide(fromRight)
plus(in)
plus(out)
barn(inVertical)
barn(inHorizontal)
barn(outVertical)
barn(outHorizontal)
randomBars(horizont
al)
2606 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2617 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
randomBars(vertical)
strips(downLeft)
strips(upLeft)
strips(downRight)
strips(upRight)
wedge
wheel(1)
wheel(2)
wheel(3)
wheel(4)
wheel(8)
©ISO/IEC 2016 – All rights reserved 2607\n\n--- Page 2618 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
wipe(right)
wipe(left)
wipe(down)
wipe(up)
[Note: The renderings shown above are for example purposes only. Exact rendering of
any animation is determined by the rendering application. As such, the same animation
can have many variations, depending on the implementation. More detail for each
rendering above can be found in transition (§19.3.1.50). end note]
[Example: Consider the following animation effect:
<p:animEffect transition="in"
filter="blinds(horizontal);blinds(vertical)">
<p:cBhvr>
<p:cTn id="7" dur="500"/>
<p:tgtEl>
<p:spTgtspid="5"/>
</p:tgtEl>
</p:cBhvr>
</p:animEffect>
There are two animation filters shown in this example. The first is the blinds (horizontal),
which the rendering application is to use as the primary animation effect. If, however,
the rendering application does not support this animation, the blinds (vertical) animation
is used. In this example there are only two animation filters listed, a primary and a
fallback, but it is possible to list multiple fallback filters using the syntax defined above.
end example]
The possible values for this attribute are defined by the W3C XML Schema string
datatype.
prLst (Property List)
2608 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2619 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
This attribute specifies a list of properties that coincide with the effect specified.
Although there are many animation types allowed, this attribute allows the setting of
specific property settings in order to describe an even wider variety of animation types.
The syntax used for the prLst attribute value is as follows: “name:value;name:value”.
When multiple animation types are listed in the filter attribute, the rendering application
attempts to apply each property value even though some might not apply to it.
Reserved Names(values):
• opacity (float values of 0.0 - 1.0)
[Example: Consider the following animation effect:
<p:animEffect filter="image" prLst="opacity: 0.5">
<p:cBhvr rctx="IE">
<p:cTn id="7" dur="indefinite"/>
<p:tgtEl>
<p:spTgtspid="3"/>
</p:tgtEl>
</p:cBhvr>
</p:animEffect>
The animation filter specified is an image filter type that has a specific property called
opacity set to a value of 0.5. end example]
The possible values for this attribute are defined by the W3C XML Schema string
datatype.
transition This attribute specifies whether to transition the element in or out or treat it as a static
(Transition) filter. The values are "none", "in" and "out", and the default value is "in".
When a value of "in" is specified, the element is not visible at the start of the animation
and is completely visible be the end of the duration. When "out" is specified, the element
is visible at the start and not visible at the end of the effect. This visibility is in addition to
the effect of setting CSS visibility or display attributes.
The possible values for this attribute are defined by the ST_TLAnimateEffectTransition
simple type (§19.7.24).
[Note: The W3C XML Schema definition of this element’s content model (CT_TLAnimateEffectBehavior) is
located in §A.3. end note]
©ISO/IEC 2016 – All rights reserved 2609\n\n--- Page 2620 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
19.5.4 animMotion (Animate Motion)
Animate motion provides an abstracted way to move positioned elements. It provides the ability to specify
from/to/by motion as well as to use more detailed path descriptions for motion over polylines or bezier curves.
[Example: Consider animating a shape from its original position to the right.. The <animMotion> element should
be used as follows:
<p:animMotion origin="layout" path="M 0 0 L 0.25 0 E" pathEditMode="relative">
<p:cBhvr>
<p:cTn id="1" dur="2000" fill="hold"/>
<p:tgtEl>
<p:spTgt spid="1"/>
</p:tgtEl>
<p:attrNameLst>
<p:attrName>ppt_x</p:attrName>
<p:attrName>ppt_y</p:attrName>
</p:attrNameLst>
</p:cBhvr>
</p:animMotion>
end example]
Attributes Description
origin (Origin) Specifies what the origin of the motion path is relative to such as the layout of the slide,
or the parent.
The possible values for this attribute are defined by the
ST_TLAnimateMotionBehaviorOrigin simple type (§19.7.25).
path (Path) Specifies the path primitive followed by coordinates for the animation motion. The
allowed values that are understood within a path are as follows:
M = move to, L = line to, C = curve to, Z=close loop, E=end
UPPERCASE = absolute coords, lowercase = relative coords
Thus total allowed set = {M,L,C,Z,E,m,l,c,z,e)
[Example: The following string is a sample path.
path: “M 0 0 L 1 1 c 1 2 3 4 4 4 Z”
end example]
The possible values for this attribute are defined by the W3C XML Schema string
datatype.
pathEditMode This attribute specifies how the motion path moves when the target element is moved.
(Path Edit Mode)
The possible values for this attribute are defined by the
ST_TLAnimateMotionPathEditMode simple type (§19.7.26).
2610 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2621 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
ptsTypes (Points This attribute describes the point type of the points in the path attribute. The allowed
Types) values that are understood for the ptsTypes attribute are as follows:
A = Auto, F = Corner, T = Straight, S = Smooth
UPPERCASE = Straight Line follows point, lowercase = curve follows point.
Thus, the total allowed set = {A,F,T,S,a,f,t,s}
The possible values for this attribute are defined by the W3C XML Schema string
datatype.
rAng (Relative The attribute describes the relative angle of the motion path.
Angle)
The possible values for this attribute are defined by the ST_Angle simple type
(§20.1.10.3).
[Note: The W3C XML Schema definition of this element’s content model (CT_TLAnimateMotionBehavior) is
located in §A.3. end note]
19.5.5 animRot (Animate Rotation)
This animation element is responsible for animating the rotation of an object. Rotation values set in the "by" ,
"to, and "from" attributes are specified in degrees measured to a 60,000th, i.e 1 degree is 60,000. Rotation
values can be larger than 360°.
The sign of the rotation angle specifies the direction for rotation. A negative rotation specifies that the rotation
should appear in the host to go counter-clockwise".
[Example: Consider trying to emphasize a shape by rotating it 360 degrees clockwise. The <animRot> element
should be used as follows:
<p:animRot by="21600000">
<p:cBhvr>
<p:cTn id="6" dur="2000" fill="hold"/>
<p:tgtEl>
<p:spTgt spid="5"/>
</p:tgtEl>
<p:attrNameLst>
<p:attrName>r</p:attrName>
</p:attrNameLst>
</p:cBhvr>
</p:animRot>
end example]
©ISO/IEC 2016 – All rights reserved 2611\n\n--- Page 2622 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
by (By) This attribute describes the relative offset value for the animation.
The possible values for this attribute are defined by the ST_Angle simple type
(§20.1.10.3).
from (From) This attribute describes the starting value for the animation.
The possible values for this attribute are defined by the ST_Angle simple type
(§20.1.10.3).
to (To) This attribute describes the ending value for the animation.
The possible values for this attribute are defined by the ST_Angle simple type
(§20.1.10.3).
[Note: The W3C XML Schema definition of this element’s content model (CT_TLAnimateRotationBehavior) is
located in §A.3. end note]
19.5.6 animScale (Animate Scale)
This animation element is responsible for animating the scale of an object. When animating the scale, the
element shall scale around the reference point of the element and the positioning system used should be
consistent with the one used for motion paths. When animating the width and height of an element, all of the
width/height animation values are calculated first then the scale animations are applied on top of that. So for
example, an animation from 0 to 100 of the width with a concurrent scale from 100% to 200% would result in
the element appearing to scale from 0 to 200.
[Example: Consider trying to emphasize a shape by scaling it larger by 150%. The <animScale> element should
be used as follows:
<p:childTnLst>
<p:animScale>
<p:cBhvr>
<p:cTn id="6" dur="2000" fill="hold"/>
<p:tgtEl>
<p:spTgt spid="5"/>
</p:tgtEl>
</p:cBhvr>
<p:by x="150000" y="150000"/>
</p:animScale>
</p:childTnLst>
end example]
2612 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2623 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
zoomContents This attribute specifies whether to zoom the contents of an object when doing a scaling
(Zoom Content) animation.
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
[Note: The W3C XML Schema definition of this element’s content model (CT_TLAnimateScaleBehavior) is located
in §A.3. end note]
19.5.7 attrName (Attribute Name)
This element is used to contain an attribute value for an Attribute Name List. This value defines the specific
attribute that an animation should be applied to, such as fill, style, and shadow, etc. A specific property is
defined by using a "property.sub-property" format which is often extended to multiple sub properties as seen in
the allowed values below.
Allowed property values:
style.opacity, style.rotation, style.visibility, style.color, style.fontSize,
style.fontWeight, style.fontStyle, style.fontFamily, style.textEffectEmboss,
style.textShadow, style.textTransform, style.textDecorationUnderline,
style.textEffectOutline, style.textDecorationLineThrough, style.sRotation,
imageData.cropTop, imageData.cropBottom, imageData.cropLeft,
imageData.cropRight, imageData.cropRight, imageData.gain, imageData.blacklevel,
imageData.gamma, imageData.grayscale, imageData.chromakey, fill.on, fill.type,
fill.color, fill.opacity, fill.color2, fill.method, fill.opacity2, fill.angle,
fill.focus, fill.focusposition.x, fill.focusposition.y, fill.focussize.x,
fill.focussize.y, stroke.on, stroke.color, stroke.weight, stroke.opacity,
stroke.linestyle, stroke.dashstyle, stroke.filltype, stroke.src, stroke.color2,
stroke.imagesize.x, stroke.imagesize.y, stroke.startArrow, stroke.endArrow,
stroke.startArrowWidth, stroke.startArrowLength, stroke.endArrowWidth,
stroke.endArrowLength, shadow.on, shadow.type, shadow.color, shadow.color2,
shadow.opacity, shadow.offset.x, shadow.offset.y, shadow.offset2.x,
shadow.offset2.y, shadow.origin.x, shadow.origin.y, shadow.matrix.xtox,
shadow.matrix.ytox, shadow.matrix.xtox, shadow.matrix.ytoy,
shadow.matrix.perspectiveX, shadow.matrix.perspectiveY, skew.on, skew.offset.x,
skew.offset.y, skew.origin.x, skew.origin.y, skew.matrix.xtox, skew.matrix.ytox,
skew.matrix.xtox, skew.matrix.ytoy, skew.matrix.perspectiveX,
skew.matrix.perspectiveY, extrusion.on, extrusion.type, extrusion.render,
extrusion.viewpointorigin.x, extrusion.viewpointorigin.y, extrusion.viewpoint.x,
extrusion.viewpoint.y, extrusion.viewpoint.z, extrusion.plane,
extrusion.skewangle, extrusion.skewamt, extrusion.backdepth,
extrusion.foredepth, extrusion.orientation.x, extrusion.orientation.y,
©ISO/IEC 2016 – All rights reserved 2613\n\n--- Page 2624 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
extrusion.orientation.z, extrusion.orientationangle, extrusion.color,
extrusion.rotationangle.x, extrusion.rotationangle.y,
extrusion.lockrotationcenter, extrusion.autorotationcenter,
extrusion.rotationcenter.x, extrusion.rotationcenter.y,
extrusion.rotationcenter.z, and extrusion.colormode.
[Example: Consider trying to emphasize the txt font size within the body of a shape. The attribute would be
'style.fontSize' and this can be done by doing the following:
<p:anim to="1.5" calcmode="lin" valueType="num">
<p:cBhvr override="childStyle">
<p:cTn id="6" dur="2000" fill="hold"/>
<p:tgtEl>
<p:spTgt spid="3">
<p:txEl>
<p:charRg st="4294967295" end="4294967295"/>
</p:txEl>
</p:spTgt>
</p:tgtEl>
<p:attrNameLst>
<p:attrName>style.fontSize</p:attrName>
</p:attrNameLst>
</p:cBhvr>
</p:anim>
end example]
The possible values for this element are defined by the W3C XML Schema string datatype.
19.5.8 attrNameLst (Attribute Name List)
This element is used to describe a list of attributes in which to apply an animation to.
[Example: Consider trying to emphasize the txt font size within the body of a shape. The attribute would be
'style.fontSize' and this can be done by doing the following:
<p:anim to="1.5" calcmode="lin" valueType="num">
<p:cBhvr override="childStyle">
<p:cTn id="6" dur="2000" fill="hold"/>
<p:tgtEl>
<p:spTgt spid="3">
<p:txEl>
<p:charRg st="4294967295" end="4294967295"/>
</p:txEl>
</p:spTgt>
</p:tgtEl>
2614 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2625 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
<p:attrNameLst>
<p:attrName>style.fontSize</p:attrName>
</p:attrNameLst>
</p:cBhvr>
</p:anim>
end example]
[Note: The W3C XML Schema definition of this element’s content model (CT_TLBehaviorAttributeNameList) is
located in §A.3. end note]
19.5.9 audio (Audio)
This element is used to include audio during an animation. This element specifies that this node within the
animation tree triggers the playback of an audio file; the actual audio file used is specified by the sndTgt
element (§19.5.70).
[Example: Consider adding applause sound to an animation sequence. The audio element is used as follows:
<p:cTn …>
<p:stCondLst>…</p:stCondLst>
<p:childTnLst>…</p:childTnLst>
<p:subTnLst>
<p:audio>
<p:cMediaNode vol="50%">…
<p:tgtEl>
<p:sndTgt r:embed="rId2" />
</p:tgtEl>
</p:cMediaNode>
</p:audio>
</p:subTnLst>
</p:cTn>
The audio element specifies the location of the audio playback within the animation; its child sndTgt element
specifies that the audio to be played is the target of the relationship with ID rId2.
end example]
Attributes Description
isNarration (Is This attribute indicates whether the audio is a narration for the slide.
Narration)
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
©ISO/IEC 2016 – All rights reserved 2615\n\n--- Page 2626 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
[Note: The W3C XML Schema definition of this element’s content model (CT_TLMediaNodeAudio) is located in
§A.3. end note]
19.5.10 bg (Background)
This element is used to specify animating the background of an object.
[Example: Consider adding animation to the background of Shape Id 3. The <bg> tag can be used as follows:
<p:tgtEl>
<p:spTgt spid="3">
<p:bg/>
</p:spTgt>
</p:tgtEl>
end example]
[Note: The W3C XML Schema definition of this element’s content model (CT_Empty) is located in §A.3. end note]
19.5.11 bldAsOne (Build As One)
This element specifies in the build list to build the entire graphical object as one entity.
[Example: Consider having a graph appear as on entity as opposed to by category. The <bldAsOne> element
should be used as follows:
<p:bldLst>
<p:bldGraphic spid="4" grpId="0">
<p:bldAsOne/>
</p:bldGraphic>
</p:bldLst>
end example]
[Note: The W3C XML Schema definition of this element’s content model (CT_Empty) is located in §A.3. end note]
19.5.12 bldDgm (Build Diagram)
This element specifies how to build the animation for a diagram.
[Example: Consider the following example where a chart is specified to be animated by category rather than as
one entity. Thus, the bldChart element should be used as follows:
<p:bdldLst>
<p:bldGraphic spid="4" grpId="0">
<p:bldSub>
<a:bldChart bld="category"/>
</p:bldSub>
</p:bldGraphic>
2616 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2627 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
</p:bldLst>
end example]
Attributes Description
bld (Diagram Build This attribute describes how the diagram is built. The animation animates the sub-
Types) elements in the container in the particular order defined by this attribute.
The possible values for this attribute are defined by the ST_TLDiagramBuildType simple
type (§19.7.33).
grpId (Group ID) This attribute ties effects persisted in the animation to the build information. The
attribute is used by the editor when changes to the build information are made.
GroupIDs are unique for a given shape. They are not guaranteed to be unique IDs across
all shapes on a slide.
The possible values for this attribute are defined by the W3C XML Schema unsignedInt
datatype.
spid (Shape ID) This attribute specifies the shape to which the build applies.
The possible values for this attribute are defined by the ST_DrawingElementId simple
type (§20.1.10.21).
uiExpand (Expand This attribute describes the view option indicating if the build should be displayed
UI) expanded.
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
[Note: The W3C XML Schema definition of this element’s content model (CT_TLBuildDiagram) is located in §A.3.
end note]
19.5.13 bldGraphic (Build Graphics)
This element specifies how to build a graphical element.
[Example: Consider having a chart graphical element appear as a whole as opposed to by a category. The
<bldGraphic> element should be used as follows:
<p:bldLdst>
<p:bldGraphic spid="3" grpId="0">
<p:bldSub>
<a:bldChart bld="category"/>
</p:bldSub>
</p:bldGraphic>
</p:bldLst>
©ISO/IEC 2016 – All rights reserved 2617\n\n--- Page 2628 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
end example]
Attributes Description
grpId (Group ID) This attribute ties effects persisted in the animation to the build information. The
attribute is used by the editor when changes to the build information are made.
GroupIDs are unique for a given shape. They are not guaranteed to be unique IDs across
all shapes on a slide.
The possible values for this attribute are defined by the W3C XML Schema unsignedInt
datatype.
spid (Shape ID) This attribute specifies the shape to which the build applies.
The possible values for this attribute are defined by the ST_DrawingElementId simple
type (§20.1.10.21).
uiExpand (Expand This attribute describes the view option indicating if the build should be displayed
UI) expanded.
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
[Note: The W3C XML Schema definition of this element’s content model (CT_TLGraphicalObjectBuild) is located
in §A.3. end note]
19.5.14 bldLst (Build List)
This element specifies the list of graphic elements to build. This refers to how the different sub-shapes or sub-
components of a object are displayed. The different objects that can have build properties are text, diagrams,
and charts.
[Example: Consider animating a pie chart but based on category as shown below:
2618 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2629 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
The <bldList> element should be used as follows:
<p:bldLst>
<p:bldGraphic spid="1" grpId="0">
<p:bldSub>
<a:bldChart bld="category"/>
</p:bldSub>
</p:bldGraphic>
</p:bldLst>
end example]
[Note: The W3C XML Schema definition of this element’s content model (CT_BuildList) is located in §A.3. end
note]
19.5.15 bldOleChart (Build Embedded Chart)
This element describes animation an a embedded Chart.
[Example: Consider displaying animation on a embedded graphical chart. The <bldOleChart>element should be
use as follows:
<p:bldLst>
©ISO/IEC 2016 – All rights reserved 2619\n\n--- Page 2630 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
<p:bldOleChart spid="1025" grpId="0"/>
</p:bldLst>
end example]
Attributes Description
animBg (Animate This attribute describes whether to animate the background of the shape.
Background)
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
bld (Build) This attribute describes how the diagram is built. The animation animates the sub-
elements in the container in the particular order defined by this attribute.
The possible values for this attribute are defined by the ST_TLOleChartBuildType simple
type (§19.7.35).
grpId (Group ID) This attribute ties effects persisted in the animation to the build information. The
attribute is used by the editor when changes to the build information are made.
GroupIDs are unique for a given shape. They are not guaranteed to be unique IDs across
all shapes on a slide.
The possible values for this attribute are defined by the W3C XML Schema unsignedInt
datatype.
spid (Shape ID) This attribute specifies the shape to which the build applies.
The possible values for this attribute are defined by the ST_DrawingElementId simple
type (§20.1.10.21).
uiExpand (Expand This attribute describes the view option indicating if the build should be displayed
UI) expanded.
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
[Note: The W3C XML Schema definition of this element’s content model (CT_TLOleBuildChart) is located in §A.3.
end note]
19.5.16 bldP (Build Paragraph)
This element specifies how to build paragraph level properties.
[Example: Consider having animation applied only to 1st level paragraphs. The <bldP> element should be used
as follows:
<p:bldLst>
<p:bldP spid="3" grpId="0" build="p"/>
</p:bldLst>
2620 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2631 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
end example]
Attributes Description
advAuto (Auto This attribute specifies time after which to automatically advance the build to the next
Advance Time) step.
The possible values for this attribute are defined by the ST_TLTime simple type
(§19.7.38).
animBg (Animate This attribute indicates whether to animate the background of the shape associated with
Background) the text.
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
autoUpdateAnimB This attribute indicates whether to automatically update the "animateBg" setting to true
g (Auto Update when the shape associated with the text has a fill or line.
Animation
Background)
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
bldLvl (Build Level) This attribute describes the build level for the paragraph. It is only supported in
paragraph type builds i.e the build attribute shall also be set to "byParagraph" for this
attribute to apply.
The possible values for this attribute are defined by the W3C XML Schema unsignedInt
datatype.
build (Build Types) This attribute describe the build types.
The possible values for this attribute are defined by the ST_TLParaBuildType simple
type (§19.7.36).
grpId (Group ID) This attribute ties effects persisted in the animation to the build information. The
attribute is used by the editor when changes to the build information are made.
GroupIDs are unique for a given shape. They are not guaranteed to be unique IDs across
all shapes on a slide.
The possible values for this attribute are defined by the W3C XML Schema unsignedInt
datatype.
rev (Reverse) This attribute is only supported in paragraph type builds. This specifies the direction of
the build relative to the order of the elements in the container. When this is set to "true",
the animations for the paragraphs are persisted in reverse order to the order of the
paragraphs themselves such that the last paragraph animates first. Default value is
"false".
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
spid (Shape ID) This attribute specifies the shape to which the build applies.
©ISO/IEC 2016 – All rights reserved 2621\n\n--- Page 2632 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
The possible values for this attribute are defined by the ST_DrawingElementId simple
type (§20.1.10.21).
uiExpand (Expand This attribute describes the view option indicating if the build should be displayed
UI) expanded.
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
[Note: The W3C XML Schema definition of this element’s content model (CT_TLBuildParagraph) is located in
§A.3. end note]
19.5.17 bldSub (Build Sub Elements)
This element specifies the animation properties of a graphical object's sub-elements.
[Example: Consider applying animation to a graphical element consisting of a diagram. The <bldSub> element
should be used as follows:
<p:bldLst>
<p:bldGraphic spid="5" grpId="0">
<p:bldSub>
<a:bldDgm bld="one"/>
</p:bldSub>
</p:bldGraphic>
</p:bldLst>
end example]
[Note: The W3C XML Schema definition of this element’s content model
(CT_AnimationGraphicalObjectBuildProperties) is located in §A.4.1. end note]
19.5.18 blinds (Blinds Slide Transition)
This element describes the blinds slide transition effect, which uses a set of horizontal or vertical bars and wipes
them either left-to-right or top-to-bottom, respectively, until the new slide is fully shown. The rendering of this
transition depends upon the attributes specified.
[Example: Consider the following cases in which the “blinds” slide transition is applied to a slide, along with a set
of attributes. The proper usage and sample renderings are shown below, with the XML fragments preceding the
corresponding rendering:
<p:transition>
<p:blinds dir="horz"/>
</p:transition>
2622 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2633 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
<p:transition>
<p:blinds dir="vert"/>
</p:transition>
end example]
[Note: Any rendering shown above is for example purposes only. Exact rendering of any transition is determined
by the rendering application. As such, the same transition can have many variations depending on the
implementation. end note]
Attributes Description
dir (Transition This attribute specifies a horizontal or vertical transition.
Direction)
The possible values for this attribute are defined by the ST_Direction simple type
(§19.7.2).
[Note: The W3C XML Schema definition of this element’s content model (CT_OrientationTransition) is located in
§A.3. end note]
19.5.19 boolVal (Boolean Variant)
This element specifies a boolean value to be used for evaluation by a parent element. The exact meaning of the
value contained within this element is not defined here but is dependent on the usage of this element in
conjunction with one of the listed parent elements.
Attributes Description
val (Value) This attribute specifies the boolean value that this element contains and that should be
used in evaluating this element.
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
[Note: The W3C XML Schema definition of this element’s content model (CT_TLAnimVariantBooleanVal) is
located in §A.3. end note]
©ISO/IEC 2016 – All rights reserved 2623\n\n--- Page 2634 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
19.5.20 by (By)
This element describes the relative offset value for the color animation.
[Example: Consider a shape with a lightening emphasis animation applied to it. The <by> element should be
used as follows:
<p:animClr clrSpc="hsl">
<p:cBhvr>
<p:cTn id="8" dur="500" fill="hold"/>
<p:tgtEl>
<p:spTgt spid="4"/>
</p:tgtEl>
<p:attrNameLst>
<p:attrName>stroke.color</p:attrName>
</p:attrNameLst>
</p:cBhvr>
<p:by>
<p:hsl h="0" s="0" l="0"/>
</p:by>
</p:animClr>
end example]
[Note: The W3C XML Schema definition of this element’s content model (CT_TLByAnimateColorTransform) is
located in §A.3. end note]
19.5.21 by (By)
This element describes the relative offset value for the animation.
[Example: Consider a shape with an animation effect that scales the size of an object by 150%. The <by>
element should be used as follows:
<p:animScale>
<p:cBhvr>
<p:cTn id="6" dur="2000" fill="hold"/>
<p:tgtEl>
<p:spTgt spid="4"/>
</p:tgtEl>
</p:cBhvr>
<p:by x="150.000%" y="150.000%"/>
</p:animScale>
end example]
2624 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2635 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
x (X coordinate) This attribute describes the X coordinate.
The possible values for this attribute are defined by the ST_Percentage simple type
(§20.1.10.40).
y (Y coordinate) This attribute describes the Y coordinate.
The possible values for this attribute are defined by the ST_Percentage simple type
(§20.1.10.40).
[Note: The W3C XML Schema definition of this element’s content model (CT_TLPoint) is located in §A.3. end
note]
19.5.22 cBhvr (Common Behavior)
This element describes the common behaviors of animations.
[Example: Consider trying to emphasize text within a shape by changing the size of its font. The <anim> element
should be used as follows:
<p:anim to="1.5" calcmode="lin" valueType="num">
<p:cBhvr override="childStyle">
<p:cTn id="6" dur="2000" fill="hold"/>
<p:tgtEl>
<p:spTgt spid="3">
<p:txEl>
<p:charRg st="4294967295" end="4294967295"/>
</p:txEl>
</p:spTgt>
</p:tgtEl>
<p:attrNameLst>
<p:attrName>style.fontSize</p:attrName>
</p:attrNameLst>
</p:cBhvr>
</p:anim>
end example]
Attributes Description
accumulate This attribute makes a repeating animation build with each iteration when set to
(Accumulate) "always."
The possible values for this attribute are defined by the ST_TLBehaviorAccumulateType
simple type (§19.7.27).
©ISO/IEC 2016 – All rights reserved 2625\n\n--- Page 2636 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
additive (Additive) This attribute specifies how to apply the animation values to the original value for the
property.
The possible values for this attribute are defined by the ST_TLBehaviorAdditiveType
simple type (§19.7.28).
by (By) This attribute specifies a relative offset value for the animation..
The possible values for this attribute are defined by the W3C XML Schema string
datatype.
from (From) This attribute specifies the starting value of the animation.
The possible values for this attribute are defined by the W3C XML Schema string
datatype.
override (Override) This attribute specifies how a behavior should override values of the attribute being
animated on the target element. The "childStyle" clears the attributes on the children
contained inside the target element.
The possible values for this attribute are defined by the ST_TLBehaviorOverrideType
simple type (§19.7.29).
rctx (Runtime This attribute describes the runtime context of the animation. The currently-understood
Context) values are “PPT” and “IE.” This is used to specify the behavior used when animating in the
PPT slideshow vs. IE HTML runtime. An example can be seen with the transparency
effect. In IE, the transparency is animated as a bitmap, where in PPT, the style.opacity
property of a shape is used to animate the transparency.
The possible values for this attribute are defined by the W3C XML Schema string
datatype.
to (To) This attribute specifies the ending value of the animation.
The possible values for this attribute are defined by the W3C XML Schema string
datatype.
xfrmType This attribute specifies the kind of transform to be used.
(Transform Type)
The possible values for this attribute are defined by the ST_TLBehaviorTransformType
simple type (§19.7.30).
[Note: The W3C XML Schema definition of this element’s content model (CT_TLCommonBehaviorData) is located
in §A.3. end note]
19.5.23 charRg (Character Range)
This element specifies animation on a character range defined by a start and end character position.
2626 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2637 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
[Example: Consider animating the first word (characters 1 through 9) within a sentence. The <charRg> element
should be used as follows:
<p:animMotion>
<p:cBhvr>
<p:cTn id="6" dur="2000" fill="hold"/>
<p:tgtEl>
<p:spTgt spid="3">
<p:txEl>
<p:charRg st="0" end="9"/>
</p:txEl>
</p:spTgt>
</p:tgtEl>
<p:attrNameLst>
<p:attrName>ppt_x</p:attrName>
<p:attrName>ppt_y</p:attrName>
</p:attrNameLst>
</p:cBhvr>
</p:animMotion>
end example]
Attributes Description
end (End) This attribute defines the end of the index range.
The possible values for this attribute are defined by the ST_Index simple type (§19.7.3).
st (Start) This attribute defines the start of the index range.
The possible values for this attribute are defined by the ST_Index simple type (§19.7.3).
[Note: The W3C XML Schema definition of this element’s content model (CT_IndexRange) is located in §A.3. end
note]
19.5.24 checker (Checker Slide Transition)
This element describes the checker slide transition effect, which uses a set of horizontal or vertical
checkerboard squares and wipes them either left-to-right or top-to-bottom, respectively, until the new slide is
fully shown. The rendering of this transition depends upon the attributes specified.
©ISO/IEC 2016 – All rights reserved 2627\n\n--- Page 2638 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
[Example: Consider the following cases in which the “checker” slide transition is applied to a slide, along with a
set of attributes. The proper usage and sample renderings are shown below, with the XML fragments preceding
the corresponding rendering:
<p:transition>
<p:checker dir="horz"/>
</p:transition>
<p:transition>
<p:checker dir="vert"/>
</p:transition>
end example]
[Note: Any rendering shown above is for example purposes only. Exact rendering of any transition is determined
by the rendering application. As such, the same transition can have many variations depending on the
implementation. end note]
Attributes Description
dir (Transition This attribute specifies a horizontal or vertical transition.
Direction)
The possible values for this attribute are defined by the ST_Direction simple type
(§19.7.2).
[Note: The W3C XML Schema definition of this element’s content model (CT_OrientationTransition) is located in
§A.3. end note]
19.5.25 childTnLst (Children Time Node List)
This element describes the list of time nodes that have a fixed location in the timing tree based on their parent
time node. The children's start time is defined relative to their parent time node’s start.
[Note: The W3C XML Schema definition of this element’s content model (CT_TimeNodeList) is located in §A.3.
end note]
2628 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2639 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
19.5.26 circle (Circle Slide Transition)
This element describes the circle slide transition effect, which uses a circle pattern centered on the slide that
increases in size until the new slide is fully shown. The rendering of this transition has been shown below.
[Example: Consider the following case in which the “circle” slide transition is applied to a slide, along with a set
of attributes. The proper usage and a sample rendering are shown below, with the XML fragments preceding the
corresponding rendering:
<p:transition>
<p:circle/>
</p:transition>
end example]
[Note: Any rendering shown above is for example purposes only. Exact rendering of any transition is determined
by the rendering application. As such, the same transition can have many variations depending on the
implementation. end note]
[Note: The W3C XML Schema definition of this element’s content model (CT_Empty) is located in §A.3. end note]
19.5.27 clrVal (Color Value)
This element describes the color variant. This is used to specify a color that is to be used for animating the color
property of an object.
[Example: Consider trying to emphasize text within a shape by changing the color its font.
<p:set>
<p:cBhvr override="childStyle">
…
</p:cBhvr>
<p:to>
<p:clrVal>
<a:schemeClr val="accent2"/>
</p:clrVal>
</p:to>
</p:set>
end example]
[Note: The W3C XML Schema definition of this element’s content model (CT_Color) is located in §A.4.1. end
note]
©ISO/IEC 2016 – All rights reserved 2629\n\n--- Page 2640 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
19.5.28 cmd (Command)
This element describes the several non-durational commands that can be executed within a timeline. This can
be used to send events, call functions on elements, and send verbs to embedded objects. For example “Object
Action” effects for Embedded objects and Media commands for sounds/movies such as "PlayFrom(0.0)" and
"togglePause".
Attributes Description
cmd (Command) This attribute defines the actual command to be issued. Depending on the command
specified, the actual command can be made to invoke a wide range of actions on the
linked or embedded object.
Reserved Values (when type = “call”):
Value Description
play play corresponding media
playFrom(s) play corresponding media starting from s, where s is the number of
seconds from the beginning of the clip
pause pause corresponding media
resume resume play of corresponding media
stop stop play of corresponding media
togglePause play corresponding media if media is already paused, pause
corresponding media if media is already playing. If the corresponding
media is not active, this command restarts the media and plays from
its beginning.
Reserved Values (when type = “evt”):
Value Description
onstopaudio stop play of all audio
Reserved Values (when type = “verb”):
Value Description
0 Open the object for editing
1 Open the object for viewing
The value of the cmd attribute shall be the string representation of an integer that
represents the embedded object verb number. This verb number determines the action
that the rendering application should take corresponding to this object when this point in
the animation is reached.
[Example: Consider the following command
2630 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2641 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
<p:cmd type="evt" cmd="onstopaudio">
<p:cBhvr>
<p:cTn display="0" masterRel="sameClick">
<p:stCondLst>
<p:cond evt="begin" delay="0">
<p:tn val="5"/>
</p:cond>
</p:stCondLst>
</p:cTn>
<p:tgtEl>
<p:sldTgt/>
</p:tgtEl>
</p:cBhvr>
</p:cmd>
end example]
In the above example, the event of onstopaudio stops all audio from playing once this
particular animation is reached in the timeline.
The possible values for this attribute are defined by the W3C XML Schema string
datatype.
type (Command
Type)
This attribute specifies the kind of command that is issued by the rendering application to
the appropriate target application or object.
There are three possible values, call, evt, and verb. A call command type is used to
specify the class of commands that can then be issued.
Call commands (type=”call”): This command type is used to call methods on the object
specified (play(), pause(), etc.)
Event Commands (type=”evt”): This command type is used to set an event for the object
at this point in the timeline (onstopaudio, etc.)
Verb Commands (type=”verb”): This command type is used to set verbs for the object to
occur at this point in the timeline (0, 1, etc.)
The possible values for this attribute are defined by the ST_TLCommandType simple
type (§19.7.32).
[Note: The W3C XML Schema definition of this element’s content model (CT_TLCommandBehavior) is located in
§A.3. end note]
©ISO/IEC 2016 – All rights reserved 2631\n\n--- Page 2642 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
19.5.29 cMediaNode (Common Media Node Properties)
This element is used to describe behavior of media elements, such as sound or movies, in an animation.
[Example: Consider a shape with a sound effect attached to its animation. The <cMediaNode> element should
be used as follows:
<p:audio>
<p:cMediaNode mute="1">
<p:cTn display="0" masterRel="sameClick">
<p:stCondLst> … </p:stCondLst>
<p:endCondLst> … </p:endCondLst>
</p:cTn>
<p:tgtEl> … </p:tgtEl>
</p:cMediaNode>
</p:audio>
end example]
Attributes Description
mute (Mute) This attribute describes whether the media should be mute.
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
numSld (Number of This attribute describes the numbers of slides across which the media should play.
Slides)
The possible values for this attribute are defined by the W3C XML Schema unsignedInt
datatype.
showWhenStopped This attribute describes whether the media should be displayed when it is stopped.
(Show When
Stopped)
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
vol (Volume) This attribute describes the volume of the media element.
The possible values for this attribute are defined by the ST_PositiveFixedPercentage
simple type (§20.1.10.45).
[Note: The W3C XML Schema definition of this element’s content model (CT_TLCommonMediaNodeData) is
located in §A.3. end note]
2632 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2643 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
19.5.30 comb (Comb Slide Transition)
This element describes the comb slide transition effect, which uses a set of horizontal or vertical bars and wipes
them from one end of the slide to the other until the new slide is fully shown. The rendering of this transition
depends upon the attributes specified which have been shown below.
[Example: Consider the following cases in which the “comb” slide transition is applied to a slide, along with a set
of attributes. The proper usage and sample renderings are shown below, with the XML fragments preceding the
corresponding rendering:
<p:transition>
<p:comb dir="horz"/>
</p:transition>
<p:transition>
<p:comb dir="vert"/>
</p:transition>
end example]
[Note: Any rendering shown above is for example purposes only. Exact rendering of any transition is determined
by the rendering application. As such, the same transition can have many variations depending on the
implementation. end note]
Attributes Description
dir (Transition This attribute specifies a horizontal or vertical transition.
Direction)
The possible values for this attribute are defined by the ST_Direction simple type
(§19.7.2).
[Note: The W3C XML Schema definition of this element’s content model (CT_OrientationTransition) is located in
§A.3. end note]
19.5.31 cond (Condition)
This element specifies conditions on time nodes in a timeline. It is used within a list of start condition or list of
end condition elements.
©ISO/IEC 2016 – All rights reserved 2633\n\n--- Page 2644 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
[Example: For example, suppose we have a shape with a two second delay after the animation is started.
<p:cTn>
<p:stCondLst>
<p:cond delay="2000"/>
</p:stCondLst>
<p:childTnLst>
<p:set> … </p:set>
<p:animEffect transition="in" filter="blinds(horizontal)">
<p:cBhvr>
<p:cTn id="7" dur="1000"/>
<p:tgtEl>
<p:spTgt spid="4"/>
</p:tgtEl>
</p:cBhvr>
</p:animEffect>
</p:childTnLst>
</p:cTn>
end example]
Attributes Description
delay (Trigger This attribute describes the delay after an animation is triggered.
Delay)
The possible values for this attribute are defined by the ST_TLTime simple type
(§19.7.38).
evt (Trigger Event) This attribute describes the event that triggers an animation.
The possible values for this attribute are defined by the ST_TLTriggerEvent simple type
(§19.7.48).
[Note: The W3C XML Schema definition of this element’s content model (CT_TLTimeCondition) is located in
§A.3. end note]
19.5.32 cover (Cover Slide Transition)
This element describes the cover slide transition effect, which moves the new slide in from an off-screen
location, continually covering more of the previous slide until the new slide is fully shown. The rendering of this
transition depends upon the attributes specified which have been shown below.
[Example: Consider the following cases in which the “cover” slide transition is applied to a slide, along with a set
of attributes. The proper usage and sample renderings are shown below, with the XML fragments preceding the
corresponding rendering:
<p:transition>
2634 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2645 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
<p:cover dir="d"/>
</p:transition>
<p:transition>
<p:cover dir="l"/>
</p:transition>
<p:transition>
<p:cover dir="r"/>
</p:transition>
<p:transition>
<p:cover dir="u"/>
</p:transition>
<p:transition>
<p:cover dir="ld"/>
</p:transition>
<p:transition>
<p:cover dir="lu"/>
</p:transition>
©ISO/IEC 2016 – All rights reserved 2635\n\n--- Page 2646 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
<p:transition>
<p:cover dir="rd"/>
</p:transition>
<p:transition>
<p:cover dir="ru"/>
</p:transition>
end example]
[Note: Any rendering shown above is for example purposes only. Exact rendering of any transition is determined
by the rendering application. As such, the same transition can have many variations depending on the
implementation. end note]
Attributes Description
dir (Direction) This attribute specifies if the direction of the transition.
The possible values for this attribute are defined by the
ST_TransitionEightDirectionType simple type (§19.7.51).
[Note: The W3C XML Schema definition of this element’s content model (CT_EightDirectionTransition) is located
in §A.3. end note]
19.5.33 cTn (Common Time Node Properties)
This element describes the properties that are common for time nodes.
Attributes Description
accel (Acceleration) This attribute describes the percentage of specified duration over which the element's
time takes to accelerate from 0 up to the "run rate."
The possible values for this attribute are defined by the ST_PositiveFixedPercentage
2636 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2647 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
simple type (§20.1.10.45).
afterEffect (After This attribute specifies whether there is an after effect applied to the time node.
Effect)
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
autoRev (Auto This attribute describes whether to automatically play the animation in reverse after
Reverse) playing it in the forward direction.
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
bldLvl (Build level) This attribute describes the build level of the animation.
The possible values for this attribute are defined by the W3C XML Schema int datatype.
decel (Deceleration) This attribute describes the percentage of specified duration over which the element's
time takes to decelerate from the "run rate" down to 0.
The possible values for this attribute are defined by the ST_PositiveFixedPercentage
simple type (§20.1.10.45).
display (Display) This attribute describes whether the state of the time node is visible or hidden.
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
dur (Duration) This attribute describes the duration of the time node, expressed as unit time.
The possible values for this attribute are defined by the ST_TLTime simple type
(§19.7.38).
evtFilter (Event This attribute describes the event filter for this time node.
Filter)
The possible values for this attribute are defined by the W3C XML Schema string
datatype.
fill (Fill) This attribute describes the fill type for the time node.
The possible values for this attribute are defined by the ST_TLTimeNodeFillType simple
type (§19.7.41).
grpId (Group ID) This attribute describes the Group ID of the time node.
The possible values for this attribute are defined by the W3C XML Schema unsignedInt
datatype.
id (ID) This attribute specifies the identifier for the timenode.
The possible values for this attribute are defined by the ST_TLTimeNodeID simple type
©ISO/IEC 2016 – All rights reserved 2637\n\n--- Page 2648 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
(§19.7.42).
masterRel (Master This attribute specifies how the time node plays back relative to its master time node.
Relation)
The possible values for this attribute are defined by the ST_TLTimeNodeMasterRelation
simple type (§19.7.43).
nodePh (Node This attribute describes whether this node is a placeholder.
Placeholder)
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
nodeType (Node This attribute specifies the type of time node.
Type)
The possible values for this attribute are defined by the ST_TLTimeNodeType simple
type (§19.7.47).
presetClass (Preset This attribute descries the class of effect in which it belongs.
Types)
The possible values for this attribute are defined by the
ST_TLTimeNodePresetClassType simple type (§19.7.44).
presetID (Preset ID) This attribute describes the preset identifier for the time node.
The possible values for this attribute are defined by the W3C XML Schema int datatype.
presetSubtype This attribute is a bitflag that specifies a direction or some other attribute of the effect.
(Preset SubType) For example it can be set to specify a “From Bottom” for the Fly In effect, or “Bold” for
the Change Font Style effect.
The possible values for this attribute are defined by the W3C XML Schema int datatype.
repeatCount This attribute describes the number of times the element should repeat, in units of
(Repeat Count) thousandths.
The possible values for this attribute are defined by the ST_TLTime simple type
(§19.7.38).
repeatDur (Repeat This attribute describes the amount of time over which the element should repeat. If
Duration) absent, the attribute is taken to be the same as the specified duration.
The possible values for this attribute are defined by the ST_TLTime simple type
(§19.7.38).
restart (Restart) This attribute specifies if a node is to restart when it completes its action.
The possible values for this attribute are defined by the ST_TLTimeNodeRestartType
simple type (§19.7.45).
spd (Speed) This attribute specifies the percentage by which to speed up (or slow down) the timing. If
negative, the timing is reversed. [Example: if speed is 200% and the specified duration is
10 seconds, the actual duration is 5 seconds. end example]
2638 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2649 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
The possible values for this attribute are defined by the ST_Percentage simple type
(§20.1.10.40).
syncBehavior This attribute specifies how the time node synchronizes to its group.
(Synchronization
Behavior) The possible values for this attribute are defined by the ST_TLTimeNodeSyncType
simple type (§19.7.46).
tmFilter (Time This attribute specifies the time filter for the time node.
Filter)
The possible values for this attribute are defined by the W3C XML Schema string
datatype.
[Note: The W3C XML Schema definition of this element’s content model (CT_TLCommonTimeNodeData) is
located in §A.3. end note]
19.5.34 cut (Cut Slide Transition)
This element describes the cut slide transition effect, which simply replaces the previous slide with the new slide
instantaneously. No animation is used, but an option exists to cut to a black screen before showing the new
slide. The rendering of this transition depends upon the attributes specified which have been shown below.
[Example: Consider the following cases in which the “cut” slide transition is applied to a slide, along with a set of
attributes. The proper usage and sample renderings are shown below, with the XML fragments preceding the
corresponding rendering:
<p:transition>
<p:cut thruBlk="0"/>
</p:transition>
<p:transition>
<p:cut thruBlk="1"/>
</p:transition>
black
screen
©ISO/IEC 2016 – All rights reserved 2639\n\n--- Page 2650 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
end example]
[Note: Any rendering shown above is for example purposes only. Exact rendering of any transition is determined
by the rendering application. As such, the same transition can have many variations depending on the
implementation. end note]
Attributes Description
thruBlk (Transition This attribute specifies if the transition starts from a black screen (and then transition the
Through Black) new slide over black).
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
[Note: The W3C XML Schema definition of this element’s content model (CT_OptionalBlackTransition) is located
in §A.3. end note]
19.5.35 diamond (Diamond Slide Transition)
This element describes the diamond slide transition effect, which uses a diamond pattern centered on the slide
that increases in size until the new slide is fully shown. The rendering of this transition has been shown below.
[Example: Consider the following case in which the “diamond” slide transition is applied to a slide, along with a
set of attributes. The proper usage and a sample rendering are shown below, with the XML fragments preceding
the corresponding rendering:
<p:transition>
<p:diamond/>
</p:transition>
end example]
[Note: Any rendering shown above is for example purposes only. Exact rendering of any transition is determined
by the rendering application. As such, the same transition can have many variations depending on the
implementation. end note]
[Note: The W3C XML Schema definition of this element’s content model (CT_Empty) is located in §A.3. end note]
19.5.36 dissolve (Dissolve Slide Transition)
This element describes the dissolve slide transition effect, which uses a set of randomly placed squares on the
slide that continue to be added to until the new slide is fully shown. The rendering of this transition has been
shown below.
2640 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2651 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
[Example: Consider the following case in which the “dissolve” slide transition is applied to a slide, along with a
set of attributes. The proper usage and a sample rendering are shown below, with the XML fragments preceding
the corresponding rendering:
<p:transition>
<p:dissolve/>
</p:transition>
end example]
[Note: Any rendering shown above is for example purposes only. Exact rendering of any transition is determined
by the rendering application. As such, the same transition can have many variations depending on the
implementation. end note]
[Note: The W3C XML Schema definition of this element’s content model (CT_Empty) is located in §A.3. end note]
19.5.37 endCondLst (End Conditions List)
This element describes a list of the end conditions that shall be met in order to stop the time node.
[Example: Consider a shape a shape with an audio attached to the animation. The <endCondList> element
should be used as follows to specifies when the sound is done:
<p:audio>
<p:cMediaNode>
<p:cTn display="0" masterRel="sameClick">
<p:stCondLst> … </p:stCondLst>
<p:endCondLst>
<p:cond evt="onStopAudio" delay="0">
<p:tgtEl>
<p:sldTgt/>
</p:tgtEl>
</p:cond>
</p:endCondLst>
</p:cTn>
<p:tgtEl> … </p:tgtEl>
</p:cMediaNode>
</p:audio>
end example]
©ISO/IEC 2016 – All rights reserved 2641\n\n--- Page 2652 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
[Note: The W3C XML Schema definition of this element’s content model (CT_TLTimeConditionList) is located in
§A.3. end note]
19.5.38 endSnd (Stop Sound Action)
This element stops all previous sounds during a slide transition.
[Example: Consider a slide transition that stops all previous sounds. The<endSnd> element should be used as
follows:
<p:transition>
<p:sndAc>
<p:endSnd/>
</p:sndAc>
</p:transition>
end example]
[Note: The W3C XML Schema definition of this element’s content model (CT_Empty) is located in §A.3. end note]
19.5.39 endSync (EndSync)
This element is used to synchronizes the stopping of parallel elements in the timing tree. It is used on interactive
timeline sequences to specify that the interactive sequence’s duration ends when all of the child timenodes
have ended. It is also used to make interactive sequences restart-able (so that the entire interactive sequence
can be repeated if the trigger object is clicked on repeatedly).
[Example: Consider a shape with a fill change animation. The <endSync> element should be used as follows:
<p:seq concurrent="1" nextAc="seek">
<p:cTn>
<p:stCondLst/>
<p:endSync evt="end" delay="0">
<p:rtn val="all"/>
</p:endSync>
<p:childTnLst/>
</p:cTn>
<p:nextCondLst/>
</p:seq>
end example]
Attributes Description
delay (Trigger This attribute describes the delay after an animation is triggered.
Delay)
The possible values for this attribute are defined by the ST_TLTime simple type
(§19.7.38).
2642 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2653 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
evt (Trigger Event) This attribute describes the event that triggers an animation.
The possible values for this attribute are defined by the ST_TLTriggerEvent simple type
(§19.7.48).
[Note: The W3C XML Schema definition of this element’s content model (CT_TLTimeCondition) is located in
§A.3. end note]
19.5.40 excl (Exclusive)
This element describes the Exclusive time node. This time node is used to pause all other timelines when it is
activated. Conceptually it can be though of as follows:
[Note: The W3C XML Schema definition of this element’s content model (CT_TLTimeNodeExclusive) is located in
§A.3. end note]
19.5.41 fade (Fade Slide Transition)
This element describes the fade slide transition effect, which smoothly fades the previous slide either directly to
the new slide or first to a black screen and then to the new slide. The rendering of this transition depends upon
the attributes specified which have been shown below.
[Example: Consider the following cases in which the “fade” slide transition is applied to a slide, along with a set
of attributes. The proper usage and sample renderings are shown below, with the XML fragments preceding the
corresponding rendering:
<p:transition>
<p:fade thruBlk="0"/>
©ISO/IEC 2016 – All rights reserved 2643\n\n--- Page 2654 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
</p:transition>
<p:transition>
<p:fade thruBlk="1"/>
</p:transition>
black black black
screen screen screen
end example]
[Note: Any rendering shown above is for example purposes only. Exact rendering of any transition is determined
by the rendering application. As such, the same transition can have many variations depending on the
implementation. end note]
Attributes Description
thruBlk (Transition This attribute specifies if the transition starts from a black screen (and then transition the
Through Black) new slide over black).
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
[Note: The W3C XML Schema definition of this element’s content model (CT_OptionalBlackTransition) is located
in §A.3. end note]
19.5.42 fltVal (Float Value)
This element specifies a floating point value to be used for evaluation by a parent element. The exact meaning
of the value contained within this element is not defined here but is dependent on the usage of this element in
conjunction with one of the listed parent elements.
Attributes Description
val (Value) This attribute specifies the floating point value that this element contains and that should
be used in evaluating this element.
The possible values for this attribute are defined by the W3C XML Schema float datatype.
2644 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2655 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
[Note: The W3C XML Schema definition of this element’s content model (CT_TLAnimVariantFloatVal) is located
in §A.3. end note]
19.5.43 from (From)
This element is used to specify the starting color of the target element.
[Example: Consider a shape with an animation fill change from one accent color to another. The <from>
element should be used as follows:
<p:animClr clrSpc="rgb" dir="cw">
<p:cBhvr>
<p:cTn id="6" dur="2000" fill="hold"/>
<p:tgtEl> … </p:tgtEl>
<p:attrNameLst>
<p:attrName>fillcolor</p:attrName>
</p:attrNameLst>
</p:cBhvr>
<p:from>
<a:schemeClr val="accent3"/>
</p:from>
<p:to>
<a:schemeClr val="accent2"/>
</p:to>
</p:animClr>
end example]
[Note: The W3C XML Schema definition of this element’s content model (CT_Color) is located in §A.4.1. end
note]
19.5.44 from (From)
This element specifies an x/y co-ordinate to start the animation from.
[Example: Consider a shape with an animation sequence that needs to start at a certain coordinate. The <from>
element should be used as follows:
<p:animScale>
<p:cBhvr>
<p:cTn> … </p:cTn>
<p:tgtEl>
<p:spTgt spid="4"/>
</p:tgtEl>
</p:cBhvr>
<p:from x="100%" y="100%"/>
<p:to x="80%" y="100%"/>
©ISO/IEC 2016 – All rights reserved 2645\n\n--- Page 2656 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
</p:animScale>
end example]
Attributes Description
x (X coordinate) This attribute describes the X coordinate.
The possible values for this attribute are defined by the ST_Percentage simple type
(§20.1.10.40).
y (Y coordinate) This attribute describes the Y coordinate.
The possible values for this attribute are defined by the ST_Percentage simple type
(§20.1.10.40).
[Note: The W3C XML Schema definition of this element’s content model (CT_TLPoint) is located in §A.3. end
note]
19.5.45 graphicEl (Graphic Element)
This element specifies a graphical element which to animate.
[Example: Consider a diagram with an animation effect applied to it. The <graphicEl> element should be used as
follows:
<p:set>
<p:cBhvr>
<p:cTn id="6" dur="1" fill="hold"> … </p:cTn>
<p:tgtEl>
<p:spTgt spid="4">
<p:graphicEl>
<a:dgm id="{87C2C707-C3F4-4E81-A967-A8B8AE13E575}"/>
</p:graphicEl>
</p:spTgt>
</p:tgtEl>
<p:attrNameLst> … </p:attrNameLst>
</p:cBhvr>
<p:to> … </p:to>
</p:set>
end example]
[Note: The W3C XML Schema definition of this element’s content model (CT_AnimationElementChoice) is
located in §A.4.1. end note]
2646 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2657 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
19.5.46 hsl (HSL)
This element specifies an incremental HSL (Hue, Saturation, Lightness) value to add to a color animation.
[Example: Consider a shape with a lightening emphasis animation. The <hsl> element should be used as follows:
<p:animClr clrSpc="hsl">
<p:cBhvr>
<p:cTn id="8" dur="500" fill="hold"/>
<p:tgtEl>
<p:spTgt spid="4"/>
</p:tgtEl>
<p:attrNameLst>
<p:attrName>stroke.color</p:attrName>
</p:attrNameLst>
</p:cBhvr>
<p:by>
<p:hsl h="0" s="0" l="0"/>
</p:by>
</p:animClr>
end example]
Attributes Description
h (Hue) Specifies hue as an angle. The values range from [0, 360] degrees.
The possible values for this attribute are defined by the ST_Angle simple type
(§20.1.10.3).
l (Lightness) Specifies a lightness as a percentage. The values are in the range [-100%, 100%].
The possible values for this attribute are defined by the ST_FixedPercentage simple type
(§20.1.10.24).
s (Saturation) Specifies a saturation as a percentage. The values are in the range [-100%, 100%].
The possible values for this attribute are defined by the ST_FixedPercentage simple type
(§20.1.10.24).
[Note: The W3C XML Schema definition of this element’s content model (CT_TLByHslColorTransform) is located
in §A.3. end note]
19.5.47 inkTgt (Ink Target)
This element specifies an animation target element that is represented by a sub-shape in a legacy graphical
object.
©ISO/IEC 2016 – All rights reserved 2647\n\n--- Page 2658 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
[Example: Consider an ink diagram with an animation blinds transition effect applied to it. The <inkTgt> element
should be used as follows:
<p:animEffect transition="in" filter="blinds(horizontal)">
<p:cBhvr>
<p:cTn id="7" dur="500"/>
<p:tgtEl>
<p:inkTgt spid="_x0000_s2057"/>
</p:tgtEl>
</p:cBhvr>
</p:animEffect>
end example]
Attributes Description
spid (Shape ID) This attribute specifies the shape identifier.
The possible values for this attribute are defined by the ST_DrawingElementId simple
type (§20.1.10.21).
[Note: The W3C XML Schema definition of this element’s content model (CT_TLSubShapeId) is located in §A.3.
end note]
19.5.48 intVal (Integer)
This element specifies an integer value to be used for evaluation by a parent element. The exact meaning of the
value contained within this element is not defined here but is dependent on the usage of this element in
conjunction with one of the listed parent elements.
Attributes Description
val (Value) This attribute specifies the integer value that this element contains and that should be
used in evaluating this element.
The possible values for this attribute are defined by the W3C XML Schema int datatype.
[Note: The W3C XML Schema definition of this element’s content model (CT_TLAnimVariantIntegerVal) is
located in §A.3. end note]
19.5.49 iterate (Iterate)
This element specifies how the animation should be successively applied to sub elements of the target element
for a repeated effect. It can be applied to contained timing and animation structures over the letters, words, or
shapes within a target element.
2648 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2659 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
[Example: Consider a text animation where the words appear letter by letter. The <iterate> element should be
used as follows:
<p:par>
<p:cTn id="1" >
<p:stCondLst> … </p:stCondLst>
<p:iterate type="lt">
<p:tmPct val="10000"/>
</p:iterate>
<p:childTnLst> … </p:childTnLst>
</p:cTn>
</p:par>
end example]
Attributes Description
backwards This attribute specifies whether to go backwards in the timeline to the previous node.
(Backwards)
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
type (Iterate Type) This attribute specifies the iteration behavior and applies it to each letter, word or shape
within a container element.
Values are by word, by letter, or by element. If there is no text or block elements such as
shapes within the container or a single word, letter, or shape (depending on iterate type)
then no iteration happens and the behavior is applied to the element itself instead.
The possible values for this attribute are defined by the ST_IterateType simple type
(§19.7.4).
[Note: The W3C XML Schema definition of this element’s content model (CT_TLIterateData) is located in §A.3.
end note]
19.5.50 newsflash (Newsflash Slide Transition)
This element describes the newsflash slide transition effect, which grows and spins the new slide counter-
clockwise into place over the previous slide. The rendering of this transition has been shown below.
[Example: Consider the following case in which the “newsflash” slide transition is applied to a slide, along with a
set of attributes. The proper usage and a sample rendering are shown below, with the XML fragments preceding
the corresponding rendering:
<p:transition>
©ISO/IEC 2016 – All rights reserved 2649\n\n--- Page 2660 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
<p:newsflash/>
</p:transition>
end example]
[Note: Any rendering shown above is for example purposes only. Exact rendering of any transition is determined
by the rendering application. As such, the same transition can have many variations depending on the
implementation. end note]
[Note: The W3C XML Schema definition of this element’s content model (CT_Empty) is located in §A.3. end note]
19.5.51 nextCondLst (Next Conditions List)
This element describes a list of conditions that shall be met to advance to the next animation sequence.
[Example: Consider a shape with a text emphasis changing the size of its font.
<p:seq concurrent="1" nextAc="seek">
<p:cTn id="2" dur="indefinite" nodeType="mainSeq"> … </p:cTn>
<p:prevCondLst> … </p:prevCondLst>
<p:nextCondLst>
<p:cond evt="onNext" delay="0">
<p:tgtEl>
<p:sldTgt/>
</p:tgtEl>
</p:cond>
</p:nextCondLst>
</p:seq>
end example]
[Note: The W3C XML Schema definition of this element’s content model (CT_TLTimeConditionList) is located in
§A.3. end note]
19.5.52 oleChartEl (Embedded Chart Element)
This element specifies the subelement of an embedded chart to animate.
[Example: Consider an embedded Chart with a entrance animation effect applied to each of the graph's
categories. The <oldChartEl> element should be used as follows:
<p:animEffect transition="in" filter="blinds(horizontal)">
<p:cBhvr>
2650 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2661 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
<p:cTn id="12" dur="500"/>
<p:tgtEl>
<p:spTgt spid="19460">
<p:oleChartEl type="category" lvl="1"/>
</p:spTgt>
</p:tgtEl>
</p:cBhvr>
</p:animEffect>
end example]
Attributes Description
lvl (Level) This attribute describes the element levels to animate.
The possible values for this attribute are defined by the W3C XML Schema unsignedInt
datatype.
type (Type) This attribute specifies how to chart should be built during its animation.
The possible values for this attribute are defined by the ST_TLChartSubelementType
simple type (§19.7.31).
[Note: The W3C XML Schema definition of this element’s content model (CT_TLOleChartTargetElement) is
located in §A.3. end note]
19.5.53 par (Parallel Time Node)
This element describes the Parallel time node which can be activated along with other parallel time node
containers. Conceptually it can be thought of as follows:
[Example: Consider a simple animation with a blind entrance. The <par> element should be used as follows:
©ISO/IEC 2016 – All rights reserved 2651\n\n--- Page 2662 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
<p:timing>
<p:tnLst>
<p:par>
<p:cTn id="1" dur="indefinite" restart="never" nodeType="tmRoot">
<p:childTnLst>
<p:seq concurrent="1" nextAc="seek">
…
</p:seq>
</p:childTnLst>
</p:cTn>
</p:par>
</p:tnLst>
</p:timing>
end example]
[Note: The W3C XML Schema definition of this element’s content model (CT_TLTimeNodeParallel) is located in
§A.3. end note]
19.5.54 plus (Plus Slide Transition)
This element describes the plus slide transition effect, which uses a plus pattern centered on the slide that
increases in size until the new slide is fully shown. The rendering of this transition has been shown below.
[Example: Consider the following case in which the “plus” slide transition is applied to a slide, along with a set of
attributes. The proper usage and a sample rendering are shown below, with the XML fragments preceding the
corresponding rendering:
<p:transition>
<p:plus/>
</p:transition>
end example]
[Note: Any rendering shown above is for example purposes only. Exact rendering of any transition is determined
by the rendering application. As such, the same transition can have many variations depending on the
implementation. end note]
2652 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2663 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
[Note: The W3C XML Schema definition of this element’s content model (CT_Empty) is located in §A.3. end note]
19.5.55 prevCondLst (Previous Conditions List)
This element describes a list of conditions that shall be met in order to go backwards in an animation sequence.
[Example: Consider trying to emphasize text within a shape by changing the size of its font.
<p:seq concurrent="1" nextAc="seek">
<p:cTn id="2" dur="indefinite" nodeType="mainSeq">
</p:cTn>
<p:prevCondLst>
<p:cond evt="onPrev" delay="0">
<p:tgtEl>
<p:sldTgt/>
</p:tgtEl>
</p:cond>
</p:prevCondLst>
<p:nextCondLst>
</p:nextCondLst>
</p:seq>
end example]
[Note: The W3C XML Schema definition of this element’s content model (CT_TLTimeConditionList) is located in
§A.3. end note]
19.5.56 pRg (Paragraph Text Range)
This element specifies a text range to animate based on starting and ending paragraph number.
[Example: Consider an animation entrance of the first 3 text paragraphs. The <pRg> element should be used as
follows:
<p:animEffect transition="in" filter="checkerboard(across)">
<p:cBhvr>
<p:cTn id="12" dur="500"/>
<p:tgtEl>
<p:spTgt spid="3">
<p:txEl>
<p:pRg st="0" end="2"/>
</p:txEl>
</p:spTgt>
</p:tgtEl>
</p:cBhvr>
</p:animEffect>
©ISO/IEC 2016 – All rights reserved 2653\n\n--- Page 2664 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
end example]
Attributes Description
end (End) This attribute defines the end of the index range.
The possible values for this attribute are defined by the ST_Index simple type (§19.7.3).
st (Start) This attribute defines the start of the index range.
The possible values for this attribute are defined by the ST_Index simple type (§19.7.3).
[Note: The W3C XML Schema definition of this element’s content model (CT_IndexRange) is located in §A.3. end
note]
19.5.57 progress (Progress)
This element defines the progression of an animation. The default for the way animation progress happens
through an animEffect is a linear ramp from 0 to 1, starting at the effect’s begin time & ending at the effect’s
end time. When you specify a value for the progress attribute, you are overriding this default behaviour. The
value between 0 and 1 represents a percentage through the effect, where 0 is 0% and 1 is 100%.
Each animEffect is in fact an object-based transition. These transitions can be specified as “In” (where the object
is not visible at 0% and becomes completely visible at 100%) or “Out” (where the object is visible at 0% and
becomes completely invisible at 100%). You would set the progress attribute if you want to use the animEffect
as a “static” effect, where the transition properties do not actually change over time. As an alternative to using
the progress attribute, you can use the tmFilter (time filter), which is a base attribute of any effect/timenode, to
specify the way that progress through an effect should be performed dynamically.
[Note: The W3C XML Schema definition of this element’s content model (CT_TLAnimVariant) is located in §A.3.
end note]
19.5.58 pull (Pull Slide Transition)
This element describes the pull slide transition effect, which moves the previous slide to an off-screen location,
continually revealing more of the new slide until the new slide is fully shown. The rendering of this transition
depends upon the attributes specified which have been shown below.
[Example: Consider the following cases in which the “pull” slide transition is applied to a slide, along with a set of
attributes. The proper usage and sample renderings are shown below, with the XML fragments preceding the
corresponding rendering:
<p:transition>
<p:pull dir="d"/>
</p:transition>
2654 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2665 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
<p:transition>
<p:pull dir="l"/>
</p:transition>
<p:transition>
<p:pull dir="r"/>
</p:transition>
<p:transition>
<p:pull dir="u"/>
</p:transition>
<p:transition>
<p:pull dir="ld"/>
</p:transition>
<p:transition>
<p:pull dir="lu"/>
</p:transition>
©ISO/IEC 2016 – All rights reserved 2655\n\n--- Page 2666 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
<p:transition>
<p:pull dir="rd"/>
</p:transition>
<p:transition>
<p:pull dir="ru"/>
</p:transition>
end example]
[Note: Any rendering shown above is for example purposes only. Exact rendering of any transition is determined
by the rendering application. As such, the same transition can have many variations depending on the
implementation. end note]
Attributes Description
dir (Direction) This attribute specifies if the direction of the transition.
The possible values for this attribute are defined by the
ST_TransitionEightDirectionType simple type (§19.7.51).
[Note: The W3C XML Schema definition of this element’s content model (CT_EightDirectionTransition) is located
in §A.3. end note]
19.5.59 push (Push Slide Transition)
This element describes the push slide transition effect, which moves the new slide in from an off-screen
location, continually pushing the previous slide to an opposite off-screen location until the new slide is fully
shown. The rendering of this transition depends upon the attributes specified which have been shown below.
[Example: Consider the following cases in which the “push” slide transition is applied to a slide, along with a set
of attributes. The proper usage and sample renderings are shown below, with the XML fragments preceding the
corresponding rendering:
<p:transition>
<p:push dir="d"/>
2656 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2667 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
</p:transition>
<p:transition>
<p:push dir="l"/>
</p:transition>
<p:transition>
<p:push dir="r"/>
</p:transition>
<p:transition>
<p:push dir="u"/>
</p:transition>
end example]
[Note: Any rendering shown above is for example purposes only. Exact rendering of any transition is determined
by the rendering application. As such, the same transition can have many variations depending on the
implementation. end note]
Attributes Description
dir (Direction) This attribute specifies the direction of the slide transition.
The possible values for this attribute are defined by the
ST_TransitionSideDirectionType simple type (§19.7.53).
[Note: The W3C XML Schema definition of this element’s content model (CT_SideDirectionTransition) is located
in §A.3. end note]
©ISO/IEC 2016 – All rights reserved 2657\n\n--- Page 2668 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
19.5.60 random (Random Slide Transition)
This element describes the random slide transition effect, which chooses a random transition from the set
available in the rendering application. This transition thus can be different each time it is used.
[Example: Consider the following case in which the “random” slide transition is applied to a slide, along with a
set of attributes. The proper usage is shown below:
<p:transition>
<p:random/>
</p:transition>
end example]
[Note: The W3C XML Schema definition of this element’s content model (CT_Empty) is located in §A.3. end note]
19.5.61 randomBar (Random Bar Slide Transition)
This element describes the randomBar slide transition effect, which uses a set of randomly placed horizontal or
vertical bars on the slide that continue to be added to until the new slide is fully shown. The rendering of this
transition depends upon the attributes specified which have been shown below.
[Example: Consider the following cases in which the “randomBar” slide transition is applied to a slide, along with
a set of attributes. The proper usage and sample renderings are shown below, with the XML fragments
preceding the corresponding rendering:
<p:transition>
<p:randomBar dir="horz"/>
</p:transition>
<p:transition>
<p:randomBar dir="vert"/>
</p:transition>
2658 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2669 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
end example]
[Note: Any rendering shown above is for example purposes only. Exact rendering of any transition is determined
by the rendering application. As such, the same transition can have many variations depending on the
implementation. end note]
Attributes Description
dir (Transition This attribute specifies a horizontal or vertical transition.
Direction)
The possible values for this attribute are defined by the ST_Direction simple type
(§19.7.2).
[Note: The W3C XML Schema definition of this element’s content model (CT_OrientationTransition) is located in
§A.3. end note]
19.5.62 rCtr (Rotation Center)
This element describes the center of the rotation used to rotate a motion path by X angle.
[Example: For example, suppose we have a simple animation with a checkerbox text entrance.
<p:animMotion origin="layout" path="M 0 0 L 0.25 0.33333 E"
pathEditMode="relative" rAng="0" ptsTypes="">
<p:cBhvr>
<p:cTn id="6" dur="2000" fill="hold"/>
<p:tgtEl>
<p:spTgt spid="3"/>
</p:tgtEl>
<p:attrNameLst>
<p:attrName>ppt_x</p:attrName>
<p:attrName>ppt_y</p:attrName>
</p:attrNameLst>
</p:cBhvr>
<p:rCtr x="56.7%" y="83.4%"/>
</p:animMotion>
end example]
Attributes Description
x (X coordinate) This attribute describes the X coordinate.
The possible values for this attribute are defined by the ST_Percentage simple type
(§20.1.10.40).
y (Y coordinate) This attribute describes the Y coordinate.
©ISO/IEC 2016 – All rights reserved 2659\n\n--- Page 2670 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
The possible values for this attribute are defined by the ST_Percentage simple type
(§20.1.10.40).
[Note: The W3C XML Schema definition of this element’s content model (CT_TLPoint) is located in §A.3. end
note]
19.5.63 rgb (RGB)
The element specifies an incremental RGB value to add to the color property.
[Example: Consider a shape with a color emphasis animation. The <rgb> element should be used as follows:
<p:animClr clrSpc="rgb">
<p:cBhvr>
<p:cTn id="8" dur="500" fill="hold"/>
<p:tgtEl>
<p:spTgt spid="4"/>
</p:tgtEl>
<p:attrNameLst>
<p:attrName>stroke.color</p:attrName>
</p:attrNameLst>
</p:cBhvr>
<p:by>
<p:rgb r="10" g="20" b="30"/>
</p:by>
</p:animClr>
end example]
Attributes Description
b (Blue) This attribute specifies a blue component luminance as a percentage. Values are in the
range [-100%, 100%].
The possible values for this attribute are defined by the ST_FixedPercentage simple type
(§20.1.10.24).
g (Green) This attribute specifies a green component luminance as a percentage.
Values are in the range [-100%, 100%].
The possible values for this attribute are defined by the ST_FixedPercentage simple type
(§20.1.10.24).
r (Red) This attribute specifies a red component luminance as a percentage. Values are in the
range [-100%, 100%].
2660 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2671 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
The possible values for this attribute are defined by the ST_FixedPercentage simple type
(§20.1.10.24).
[Note: The W3C XML Schema definition of this element’s content model (CT_TLByRgbColorTransform) is located
in §A.3. end note]
19.5.64 rtn (Runtime Node Trigger Choice)
This element specifies the child time node that triggers a time condition. References a child time node or all
child nodes. Order is based on the child's end time.
[Example: Consider an animation which ends the synchronization of all parallel time nodes when all the child
nodes have ended their animation. The <rtn> element should be used as follows:
<p:cTn>
<p:stCondLst> … </p:stCondLst>
<p:endSync evt="end" delay="0">
<p:rtn val="all"/>
</p:endSync>
<p:childTnLst> … </p:childTnLst>
</p:cTn>
end example]
Attributes Description
val (Value) This attribute describes the value that triggers the runtime node.
The possible values for this attribute are defined by the ST_TLTriggerRuntimeNode
simple type (§19.7.49).
[Note: The W3C XML Schema definition of this element’s content model (CT_TLTriggerRuntimeNode) is located
in §A.3. end note]
19.5.65 seq (Sequence Time Node)
This element describes the Sequence time node and it can only be activated when the one before it finishes.
Conceptually it can be though of as follows:
©ISO/IEC 2016 – All rights reserved 2661\n\n--- Page 2672 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
[Example: For example, suppose we have a simple animation with a blind entrance.
<p:timing>
<p:tnLst>
<p:par>
<p:cTn id="1" dur="indefinite" restart="never" nodeType="tmRoot">
<p:childTnLst>
<p:seq concurrent="1" nextAc="seek">
…
</p:seq>
</p:childTnLst>
</p:cTn>
</p:par>
</p:tnLst>
</p:timing>
end example]
Attributes Description
concurrent This attribute specifies if concurrency is enabled or disabled. By default this attribute has
(Concurrent) a value of "disabled". When the value is set to "enabled", the previous element is left
enabled when advancing to the next element in a sequence instead of being ended. This
is only relevant for advancing via the next condition element being triggered. The only
other way to advance to the next element would be to have the current element end,
which implies it is no longer concurrent.
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
nextAc (Next This attribute specifies what to do when going forward in sequence. By default this
Action) attribute has a value of "none". When this is set to seek it seeks the element to a natural
end time (not necessarily the actual end time).
2662 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2673 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
The natural end position is defined as the latest non-infinite end time of the children. If a
child loops forever, the end of its first loop is used as its "end time" for the purposes of
this calculation.
Some container elements can have infinite durations due to an infinite-duration child
element. The engine needs to recurse down through all infinite duration containers to
calculate their natural duration in case a child might have non-infinite duration within it
that needs to be taken into account.
The possible values for this attribute are defined by the ST_TLNextActionType simple
type (§19.7.34).
prevAc (Previous This attribute specifies what to do when going backwards in a sequence. By default it is
Action) set to "none" and nothing special is done. When the value is "skipTimed", the sequence
continues to go backwards until it reaches a sequence element that was defined to begin
only on the next condition element.
The possible values for this attribute are defined by the ST_TLPreviousActionType
simple type (§19.7.37).
[Note: The W3C XML Schema definition of this element’s content model (CT_TLTimeNodeSequence) is located in
§A.3. end note]
19.5.66 set (Set Time Node Behavior)
This element allows the setting of a particular property value to a fixed value while the behavior is active and
restores the value when the behavior is reset or turned off.
[Example: For example, suppose we want to set certain properties during an animation effect. The <set>
element should be used as follows:
<p:childTnLst>
<p:set>
<p:cBhvr>
<p:cTn id="6" dur="1" fill="hold"> … </p:cTn>
<p:tgtEl>
<p:spTgt spid="4"/>
</p:tgtEl>
<p:attrNameLst>
<p:attrName>style.visibility</p:attrName>
</p:attrNameLst>
</p:cBhvr>
<p:to>
<p:strVal val="visible"/>
©ISO/IEC 2016 – All rights reserved 2663\n\n--- Page 2674 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
</p:to>
</p:set>
<p:animEffect transition="in" filter="blinds(horizontal)">
…
</p:animEffect>
</p:childTnLst>
end example]
[Note: The W3C XML Schema definition of this element’s content model (CT_TLSetBehavior) is located in §A.3.
end note]
19.5.67 sldTgt (Slide Target)
This element specifies the slide as the target element.
[Example: For example, suppose we have a simple animation with a blind entrance.
<p:seq concurrent="1" nextAc="seek">
<p:cTn id="2" dur="indefinite" nodeType="mainSeq"> … </p:cTn>
<p:prevCondLst> … </p:prevCondLst>
<p:nextCondLst>
<p:cond evt="onNext" delay="0">
<p:tgtEl>
<p:sldTgt/>
</p:tgtEl>
</p:cond>
</p:nextCondLst>
</p:seq>
end example]
[Note: The W3C XML Schema definition of this element’s content model (CT_Empty) is located in §A.3. end note]
19.5.68 snd (Sound)
This element specifies the audio information to play during a slide transition.
[Example: Consider a slide transition with an audio effect. The <snd> element should be used as follows:
<p:transition>
<p:sndAc>
<p:stSnd>
<p:snd r:embed="rId2""/>
</p:stSnd>
</p:sndAc>
</p:transition>
2664 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2675 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
end example]
Attributes Description
embed (Embedded Specifies the identification information for an embedded audio file. This attribute is used
Audio File to specify the location of an object that resides locally within the file. [Note: A list of
Relationship ID) suggested audio types is provided in §15.2.2. end note]
Namespace: The possible values for this attribute are defined by the ST_RelationshipId simple type
http://purl.oclc.or (§22.8.2.1).
g/ooxml/officeDoc
ument/relationshi
ps
name (Sound Specifies the original name or given short name for the corresponding sound. This is used
Name) to distinguish this sound from others by providing a human readable name for the
attached sound should the user need to identify the sound among others within the UI.
Namespace:
http://purl.oclc.or The possible values for this attribute are defined by the W3C XML Schema string
g/ooxml/drawing datatype.
ml/main
[Note: The W3C XML Schema definition of this element’s content model (CT_EmbeddedWAVAudioFile) is
located in §A.4.1. end note]
19.5.69 sndAc (Sound Action)
This element describes a sound action for slide transition. This element specifies that the start of the slide
transition is accompanied by the playback of an audio file; the actual audio file used is specified by the snd
element (§19.5.68).
[Example: Consider a slide transition with a sound effect. The <sndAc> element should be used as follows:
<p:transition>
<p:sndAc>
<p:stSnd>
<p:snd r:embed="rId2"/>
</p:stSnd>
</p:sndAc>
</p:transition>
end example]
[Note: The W3C XML Schema definition of this element’s content model (CT_TransitionSoundAction) is located
in §A.3. end note]
©ISO/IEC 2016 – All rights reserved 2665\n\n--- Page 2676 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
19.5.70 sndTgt (Sound Target)
This element describes the sound information for a target object.
[Example: Consider a shape with a sound effect animation. The <sndTgt> element should be used as follows:
<p:subTnLst>
<p:audio>
<p:cMediaNode>
<p:cTn display="0" masterRel="sameClick"> … </p:cTn>
<p:tgtEl>
<p:sndTgt r:embed="rId2" r:link="rId3"/>
</p:tgtEl>
</p:cMediaNode>
</p:audio>
</p:subTnLst>
end example]
Attributes Description
embed (Embedded Specifies the identification information for an embedded audio file. This attribute is used
Audio File to specify the location of an object that resides locally within the file. [Note: A list of
Relationship ID) suggested audio types is provided in §15.2.2. end note]
Namespace: The possible values for this attribute are defined by the ST_RelationshipId simple type
http://purl.oclc.or (§22.8.2.1).
g/ooxml/officeDoc
ument/relationshi
ps
name (Sound Specifies the original name or given short name for the corresponding sound. This is used
Name) to distinguish this sound from others by providing a human readable name for the
attached sound should the user need to identify the sound among others within the UI.
Namespace:
http://purl.oclc.or The possible values for this attribute are defined by the W3C XML Schema string
g/ooxml/drawing datatype.
ml/main
[Note: The W3C XML Schema definition of this element’s content model (CT_EmbeddedWAVAudioFile) is
located in §A.4.1. end note]
19.5.71 split (Split Slide Transition)
This element describes the split slide transition effect, which reveals the new slide directly on top of the
previous one by wiping either horizontal or vertical from the outside in, or from the inside out, until the new
slide is fully shown. The rendering of this transition depends upon the attributes specified which have been
shown below.
2666 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2677 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
[Example: Consider the following cases in which the “split” slide transition is applied to a slide, along with a set
of attributes. The proper usage and sample renderings are shown below, with the XML fragments preceding the
corresponding rendering:
<p:transition>
<p:split orient="horz" dir="in"/>
</p:transition>
<p:transition>
<p:split orient="horz" dir="out"/>
</p:transition>
<p:transition>
<p:split orient="vert" dir="in"/>
</p:transition>
<p:transition>
<p:split orient="vert" dir="out"/>
</p:transition>
end example]
[Note: Any rendering shown above is for example purposes only. Exact rendering of any transition is determined
by the rendering application. As such, the same transition can have many variations depending on the
implementation. end note]
Attributes Description
dir (Direction) This attribute specifies the direction of a "split" slide transition.
©ISO/IEC 2016 – All rights reserved 2667\n\n--- Page 2678 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
The possible values for this attribute are defined by the
ST_TransitionInOutDirectionType simple type (§19.7.52).
orient (Orientation) This attribute specifies the orientation of a "split" slide transition.
The possible values for this attribute are defined by the ST_Direction simple type
(§19.7.2).
[Note: The W3C XML Schema definition of this element’s content model (CT_SplitTransition) is located in §A.3.
end note]
19.5.72 spTgt (Shape Target)
The element specifies the shape in which to apply a certain animation to.
[Example: Consider a shape whose id is 3 in which we want to apply a fade animation effect. The <spTgt> should
be used as follows:
<p:animEffect transition="in" filter="fade">
<p:cBhvr>
<p:cTn id="7" dur="2000"/>
<p:tgtEl>
<p:spTgt spid="3"/>
</p:tgtEl>
</p:cBhvr>
</p:animEffect>
end example]
Attributes Description
spid (Shape ID) This attribute specifies the shape identifier.
The possible values for this attribute are defined by the ST_DrawingElementId simple
type (§20.1.10.21).
[Note: The W3C XML Schema definition of this element’s content model (CT_TLShapeTargetElement) is located
in §A.3. end note]
19.5.73 stCondLst (Start Conditions List)
This element contains a list conditions that shall be met for a time node to be activated.
2668 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2679 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
[Example: For example, suppose we have a shape with an entrance appearance after 5 seconds. The
<stCondLst>element should be used as follows:
<p:par>
<p:cTn id="5" nodeType="clickEffect">
<p:stCondLst>
<p:cond delay="5000"/>
</p:stCondLst>
<p:childTnLst> … </p:childTnLst>
</p:cTn>
</p:par>
end example]
[Note: The W3C XML Schema definition of this element’s content model (CT_TLTimeConditionList) is located in
§A.3. end note]
19.5.74 strips (Strips Slide Transition)
This element describes the strips slide transition effect, which uses a set of bars that are arranged in a staggered
fashion and wipes them across the screen until the new slide is fully shown. The rendering of this transition
depends upon the attributes specified which have been shown below.
[Example: Consider the following cases in which the “strips” slide transition is applied to a slide, along with a set
of attributes. The proper usage and sample renderings are shown below, with the XML fragments preceding the
corresponding rendering:
<p:transition>
<p:strips dir="ld"/>
</p:transition>
<p:transition>
<p:strips dir="lu"/>
</p:transition>
<p:transition>
<p:strips dir="rd"/>
</p:transition>
©ISO/IEC 2016 – All rights reserved 2669\n\n--- Page 2680 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
<p:transition>
<p:strips dir="ru"/>
</p:transition>
end example]
[Note: Any rendering shown above is for example purposes only. Exact rendering of any transition is determined
by the rendering application. As such, the same transition can have many variations depending on the
implementation. end note]
Attributes Description
dir (Direction) This attribute specifies if the direction of the transition.
The possible values for this attribute are defined by the
ST_TransitionCornerDirectionType simple type (§19.7.50).
[Note: The W3C XML Schema definition of this element’s content model (CT_CornerDirectionTransition) is
located in §A.3. end note]
19.5.75 strVal (String Value)
This element specifies a string value to be used for evaluation by a parent element. The exact meaning of the
value contained within this element is not defined here but is dependent on the usage of this element in
conjunction with one of the listed parent elements.
Attributes Description
val (Value) This attribute specifies the string value that this element contains and that should be
used in evaluating this element.
The possible values for this attribute are defined by the W3C XML Schema string
datatype.
[Note: The W3C XML Schema definition of this element’s content model (CT_TLAnimVariantStringVal) is located
in §A.3. end note]
2670 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2681 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
19.5.76 stSnd (Start Sound Action)
This element describes the sound that starts playing during a slide transition.
[Example: Consider a slide transition that starts with a sound effect. The <stSnd> element should be used as
follows:
<p:transition>
<p:sndAc>
<p:stSnd>
<p:snd r:embed="rId2"/>
</p:stSnd>
</p:sndAc>
</p:transition>
end example]
Attributes Description
loop (Loop Sound) This attribute specifies if the sound loops until the next sound event occurs in slideshow.
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
[Note: The W3C XML Schema definition of this element’s content model (CT_TransitionStartSoundAction) is
located in §A.3. end note]
19.5.77 subSp (Subshape)
This element specifies the subshape of a legacy graphical object to animate.
[Example: Consider adding animation to a legacy diagram. The <subSp> element should be used as follows:
<p:animEffect transition="in" filter="blinds(horizontal)">
<p:cBhvr>
<p:cTn id="7" dur="500"/>
<p:tgtEl>
<p:spTgt spid="2053">
<p:subSp spid="_x0000_s70664"/>
</p:spTgt>
</p:tgtEl>
</p:cBhvr>
</p:animEffect>
end example]
©ISO/IEC 2016 – All rights reserved 2671\n\n--- Page 2682 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
spid (Shape ID) This attribute specifies the shape identifier.
The possible values for this attribute are defined by the ST_DrawingElementId simple
type (§20.1.10.21).
[Note: The W3C XML Schema definition of this element’s content model (CT_TLSubShapeId) is located in §A.3.
end note]
19.5.78 subTnLst (Sub-TimeNodes List)
This element describes time nodes that have a start time which is not based on the containing timenode. It is
instead based on their master relationship (masterRel). At runtime, they are inserted dynamically into the
timing tree as child timenodes for playback, based on the logic defined by the master relationship. These
elements are used for animations such as "dim after" and "play sound effects"
[Example: Consider an animation with a "Fly In" effect on paragraphs so that each paragraph flies in on a
separate click. Then the "Dim After" effect for paragraph 1 doe not happen until paragraph 2 flies in. The
<subTnLst> element should be used as follows:
<p:par>
<p:cTn id="5" grpId="0" nodeType="clickEffect">
<p:stCondLst> … </p:stCondLst>
<p:childTnLst> … </p:childTnLst>
<p:subTnLst>
<p:set>
<p:cBhvr override="childStyle">
<p:cTn fill="hold" masterRel="nextClick" afterEffect="1"/>
<p:tgtEl> … </p:tgtEl>
<p:attrNameLst> … </p:attrNameLst>
</p:cBhvr>
<p:to> … </p:to>
</p:set>
</p:subTnLst>
</p:cTn>
</p:par>
end example]
[Note: The W3C XML Schema definition of this element’s content model (CT_TimeNodeList) is located in §A.3.
end note]
19.5.79 tav (Time Animate Value)
This element defines a "keypoint" in animation interpolation.
2672 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2683 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
[Example: Consider a shape with a "fly-in" animation. The <tav> element should be used as follows:
<p:anim calcmode="lin" valueType="num">
<p:cBhvr additive="base"> … </p:cBhvr>
<p:tavLst>
<p:tav tm="0%">
<p:val>
<p:strVal val="1+#ppt_h/2"/>
</p:val>
</p:tav>
<p:tav tm="100%">
<p:val>
<p:strVal val="#ppt_y"/>
</p:val>
</p:tav>
</p:tavLst>
</p:anim>
end example]
Attributes Description
fmla (Formula)
This attribute allows for the specification of a formula to be used for describing a
complex motion for an animated object. The formula manipulates the motion of the
object by modifying a property of the object over a specified period of time. Each formula
has zero or more inputs specified by the ($) symbol, zero or more variables specified by
the (#) symbol pre-pended to the variable name and a target variable which is specified
by the previously specified attrName element. The formula can contain one or more of
any of the constants, operators or functions listed below. In addition to this, the formula
can also contain floating point numbers and parentheses.
Mathematical operations have the following order of precedence, listed from lowest to
highest. Operators listed on the same line have equal precedence.
 “+”, “-“
 “*”, “/”, “%”
 “^”
 Unary minus, Unary plus (e.g. -2, meaning 3*-2 is the same as 3*(-2))
 Variables, Constants (including numbers) and Functions (as listed previously)
Language Description:
Digit = '0' | '1' | ‘2’ | ‘3’ | ‘4’ | ‘5’ | ‘6’ | ‘7’
| ‘8’ | '9' ;
©ISO/IEC 2016 – All rights reserved 2673\n\n--- Page 2684 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
number = digit , { digit } ;
exponent = [ '-' ] , ( 'e' | 'E' ) , number ;
value = number , [ '.' number ] , [ exponent ] ;
variable = '$' | 'ppt_x' | 'ppt_y' | 'ppt_w' | 'ppt_h' ;
constant = value | 'pi' | 'e' ;
ident = 'abs' | ‘acos’ | ‘asin’ | ‘atan’ | ‘ceil’
| ‘cos’ | ‘cosh’ | ‘deg’ | ‘exp’ | ‘floor’ | ‘ln’
| ‘max’ | ‘min’ | ‘rad’ | ‘rand’ | ‘sin’ | ‘sinh’
| ‘sqrt’ | ‘tan’ | 'tanh' ;
function = ident , '(' , formula [ ',' , formula ] , ')' ;
formula = term , { [ '+' | '-' ] , term } ;
term = power , { [ '*' | '/' | '%' ] , power } ;
power = unary [ '^' , unary ] ;
unary = [ '+' | '-' ] , factor ;
factor = variable | constant | function | parens ;
parens = '(' , formula , ')' ;
[Note: Formulas can only support a calcMode (Calculation Mode) of linear or discrete. If
another calcMode is specified or no calcMode is specified then a calcMode of linear is
assumed. end note]
[Note: Any additional characters in the formula string that are not contained within the
set described are considered invalid. end note]
Variables:
Name Description
$ Formula input
ppt_x Pre-animation x position of the object on the slide
Position on the slide is represented using an abstract coordinate space
where 0 represents the left side of the slide and 1 represents the right
side of the slide.
ppt_y Pre-animation y position of the object on the slide
Position on the slide is represented using an abstract coordinate space
where 0 represents the top of the slide and 1 represents the bottom of
the slide.
ppt_w Pre-animation width of the object
Width is represented using an abstract coordinate space relative to the
size of the slide, where 1 represents the width of the slide.
ppt_h Pre-animation height of the object
Height is represented using an abstract coordinate space relative to the
size of the slide, where 1 represents the height of the slide.
Constants:
Name Description
2674 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2685 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
pi Mathematical constant pi
e Mathematical constant e
Operators:
Name Description Usage
+ Addition “x+y”, adds x to the value y
- Subtraction “x-y”, subtracts y from the value x
* Multiplication “x*y”, multiplies x by the value y
/ Division “x/y”, divides x by the value y
% Modulus “x%y”, the remainder of x/y
^ Power “x^y”, x raised to the power y
Functions:
Name Description Usage
abs Absolute value “abs(x)”, absolute value of x
acos Arc Cosine “acos(x)”, arc cosine of the value x
asin Arc Sine “asin(x)”, arc sine of the value x
atan Arc Tangent “atan(x)”, arc tangent of the value x
ceil Ceil value “ceil(x)”, value of x rounded up
cos Cosine “cos(x)”, cosine of the value of x
cosh Hyperbolic Cosine “cosh(x)", hyperbolic cosine of the value
x
deg Radiant to Degree convert “deg(x)”, the degree value of radiant
value x
exp Exponent “exp(x)”, value of constant e raised to
the power of x
floor Floor value “floor(x)”, value of x rounded down
ln Natural logarithm “ln(x)”, natural logarithm of x
max Maximum of two values “max(x,y)”, returns x if (x > y) or returns y
if (y > x)
min Minimum of two values “min(x,y)", returns x if (x < y) or returns y
if (y < x)
rad Degree to Radiant convert “rad(x)”, the radiant value of degree
value x
rand Random value “rand(x)”, returns a random floating
point value between 0 and x
sin Sine “sin(x)”, sine of the value x
©ISO/IEC 2016 – All rights reserved 2675\n\n--- Page 2686 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
sinh Hyperbolic Sine "sinh(x)”, hyperbolic sine of the value x
sqrt Square root “sqrt(x)”, square root of the value x
tan Tangent “tan(x)”, tangent of the value x
tanh Hyperbolic Tangent “tanh(x)", hyperbolic tangent of the
value x
[Example: Consider the following animation path:
<p:animcalcmode="lin" valueType="num">
<p:cBhvr>
<p:cTn id="9" dur="664" tmFilter="0.0,0.0; 0.25,0.07;
0.50,0.2; 0.75,0.467; 1.0,1.0">
<p:stCondLst>
<p:cond delay="0"/>
</p:stCondLst>
</p:cTn>
<p:tgtEl>
<p:spTgtspid="4"/>
</p:tgtEl>
<p:attrNameLst>
<p:attrName>ppt_y</p:attrName>
</p:attrNameLst>
</p:cBhvr>
<p:tavLst>
<p:tav tm="0%" fmla="#ppt_y-sin(pi*$)/3">
<p:val>
<p:fltValval="0.5"/>
</p:val>
</p:tav>
<p:tav tm="100%">
<p:val>
<p:fltValval="1"/>
</p:val>
</p:tav>
</p:tavLst>
</p:anim>
The animation example above modifies the ppt_y variable of the object by subtracting
sin(pi*$)/3 from the non-animated value of ppt_y. The start value is 0.5 and the end
value is 1 specified in each of the val elements. The total time for this animation is
specified within the dur attribute and the filtered time graph is specified by the tmFilter
attribute. The end result is that the object moves from a point above its non-animated
position back to its non-animated position. With the specification of the tmFilter it has a
modified time graph such that it also appears to accelerate as it reaches its final position.
2676 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2687 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
[Note: For this example, the non-animated value of ppt_y is the value of this variable if
the object were to be statically rendered on the slide without animation properties. end
note]
end example]
The possible values for this attribute are defined by the W3C XML Schema string
datatype.
tm (Time) This attribute specifies the time at which the attribute being animated takes on the value.
The possible values for this attribute are defined by the ST_TLTimeAnimateValueTime
simple type (§19.7.39).
[Note: The W3C XML Schema definition of this element’s content model (CT_TLTimeAnimateValue) is located in
§A.3. end note]
19.5.80 tavLst (Time Animated Value List)
This element specifies a list of time animated value elements.
[Example: Consider a shape with a "fly-in" animation. The <tav> element should be used as follows:
<p:anim calcmode="lin" valueType="num">
<p:cBhvr additive="base"> … </p:cBhvr>
<p:tavLst>
<p:tav tm="0%">
<p:val>
<p:strVal val="1+#ppt_h/2"/>
</p:val>
</p:tav>
<p:tav tm="100000">
<p:val>
<p:strVal val="#ppt_y"/>
</p:val>
</p:tav>
</p:tavLst>
</p:anim>
end example]
[Note: The W3C XML Schema definition of this element’s content model (CT_TLTimeAnimateValueList) is located
in §A.3. end note]
©ISO/IEC 2016 – All rights reserved 2677\n\n--- Page 2688 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
19.5.81 tgtEl (Target Element)
This element specifies the target children elements which have the animation effects applied to.
[Example: Consider a shape with ID 3 with a fade effect animation applied to it. The <tgtEl> element should be
used as follows:
<p:animEffect transition="in" filter="fade">
<p:cBhvr>
<p:cTn id="7" dur="2000"/>
<p:tgtEl>
<p:spTgt spid="3"/>
</p:tgtEl>
</p:cBhvr>
</p:animEffect>
end example]
[Note: The W3C XML Schema definition of this element’s content model (CT_TLTimeTargetElement) is located in
§A.3. end note]
19.5.82 tmAbs (Time Absolute)
This element describes the duration of the iteration interval in absolute time.
[Example: Consider a text animation where the words appear letter by letter every 10 seconds. The <tmAbs>
element should be used as follows:
<p:par>
<p:cTn id="5" >
<p:stCondLst> … </p:stCondLst>
<p:iterate type="lt">
<p:tmAbs val="10000"/>
</p:iterate>
<p:childTnLst> … </p:childTnLst>
</p:cTn>
</p:par>
end example]
Attributes Description
val (Time) This attribute describes an amount of time, in milliseconds.
The possible values for this attribute are defined by the ST_TLTime simple type
(§19.7.38).
2678 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2689 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
[Note: The W3C XML Schema definition of this element’s content model (CT_TLIterateIntervalTime) is located in
§A.3. end note]
19.5.83 tmPct (Time Percentage)
This element describes the duration of the iteration interval in a percentage of time.
[Example: Consider a text animation where the words appear letter by letter every 10th of the animation
duration. The <tmPct> element should be used as follows:
<p:par>
<p:cTn id="5" >
<p:stCondLst> … </p:stCondLst>
<p:iterate type="lt">
<p:tmPct val="10%"/>
</p:iterate>
<p:childTnLst> … </p:childTnLst>
</p:cTn>
</p:par>
end example]
Attributes Description
val (Value) This attribute specifies the time expressed as a percentage.
The possible values for this attribute are defined by the ST_PositivePercentage simple
type (§20.1.10.46).
[Note: The W3C XML Schema definition of this element’s content model (CT_TLIterateIntervalPercentage) is
located in §A.3. end note]
19.5.84 tmpl (Template Effects)
This element specifies the "template" effects that are used by the build element. Template effects are used in
text builds on the master slide. They define the rules of what effect should be applied to the 1st level
paragraph, 2nd level paragraph, etc.
[Example: Consider a template with a fade in effect applied to it. The <tmpl> element should be used as follows:
<p:timing>
<p:tnLst> … </p:tnLst>
<p:bldLst>
<p:bldP spid="3" grpId="0" build="p">
<p:tmplLst>
©ISO/IEC 2016 – All rights reserved 2679\n\n--- Page 2690 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
<p:tmpl lvl="1">
</p:tmpl>
</p:tmplLst>
</p:bldP>
</p:bldLst>
</p:timing>
end example]
Attributes Description
lvl (Level) This attribute describes the paragraph indent level to which this template effect applies.
The possible values for this attribute are defined by the W3C XML Schema unsignedInt
datatype.
[Note: The W3C XML Schema definition of this element’s content model (CT_TLTemplate) is located in §A.3. end
note]
19.5.85 tmplLst (Template effects)
This element describes a list of template effects that describe what kind of effects should be applied to a
paragraph level properties.
[Example: Consider a template with a fade in effect applied to it. The <tmpl> element should be used as follows:
<p:timing>
<p:tnLst> … </p:tnLst>
<p:bldLst>
<p:bldP spid="3" grpId="0" build="p">
<p:tmplLst>
<p:tmpl lvl="1">
</p:tmpl>
</p:tmplLst>
</p:bldP>
</p:bldLst>
</p:timing>
end example]
[Note: The W3C XML Schema definition of this element’s content model (CT_TLTemplateList) is located in §A.3.
end note]
19.5.86 tn (Time Node)
This element describes the time node trigger choice.
2680 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2691 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
[Example: Consider a time node with an event condition. The <tn> element should be used as follows:
<p:par>
<p:cTn id="5">
<p:stCondLst>
<p:cond delay="0"/>
</p:stCondLst>
<p:endCondLst>
<p:cond evt="begin" delay="0">
<p:tn val="5"/>
</p:cond>
</p:endCondLst>
<p:childTnLst> … </p:childTnLst>
</p:cTn>
</p:par>
end example]
Attributes Description
val (Value) This attribute specifies a time node identifier.
The possible values for this attribute are defined by the ST_TLTimeNodeID simple type
(§19.7.42).
[Note: The W3C XML Schema definition of this element’s content model (CT_TLTriggerTimeNodeID) is located in
§A.3. end note]
19.5.87 tnLst (Time Node List)
This element specifies a list of time node elements used in an animation sequence.
[Example: Consider a simple animation sequence. The <tnLst> element should be used as follows:
<p:timing>
<p:tnLst>
<p:par> … </p:par>
</p:tnLst>
</p:timing>
end example]
[Note: The W3C XML Schema definition of this element’s content model (CT_TimeNodeList) is located in §A.3.
end note]
©ISO/IEC 2016 – All rights reserved 2681\n\n--- Page 2692 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
19.5.88 to (To)
This element specifies the target location for an animation motion or animation scale effect
[Example: Consider an animation with a "light speed" entrance effect.
<p:animScale>
<p:cBhvr>
<p:cTn id="9" dur="200" decel="10.5%" autoRev="1" fill="hold">
<p:stCondLst>
<p:cond delay="600"/>
</p:stCondLst>
</p:cTn>
<p:tgtEl>
<p:spTgt spid="4"/>
</p:tgtEl>
</p:cBhvr>
<p:from x="100%" y="100%"/>
<p:to x="80%" y="100%"/>
</p:animScale>
end example]
Attributes Description
x (X coordinate) This attribute describes the X coordinate.
The possible values for this attribute are defined by the ST_Percentage simple type
(§20.1.10.40).
y (Y coordinate) This attribute describes the Y coordinate.
The possible values for this attribute are defined by the ST_Percentage simple type
(§20.1.10.40).
[Note: The W3C XML Schema definition of this element’s content model (CT_TLPoint) is located in §A.3. end
note]
19.5.89 to (To)
The element specifies the certain attribute of a time node after an animation effect.
[Example: Consider an animation effect that leaves a string value visible afterwards. The <to> element should
be used as follows:
<p:childTnLst>
<p:set>
<p:cBhvr> … </p:cBhvr>
2682 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2693 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
<p:to>
<p:strVal val="visible"/>
</p:to>
</p:set>
<p:anim calcmode="lin" valueType="num"> … </p:anim>
…</p:childTnLst>
end example]
[Note: The W3C XML Schema definition of this element’s content model (CT_TLAnimVariant) is located in §A.3.
end note]
19.5.90 to (To)
This element specifies the resulting color for the animation color change.
[Example: Consider emphasize a shape by changing its fill color from blue to red. The <to> element should be
used as follows:
<p:childTnLst>
<p:animClr clrSpc="rgb">
<p:cBhvr> … </p:cBhvr>
<p:to>
<a:schemeClr val="accent2"/>
</p:to>
</p:animClr>
</p:childTnLst>
end example]
[Note: The W3C XML Schema definition of this element’s content model (CT_Color) is located in §A.4.1. end
note]
19.5.91 txEl (Text Element)
This element specifies a text element to animate.
[Example: Consider a shape containing text to be animated. The <txEl> should be used as follows:
<p:tgtEl>
<p:spTgt spid="5">
<p:txEl>
<p:pRg st="1" end="1"/>
</p:txEl>
</p:spTgt>
</p:tgtEl>
©ISO/IEC 2016 – All rights reserved 2683\n\n--- Page 2694 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
end example]
[Note: The W3C XML Schema definition of this element’s content model (CT_TLTextTargetElement) is located in
§A.3. end note]
19.5.92 val (Value)
The element specifies a value for a time animate.
[Example: Consider a shape with a fade in animation effect. The <val> element should be used as follows:
<p:anim calcmode="lin" valueType="num">
<p:cBhvr additive="base"> … </p:cBhvr>
<p:tavLst>
<p:tav tm="0%">
<p:val>
<p:strVal val="0-#ppt_w/2"/>
</p:val>
</p:tav>
<p:tav tm="100%">
<p:val>
<p:strVal val="#ppt_x"/>
</p:val>
</p:tav>
</p:tavLst>
</p:anim>
end example]
[Note: The W3C XML Schema definition of this element’s content model (CT_TLAnimVariant) is located in §A.3.
end note]
19.5.93 video (Video)
This element specifies video information in an animation sequence. This element specifies that this node within
the animation tree triggers the playback of a video file; the actual video file used is specified by the videoFile
element (§20.1.3.6).
[Example: Consider a slide with an animated video content. The <video> element is used as follows:
<p:cSld>
<p:spTree>
<p:pic>
<p:nvPicPr>
<p:cNvPr id="4"/>
…
<p:nvPr>
2684 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2695 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
<a:videoFile r:link="rId1" contentType="video/ogg"/>
</p:nvPr>
</p:nvPicPr>
…
</p:pic>
</p:spTree>
</p:cSld>
…
<p:childTnLst>
<p:seq concurrent="1" nextAc="seek">
…
</p:seq>
<p:video>
<p:cMediaNode>
…
<p:tgtEl>
<p:spTgt spid="4"/>
</p:tgtEl>
</p:cMediaNode>
</p:video>
</p:childTnLst>
The video element specifies the location of the video playback within the animation sequence; its child spTgt
element specifies that the shape which contains the video to be played has a shape ID of 4. If we look at the
shape with that ID value, its child videoFile element references an external video file of content type video/ogg
located at the target of the relationship with ID rId1.end example]
Attributes Description
fullScrn (Full This attribute specifies if the video is displayed in full-screen.
Screen)
The possible values for this attribute are defined by the W3C XML Schema boolean
datatype.
[Note: The W3C XML Schema definition of this element’s content model (CT_TLMediaNodeVideo) is located in
§A.3. end note]
19.5.94 wedge (Wedge Slide Transition)
This element describes the wedge slide transition effect, which uses two radial edges that wipe from top to
bottom in opposite directions until the new slide is fully shown. The rendering of this transition has been shown
below.
©ISO/IEC 2016 – All rights reserved 2685\n\n--- Page 2696 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
[Example: Consider the following case in which the “wedge” slide transition is applied to a slide, along with a set
of attributes. The proper usage and a sample rendering are shown below, with the XML fragments preceding the
corresponding rendering:
<p:transition>
<p:wedge/>
</p:transition>
end example]
[Note: Any rendering shown above is for example purposes only. Exact rendering of any transition is determined
by the rendering application. As such, the same transition can have many variations depending on the
implementation. end note]
[Note: The W3C XML Schema definition of this element’s content model (CT_Empty) is located in §A.3. end
note]
19.5.95 wheel (Wheel Slide Transition)
This element describes the wheel slide transition effect, which uses a set of radial edges and wipes them in the
clockwise direction until the new slide is fully shown. The rendering of this transition depends upon the
attributes specified which have been shown below.
[Example: Consider the following cases in which the “wheel” slide transition is applied to a slide, along with a set
of attributes. The proper usage and sample renderings are shown below, with the XML fragments preceding the
corresponding rendering:
<p:transition>
<p:wheel spokes="1"/>
</p:transition>
<p:transition>
<p:wheel spokes="2"/>
</p:transition>
2686 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2697 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
<p:transition>
<p:wheel spokes="3"/>
</p:transition>
<p:transition>
<p:wheel spokes="4"/>
</p:transition>
<p:transition>
<p:wheel spokes="8"/>
</p:transition>
end example]
[Note: Any rendering shown above is for example purposes only. Exact rendering of any transition is determined
by the rendering application. As such, the same transition can have many variations depending on the
implementation. end note]
Attributes Description
spokes (Spokes) This attributes specifies the number of spokes ("pie pieces") in the wheel
The possible values for this attribute are defined by the W3C XML Schema unsignedInt
datatype.
[Note: The W3C XML Schema definition of this element’s content model (CT_WheelTransition) is located in §A.3.
end note]
©ISO/IEC 2016 – All rights reserved 2687\n\n--- Page 2698 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
19.5.96 wipe (Wipe Slide Transition)
This element describes the wipe slide transition effect, which wipes the new slide over the previous slide from
one edge of the screen to the opposite until the new slide is fully shown. The rendering of this transition
depends upon the attributes specified which have been shown below.
[Example: Consider the following cases in which the “wipe” slide transition is applied to a slide, along with a set
of attributes. The proper usage and sample renderings are shown below, with the XML fragments preceding the
corresponding rendering:
<p:transition>
<p:wipe dir="d"/>
</p:transition>
<p:transition>
<p:wipe dir="l"/>
</p:transition>
<p:transition>
<p:wipe dir="r"/>
</p:transition>
<p:transition>
<p:wipe dir="u"/>
</p:transition>
end example]
2688 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2699 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
[Note: Any rendering shown above is for example purposes only. Exact rendering of any transition is determined
by the rendering application. As such, the same transition can have many variations depending on the
implementation. end note]
Attributes Description
dir (Direction) This attribute specifies the direction of the slide transition.
The possible values for this attribute are defined by the
ST_TransitionSideDirectionType simple type (§19.7.53).
[Note: The W3C XML Schema definition of this element’s content model (CT_SideDirectionTransition) is located
in §A.3. end note]
19.5.97 zoom (Zoom Slide Transition)
This element describes the zoom slide transition effect, which uses a box pattern centered on the slide that
increases in size until the new slide is fully shown. The rendering of this transition depends upon the attributes
specified which have been shown below.
[Example: Consider the following cases in which the “zoom” slide transition is applied to a slide, along with a set
of attributes. The proper usage and sample renderings are shown below, with the XML fragments preceding the
corresponding rendering:
<p:transition>
<p:zoom dir="in"/>
</p:transition>
<p:transition>
<p:zoom dir="out"/>
</p:transition>
end example]
[Note: Any rendering shown above is for example purposes only. Exact rendering of any transition is determined
by the rendering application. As such, the same transition can have many variations depending on the
implementation. end note]
©ISO/IEC 2016 – All rights reserved 2689\n\n--- Page 2700 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
dir (Direction) This attribute specifies the direction of an "in/out" slide transition.
The possible values for this attribute are defined by the
ST_TransitionInOutDirectionType simple type (§19.7.52).
[Note: The W3C XML Schema definition of this element’s content model (CT_InOutTransition) is located in §A.3.
end note]
19.6 Slide Synchronization Data
It is often the case that slides are repurposed from existing presentations to be used in other presentations. In
such cases, it is often beneficial for there to be an association, or a pairing, between the original slide and all
copied instances of it. In the presence of such a pairing, applications can enable a variety of time-saving
features, including the automatic updates of copied slides when the original slide changes. The Slide
Synchronization Data part is designed to enable such application-defined functionality.
This information is stored in the Slide Synchronization Data part, which is referenced via an implicit relationship
from the associated Slide part.
19.6.1 sldSyncPr (Slide Synchronization Properties)
This element specifies the information needed to associate the original slide with all copied instances of it.
Attributes Description
clientInsertedTime The date and time that the original slide was last updated in the current presentation.
(Client Slide
Insertion date/time) The date/time is stored in ISO 8601 format.
[Note: This value can be used to inform the user of when the last synchronization was, as
well as to determine when to next check for an updated version. end note]
The possible values for this attribute are defined by the W3C XML Schema dateTime
datatype.
serverSldId A string that, when paired with the target of the Slide Synchronization Data part’s
(Server's Slide File external relationship, uniquely identifies the original slide.
ID)
The possible values for this attribute are defined by the W3C XML Schema string
datatype.
serverSldModified The date and time that the original slide was last modified in its location as defined by
Time (Server's Slide the target of the Slide Synchronization Data part’s external relationship.
File's modification
2690 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2701 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Attributes Description
date/time)
The date and time are stored in ISO 8601 format.
The possible values for this attribute are defined by the W3C XML Schema dateTime
datatype.
[Note: The W3C XML Schema definition of this element’s content model (CT_SlideSyncProperties) is located in
§A.3. end note]
19.7 Simple Types
This is the complete list of simple types dedicated to PresentationML.
19.7.1 ST_BookmarkIdSeed (Bookmark ID Seed)
This simple type specifies constraints for value of the Bookmark ID seed.
This simple type's contents are a restriction of the W3C XML Schema unsignedInt datatype.
This simple type also specifies the following restrictions:
 This simple type has a minimum value of greater than or equal to 1.
 This simple type has a maximum value of less than 2147483648.
[Note: The W3C XML Schema definition of this simple type’s content model (ST_BookmarkIdSeed) is located in
§A.3. end note]
19.7.2 ST_Direction (Direction)
This simple type defines a direction of either horizontal or vertical.
This simple type's contents are a restriction of the W3C XML Schema token datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
horz (Horizontal) Defines a horizontal direction.
vert (Vertical) Defines a vertical direction.
[Note: The W3C XML Schema definition of this simple type’s content model (ST_Direction) is located in §A.3. end
note]
19.7.3 ST_Index (Index)
This simple type defines the position of an object in an ordered list.
©ISO/IEC 2016 – All rights reserved 2691\n\n--- Page 2702 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
This simple type's contents are a restriction of the W3C XML Schema unsignedInt datatype.
[Note: The W3C XML Schema definition of this simple type’s content model (ST_Index) is located in §A.3. end
note]
19.7.4 ST_IterateType (Iterate Type)
This simple type specifies how the animation is applied over subelements of the target element.
This simple type's contents are a restriction of the W3C XML Schema token datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
el (Element) Iterate by element.
lt (Letter) Iterate by Letter.
wd (Word) Iterate by Word.
[Note: The W3C XML Schema definition of this simple type’s content model (ST_IterateType) is located in §A.3.
end note]
19.7.5 ST_Name (Name string)
This simple type specifies a name, such as for a comment author or custom show.
This simple type's contents are a restriction of the W3C XML Schema string datatype.
[Note: The W3C XML Schema definition of this simple type’s content model (ST_Name) is located in §A.3. end
note]
19.7.6 ST_OleObjectFollowColorScheme (Embedded object to Follow Color
Scheme)
This simple type determines if the Embedded object is re-colored to reflect changes to the color schemes.
This simple type's contents are a restriction of the W3C XML Schema token datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
full (Full) Setting this enumeration causes the Embedded object
to respond to all changes in the color scheme in the
presentation.
none (None) Setting this enumeration causes the Embedded object
to not respond to changes in the color scheme in the
presentation.
textAndBackground (Text and Background) Setting this enumeration causes the Embedded object
2692 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2703 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
to respond only to changes in the text and background
colors of the color scheme in the presentation.
[Note: The W3C XML Schema definition of this simple type’s content model (ST_OleObjectFollowColorScheme) is
located in §A.3. end note]
19.7.7 ST_PhotoAlbumFrameShape (Photo Album Shape for Photo Mask)
This simple type specifies the values for photo frame types within a photo album presentation.
This simple type's contents are a restriction of the W3C XML Schema token datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
frameStyle1 (Rectangle Photo Frame)
frameStyle2 (Rounded Rectangle Photo Frame)
frameStyle3 (Simple White Photo Frame)
frameStyle4 (Simple Black Photo Frame)
frameStyle5 (Compound Black Photo Frame)
frameStyle6 (Center Shadow Photo Frame)
frameStyle7 (Soft Edge Photo Frame)
©ISO/IEC 2016 – All rights reserved 2693\n\n--- Page 2704 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
[Note: The W3C XML Schema definition of this simple type’s content model (ST_PhotoAlbumFrameShape) is
located in §A.3. end note]
19.7.8 ST_PhotoAlbumLayout (Photo Album Layout Definition)
This simple type specifies the values for photo layouts within a photo album presentation.
This simple type's contents are a restriction of the W3C XML Schema token datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
1pic (1 Photo per Slide)
Specifies that photo album slides should have a single
picture, centered horizontally and vertically, on the
slide with no title.
1picTitle (1 Photo per Slide with Titles)
Specifies that photo album slides should have a single
picture and a single title text box, centered
horizontally and vertically, on the slide.
2pic (2 Photos per Slide)
Specifies that photo album slides should have two
pictures of the same size, positioned side-by-side,
centered horizontally and vertically, on the slide with
no title.
2picTitle (2 Photos per Slide with Titles)
Specifies that photo album slides should have two
pictures of the same size, positioned side-by-side, with
a single title text box centered over them, collectively
centered horizontally and vertically, on the slide.
4pic (4 Photos per Slide)
Specifies that photo album slides should have four
pictures of the same size, positioned in a two-by-two
2694 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2705 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
matrix, centered horizontally and vertically, on the
slide with no title.
4picTitle (4 Photos per Slide with Titles)
Specifies that photo album slides should have four
pictures of the same size, positioned in a two-by-two
matrix, with a single title text box centered over the
matrix, centered horizontally and vertically, on the
slide.
fitToSlide (Fit Photos to Slide)
Specifies that photo album slides should have a single
picture, stretched to fit the entire slide size, with no
title.
[Note: The W3C XML Schema definition of this simple type’s content model (ST_PhotoAlbumLayout) is located in
§A.3. end note]
19.7.9 ST_PlaceholderSize (Placeholder Size)
This simple type facilitates the storing of the size of the placeholder. This size is described relative to the body
placeholder on the master.
This simple type's contents are a restriction of the W3C XML Schema token datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
full (Full) Specifies that the placeholder should take the full size
of the body placeholder on the master.
half (Half) Specifies that the placeholder should take the half size
of the body placeholder on the master. Half size
vertically or horizontally? Needs a picture.
quarter (Quarter) Specifies that the placeholder should take a quarter of
the size of the body placeholder on the master. Picture
would be helpful
[Note: The W3C XML Schema definition of this simple type’s content model (ST_PlaceholderSize) is located in
§A.3. end note]
©ISO/IEC 2016 – All rights reserved 2695\n\n--- Page 2706 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
19.7.10 ST_PlaceholderType (Placeholder IDs)
This simple type facilitates the storing of the content type a placeholder should contain.
[Note: Some placeholder types are not allowed for all SlideBase types. end note]
This simple type's contents are a restriction of the W3C XML Schema token datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
body (Body) Contains body text. Allowed for Slide, Slide Layout,
Slide Master, Notes, Notes Master. Can be horizontal
or vertical on Slide and Slide Layout.
chart (Chart) Contains a chart or graph. Special type. Allowed for
Slide and Slide Layout.
clipArt (Clip Art) Contains a single clip art image. Special type. Allowed
for Slide and Slide Layout.
ctrTitle (Centered Title) Contains a title intended to be centered on the slide.
Allowed for Slide and Slide Layout.
dgm (Diagram) Contains a diagram. Special type. Allowed for Slide and
Slide Layout.
dt (Date and Time) Contains the date and time. Allowed for Slide, Slide
Layout, Slide Master, Notes, Notes Master, Handout
Master
ftr (Footer) Contains text to be used as a footer in the document.
Allowed for Slide, Slide Layout, Slide Master, Notes,
Notes Master, Handout Master
hdr (Header) Contains text to be used as a header for the
document. Allowed for Notes, Notes Master, Handout
Master .
media (Media) Contains multimedia content such as audio or a movie
clip. Special type. Allowed for Slide and Slide Layout.
obj (Object) Contains any content type. Special type. Allowed for
Slide and Slide Layout.
pic (Picture) Contains a picture. Special type. Allowed for Slide and
Slide Layout.
sldImg (Slide Image) Contains an image of the slide. Allowed for Notes and
Notes Master.
sldNum (Slide Number) Contains the number of a slide. Allowed for Slide, Slide
Layout, Slide Master, Notes, Notes Master, Handout
Master
subTitle (Subtitle) Contains a subtitle. Allowed for Slide and Slide Layout.
2696 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2707 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
tbl (Table) Contains a table. Special type. Allowed for Slide and
Slide Layout.
title (Title) Contains a slide title. Allowed for Slide, Slide Layout
and Slide Master. Can be horizontal or vertical on Slide
and Slide Layout.
[Note: The W3C XML Schema definition of this simple type’s content model (ST_PlaceholderType) is located in
§A.3. end note]
19.7.11 ST_PrintColorMode (Print Color Mode)
This simple type specifies the color mode that should be used when printing a presentation document.
This simple type's contents are a restriction of the W3C XML Schema token datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
bw (Black and White Mode) Print should be in Black and White only
clr (Color Mode) Print should be in Full Color
gray (Grayscale Mode) Print should be in Grayscale only
[Note: The W3C XML Schema definition of this simple type’s content model (ST_PrintColorMode) is located in
§A.3. end note]
19.7.12 ST_PrintWhat (Default print output)
This simple type specifies the default print layout that should be used when printing
This simple type's contents are a restriction of the W3C XML Schema token datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
handouts1 (1 Slide / Handout Page) 1 Slide and Handout Page layout should be used.
handouts2 (2 Slides / Handout Page) 2 Slides and Handout Page layout should be used.
handouts3 (3 Slides / Handout Page) 3 Slides and Handout Page layout should be used.
handouts4 (4 Slides / Handout Page) 4 Slides and Handout Page layout should be used.
handouts6 (6 Slides / Handout Page) 6 Slides and Handout Page layout should be used.
handouts9 (9 Slides / Handout Page) 9 Slides and Handout Page layout should be used.
notes (Notes) Notes layout should be used.
outline (Outline) Outline layout should be used.
©ISO/IEC 2016 – All rights reserved 2697\n\n--- Page 2708 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
slides (Slides) Slides layout should be used.
[Note: The W3C XML Schema definition of this simple type’s content model (ST_PrintWhat) is located in §A.3.
end note]
19.7.13 ST_SlideId (Slide Identifier)
This simple type specifies the allowed numbering for the slide identifier.
This simple type's contents are a restriction of the W3C XML Schema unsignedInt datatype.
This simple type also specifies the following restrictions:
 This simple type has a maximum value of less than 2147483648.
 This simple type has a minimum value of greater than or equal to 256.
[Note: The W3C XML Schema definition of this simple type’s content model (ST_SlideId) is located in §A.3. end
note]
19.7.14 ST_SlideLayoutId (Slide Layout ID)
This simple type sets the bounds for the slide layout id value. This layout id is used to identify the different slide
layout designs.
This simple type's contents are a restriction of the W3C XML Schema unsignedInt datatype.
This simple type also specifies the following restrictions:
 This simple type has a minimum value of greater than or equal to 2147483648.
[Note: The W3C XML Schema definition of this simple type’s content model (ST_SlideLayoutId) is located in §A.3.
end note]
19.7.15 ST_SlideLayoutType (Slide Layout Type)
This simple type defines an arrangement of content on a slide. Each layout type is not tied to an exact
positioning of placeholders, but rather provides a higher-level description of the content type and positioning of
placeholders. This information can be used by the application to aid in mapping between different layouts. The
application can choose which, if any, of these layouts to make available through its user interface.
Each layout contains zero or more placeholders, each with a specific content type. An "object" placeholder can
contain any kind of data. Media placeholders are intended to hold video or audio clips. The enumeration value
descriptions include illustrations of sample layouts for each value of the simple type.
This simple type's contents are a restriction of the W3C XML Schema token datatype.
2698 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2709 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
blank (Slide Layout Type Enumeration ( Blank )) Blank
chart (Chart) Title and chart
chartAndTx (Slide Layout Type Enumeration ( Chart Title, chart on left and text on right
and Text ))
clipArtAndTx (Clip Art and Text) Title, clipart on left, text on right
clipArtAndVertTx (Clip Art and Vertical Text) Title, clip art on left, vertical text on
right
cust (Slide Layout Type Enumeration ( Custom )) Custom layout defined by user
dgm (Slide Layout Type Enumeration ( Diagram )) Title and diagram
fourObj (Four Objects) Title and four objects
mediaAndTx (Slide Layout Type Enumeration ( Media Title, media on left, text on right
and Text ))
obj (Title and Object) Title and object
objAndTwoObj (Object and Two Object) Title, one object on left, two objects on
right
objAndTx (Slide Layout Type Enumeration ( Object Title, object on left, text on right
and Text ))
objOnly (Object) Object only
©ISO/IEC 2016 – All rights reserved 2699\n\n--- Page 2710 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
objOverTx (Slide Layout Type Enumeration ( Object Title, object on top, text on bottom
over Text))
objTx (Title, Object, and Caption) Title, object and caption text
picTx (Picture and Caption) Title, picture, and caption text
secHead (Section Header) Section header title and subtitle text
tbl (Slide Layout Type Enumeration ( Table )) Title and table
title (Slide Layout Type Enumeration ( Title )) Title layout with centered title and
subtitle placeholders
titleOnly (Slide Layout Type Enumeration ( Title Only )) Title only
twoColTx (Slide Layout Type Enumeration ( Two Title, text on left, text on right
Column Text ))
twoObj (Two Objects) Title, object on left, object on right
twoObjAndObj (Two Objects and Object) Title, two objects on left, one object on
right
twoObjAndTx (Two Objects and Text) Title, two objects on left, text on right
twoObjOverTx (Two Objects over Text) Title, two objects on top, text on bottom
2700 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2711 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
twoTxTwoObj (Two Text and Two Objects) Title, two objects each with text
tx (Slide Layout Type Enumeration ( Text )) Title and text
txAndChart (Slide Layout Type Enumeration ( Text and Title, text on left and chart on right
Chart ))
txAndClipArt (Text and Clip Art) Title, text on left, clip art on right
txAndMedia (Slide Layout Type Enumeration ( Text Title, text on left, media on right
and Media ))
txAndObj (Slide Layout Type Enumeration ( Text and Title, text on left, object on right
Object ))
txAndTwoObj (Text and Two Objects) Title, text on left, two objects on right
txOverObj (Slide Layout Type Enumeration ( Text over Title, text on top, object on bottom
Object))
vertTitleAndTx (Vertical Title and Text) Vertical title on right, vertical text on left
vertTitleAndTxOverChart (Vertical Title and Text Vertical title on right, vertical text on
Over Chart) top, chart on bottom
vertTx (Vertical Text) Title and vertical text body
[Note: The W3C XML Schema definition of this simple type’s content model (ST_SlideLayoutType) is located in
§A.3. end note]
©ISO/IEC 2016 – All rights reserved 2701\n\n--- Page 2712 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
19.7.16 ST_SlideMasterId (Slide Master ID)
This simple type specifies the allowed numbering for the slide master identifier.
This simple type's contents are a restriction of the W3C XML Schema unsignedInt datatype.
This simple type also specifies the following restrictions:
 This simple type has a minimum value of greater than or equal to 2147483648.
[Note: The W3C XML Schema definition of this simple type’s content model (ST_SlideMasterId) is located in
§A.3. end note]
19.7.17 ST_SlideSizeCoordinate (Slide Size Coordinate)
This simple type specifies the slide size coordinate in EMUs (English Metric Units).
This simple type's contents are a restriction of the ST_PositiveCoordinate32 datatype (§20.1.10.43).
This simple type also specifies the following restrictions:
 This simple type has a maximum value of less than or equal to 51206400.
 This simple type has a minimum value of greater than or equal to 914400.
[Note: The W3C XML Schema definition of this simple type’s content model (ST_SlideSizeCoordinate) is located
in §A.3. end note]
19.7.18 ST_SlideSizeType (Slide Size Type)
This simple type specifies the kind of slide size that the slide should be optimized for.
This simple type's contents are a restriction of the W3C XML Schema token datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
35mm (35mm Film) Slide size should be optimized for 35mm film output
A3 (A3) Slide size should be optimized for A3 output
A4 (A4) Slide size should be optimized for A4 output
B4ISO (B4ISO) Slide size should be optimized for B4ISO output
B4JIS (B4JIS) Slide size should be optimized for B4JIS output
B5ISO (B5ISO) Slide size should be optimized for B5ISO output
B5JIS (B5JIS) Slide size should be optimized for B5JIS output
banner (Banner) Slide size should be optimized for banner output
custom (Custom) Slide size should be optimized for custom output
hagakiCard (Hagaki Card) Slide size should be optimized for hagaki card output
2702 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2713 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
ledger (Ledger) Slide size should be optimized for ledger output
letter (Letter) Slide size should be optimized for letter output
overhead (Overhead) Slide size should be optimized for overhead output
screen16x10 (Screen 16x10) Slide size should be optimized for 16x10 screen output
screen16x9 (Screen 16x9) Slide size should be optimized for 16x9 screen output
screen4x3 (Screen 4x3) Slide size should be optimized for 4x3 screen output
[Note: The W3C XML Schema definition of this simple type’s content model (ST_SlideSizeType) is located in §A.3.
end note]
19.7.19 ST_SplitterBarState (Splitter Bar State)
This simple type specifies the state that the splitter bar should be shown in. The splitter bar separates a primary
and secondary region within a viewing area.
This simple type's contents are a restriction of the W3C XML Schema token datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
maximized (Max) The primary region occupies the greatest amount of
the viewing area allowed by the application.
minimized (Min) The primary region occupies the least amount of the
viewing area allowed by the application.
restored (Restored) The primary region has a specific intermediate size.
[Note: The W3C XML Schema definition of this simple type’s content model (ST_SplitterBarState) is located in
§A.3. end note]
19.7.20 ST_TLAnimateBehaviorCalcMode (Time List Animate Behavior Calculate
Mode)
This simple type specifies how the animation flows from point to point.
This simple type's contents are a restriction of the W3C XML Schema token datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
discrete (Calc Mode Enum ( Discrete )) Descrete
fmla (Calc Mode Enum ( Formula )) Formula
lin (Calc Mode Enum ( Linear )) Linear
©ISO/IEC 2016 – All rights reserved 2703\n\n--- Page 2714 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
[Note: The W3C XML Schema definition of this simple type’s content model (ST_TLAnimateBehaviorCalcMode) is
located in §A.3. end note]
19.7.21 ST_TLAnimateBehaviorValueType (Time List Animate Behavior Value
Types)
This simple type specifies the type of property value.
This simple type's contents are a restriction of the W3C XML Schema token datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
clr (Value Type Enum ( Color )) Color
num (Value Type Enum ( Number )) Number
str (Value Type Enum ( String )) String
[Note: The W3C XML Schema definition of this simple type’s content model (ST_TLAnimateBehaviorValueType)
is located in §A.3. end note]
19.7.22 ST_TLAnimateColorDirection (Time List Animate Color Direction)
This simple type specifies the direction in which to interpolate the animation (clockwise or counterclockwise).
This simple type's contents are a restriction of the W3C XML Schema token datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
ccw (Counter-Clockwise) Counter-Clockwise
cw (Direction Enum ( Clockwise )) Clockwise
[Note: The W3C XML Schema definition of this simple type’s content model (ST_TLAnimateColorDirection) is
located in §A.3. end note]
19.7.23 ST_TLAnimateColorSpace (Time List Animate Color Space)
This simple type specifies the color space of the animation.
This simple type's contents are a restriction of the W3C XML Schema token datatype.
2704 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2715 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
hsl (Color Space Enum ( HSL )) Hue, Saturation, Luminance
rgb (Color Space Enum ( RGB )) Red, Green, Blue
[Note: The W3C XML Schema definition of this simple type’s content model (ST_TLAnimateColorSpace) is
located in §A.3. end note]
19.7.24 ST_TLAnimateEffectTransition (Time List Animate Effect Transition)
This simple type specifies whether the effect is a transition in, transition out, or neither.
This simple type's contents are a restriction of the W3C XML Schema token datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
in (Transition Enum ( In )) In
none (Transition Enum ( None )) None
out (Transition Enum ( Out )) Out
[Note: The W3C XML Schema definition of this simple type’s content model (ST_TLAnimateEffectTransition) is
located in §A.3. end note]
19.7.25 ST_TLAnimateMotionBehaviorOrigin (Time List Animate Motion Behavior
Origin)
This simple type specifies what the origin of the motion path is relative to.
This simple type's contents are a restriction of the W3C XML Schema token datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
layout (Origin Enum ( Layout )) Layout
parent (Origin Enum ( Parent )) Parent
[Note: The W3C XML Schema definition of this simple type’s content model
(ST_TLAnimateMotionBehaviorOrigin) is located in §A.3. end note]
19.7.26 ST_TLAnimateMotionPathEditMode (Time List Animate Motion Path Edit
Mode)
This simple type specifies how the motion path moves when the target element is moved.
©ISO/IEC 2016 – All rights reserved 2705\n\n--- Page 2716 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
This simple type's contents are a restriction of the W3C XML Schema token datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
fixed (Path Edit Mode Enum ( Fixed )) Fixed
relative (Path Edit Mode Enum ( Relative )) Relative
[Note: The W3C XML Schema definition of this simple type’s content model
(ST_TLAnimateMotionPathEditMode) is located in §A.3. end note]
19.7.27 ST_TLBehaviorAccumulateType (Behavior Accumulate Type)
This simple type makes a repeating animation build with each iteration when set to "always."
This simple type's contents are a restriction of the W3C XML Schema token datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
always (Accumulate Enum ( Always )) Always
none (Accumulate Enum ( None )) None
[Note: The W3C XML Schema definition of this simple type’s content model (ST_TLBehaviorAccumulateType) is
located in §A.3. end note]
19.7.28 ST_TLBehaviorAdditiveType (Behavior Additive Type)
This simple type specifies how to apply the animation values to the original value for the property.
This simple type's contents are a restriction of the W3C XML Schema token datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
base (Additive Enum ( Base )) Base
mult (Additive Enum ( Multiply )) Multiply
none (None) None
repl (Additive Enum ( Replace )) Replace
sum (Additive Enum ( Sum )) Sum
[Note: The W3C XML Schema definition of this simple type’s content model (ST_TLBehaviorAdditiveType) is
located in §A.3. end note]
2706 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2717 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
19.7.29 ST_TLBehaviorOverrideType (Behavior Override Type)
This simple type specifies how a behavior should override values of the attribute being animated on the target
element. The "childStyle" clears the attributes on the children contained inside the target element.
This simple type's contents are a restriction of the W3C XML Schema token datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
childStyle (Override Enum ( Child Style )) Child Style
normal (Override Enum ( Normal )) Normal
[Note: The W3C XML Schema definition of this simple type’s content model (ST_TLBehaviorOverrideType) is
located in §A.3. end note]
19.7.30 ST_TLBehaviorTransformType (Behavior Transform Type)
This simple type specifies how the behavior animates the target element.
This simple type's contents are a restriction of the W3C XML Schema token datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
img (Image) Image transform
pt (Point) Point transform
[Note: The W3C XML Schema definition of this simple type’s content model (ST_TLBehaviorTransformType) is
located in §A.3. end note]
19.7.31 ST_TLChartSubelementType (Chart Subelement Type)
This simple type defines an animation target element that is represented by a subelement of a chart.
This simple type's contents are a restriction of the W3C XML Schema token datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
category (Category Axis) Category
gridLegend (Grid Legend) Background Element (Grid and Legend)
ptInCategory (Single Point in Category) Category Element
ptInSeries (Single Point in Data Series) Series Element
series (Data Series) Series
©ISO/IEC 2016 – All rights reserved 2707\n\n--- Page 2718 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
[Note: The W3C XML Schema definition of this simple type’s content model (ST_TLChartSubelementType) is
located in §A.3. end note]
19.7.32 ST_TLCommandType (Command Type)
This simple type specifies a command type.
This simple type's contents are a restriction of the W3C XML Schema token datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
call (Command Type Enum ( Call )) Call
evt (Command Type Enum ( Event )) Event
verb (Command Type Enum ( Verb )) Verb
[Note: The W3C XML Schema definition of this simple type’s content model (ST_TLCommandType) is located in
§A.3. end note]
19.7.33 ST_TLDiagramBuildType (Diagram Build Types)
This simple type specifies the different diagram build types.
This simple type's contents are a restriction of the W3C XML Schema token datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
allAtOnce (Diagram Build Type Enum ( All At Once )) All At Once
breadthByLvl (Diagram Build Type Enum ( Breadth By Breadth By Level
Level ))
breadthByNode (Diagram Build Type Enum ( Breadth Breadth By Node
By Node ))
ccw (Diagram Build Type Enum ( Counter-Clockwise )) Counter-Clockwise
ccwIn (Diagram Build Type Enum ( Counter-Clockwise- Counter-Clockwise-In
In ))
ccwOut (Diagram Build Type Enum ( Counter- Counter-Clockwise-Out
Clockwise-Out ))
cust (Diagram Build Type Enum ( Custom )) Custom
cw (Diagram Build Type Enum ( Clockwise )) Clockwise
cwIn (Diagram Build Type Enum ( Clockwise-In )) Clockwise-In
cwOut (Diagram Build Type Enum ( Clockwise-Out )) Clockwise-Out
2708 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 2719 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Enumeration Value Description
depthByBranch (Diagram Build Type Enum ( Depth By Depth By Branch
Branch ))
depthByNode (Diagram Build Type Enum ( Depth By Depth By Node
Node ))
down (Diagram Build Type Enum ( Down )) Down
inByRing (Diagram Build Type Enum ( In-By-Ring )) In-By-Ring
outByRing (Diagram Build Type Enum ( Out-By-Ring )) Out-By-Ring
up (Diagram Build Type Enum ( Up )) Up
whole (Diagram Build Type Enum ( Whole )) Whole
[Note: The W3C XML Schema definition of this simple type’s content model (ST_TLDiagramBuildType) is located
in §A.3. end note]
19.7.34 ST_TLNextActionType (Next Action Type)
This simple type specifies what to do when going forward in a sequence. When the value is "seek," it seeks the
current child element to its natural end time before advancing to the next element.
This simple type's contents are a restriction of the W3C XML Schema token datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
none (Next Action Type Enum ( None )) None
seek (Next Action Type Enum ( Seek )) Seek
[Note: The W3C XML Schema definition of this simple type’s content model (ST_TLNextActionType) is located in
§A.3. end note]
19.7.35 ST_TLOleChartBuildType (Embedded Chart Build Type)
This simple type describes how to build an embedded Chart.
This simple type's contents are a restriction of the W3C XML Schema token datatype.
This simple type is restricted to the values listed in the following table:
Enumeration Value Description
allAtOnce (Chart Build Type Enum ( All At Once )) All At Once
category (Chart Build Type Enum ( Category )) By Category
categoryEl (Chart Build Type Enum ( Category Element By Category Element
))
©ISO/IEC 2016 – All rights reserved 2709\n