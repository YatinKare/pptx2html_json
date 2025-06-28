\n--- Page 100 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
12.3.16 Shared Workbook Revision Headers Part
Content Type: application/vnd.openxmlformats-officedocument.spreadsheetml.revisionHeaders+xml
Root http://purl.oclc.org/ooxml/spreadsheetml/main
Namespace:
Source http://purl.oclc.org/ooxml/officeDocument/relationships/revisionHeaders
Relationship:
An instance of this part type contains information about each of the editing sessions performed on the parent
workbook at the worksheet level (worksheets added and rearranged in each session).
A package shall contain at most one Shared Workbook Revision Headers part. If it exists, that part shall be the
target of an implicit relationship from the Workbook (§12.3.23) part.
[Example: The following Workbook part-relationship item contains a relationship to the Shared Workbook
Revision Headers part, which is stored in the ZIP item handout revisions/revisionHeaders.xml:
<Relationships xmlns="…">
<Relationship Id="rId9"
Type="http://…/revisionHeaders"
Target="revisions/revisionHeaders.xml"/>
</Relationships>
end example]
The root element for a part of this content type shall be headers.
[Example: revisionHeaders.xml contains the following:
<headers xmlns:r="…" guid="{233BEE23-EB5C-4542-905D-0230EFFED88B}"
diskRevisions="1" revisionId="4" version="3">
<header guid="…" dateTime="…" maxSheetId="4" userName="…" r:id="rId1">
<sheetIdMap count="3">
…
</sheetIdMap>
</header>
…
<header guid="…" dateTime="…" maxSheetId="4" userName="…" r:id="rId3">
<sheetIdMap count="3">
…
</sheetIdMap>
</header>
</headers>
end example]
90 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 101 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
A Shared Workbook Revision Headers part shall be located within the package containing the relationships part
(expressed syntactically, the TargetMode attribute of the Relationship element shall be Internal).
A Shared Workbook Revision Headers part is permitted to have explicit relationships to the following parts
defined by ISO/IEC 29500:
 Shared Workbook Revision Log (§12.3.17)
A Shared Workbook Revision Headers part shall not have any implicit or explicit relationships to other parts
defined by ISO/IEC 29500.
12.3.17 Shared Workbook Revision Log Part
Content Type: application/vnd.openxmlformats-officedocument.spreadsheetml.revisionLog+xml
Root http://purl.oclc.org/ooxml/spreadsheetml/main
Namespace:
Source http://purl.oclc.org/ooxml/officeDocument/relationships/revisionLog
Relationship:
An instance of this part type contains information about edits performed on individual cells in the parent
workbook’s worksheets in each editing session.
A package shall contain one Shared Workbook Revision Log part for each session's set of changes, and those
parts shall be the target of an explicit relationship from the Shared Workbook Revision Headers (§12.3.16) part.
[Example: The following Shared Workbook Revision Headers part-relationship item contains a number of
relationships to Shared Workbook Revision Log parts, which are stored in the ZIP item revisionLogN.xml:
<Relationships xmlns="…">
<Relationship Id="rId1"
Type="http://…/revisionLog" Target="revisionLog1.xml"/>
…
<Relationship Id="rId6"
Type="http://…/revisionLog" Target="revisionLog6.xml"/>
</Relationships>
end example]
The root element for a part of this content type shall be revisions.
[Example: revisionLog2.xml contains the following:
©ISO/IEC 2016 – All rights reserved 91\n\n--- Page 102 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
<revisions xmlns:xs="…" …>
<rfmt sheetId="1" sqref="B4:B15">
<dxf>
<xs:fill>
<xs:pattern patternType="solid">
<xs:fgColor type="icv" val="64"/>
<xs:bgColor type="rgb" val="4278252287"/>
</xs:pattern>
</xs:fill>
</dxf>
</rfmt>
<rcv guid="{CBCE5672-5A4D-48C9-A120-F72804F8CF64}" action="delete"/>
<rcv guid="{CBCE5672-5A4D-48C9-A120-F72804F8CF64}" action="add"/>
</revisions>
end example]
A Shared Workbook Revision Log part shall be located within the package containing the relationships part
(expressed syntactically, the TargetMode attribute of the Relationship element shall be Internal).
A Shared Workbook Revision Log part shall not have implicit or explicit relationships to any other part defined by
ISO/IEC 29500.
12.3.18 Shared Workbook User Data Part
Content Type: application/vnd.openxmlformats-officedocument.spreadsheetml.userNames+xml
Root http://purl.oclc.org/ooxml/spreadsheetml/main
Namespace:
Source http://purl.oclc.org/ooxml/officeDocument/relationships/usernames
Relationship:
An instance of this part type contains a list of all the users that are sharing the parent workbook.
A package shall contain at most one Shared Workbook User Data part, and that part shall be the target of an
implicit relationship in the Workbook (§12.3.23) part.
[Example: The following Workbook part-relationship item contains a relationship to the Shared Workbook User
Data part, which is stored in the ZIP item revisions/userNames.xml:
<Relationships xmlns="…">
Relationship Id="rId8"
Type="http://…/usernames" Target="revisions/userNames.xml"/>
</Relationships>
end example]
92 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 103 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
The root element for a part of this content type shall be users.
[Example: userNames.xml shows that there are two users sharing this workbook:
<users … count="2">
<usrinfo guid="{B5A024F7-40BE-4A48-9B6D-B1655241C84D}"
name="Mary Jones" id="-264292310" dateTime="2005-11-18T18:53:16"/>
<usrinfo …/>
</users>
end example]
A Shared Workbook User Data part shall be located within the package containing the relationships part
(expressed syntactically, the TargetMode attribute of the Relationship element shall be Internal).
A Shared Workbook User Data part shall not have implicit or explicit relationships to any other part defined by
ISO/IEC 29500.
12.3.19 Single Cell Table Definitions Part
Content Type: application/vnd.openxmlformats-officedocument.spreadsheetml.tableSingleCells+xml
Root http://purl.oclc.org/ooxml/spreadsheetml/main
Namespace:
Source http://purl.oclc.org/ooxml/officeDocument/relationships/tableSingleCells
Relationship:
An instance of this part type contains information on how to map non-repeating elements from a custom XML
file into cells in a worksheet. [Note: Repeating custom XML elements are mapped using a Table (§12.3.21). end
note]
A package shall contain at most one Single Cell Table Definitions part per worksheet, and that part shall be the
target of an implicit relationship from a Worksheet (§12.3.24) part. A Single Cell Table Definitions part can
describe one or more single cell table definitions for any given worksheet.
[Example: The following Worksheet part-relationship item contains a relationship to the Single Cell Table
Definitions part, which is stored in the ZIP item ../tables/tableSingleCells1.xml:
<Relationships xmlns="…">
<Relationship Id="rId1"
Type="http://…/tableSingleCells"
Target="../tables/tableSingleCells1.xml"/>
</Relationships>
end example]
The root element for a part of this content type shall be singleXmlCells.
©ISO/IEC 2016 – All rights reserved 93\n\n--- Page 104 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
[Example: A worksheet contains two single cell table definitions; e.g., ../tables/tableSingleCells1.xml contains
the following, where the elements id and count are nested inside element names:
<singleXmlCells …>
<singleCell id="1" name="Table1" displayName="Table1" ref="B4">
<cellPr id="1" uniqueName="id">
<xmlPr mapId="1" xpath="/names/id" xmlDataType="string"/>
</cellPr>
</singleCell>
<singleCell id="2" name="Table2" displayName="Table2" ref="B7">
<cellPr id="1" uniqueName="count">
<xmlPr mapId="1" xpath="/names/count" xmlDataType="integer"/>
</cellPr>
</singleCell>
</singleXmlCells>
end example]
A Single Cell Table Definitions part shall be located within the package containing the relationships part
(expressed syntactically, the TargetMode attribute of the Relationship element shall be Internal).
A Single Cell Table Definitions part shall not have implicit or explicit relationships to any other part defined by
ISO/IEC 29500.
12.3.20 Styles Part
Content Type: application/vnd.openxmlformats-officedocument.spreadsheetml.styles+xml
Root http://purl.oclc.org/ooxml/spreadsheetml/main
Namespace:
Source http://purl.oclc.org/ooxml/officeDocument/relationships/styles
Relationship:
An instance of this part type contains all the characteristics for all the cells in the workbook. Such information
includes numeric and text formatting, alignment, font, color, and border.
A package shall contain no more than one Styles part, and that part shall be the target of an implicit relationship
from the Workbook (§12.3.23) part.
[Example: The following Workbook part-relationship item contains a relationship to the Styles part, which is
stored in the ZIP item styles.xml:
<Relationships xmlns="…">
<Relationship Id="rId5"
Type="http://…/styles" Target="styles.xml"/>
</Relationships>
94 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 105 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
end example]
The root element for a part of this content type shall be styleSheet.
[Example:
<styleSheet xmlns="…">
<numFmts count="5">
<numFmt numFmtId="164" formatCode="&quot;$&quot;#,##0.00"/>
<numFmt numFmtId="165"
formatCode="&quot;Yes&quot;;&quot;Yes&quot;;&quot;No&quot;"/>
<numFmt numFmtId="166"
formatCode="&quot;True&quot;;&quot;True&quot;;&quot;False&quot;"/>
<numFmt numFmtId="167"
formatCode="&quot;On&quot;;&quot;On&quot;;&quot;Off&quot;"/>
<numFmt numFmtId="168"
formatCode="[$€-2]\ #,##0.00_);[Red]\([$€-2]\ #,##0.00\)"/>
</numFmts>
<fonts count="5">
…
</fonts>
<fills count="4">
…
</fills>
<borders count="1">
…
</borders>
…
<colors>
…
</colors>
</styleSheet>
end example]
A Styles part shall be located within the package containing the relationships part (expressed syntactically, the
TargetMode attribute of the Relationship element shall be Internal).
A Styles part shall not have implicit or explicit relationships to any other part defined by ISO/IEC 29500.
12.3.21 Table Definition Part
Content Type: application/vnd.openxmlformats-officedocument.spreadsheetml.table+xml
Root http://purl.oclc.org/ooxml/spreadsheetml/main
Namespace:
©ISO/IEC 2016 – All rights reserved 95\n\n--- Page 106 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Source http://purl.oclc.org/ooxml/officeDocument/relationships/table
Relationship:
An instance of this part type contains a description of a single table and its autofilter information. (The data for
the table is stored in the corresponding Worksheet part.)
A package shall contain one Table Definition part per table, and each such part shall be the target of an implicit
relationship from the Worksheet (§12.3.24) part that corresponds to the worksheet containing that table.
[Example: The following Worksheet part-relationship item contains relationships to two Table Definition parts,
which are stored in the ZIP items ../tables/tableN.xml:
<Relationships xmlns="…">
<Relationship Id="rId2"
Type="http://…/table" Target="../tables/table1.xml"/>
<Relationship Id="rId3"
Type="http://…/table" Target="../tables/table2.xml"/>
</Relationships>
end example]
The root element for a part of this content type shall be table.
[Example: table2.xml describes a table that spans a 2-column range of cells, F2:G19:
<table xmlns:af="…" … id="2" name="Table2" displayName="Table2" ref="F2:G19"
totalsRowShown="0" headerRowDxfId="7">
<autoFilter ref="F2:G19"/>
<tableColumns count="2">
<tableColumn id="1" name="Salesman" dataDxfId="9" totalsRowDxfId="6"/>
<tableColumn id="2" name="Units" dataDxfId="8" totalsRowDxfId="5"/>
</tableColumns>
<tableStyle name="TableStyle2" showFirstColumn="0" showLastColumn="0"
showRowStripes="1" showColumnStripes="1"/>
</table>
When the filter "Salesman equal to Smith" is applied, the autoFilter element in table2.xml is extended, as
follows:
96 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 107 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
<autoFilter ref="F2:G19">
<af:filterColumn colId="0">
<af:filters>
<af:filter val="Smith"/>
</af:filters>
</af:filterColumn>
</autoFilter>
end example]
A Table Definition part shall be located within the package containing the relationships part (expressed
syntactically, the TargetMode attribute of the Relationship element shall be Internal).
A Table Definition part is permitted to explicit relationships to the following parts defined by ISO/IEC 29500:
 Query Table (§12.3.14)
A Table Definition part shall not have any implicit or explicit relationships to any other part defined by ISO/IEC
29500.
12.3.22 Volatile Dependencies Part
Content Type: application/vnd.openxmlformats-officedocument.spreadsheetml.volatileDependencies+xml
Root http://purl.oclc.org/ooxml/spreadsheetml/main
Namespace:
Source http://purl.oclc.org/ooxml/officeDocument/relationships/volatileDependencies
Relationship:
An instance of this part type contains information involving real-time data formulas in a workbook. Real-time
data formulas return values that change over time — often every few seconds — and require connectivity to
programs outside of the workbook to retrieve their data. In cases where those programs are not available, real-
time data formulas can use the information stored in the Volatile Dependencies part to calculate results, rather
than generate errors. More information on real-time data functions can be found in §18.17.7.284 and
§18.17.7.65 through §18.17.7.71.
A package shall contain exactly one Volatile Dependencies part, and that part shall be the target of an implicit
relationship from the Workbook (§12.3.23) part.
[Example: The following Workbook part-relationship item contains a relationship to the Volatile Dependencies
part, which is stored in the ZIP item volatileDependencies.xml:
©ISO/IEC 2016 – All rights reserved 97\n\n--- Page 108 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
<Relationships xmlns="…">
<Relationship Id="rId8"
Type="http://…/volatileDependencies"
Target="volatileDependencies.xml"/>
</Relationships>
end example]
The root element for a part of this content type shall be volTypes.
[Example:
<volTypes xmlns="…"/>
end example]
A Volatile Dependencies part shall be located within the package containing the relationships part (expressed
syntactically, the TargetMode attribute of the Relationship element shall be Internal).
A Volatile Dependencies part shall not have implicit or explicit relationships to any other part defined by ISO/IEC
29500.
12.3.23 Workbook Part
Content application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml
Type(s): application/vnd.openxmlformats-officedocument.spreadsheetml.template.main+xml
Root http://purl.oclc.org/ooxml/spreadsheetml/main
Namespace:
Source http://purl.oclc.org/ooxml/officeDocument/relationships/officeDocument
Relationship:
An instance of this part type contains workbook data and references to all of its worksheets.
A package shall contain exactly one Workbook part, and that part shall be the target of a relationship in the
package-relationship item.
[Example: The following SpreadsheetML package-relationship item contains a relationship to the Workbook
part, which is stored in the ZIP item xl/workbook.xml:
<Relationships xmlns="…">
<Relationship Id="rId1"
Type="http://…/officeDocument" Target="xl/workbook.xml"/>
</Relationships>
end example]
98 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 109 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
The root element for a part of this content type shall be workbook.
[Example: This workbook has three worksheets, named January, February, and March:
<workbook xmlns="…" xmlns:r="…">
<fileVersion lastEdited="4" lowestEdited="4" rupBuild="3417"/>
<bookViews>
<workbookView xWindow="240" yWindow="15" windowWidth="8505"
windowHeight="6240"/>
</bookViews>
<sheets>
<sheet name="January" sheetId="1" r:id="rId1"/>
<sheet name="February" sheetId="2" r:id="rId2"/>
<sheet name="March" sheetId="3" r:id="rId3"/>
</sheets>
<workbookPr showObjects="all"/>
<webPublishing codePage="1252"/>
<calcPr calcId="122211" fullCalcOnLoad="1"/>
</workbook>
end example]
A Workbook part shall be located within the package containing the relationships part (expressed syntactically,
the TargetMode attribute of the Relationship element shall be Internal).
A Workbook part is permitted to have implicit relationships to the following parts defined by ISO/IEC 29500:
 Additional Characteristics (§15.2.1)
 Bibliography (§15.2.3)
 Calculation Chain (§12.3.1)
 Cell Metadata (§12.3.10)
 Connections (§12.3.4)
 Custom XML Mappings (§12.3.6)
 Custom XML Data Storage (§15.2.4)
 Shared String Table (§12.3.15)
 Shared Workbook Revision Headers (§12.3.16)
 Shared Workbook User Data (§12.3.18)
 Styles (§12.3.20)
 Theme (§14.2.7)
 Thumbnail (§15.2.16)
 Volatile Dependencies (§12.3.22)
A Workbook part is permitted to have explicit relationships to the following parts defined by ISO/IEC 29500:
©ISO/IEC 2016 – All rights reserved 99\n\n--- Page 110 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
 Chartsheet (§12.3.2)
 Dialogsheet (§12.3.7)
 External Workbook References (§12.3.8)
 Pivot Table Cache Definition (§12.3.12)
 Worksheet (§12.3.24)
A Workbook part shall not have implicit or explicit relationships to any other part defined by ISO/IEC 29500.
12.3.24 Worksheet Part
Content Type: application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml
Root http://purl.oclc.org/ooxml/spreadsheetml/main
Namespace:
Source http://purl.oclc.org/ooxml/officeDocument/relationships/worksheet
Relationship:
An instance of this part type contains all the data, formulas, and characteristics associated with a given
worksheet.
A package shall contain exactly one Worksheet part per worksheet, and those parts shall be the target of an
explicit relationship from the Workbook (§12.3.23) part. Specifically, the id attribute on the sheet element shall
reference the desired worksheet part.
[Example: The following Workbook part-relationship item contains three relationships to Worksheet parts,
which are stored in the ZIP items worksheets/sheetN.xml:
<Relationships xmlns="…">
<Relationship Id="rId1"
Type="http://…/worksheet" Target="worksheets/sheet1.xml"/>
<Relationship Id="rId2"
Type="http://…/worksheet" Target="worksheets/sheet2.xml"/>
<Relationship Id="rId3"
Type="http://…/worksheet" Target="worksheets/sheet3.xml"/>
</Relationships>
end example]
The root element for a part of this content type shall be worksheet.
[Example: This worksheet, has cells in the range B1 to F8. Row 8 contains three cells whose values are calculated
using the following formulas: D8=SUM(D5:D7), E8=SUM(E5:E7), and F8= D8-E8:
<worksheet xmlns="…" …>
<sheetPr/>
<dimension range="B1:F8"/>
100 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 111 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
…
<sheetData>
<row r="1" spans="2:6" ht="360">
<c r="B1" s="1" t="s">
<v>0</v>
</c>
</row>
…
<row r="8" spans="2:6" ht="360">
<c r="D8" s="5">
<f>SUM(D5:D7)</f>
<v>2280.5299999999997</v>
</c>
<c r="E8" s="5">
<f>SUM(E5:E7)</f>
<v>1251.31</v>
</c>
<c r="F8" s="6">
<f>D8-E8</f>
<v>1029.2199999999998</v>
</c>
</row>
</sheetData>
…
</worksheet>
end example]
A Worksheet part shall be located within the package containing the relationships part (expressed syntactically,
the TargetMode attribute of the Relationship element shall be Internal).
A Worksheet part is permitted to have implicit relationships to the following parts defined by ISO/IEC 29500:
 Comments (§12.3.3)
 Pivot Table Definitions (§12.3.11)
 Printer Settings (§15.2.15)
 Query Table Part (§12.3.14)
 Single Cell Table Definitions (§12.3.19)
 Table Definition (§12.3.21)
A Worksheet part is permitted to contain explicit relationships to the following parts defined by ISO/IEC 29500:
 Drawings (§12.3.8)
 Embedded Control Persistence (§15.2.9)
©ISO/IEC 2016 – All rights reserved 101\n\n--- Page 112 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
 Embedded Object (§15.2.10)
 Embedded Package (§15.2.11)
 Hyperlinks (§15.3)
 Images (§15.2.14)
A Worksheet part shall not have implicit or explicit relationships to any other part defined by ISO/IEC 29500.
12.4 External Workbooks
Source http://purl.oclc.org/ooxml/officeDocument/relationships/externalLinkPath
Relationship:
An external workbook is a SpreadsheetML package whose contents are being referenced by the current
SpreadsheetML package. When a package refers to external workbooks, it shall store the location of those
workbooks using this relationship.
A package is permitted to contain one or more External Workbook relationships, and those relationships shall be
an explicit relationship from the External Workbook References (§12.3.9) part.
[Example: An External Workbook References part, which references the package c:\sourceData.xlsx would have
an External Workbook relationship, which points at that file:
<Relationships xmlns="…">
<Relationship Id="rId1"
Type="http://…/externalLinkPath"
Target="c:\sourceData.xlsx" TargetMode="External"/>
</Relationships>
end example]
A external workbook shall be located external to the package containing the relationships part (expressed
syntactically, the TargetMode attribute of the Relationship element shall be External).
102 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 113 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
13. PresentationML
This clause contains specifications for relationship items and parts that are specific to PresentationML. Parts
than can occur in a PresentationML document, but are not PresentationML-specific, are specified in §15.2.
Unless stated explicitly, all references to relationship items, content-type items, and parts in this clause refer to
PresentationML ZIP items.
13.1 Glossary of PresentationML-Specific Terms
The following terms are used in the context of a PresentationML document:
handout — A printed set of slides that can be handed out to an audience for future reference.
note — A slide annotation, reminder, or piece of text intended for the presenter or the audience.
presentation — A collection of slides intended to be viewed by an audience.
slide — A frame containing one or more pieces of text and/or images.
slide layout — The organization of elements on a slide.
13.2 Package Structure
A PresentationML package shall contain a package-relationship item and a content-type item. The package-
relationship item shall have implicit relationships with targets of the following type:
 One Presentation part (§13.3.6).
The package-relationship item is permitted to have implicit relationships with targets of the following type:
 Digital Signature Origin (§15.2.7)
 File Property parts (§15.2.12) (Application-Defined File Properties, Core File Properties, and Custom File
Properties), as appropriate.
 Thumbnail (§15.2.16).
The required and optional relationships between parts are defined in §13.3 and its subordinate clauses.
[Example: The following package represents the minimal conformant PresentationML package as defined by
ISO/IEC 29500:
First, the content type for relationship parts and the Main Presentation part (the only required part) must be
defined (physically located at /[Content_Types].xml in the package):
©ISO/IEC 2016 – All rights reserved 103\n\n--- Page 114 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
<Types xmlns="…">
<Default Extension="rels"
ContentType="application/vnd.openxmlformats-
package.relationships+xml"/>
<Override PartName="/presentation.xml"
ContentType="application/vnd.openxmlformats-
officedocument.presentationml.presentation.main+xml"/>
</Types>
Next, the single required relationship (the package-level relationship to the Main Presentation part) must be
defined (physically located at /_rels/.rels in the package):
<Relationships xmlns="…">
<Relationship Id="rId1"
Type="http://purl.oclc.org/ooxml/officeDocument/relationships/officeDocument"
Target="presentation.xml"/>
</Relationships>
Finally, the minimum content for the Main Presentation part must be defined (physically located at
/presentation.xml in the package):
<p:presentation xmlns:p="…">
<p:notesSz cx="913607" cy="913607"/>
</p:presentation>
end example]
[Example: Consider a simple PresentationML document containing two slides, which both use an image as a
template. Here’s an example of the hierarchical folder structure that might be used for the ZIP items in the
package for that document. As shown, a number of parts have their own relationship items:
/_rels/.rels Package-relationship item
/[Content_Types].xml Content-type item
/docProps/app.xml Application-Defined File Properties
part
/docProps/core.xml Core File Properties part
/docProps/custom.xml Custom File Properties part
/docProps/thumbnail.wmf Package thumbnail image
/ppt/presentation.xml Presentation part
/ppt/_rels/presentation.xml.rels Part-relationship item
/ppt/presProps.xml Presentation Properties part
/ppt/tableStyles.xml Table Styles part
/ppt/viewProps.xml View Properties part
104 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 115 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
/ppt/handoutMasters/handoutMaster1.xml Handout Master part
/ppt/handoutMasters/_rels/handoutMaster1.xml.rels
Part-relationship item
/ppt/media/image1.jpeg Slide template image
/ppt/notesMasters/notesMaster1.xml Notes Master part
/ppt/notesMasters/_rels/notesMaster1.xml.rels
Part-relationship item
/ppt/notesSlides/notesSlide1.xml Notes Slide parts
/ppt/notesSlides/notesSlide2.xml
/ppt/notesSlides/_rels/notesSlide1.xml.rels
Part-relationship items
/ppt/notesSlides/_rels/notesSlide2.xml.rels
/ppt/slideLayouts/slideLayout1.xml Slide Layout parts 1–6
/ppt/slideLayouts/slideLayout2.xml
/ppt/slideLayouts/slideLayout3.xml
/ppt/slideLayouts/slideLayout4.xml
/ppt/slideLayouts/slideLayout5.xml
/ppt/slideLayouts/slideLayout6.xml
/ppt/slideLayouts/_rels/slideLayout1.xml.rels
Part-relationship items
/ppt/slideLayouts/_rels/slideLayout2.xml.rels
/ppt/slideLayouts/_rels/slideLayout3.xml.rels
/ppt/slideLayouts/_rels/slideLayout4.xml.rels
/ppt/slideLayouts/_rels/slideLayout5.xml.rels
/ppt/slideLayouts/_rels/slideLayout6.xml.rels
/ppt/slideMasters/slideMaster1.xml Slide Master part
/ppt/slideMasters/_rels/slideMaster1.xml.rels
Part-relationship item
/ppt/slides/slide1.xml Slide parts
/ppt/slides/slide2.xml
/ppt/slides/_rels/slide1.xml.rels Part-relationship items
/ppt/slides/_rels/slide2.xml.rels
/ppt/theme/theme1.xml Theme parts
/ppt/theme/theme2.xml
/ppt/theme/theme3.xml
©ISO/IEC 2016 – All rights reserved 105\n\n--- Page 116 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
/ppt/theme/themeOverride1.xml Theme Override parts
/ppt/theme/themeOverride2.xml
/ppt/theme/themeOverride3.xml
/ppt/theme/themeOverride4.xml
/ppt/theme/themeOverride5.xml
/ppt/theme/themeOverride6.xml
/ppt/theme/themeOverride7.xml
/ppt/theme/themeOverride8.xml
/ppt/theme/themeOverride9.xml
/ppt/theme/themeOverride10.xml
The package-relationship item contains the following:
<Relationships xmlns="…">
<Relationship Id="rId1"
Type="http://…/officeDocument" Target="ppt/presentation.xml"/>
<Relationship Id="rId3"
Type="http://…/core-properties" Target="docProps/core.xml"/>
<Relationship Id="rId2"
Type="http://…/thumbnail" Target="docProps/thumbnail.wmf"/>
<Relationship Id="rId4"
Type="http://…/extended-properties" Target="docProps/app.xml"/>
</Relationships>
end example]
13.3 Part Summary
The subclauses subordinate to this one describe in detail each of the part types specific to PresentationML.
[Note: For convenience, information from those subclauses is summarized in the following table:
Part Relationship Target of Root Element Ref.
Comment Authors Presentation cmAuthorLst §13.3.1
Comments Slide cmLst §13.3.2
Handout Master Presentation handoutMaster §13.3.3
Notes Master Notes Slide, Presentation notesMaster §13.3.4
Notes Slide Slide notes §13.3.5
Presentation PresentationML package presentation §13.3.6
Presentation Presentation presentationPr §13.3.7
Properties
Slide Presentation sld §13.3.8
Slide Layout Slide Master, Notes Slide, sldLayout §13.3.9
106 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 117 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Part Relationship Target of Root Element Ref.
Presentation, Slide, Slide
Master
Slide Master Presentation, Slide Layout sldMaster §13.3.10
Slide Synchronization Slide sldSyncPr §13.3.11
Data
User-Defined Tags Presentation, Slide tagLst §13.3.12
View Properties Presentation viewPr §13.3.13
end note]
13.3.1 Comment Authors Part
Content Type: application/vnd.openxmlformats-officedocument.presentationml.commentAuthors+xml
Root http://purl.oclc.org/ooxml/presentationml/main
Namespace:
Source http://purl.oclc.org/ooxml/officeDocument/relationships/commentAuthors
Relationship:
An instance of this part type contains information about each author who has added a comment to the
document. That information includes the author's name, initials, a unique author-ID, a last-comment-index-used
count, and a display color. (The color can be used when displaying comments to distinguish comments from
different authors.)
A package shall contain at most one Comment Authors part. If it exists, that part shall be the target of an implicit
relationship from the Presentation (§13.3.6) part.
[Example: The following Presentation part relationship item contains a relationship to the Comment Authors
part, which is stored in the ZIP item commentAuthors.xml:
<Relationships xmlns="…">
<Relationship Id="rId8"
Type="http://…/commentAuthors" Target="commentAuthors.xml"/>
</Relationships>
end example]
The root element for a part of this content type shall be cmAuthorLst.
[Example: Two people have authored comments in this document: Mary Smith and Peter Jones. Her initials are
"mas", her author-ID is 0, and her comments' display color index is 0. Since Mary's last-comment-index-used
value is 3, the next comment-index to be used for her is 4. His initials are "pjj", his author-ID is 1, and his
comments' display color index is 1. Since Peter's last-comment-index-used value is 1, the next comment-index to
be used for him is 2:
©ISO/IEC 2016 – All rights reserved 107\n\n--- Page 118 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
<p:cmAuthorLst xmlns:p="…" …>
<p:cmAuthor id="0" name="Mary Smith" initials="mas" lastIdx="3"
clrIdx="0"/>
<p:cmAuthor id="1" name="Peter Jones" initials="pjj" lastIdx="1"
clrIdx="1"/>
</p:cmAuthorLst>
end example]
A Comment Authors part shall be located within the package containing the relationships part (expressed
syntactically, the TargetMode attribute of the Relationship element shall be Internal).
A Comment Authors part shall not have implicit or explicit relationships to any other part defined by ISO/IEC
29500.
13.3.2 Comments Part
Content Type: application/vnd.openxmlformats-officedocument.presentationml.comments+xml
Root http://purl.oclc.org/ooxml/presentationml/main
Namespace:
Source http://purl.oclc.org/ooxml/officeDocument/relationships/comments
Relationship:
An instance of this part type contains the comments for a single slide. Each comment is tied to its author via an
author-ID. Each comment's index number and author-ID combination are unique.
A package shall contain one Comments part for each slide containing one or more comments, and each of those
parts shall be the target of an implicit relationship from its corresponding Slide (§13.3.8) part.
[Example: The following Slide part-relationship item contains a relationship to a Comments part, which is stored
in the ZIP item ../comments/comment2.xml:
<Relationships xmlns="…">
<Relationship Id="rId4"
Type="http://…/comments"
Target="../comments/comment2.xml"/>
</Relationships>
end example]
The root element for a part of this content type shall be cmLst .
[Example: The Comments part contains three comments, two created by one author, and one created by
another, all at the dates and times shown. The index numbers are assigned on a per-author basis, starting at 1
for an author's first comment:
108 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 119 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
<p:cmLst xmlns:p="…" …>
<p:cm authorId="0" dt="2005-11-13T17:00:22.071" idx="1">
<p:pos x="4486" y="1342"/>
<p:text>Comment text goes here.</p:text>
</p:cm>
<p:cm authorId="0" dt="2005-11-13T17:00:34.849" idx="2">
<p:pos x="3607" y="1867"/>
<p:text>Another comment's text goes here.</p:text>
</p:cm>
<p:cm authorId="1" dt="2005-11-15T00:06:46.919" idx="1">
<p:pos x="1493" y="2927"/>
<p:text>comment …</p:text>
</p:cm>
</p:cmLst>
end example]
A Comments part shall be located within the package containing the relationships part (expressed syntactically,
the TargetMode attribute of the Relationship element shall be Internal).
A Comments part shall not have implicit or explicit relationships to any other part defined by ISO/IEC 29500.
13.3.3 Handout Master Part
Content Type: application/vnd.openxmlformats-officedocument.presentationml.handoutMaster+xml
Root http://purl.oclc.org/ooxml/presentationml/main
Namespace:
Source http://purl.oclc.org/ooxml/officeDocument/relationships/handoutMaster
Relationship:
An instance of this part type contains the look, position, and size of the slides, notes, header and footer text,
date, or page number on the presentation's handout.
A package shall contain at most one Handout Master part, and it shall be the target of an explicit relationship
from the Presentation (§13.3.6) part.
[Example: The following Presentation part-relationship item contains a relationship to the Handout Master part,
which is stored in the ZIP item handoutMasters/handoutMaster1.xml:
<Relationships xmlns="…">
<Relationship Id="rId5"
Type="http://…/handoutMaster"
Target="handoutMasters/handoutMaster1.xml"/>
</Relationships>
©ISO/IEC 2016 – All rights reserved 109\n\n--- Page 120 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
end example]
The root element for a part of this content type shall be handoutMaster.
[Example:
<p:handoutMaster xmlns:p="…">
<p:cSld name="">
…
</p:cSld>
<p:clrMap … />
</p:handoutMaster>
end example]
A Handout Master part shall be located within the package containing the relationships part (expressed
syntactically, the TargetMode attribute of the Relationship element shall be Internal).
A Handout Master part is permitted to have implicit relationships to the following parts defined by ISO/IEC
29500:
 Additional Characteristics (§15.2.1)
 Bibliography (§15.2.3)
 Custom XML Data Storage (§15.2.4)
 Theme (§14.2.7)
 Thumbnail (§15.2.16)
A Handout Master part is permitted to have explicit relationships to the following parts defined by ISO/IEC
29500:
 Audio (§15.2.2)
 Chart (§14.2.1)
 Content Part (§15.2.4)
 Diagrams: Diagram Colors(§14.2.3), Diagram Data(§14.2.4), Diagram Layout Definition(§14.2.5) and
Diagram Styles (§14.2.6)
 Embedded Control Persistence (§15.2.9)
 Embedded Object (§15.2.10)
 Embedded Package (§15.2.11)
 Hyperlink (§15.3)
 Image (§15.2.14)
 Video (§15.2.15)
A Handout Master part shall not have implicit or explicit relationships to any other part defined by ISO/IEC
29500.
110 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 121 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
13.3.4 Notes Master Part
Content Type: application/vnd.openxmlformats-officedocument.presentationml.notesMaster+xml
Root http://purl.oclc.org/ooxml/presentationml/main
Namespace:
Source http://purl.oclc.org/ooxml/officeDocument/relationships/notesMaster
Relationship:
An instance of this part type contains information about the content and formatting of all notes pages.
A package shall contain at most one Notes Master part, and that part shall be the target of an implicit
relationship from the Notes Slide (§13.3.5) part, as well as an explicit relationship from the Presentation
(§13.3.6) part.
[Example: The following Presentation part-relationship item contains a relationship to the Notes Master part,
which is stored in the ZIP item notesMasters/notesMaster1.xml:
<Relationships xmlns="…">
<Relationship Id="rId4"
Type="http://…/notesMaster" Target="notesMasters/notesMaster1.xml"/>
</Relationships>
end example]
The root element for a part of this content type shall be notesMaster.
[Example:
<p:notesMaster xmlns:p="…">
<p:cSld name="">
…
</p:cSld>
<p:clrMap … />
</p:notesMaster>
end example]
A Notes Master part shall be located within the package containing the relationships part (expressed
syntactically, the TargetMode attribute of the Relationship element shall be Internal).
A Notes Master part is permitted to have implicit relationships to the following parts defined by ISO/IEC 29500:
 Additional Characteristics (§15.2.1)
 Bibliography (§15.2.3)
 Custom XML Data Storage (§15.2.4)
©ISO/IEC 2016 – All rights reserved 111\n\n--- Page 122 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
 Theme (§14.2.7)
 Thumbnail (§15.2.16)
A Notes Master part is permitted to have explicit relationships to the following parts defined by ISO/IEC 29500:
 Audio (§15.2.2)
 Chart (§14.2.1)
 Content Part (§15.2.4)
 Diagrams: Diagram Colors(§14.2.3), Diagram Data(§14.2.4), Diagram Layout Definition(§14.2.5) and
Diagram Styles (§14.2.6)
 Embedded Control Persistence (§15.2.9)
 Embedded Object (§15.2.10)
 Embedded Package (§15.2.11)
 Hyperlink (§15.3).
 Image (§15.2.14)
 Video (§15.2.15)
The Notes Master part shall not have implicit or explicit relationships to any other part defined by ISO/IEC
29500.
13.3.5 Notes Slide Part
Content Type: application/vnd.openxmlformats-officedocument.presentationml.notesSlide+xml
Root http://purl.oclc.org/ooxml/presentationml/main ain
Namespace:
Source http://purl.oclc.org/ooxml/officeDocument/relationships/notesSlide
Relationship:
An instance of this part type contains the notes for a single slide.
A package shall contain one Notes Slide part for each slide that contains notes. If they exist, those parts shall
each be the target of an implicit relationship from the Slide (§13.3.8) part.
[Example: The following Slide part-relationship item contains a relationship to a Notes Slide part, which is stored
in the ZIP item ../notesSlides/notesSlide1.xml:
<Relationships xmlns="…">
<Relationship Id="rId3"
Type="http://…/notesSlide" Target="../notesSlides/notesSlide1.xml"/>
</Relationships>
end example]
The root element for a part of this content type shall be notes.
112 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 123 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
[Example:
<p:notes xmlns:p="…">
<p:cSld name="">
…
</p:cSld>
<p:clrMapOvr>
<a:masterClrMapping/>
</p:clrMapOvr>
</p:notes>
end example]
A Notes Slide part shall be located within the package containing the relationships part (expressed syntactically,
the TargetMode attribute of the Relationship element shall be Internal).
A Notes Slide part is permitted to have implicit relationships to the following parts defined by ISO/IEC 29500:
 Additional Characteristics (§15.2.1)
 Bibliography (§15.2.3)
 Custom XML Data Storage (§15.2.4)
 Notes Master (§13.3.4)
 Theme Override(§14.2.8)
 Thumbnail (§15.2.16)
A Notes Slide part is permitted to have explicit relationships to the following parts defined by ISO/IEC 29500:
 Audio (§15.2.2)
 Chart (§14.2.1)
 Content Part (§15.2.4)
 Diagrams: Diagram Colors(§14.2.3), Diagram Data(§14.2.4), Diagram Layout Definition(§14.2.5) and
Diagram Styles (§14.2.6)
 Embedded Control Persistence (§15.2.9)
 Embedded Object (§15.2.10)
 Embedded Package (§15.2.11)
 Hyperlink (§15.3).
 Image (§15.2.14)
 Video (§15.2.15)
The Notes Slide part shall not have implicit or explicit relationships to any other part defined by ISO/IEC 29500.
13.3.6 Presentation Part
Content Type: application/vnd.openxmlformats-officedocument.presentationml.presentation.main+xml
application/vnd.openxmlformats-officedocument.presentationml.slideshow.main+xml
©ISO/IEC 2016 – All rights reserved 113\n\n--- Page 124 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
application/vnd.openxmlformats-officedocument.presentationml.template.main+xml
Root http://purl.oclc.org/ooxml/presentationml/main
Namespace:
Source http://purl.oclc.org/ooxml/officeDocument/relationships/officeDocument
Relationship:
An instance of this part type contains the definition for a slide presentation.
A package shall contain exactly one Presentation part, and that part shall be the target of a relationship in the
package-relationship item.
[Example: The following PresentationML's package-relationship item contains a relationship to the Presentation
part, which is stored in the ZIP item ppt/presentation.xml:
<Relationships xmlns="…">
<Relationship Id="rId1"
Type="http://…/officeDocument" Target="ppt/presentation.xml"/>
</Relationships>
end example]
The root element for a part of this content type shall be presentation.
[Example: This presentation contains two slides:
<p:presentation xmlns:p="…" … >
<p:sldMasterIdLst>
<p:sldMasterId
xmlns:rel="http://…/relationships" rel:id="rId1"/>
</p:sldMasterIdLst>
<p:notesMasterIdLst>
<p:notesMasterId
xmlns:rel="http://…/relationships" rel:id="rId4"/>
</p:notesMasterIdLst>
<p:handoutMasterIdLst>
<p:handoutMasterId
xmlns:rel="http://…/relationships" rel:id="rId5"/>
</p:handoutMasterIdLst>
<p:sldIdLst>
<p:sldId id="267"
xmlns:rel="http://…/relationships" rel:id="rId2"/>
<p:sldId id="256"
xmlns:rel="http://…/relationships" rel:id="rId3"/>
</p:sldIdLst>
114 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 125 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
<p:sldSz cx="9144000" cy="6858000"/>
<p:notesSz cx="6858000" cy="9144000"/>
</p:presentation>
end example]
A Presentation part shall be located within the package containing the relationships part (expressed
syntactically, the TargetMode attribute of the Relationship element shall be Internal).
A Presentation part is permitted to have implicit relationships to the following parts defined by ISO/IEC 29500:
 Additional Characteristics (§15.2.1)
 Comment Authors (§13.3.1)
 Bibliography (§15.2.3)
 Custom XML Data Storage (§15.2.4)
 Font (§15.2.13)
 Presentation Properties (§13.3.7)
 Table Styles (§14.2.9)
 Theme (§14.2.7)
 Thumbnail (§15.2.16)
 View Properties (§13.3.13).
A Presentation part is permitted to have explicit relationships to the following parts defined by ISO/IEC 29500:
 Notes Master (§13.3.4)
 Handout Master (§13.3.3)
 Slide (§13.3.8)
 Slide Master (§13.3.10)
 User Defined Tags (§13.3.12)
13.3.7 Presentation Properties Part
Content Type: application/vnd.openxmlformats-officedocument.presentationml.presProps+xml
Root http://purl.oclc.org/ooxml/presentationml/main
Namespace:
Source http://purl.oclc.org/ooxml/officeDocument/relationships/presProps
Relationship:
An instance of this part type contains all the presentation's properties.
A package shall contain exactly one Presentation Properties part, and that part shall be the target of an implicit
relationship from the Presentation (§13.3.6) part.
©ISO/IEC 2016 – All rights reserved 115\n\n--- Page 126 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
[Example: The following Presentation part-relationship item contains a relationship to the Presentation
Properties part, which is stored in the ZIP item presProps.xml:
<Relationships xmlns="…">
<Relationship Id="rId6"
Type="http://…/presProps" Target="presProps.xml"/>
</Relationships>
end example]
The root element for a part of this content type shall be presentationPr.
[Example:
<p:presentationPr xmlns:p="…" …>
<p:clrMru>
…
</p:clrMru>
…
</p:presentationPr>
end example]
A Presentation Properties part shall be located within the package containing the relationships part (expressed
syntactically, the TargetMode attribute of the Relationship element shall be Internal).
A Presentation Properties part shall not have implicit or explicit relationships to any other part defined by
ISO/IEC 29500.
13.3.8 Slide Part
Content Type: application/vnd.openxmlformats-officedocument.presentationml.slide+xml
Root http://purl.oclc.org/ooxml/presentationml/main
Namespace:
Source http://purl.oclc.org/ooxml/officeDocument/relationships/slide
Relationship:
A Slide part contains the contents of a single slide.
A package shall contain one Slide part per slide, and each of those parts shall be the target of an explicit
relationship from the Presentation (§13.3.6) part.
[Example: Consider a PresentationML document having two slides. The corresponding Presentation part-
relationship item contains two relationships to Slide parts, which are stored in the ZIP items slides/slide1.xml
and slides/slide2.xml:
116 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 127 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
<Relationships xmlns="…">
<Relationship Id="rId2"
Type="http://…/slide" Target="slides/slide1.xml"/>
<Relationship Id="rId3"
Type="http://…/slide" Target="slides/slide2.xml"/>
</Relationships>
end example]
The root element for a part of this content type shall be sld.
[Example: slides/slide1.xml contains:
<p:sld xmlns:p="…">
<p:cSld name="">
…
</p:cSld>
<p:clrMapOvr>
…
</p:clrMapOvr>
<p:timing>
<p:tnLst>
<p:par>
<p:cTn id="1" dur="indefinite" restart="never" nodeType="tmRoot"/>
</p:par>
</p:tnLst>
</p:timing>
</p:sld>
end example]
A Slide part shall be located within the package containing the relationships part (expressed syntactically, the
TargetMode attribute of the Relationship element shall be Internal).
A Slide part is permitted to have implicit relationships to the following parts defined by ISO/IEC 29500:
 Additional Characteristics (§15.2.1)
 Bibliography (§15.2.3)
 Comments (§13.3.2)
 Custom XML Data Storage (§15.2.4)
 Notes Slide (§13.3.5)
 Theme Override (§14.2.8)
 Thumbnail (§15.2.16)
 Slide Layout (§13.3.9)
 Slide Synchronization Data (§13.3.11)
©ISO/IEC 2016 – All rights reserved 117\n\n--- Page 128 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
A Slide part is permitted to have explicit relationships to the following parts defined by ISO/IEC 29500:
 Audio (§15.2.2)
 Chart (§14.2.1)
 Content Part (§15.2.4)
 Diagrams: Diagram Colors(§14.2.3), Diagram Data(§14.2.4), Diagram Layout Definition(§14.2.5) and
Diagram Styles (§14.2.6)
 Embedded Control Persistence (§15.2.9)
 Embedded Object (§15.2.10)
 Embedded Package (§15.2.11)
 Hyperlink (§15.3).
 Image (§15.2.14)
 User Defined Tags (§13.3.12)
 Video (§15.2.15)
A Slide part shall not have implicit or explicit relationships to any other part defined by ISO/IEC 29500.
13.3.9 Slide Layout Part
Content Type: application/vnd.openxmlformats-officedocument.presentationml.slideLayout+xml
Root http://purl.oclc.org/ooxml/presentationml/main
Namespace:
Source http://purl.oclc.org/ooxml/officeDocument/relationships/slideLayout
Relationship:
An instance of this part type contains the definition for a slide layout template for this presentation. This
template defines the default appearance and positioning of drawing objects on this slide type when it is created.
A package shall contain one or more Slide Layout parts, and each of those parts shall be the target of an explicit
relationship in the Slide Master (§13.3.10) part, as well as an implicit relationship from each of the Slide
(§13.3.8) parts associated with this slide layout.
[Example: The following Slide Master part-relationship item contains relationships to several Slide Layout parts,
which are stored in the ZIP items ../slideLayouts/slideLayoutN.xml:
118 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 129 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
<Relationships xmlns="…">
<Relationship Id="rId1"
Type="http://…/slideLayout"
Target="../slideLayouts/slideLayout1.xml"/>
<Relationship Id="rId2"
Type="http://…/slideLayout"
Target="../slideLayouts/slideLayout2.xml"/>
<Relationship Id="rId3"
Type="http://…/slideLayout"
Target="../slideLayouts/slideLayout3.xml"/>
</Relationships>
end example]
The root element for a part of this content type shall be sldLayout.
[Example:
<p:sldLayout xmlns:p="…" matchingName="" type="title" preserve="1">
<p:cSld name="Title Slide">
…
</p:cSld>
<p:clrMapOvr>
<a:masterClrMapping/>
</p:clrMapOvr>
<p:timing/>
</p:sldLayout>
</p:sldMaster>
end example]
A Slide Layout part is permitted to have implicit relationships to the following parts defined by ISO/IEC 29500:
 Additional Characteristics (§15.2.1)
 Bibliography (§15.2.3)
 Custom XML Data Storage (§15.2.4)
 Slide Master (§13.3.10)
 Theme Override (§14.2.8)
 Thumbnail (§15.2.16)
A Slide Layout part is permitted to have explicit relationships to the following parts defined by ISO/IEC 29500:
 Audio (§15.2.2)
 Chart (§14.2.1)
 Content Part (§15.2.4)
©ISO/IEC 2016 – All rights reserved 119\n\n--- Page 130 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
 Diagrams: Diagram Colors(§14.2.3), Diagram Data(§14.2.4), Diagram Layout Definition(§14.2.5) and
Diagram Styles (§14.2.6)
 Embedded Control Persistence (§15.2.9)
 Embedded Object (§15.2.10)
 Embedded Package (§15.2.11)
 Hyperlink (§15.3).
 Image (§15.2.14)
 Video (§15.2.15)
A Slide Layout part shall not have implicit or explicit relationships to any other part defined by ISO/IEC 29500.
13.3.10 Slide Master Part
Content Type: application/vnd.openxmlformats-officedocument.presentationml.slideMaster+xml
Root http://purl.oclc.org/ooxml/presentationml/main
Namespace:
Source http://purl.oclc.org/ooxml/officeDocument/relationships/slideMaster
Relationship:
An instance of this part type contains the master definition of formatting, text, and objects that appear on each
slide in the presentation that is derived from this slide master.
A package shall contain one or more Slide Master parts, each of which shall be the target of an explicit
relationship from the Presentation (§13.3.6) part, as well as an implicit relationship from any Slide Layout
(§13.3.9) part where that slide layout is defined based on this slide master. Each can optionally be the target of a
relationship in a Slide Layout (§13.3.9) part as well.
[Example: The following Presentation part-relationship item contains a relationship to the Slide Master part,
which is stored in the ZIP item slideMasters/slideMaster1.xml:
<Relationships xmlns="…">
<Relationship Id="rId1"
Type="http://…/slideMaster" Target="slideMasters/slideMaster1.xml"/>
</Relationships>
end example]
The root element for a part of this content type shall be sldMaster.
[Example:
120 ©ISO/IEC 2016 – All rights reserved\n