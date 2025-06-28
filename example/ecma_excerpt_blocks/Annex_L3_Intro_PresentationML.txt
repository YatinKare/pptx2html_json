\n--- Page 4769 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
</xsd:element>
</xsd:sequence>
<xsd:attribute name="currency" form="unqualified"
type="xsd:string"></xsd:attribute>
<xsd:attribute name="detailed" form="unqualified"
type="xsd:boolean"></xsd:attribute>
<xsd:attribute name="total-sum" form="unqualified"
type="xsd:double"></xsd:attribute>
</xsd:complexType>
</xsd:element>
</xsd:schema>
</Schema>
<Map ID="1" Name="expense-report_Map" RootElement="expense-report"
SchemaID="Schema1" ShowImportExportValidationErrors="false" AutoFit="true"
Append="false" PreserveSortAFLayout="true" PreserveFormat="true">
<DataBinding FileBinding="true" DataBindingLoadMode="1"/>
</Map>
</MapInfo>
 /MapInfo@SelectionNamespaces ties the prefix to the actual namespace. This is used when
writing xpath expressions at runtime against the XML instance structures, because the xpath
expressions use namespace prefixes instead of the fully spelled out namespace.
 /MapInfo/Schema stores the schemas for a particular XML map object. There can be multiple
<Schema> elements in a workbook, one for each XML map.
 /MapInfo/Schema@ID identifies the schema collection used to define a particular XML map
object.
 /MapInfo/Map/@ID identifies the map object.
 /MapInfo/Map@Name is the friendly name of the map object.
 /MapInfo/Map@RootElement is the name of the root element of the XML instance (schemas
can define more than one root node).
 /MapInfo/Map@SchemaID identifies which schema collection the map uses.
 /MapInfo/Map@ShowImportExportValidationErrors indicates that when an XML
instance is imported or exported, the schema should be used to validate the instance, and
schema errors should be shown to the user.
 /MapInfo/Map@AutoFit indicates that after refresh, all the cells should be ‘best fitted’.
 /MapInfo/Map@Append means that when refreshed, don’t discard existing data, but append
new data to it.
 /MapInfo/Map@PreserveSortAFLayout indicates whether to keep filters on (Tables).
 /MapInfo/Map@PreserveFormat indicates whether to keep the cell formatting applied or re-
apply based on schema data type.
©ISO/IEC 2016 – All rights reserved 4759\n\n--- Page 4770 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
L.2.15.4.3 The Table XML
The only difference with table definitions that are bound to XML is that @tableType="xml" and each
column has an additional set of xml-specific properties, contained in the <xmlColumnPr> collection,
which appears once for every column in the Table which has an XML data binding.
<table xmlns="http://purl.oclc.org/ooxml/spreadsheetml/main" id="7"
name="Table7" displayName="Table7" ref="B8:G12" tableType="xml"
totalsRowShown="0" connectionId="1">
<autoFilter ref="B8:G12"/>
<tableColumns count="6">
<tableColumn id="1" uniqueName="type" name="type">
<xmlColumnPr mapId="1" xpath="/expense-report/expense-
item/@type" xmlDataType="string"/>
</tableColumn>
<tableColumn id="2" uniqueName="expto" name="expto">
<xmlColumnPr mapId="1" xpath="/expense-report/expense-
item/@expto" xmlDataType="string"/>
</tableColumn>
<tableColumn id="3" uniqueName="Date" name="Date">
<xmlColumnPr mapId="1" xpath="/expense-report/expense-
item/Date" xmlDataType="date"/>
</tableColumn>
<tableColumn id="4" uniqueName="expense" name="expense">
<xmlColumnPr mapId="1" xpath="/expense-report/expense-
item/expense" xmlDataType="double"/>
</tableColumn>
<tableColumn id="5" uniqueName="description" name="description">
<xmlColumnPr mapId="1" xpath="/expense-report/expense-
item/description" xmlDataType="string"/>
</tableColumn>
<tableColumn id="6" uniqueName="misctype" name="misctype">
<xmlColumnPr mapId="1" xpath="/expense-report/expense-
item/Misc/@misctype" xmlDataType="string"/>
</tableColumn>
</tableColumns>
<tableStyleInfo name="TableStyleMedium7" showFirstColumn="0"
showLastColumn="0" showRowStripes="1" showColumnStripes="0"/>
</table>
The column in the Table titled "type" is bound to an XML mapping, whose map object Id @mapId is "1".
The @xpath value indicates an xpath expression to which this Table column is associated. In this
example the Table column "type" corresponds to @type, which is an attribute of the <expense-item>
collection. The corresponding custom schema definition for @type indicates a data type of string. This is
4760 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 4771 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
stored as an xml column property as well, in @xmlDataType. This is used for interpreting the data on
import and export, and is also used to format the cells for proper rendering in the range.
The remaining columns have similar properties set and can be understood from the discussion above.
L.2.15.4.4 Single Cell XML
Contents of tableSingleCells.xml
<singleXmlCells xmlns="http://purl.oclc.org/ooxml/spreadsheetml/main">
<singleXmlCell id="1" name="Table1" displayName="Table1" r="B3"
connectionId="1">
<xmlCellPr id="1" uniqueName="currency">
<xmlPr mapId="1" xpath="/expense-report/@currency"
xmlDataType="string"/>
</xmlCellPr>
</singleXmlCell>
<singleXmlCell id="2" name="Table2" displayName="Table2" r="C3"
connectionId="1">
<xmlCellPr id="1" uniqueName="detailed">
<xmlPr mapId="1" xpath="/expense-report/@detailed"
xmlDataType="boolean"/>
</xmlCellPr>
</singleXmlCell>
<singleXmlCell id="3" name="Table3" displayName="Table3" r="D3"
connectionId="1">
<xmlCellPr id="1" uniqueName="total-sum">
<xmlPr mapId="1" xpath="/expense-report/@total-sum"
xmlDataType="double"/>
</xmlCellPr>
</singleXmlCell>
<singleXmlCell id="4" name="Table4" displayName="Table4" r="B6"
connectionId="1">
<xmlCellPr id="1" uniqueName="First">
<xmlPr mapId="1" xpath="/expense-report/Person/First"
xmlDataType="string"/>
</xmlCellPr>
</singleXmlCell>
<singleXmlCell id="5" name="Table5" displayName="Table5" r="C6"
connectionId="1">
<xmlCellPr id="1" uniqueName="Last">
<xmlPr mapId="1" xpath="/expense-report/Person/Last"
xmlDataType="string"/>
</xmlCellPr>
</singleXmlCell>
©ISO/IEC 2016 – All rights reserved 4761\n\n--- Page 4772 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
<singleXmlCell id="6" name="Table6" displayName="Table6" r="D6"
connectionId="1">
<xmlCellPr id="1" uniqueName="Email">
<xmlPr mapId="1" xpath="/expense-report/Person/Email"
xmlDataType="string"/>
</xmlCellPr>
</singleXmlCell>
</singleXmlCells>
A single cell which has been mapped to an XML node is expressed in much the same way that an entire
table is expressed.
The <singleXmlCell> collection is the top level object, like the Table, which identifies the cell in
question.
The <xmlCellPr> collection identifies the name for the only 'column' in this structure, the single cell.
In this way it is much like a table column definition and the table column-level properties.
The <xmlPr> collection expresses the xml properties for this cell.
L.2.16 Formulas
L.2.16.1 Introduction
A SpreadsheetML formula is an equation that performs a calculation that typically involves the values of
one or more cells in one or more worksheets.
A formula is an expression that can contain the following: constants (§L.2.16.2), operators (§L.2.16.3),
cell references (§L.2.16.4), calls to functions (§L.2.16.5), and names (§L.2.16.6).
Consider the formula PI()*(A2^2). In this case,
 PI() results in a call to the function PI, which returns the value of π.
 The cell reference A2 returns the value in that cell.
 2 is a numeric constant.
 The caret (^) operator raises its left operand to the power of its right operand.
 The parentheses, ( and ), are used for grouping.
 The asterisk (*) operator performs multiplication of its two operands.
L.2.16.2 Constants
A constant is a predefined value that is not calculated, and, therefore, does not change. A constant can
be any of the following:
 A real number
 The logical values TRUE and FALSE
 A string literal
4762 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 4773 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
 An array constant
 An error constant
L.2.16.3 Operators
An operator is a symbol that specifies the type of operation to perform on one or more operands. There
are arithmetic, comparison, text, and reference operators.
Operators
Family Operator Description Precedence
Reference : Binary range operator, which takes two cell highest
operators reference (§L.2.16.3) operands, and results in
one reference to the cells inclusive of, and
between, those references. For example,
SUM(B5:C15), which references 11 cells.
, Binary union operator, which takes two cell
reference (§L.2.16.3) operands, and results in
one reference to all those, possibly non-
contiguous, cells. For example,
SUM((B5:B15,D5:D15))), which
references 22 cells, 11 from column B, and 11
from column D. The grouping parentheses
are necessary to indicate that the comma is
an operator rather than a punctuator
separating two arguments.
space Binary intersection operator, which takes two
cell reference (§L.2.16.3) operands, and
results in one reference to those, possibly
non-contiguous, cells that are common. If the
intersection is empty, the result is #NULL!.
For example, COUNT((B1:C1) (C1:D1)),
which results in a reference to C1, while
COUNT((B1:D1) (B1,D1)) results in a
single reference to B1 and D1.
Arithmetic - Unary minus
operators
% Percentage (unary postfix), which divides its
operand by 100. For example, 10.5%, which
results in 0.105.
^ Exponentiation
* Multiplication
/ Division
+ Addition
- Subtraction
©ISO/IEC 2016 – All rights reserved 4763\n\n--- Page 4774 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Operators
Text operator & Text concatenation (Each of the two
operands is converted to text, if necessary,
before concatenation.)
Comparison = Equal-to lowest
operators
<> Not-equal-to
< Less-than
<= Less-than or equal-to
> Greater-than
>= Greater-than-or-equal-to
Given that cell E38 contains the value 4, and cell F38 contains the value 2, the formula
((-1+E38^2)*3-F38)/2
produces the result 21.5.
L.2.16.4 Cell References
Each set of horizontal cells in a worksheet is a row, and each set of vertical cells is a column. A cell's row
and column combination designates the location of that cell.
A cell reference designates one or more cells on the same worksheet. Using references, one can:
 Use data contained in different parts of the same worksheet in a single formula.
 Use the value from a single cell in several formulas.
 Refer to cells on other sheets in the same workbook, and even to other workbooks. (References
to cells in other workbooks are called links.)
There are two cell reference styles: A1 and R1C1.
 In the A1 reference style, each row has a numeric heading numbered sequentially from the top
down, starting at 1. Each column has an alphabetic heading named sequentially from left-to-
right, A–Z, then AA–AZ, BA–BZ, …, ZA–ZZ, AAA–AAZ, ABA–ABZ, and so on. Column letters are not
case-sensitive.
A relative reference to a single cell is written as its column letter immediately followed by its
row number. A relative reference to a whole row is written as its row number. A relative
reference to a whole column is written as its column letter. A reference to a range of two or
more cells is written as two single-cell references separated by the binary range operator (:). An
absolute A1 reference is made up of a cell's column letter followed by its row number, with each
being preceded by a dollar character ($). For example, A2, B34, and B5:D8 are relative
4764 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 4775 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
A1 references. $A$2, $B$34, and $B$5:$D$8 are absolute A1 references. $A2, B$34, and
$B5:D$8 are mixed A1 references.
 In the R1C1 reference style, each row has a numeric heading numbered sequentially from the
top down, starting at 1. Each column has a numeric heading numbered sequentially from left-to-
right, starting at 1.
A whole row is referenced by omitting the column, and a whole column is referenced by
omitting the row. An absolute row or column reference uses absolute row or column numbers,
respectively. A relative row or column reference uses, respectively, row or column offsets from
the cell containing the formula, with a negative offset indicating a row to the left or a column
above, and a positive offset indicateing a row to the right or a column below. Specifying an
offset of zero is equivalent to omitting that offset and its delimiting brackets. For example, R[-
2]C refers to the cell two rows up and in the same column, R[2]C[2] refers to the cell two
rows down and two columns to the right, R2C2 refers to the cell in the second row and in the
second column, R[-1] refers to the entire row above the active cell, and R refers to the current
row.
The R1C1 alternate reference style can only be used at runtime.
L.2.16.5 Functions
A function is a named formula that takes zero or more arguments, performs an operation, and,
optionally, returns a result. Some examples of function calls are: PI(), POWER(A1,B3), and
SUM(C6:C10).
There are more than 300 predefined functions defined by this Office Open XML specification. User-
defined functions are also permitted.
L.2.16.6 Names
A name is an alias for a constant, a cell reference, or a formula. A name in a formula can make it easier
to understand the purpose of that formula. For example, the formula SUM(FirstQuarterSales) is
easier to identify than SUM(C20:C30).
L.2.16.7 Types and Values
Each expression has a type. SpreadsheetML formulas support the following types: array, error, logical,
number, and text.
An array value or constant represents a collection of one or more elements, whose values can have any
type (i.e., the elements of an array need not all have the same type).
L.2.16.8 Error values
The evaluation of an expression can result in an error having one of a number of error values. These
error values are:
©ISO/IEC 2016 – All rights reserved 4765\n\n--- Page 4776 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Error Reason for Occurrence
Value
#DIV/0! Intended to indicate when any number, including zero, is divided by zero.
#N/A Intended to indicate when a designated value is not available. For example,
Some functions, such as SUMX2MY2, perform a series of operations on
corresponding elements in two arrays. If those arrays do not have the same
number of elements, then for some elements in the longer array, there are no
corresponding elements in the shorter one; that is, one or more values in the
shorter array are not available.
This error value can be produced by calling the function NA.
#NAME? Intended to indicate when what looks like a name is used, but no such name has
been defined. For example, XYZ/3, where XYZ is not a defined name. Total
is & A10, where neither Total nor is is a defined name. Presumably,
"Total is " & A10 was intended. SUM(A1C10), where the range A1:C10
was intended.
#NULL! Intended to indicate when two areas are required to intersect, but do not. For
example, In the case of SUM(B1 C1), the space between B1 and C1 is treated as
the binary intersection operator, when a comma was intended.
#NUM! Intended to indicate when an argument to a function has a compatible type, but
has a value that is outside the domain over which that function is defined. (This
is known as a domain error.) For example, Certain calls to ASIN, ATANH, FACT,
and SQRT might result in domain errors.
Intended to indicate that the result of a function cannot be represented in a
value of the specified type, typically due to extreme magnitude. (This is known
as a range error.) For example, FACT(1000) might result in a range error.
#REF! Intended to indicate when a cell reference is invalid. For example, If a formula
contains a reference to a cell, and then the row or column containing that cell is
deleted, a #REF! error results. If a worksheet does not support 20,001 columns,
OFFSET(A1,0,20000) results in a #REF! error.
#VALUE! Intended to indicate when an incompatible type argument is passed to a
function, or an incompatible type operand is used with an operator. For
example, In the case of a function argument, a number was expected, but text
was provided. In the case of 1+"ABC", the binary addition operator is not
defined for text.
L.2.16.9 Dates and Times
Each unique instant in SpreadsheetML time is stored as an ISO 8601-formatted string, which is made up
of a date component, a time component, and a timezone component.
Numerous functions take dates and/or times as arguments. Functions that care only about the date
must ignore any time information that is provided. Functions that care only about the time must ignore
any date information that is provided.
4766 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 4777 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
L.2.16.9.1 Date Conversion for Serial Values
All date values stored in cells within a SpreadsheetML file are stored in the ISO 8601 format.
For compatibility, a SpreadsheetML application can interpret serial-number values in cells or in formulas
as dates. This subclause describes how serial number values can be converted to date values depending
on the compatibility mode.
A date that can be interpreted as a numeric value is a serial value. This is made up of a signed integer
date component and an unsigned fractional time component. Going forward in time, the date
component of a serial value increases by 1 each day. A serial value represents a UTC date and time, and,
as such, has no timezone information.
Three different bases can be used for converting dates into serial values:
 In the 1900 date base system, the lower limit is January 1, -9999 00:00:00, which has serial
value -4346018. The upper-limit is December 31, 9999, 23:59:59, which has serial value
2,958,465.9999884. The base date for this date base system is December 30, 1899, which has a
serial value of 0.
 In the 1900 backward compatibility date-base system, the lower limit is January 1, 1900,
00:00:00, which has serial value 1. The upper limit is December 31, 9999, 23:59:59, which has
serial value 2,958,465.9999884. The base date for this date base system is December 31, 1899,
which has a serial value of 0.
 In the 1904 backward compatibility date-base system, the lower limit is January 1, 1904,
00:00:00, which has serial value 0. The upper limit is December 31, 9999, 23:59:59, which has
serial value 2,957,003.9999884. The base date for this date base system is January 1, 1904,
which has a serial value of 0.
For the 1900 date base system:
The serial value -2338.0000000… represents 1893-08-05
The serial value 2.0000000… represents 1900-01-01
The serial value 3687.0000000… represents 1910-02-03
The serial value 38749.0000000… represents 2006-02-01
The serial value 2958465.0000000… represents 9999-12-31
For the 1904 backward compatibility date base system:
The serial value -3800.0000000… represents 1893-08-05
The serial value 0.0000000… represents 1904-01-01
The serial value 2225.0000000… represents 1910-02-03
The serial value 37287.0000000… represents 2006-02-01
The serial value 2957003.0000000… represents 9999-12-31
©ISO/IEC 2016 – All rights reserved 4767\n\n--- Page 4778 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
L.2.16.9.2 Time Conversion for Serial Values
The time component of a serial value ranges in value from 0–0.99999999, and represents times from the
instant starting 0:00:00 (12:00:00 AM) to the last instant of 23:59:59 (11:59:59 P.M.), respectively.
Going forward in time, the time component of a serial value increases by 1/86,400 each second. (As
such, the time 12:00 has a serial value time component of 0.5.)
The serial value 0.0000000… represents 00:00:00
The serial value 0.0000115… represents 00:00:01
The serial value 0.4207639… represents 10:05:54
The serial value 0.5000000… represents 12:00:00
The serial value 0.9999884… represents 23:59:59
L.2.16.9.3 Combined Date and Time Conversion for Serial Values
Any date component can be added to any time component to produce a serial value for that date/time
combination. The resulting serial value encodes that date whose (positive or negative) time span from
base date in the respective date-base equals the serial value.
For the 1900 date base system:
The serial value -2337.999989… represents 1893-08-05T00:00:01Z
The serial value 3687.4207639… represents 1910-02-03T10:05:54Z
The serial value 1.5000000… represents 1900-01-01T12:00:00Z
The serial value 2958465.9999884… represents 9999-12-31T23:59:59Z
For the 1904 backward compatibility date base system:
The serial value -3799.999989… represents 1893-08-05T00:00:01Z
The serial value 2225.4207639… represents 1910-02-03T10:05:54Z
The serial value 0.5000000… represents 1904-01-01T12:00:00Z
The serial value 2957003.9999884… represents 9999-12-31T23:59:59Z
L.2.16.10 XML Representation
A formula is represented in a worksheet's XML by an f element that contains the text of the formula,
and a v element that contains the text version of the last computed value for that formula. This pair of
elements is inside a c element, which is, in turn, is inside a row element. Consider the scalar formula
SQRT(C2^2+D2^2), where C2 refers to a cell containing the number 12.5, and D2 refers to a cell
containing the number 9.6. The corresponding XML might be as follows:
4768 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 4779 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
<row r="2" spans="2:4">
<c r="B2" s="40">
<f>SQRT(C2^2+D2^2)</f>
<v>15.761027885261798</v>
</c>
<c r="C2" s="0">
<v>12.5</v>
</c>
<c r="D2" s="0">
<v>9.6</v>
</c>
</row>
In the scalar formula CONCATENATE("The total is ",C7," units"), C7 refers to a cell
containing the number 23. The corresponding XML might be as follows:
<row r="7" spans="2:4" ht="285">
<c r="B7" s="4" t="str">
<f>CONCATENATE("The total is ",C7," units")</f>
<v>The total is 23 units</v>
</c>
<c r="C7" s="0">
<v>23</v>
</c>
</row>
As the function CONCATENATE returns a string, the value for the cell's t attribute is str.
L.3 Introduction to PresentationML
This clause contains a detailed introduction to the structure of a PresentationML document.
The PresentationML file format can be broken down into the following subjects:
 Presentation
 Slides
 Slide Content
 Animation
There are other schemas—most notably DrawingML—that make up a sizeable chunk of the
PresentationML file format. These schemas are addressed separately in §L.4.
L.3.1 Basics
L.3.1.1 Introduction
This subclause provides a high-level overview of PresentationML.
©ISO/IEC 2016 – All rights reserved 4769\n\n--- Page 4780 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
The PresentationML file format can be broken down into the following subjects:
 Presentation
 Slides
 Slide Content
 Animation
The best way to understand the content in each of these subjects is to cover them in that particular
order.
There are other schemas—most notably DrawingML—that make up a sizeable chunk of the
PresentationML file format. These schemas are addressed separately.
This subclause introduces the first subject, “Presentation”. Other subclauses build on this foundation.
L.3.1.2 Basic Utilities
PresentationML contains a set of complex types and simple types that are used by other schemas. The
types, or utilities, are used in a variety of cases. Their single implementation provides for rapid and less
error-prone changes throughout an implementation.
To provide some insight into the type of information that is being repurposed, here is a sample of these
utilities:
 Empty Element
 Name
 Direction
 Index and Index Range
 Slide Show ID
 Slide List Choice
 Slide Relationship
 Customer Data
 Future Extensibility
Each of these is discussed in the following subclauses.
L.3.1.2.1 Empty Element
Sometimes, the simple presence of an element is sufficient to convey meaning. That is, in some cases,
you do not necessarily need information to be a Boolean, an integer, or complex type.
A simple example is the Show Type element group. In this case, a slide show can be one of three types:
present, browse, or kiosk. The schema for this element group is as follows:
4770 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 4781 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
<xsd:group name="EG_ShowType">
<xsd:choice>
<xsd:element name="present" type="CT_Empty">
</xsd:element>
<xsd:element name="browse" type="CT_ShowInfoBrowse">
</xsd:element>
<xsd:element name="kiosk" type="CT_Empty">
</xsd:element>
</xsd:choice>
</xsd:group>
L.3.1.2.2 Name
Many constructs within a presentation have names associated with them. In some cases, the names are
machine-generated, such as shape names (e.g., rectangle1), while others are user-defined, such as slide
shows (e.g., customer-ready).
In one implementation the name simple type is simply an xsd:string. The intent is to restrict this to the
appropriate pattern allowed for named constructs. The tentative restriction pattern is:
[ \t]*[^ \t].*
L.3.1.2.3 Direction
This multi-purpose simple type is used to convey horizontal versus vertical direction of a variety of
types. Such usage can be found in the definition of slide transitions and various shape effects.
L.3.1.2.4 Index and Index Range
These two utilities are generally used to denote a contiguous set of items within a list. The classic
example of usage would be the selection of a set of slides to print.
From a schema-perspective, there is no way to enforce that the start index be equal to or less than the
end index.
L.3.1.2.5 Slide Show ID
This defines the ID for a slide show (also called a custom show). Because slide shows can be named, and
that name can change, an implementation needs a method of referring to a slide show that can
withstand name changes made by the user. In many cases, for example, with a slide, we can leverage
the fact that each slide has a part within the package, in which case we can use the relationship ID.
However, since there is no part for each slide show, we are forced to generate an unsigned integer for
each slide show and use that.
There is nothing in the schema that prevents two or more slide shows from having the same ID.
©ISO/IEC 2016 – All rights reserved 4771\n\n--- Page 4782 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
L.3.1.2.6 Slide List Choice
There are many cases in which a user needs to specify a set of slides for an operation. The canonical
example is what slides to include in your slide show. Because this operation is frequently required in the
file format, one implementation has provided a utility to facilitate this:
<xsd:group name="EG_SlideListChoice">
<xsd:choice>
<xsd:element name="sldAll" type="CT_Empty" />
<xsd:element name="sldRg" type="CT_IndexRange" />
<xsd:element name="custShow" type="CT_CustomShowId" />
</xsd:choice>
</xsd:group>
As the schema above declares, when selecting a set of slides, the user can select all of the slides, a slide
range (by declaring a pair of start and end indices) or a particular custom show.
L.3.1.2.7 Slide Relationship
As described in the Slide Show ID paragraphs above, there are many situations where the format needs
to store an ordered list of slides, and does so by storing their slide IDs. This is implemented using two
types: a list entry complex type and a list complex type:
<xsd:complexType name="CT_SlideRelationshipListEntry">
<xsd:attribute ref="r:id" use="required"/>
</xsd:complexType>
<xsd:complexType name="CT_SlideRelationshipList">
<xsd:sequence>
<xsd:element name="sld" type="CT_SlideRelationshipListEntry"
minOccurs="0" maxOccurs="unbounded"/>
</xsd:sequence>
</xsd:complexType>
L.3.1.2.8 Customer Data
There is a set of utilities that facilitate the storage of customer XML data within the file format.
Although a topic for a separate paper, essentially, this functionality comes down to the ability to store
extra-standard XML in the file format in a way that it can be easily queried, modified and/or surfaced in
the presentation. Suffice it to say, the data is stored in a separate part within the package, and hence
the utility pairs the object using it with the part within the package.
L.3.1.2.9 Future Extensibility
There is functionality that provides the ability to extend a subset of objects within the file format for
inclusion of additional data over the lifetime of the file format. The utilities provide both the ability to
add an alternative representation (e.g., provide a raster image in addition to the XML data for a
diagram) as well as additional properties to the objects.
4772 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 4783 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
L.3.1.3 The Presentation Object
PresentationML also defines the content of the principal or start part for a PresentationML document.
This content includes both structural and presentation-level data for the presentation.
Astute readers should quickly identify an apparent duplication of presentation-level data, as there is also
a separate part which contains presentation-level data. That being said, there is actually no duplication.
Rather, the differentiation of what presentation-level data goes into which part is based on two user
scenarios: document signatures and document sanitization.
In a document signature scenario, assume a user digitally signs a presentation. There exist two kinds of
data within the presentation package: data which changes the “content” of the presentation and data
which is intended to configure an editor or the behavior of an editor. In the first case, any modification
to data which changes the “content” of the presentation must invalidate the signature; in the second
case, any modification to that data should not invalidate the signature.
A classic example of this scenario deals with Kinsoku information and the publish path in the HTML
settings. If the user changes the Kinsoku information in a file, the file looks like (and potentially means)
something different. This is in contrast to a user setting a new HTML publish path for their particular
computer.
In a document sanitization scenario, users want to remove all non-necessary information from the file.
A typical usage case would be posting a presentation to a company’s Internet site. In this case, you
don’t want certain configuration information publicly available. The ideal manner of removal would be
to remove an entire part from the presentation package as opposed to editing a part from a package.
Going back to our Kinsoku and HTML publish path example above, the Kinsoku information needs to
remain with the file. The HTML publish path could give away internal information about web servers
that could be used to facilitate an attack or, more likely, simply provide information about the author to
the public (e.g., the path c:\documents and settings\shawnv\webpages strongly implies that “shawnv”
published this document).
Going back to the original question—what presentation-level data goes in which part—we see that data
that does not invalidate a digital signature or data that should be removed during a sanitization pass
should be stored in the Presentation Properties part and other presentation-level data should be stored
in the Presentation part.
In addition to structural and presentation-level data defined by this schema, there are also definitions
for handling customer data and future extensibility. Again, both of these are addressed in additional
papers.
L.3.1.3.1 Structural Information
From a structural information perspective, there are two sets of data defined in this schema: core lists
and sizes.
©ISO/IEC 2016 – All rights reserved 4773\n\n--- Page 4784 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
The schema first defines a number of lists that serve as the foundation for most objects in the
presentation. These lists are as follows:
 Slide IDs
 Slide Masters
 Notes Masters
 Handout Masters
 Custom Shows
It is essential that the reader fully understand the implementation of usage of these lists as they are the
foundation for almost all solutions that operate—open, interrogate, modify, write—against the
PresentationML file format.
As mentioned above, the lists are defined as a part of list entry and list complex types. The slide master
list is defined as follows:
<xsd:complexType name="CT_SlideMasterIdListEntry">
<xsd:attribute ref="r:id" use="required" />
</xsd:complexType>
<xsd:complexType name="CT_SlideMasterIdList">
<xsd:sequence>
<xsd:element name="sldMasterId" type="CT_SlideMasterIdListEntry"
minOccurs="0" maxOccurs="unbounded" />
</xsd:sequence>
</xsd:complexType>
Although not complex or difficult to understand, the lists are called out because they are vital to any
solution.
The next pieces of structural information are the sizes for the slides and the notes slides. By storing this
information at the presentation level, the implication is that all slides (or all notes slides) in a
presentation have the same size. This further implies that all slides in a presentation share the same
orientation (i.e., they are all landscape-oriented or all portrait-oriented).
L.3.1.3.2 Presentation-Level Properties
The presentation-level properties defined in this schema can be grouped into the following groupings:
 Text-Related
 Save-Related
 Editor-Related
 Content-Related
A description for each property within each group follows.
4774 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 4785 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
L.3.1.3.2.1 Text-Related Properties
The first property stores information related to the Kinsoku settings. Kinsoku settings define the list of
characters that are not allowed to start or end a line of text for a given East Asian language.
The schema definition of the Kinsoku settings is relatively straightforward: identify the language, the set
of start characters, and the set of end characters that do not afford breaking opportunities:
<xsd:complexType name="CT_Kinsoku">
<xsd:attribute name="lang" type="xsd:string" use="optional">
</xsd:attribute>
<xsd:attribute name="invalStChars" type="xsd:string" use="required">
</xsd:attribute>
<xsd:attribute name="invalEndChars" type="xsd:string" use="required">
</xsd:attribute>
</xsd:complexType>
The second property stores a flag to use strict characters for starting and ending a line of Japanese text.
Naturally, this is a simple Boolean attribute:
<xsd:attribute name="strictFirstAndLastChars"
type="xsd:boolean" use="optional" default="true"/>
The final text-related property stores information related to any fonts that are embedded in the
presentation. To do this, we need to store a list of embedded fonts that reference each part that stores
font data (generally, there is a one-font-to-one-part mapping, although this is not a strict rule). This
information is defined using three complex types:
<xsd:complexType name="CT_EmbeddedFontList">
<xsd:sequence>
<xsd:element name="embeddedFont" type="CT_EmbeddedFontListEntry"
minOccurs="0" maxOccurs="unbounded" />
</xsd:sequence>
</xsd:complexType>
©ISO/IEC 2016 – All rights reserved 4775\n\n--- Page 4786 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
<xsd:complexType name="CT_EmbeddedFontListEntry">
<xsd:sequence>
<xsd:element name="font" type="a:CT_TextFont" minOccurs="1"
maxOccurs="1" />
<xsd:element name="regular" type="CT_EmbeddedFontDataId"
minOccurs="0" maxOccurs="1"/>
<xsd:element name="bold" type="CT_EmbeddedFontDataId"
minOccurs="0" maxOccurs="1"/>
<xsd:element name="italic" type="CT_EmbeddedFontDataId"
minOccurs="0" maxOccurs="1"/>
<xsd:element name="boldItalic" type="CT_EmbeddedFontDataId"
minOccurs="0" maxOccurs="1" />
</xsd:sequence>
</xsd:complexType>
<xsd:complexType name="CT_EmbeddedFontDataId" >
<xsd:attribute ref="r:id" use="required"/>
</xsd:complexType>
L.3.1.3.2.2 Save-Related Properties
There is a set of properties that indicate to the editor what should be saved as part of the presentation.
The first such property controls the inclusion of Personally Identifiable Information (“PII”). PII is any
information that can be used to identify the author or contributor to a presentation. And while there
are cases where this information is exposed visually to the user (e.g., author name in a comment shape),
there are other cases where the information is not immediately evident to the user (e.g., the document
author name in the list of document properties).
An implementation can provide a mechanism by which the author of a presentation can configure a file
to always remove any PII that might otherwise by normally included during a regular save operation.
While not a guarantee that no PII is stored in the file (e.g., consider a shape with my name in it—in some
cases it describes content in the file [my position in my group’s organization chart] whereas in others it
is an editorial directive [“check with ShawnV on this point”]. Given this ambiguity, we cannot solve all
cases of this. As a result, this is more a convenience feature than a privacy management feature.
The second set of save-related properties has two groupings of properties. The first controls whether or
not fonts are embedded into the package representing the presentation. The second, enabled by
setting the first, allows an implementation to optimize such font embedding to keep the size minimal, at
the cost of future editing on other machines.
<xsd:attribute name="embedTrueTypeFonts" type="xsd:boolean"
use="optional" default="false"/>
<xsd:attribute name="saveSubsetFonts" type="xsd:boolean"
use="optional" default="false"/>
4776 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 4787 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
The user scenario behind these properties is as follows. Assume you are putting together a presentation
to distribute to external customers. You happen to use an East Asian font with an on-disk file size of
around 5 megabytes.
Assuming that this font is not a standard font that is widely distributed, not including this font causes
font substitution when the presentation is opened on machines that don’t have a copy of the font. In
any case, this can radically change the visual appearance of the presentation; in some cases, it can
render the presentation unreadable.
Because you cannot afford the presentation to be unreadable or to look unprofessional, you decide to
embed the font. By default, the implementation sets embedTrueTypeFonts to true and embeds the
entire 5 megabyte font file in the presentation package. This clearly bloats the file, but ensures that
anyone viewing or editing this file has the same font experience as you originally had (subject to
licensing restrictions, of course).
Since you are distributing the presentation, and your primary purpose is for people to view the
presentation, you can reduce the amount of font data embedded in the presentation package. By
setting the second property (saveSubsetFonts) to true, only those characters in the font that were
actually used to create the presentation are saved. This yields less font data stored in the file at the cost
of not being able to use unused characters in future edits of the presentation on different machines.
The third property related to saving, controls whether or not an implementation can automatically
compress pictures contained in the presentation. This is particularly important given the proliferation of
digital cameras and scanners and the increasing importance of small files (e.g., to save network
bandwidth, reduce storage required for mail and file servers, etc.).
The final property in this set specifies a password that is required to enable editing of the file using the
implementation. Because this is a convenience feature intended to prevent accidental changes to
information, it is stored in clear text as an xsd:string.
By storing this information in the file, the implementation prompts the user for this password in order to
open the file read/write; if the user does not provide the correct modify password, the
implementationopens the file read-only.
L.3.1.3.2.3 Editor-Related Properties
The presentation file itself contains data that provide configuration information for the
implementation’s editor.
For example, the presentation can define a set of smart tags for use while editing the particular
presentation. Because Smart Tags are stored in a separate part, the presentation object contains the
relationship ID of the Smart Tag part.
In a fully functioning OLE server, PresentationML objects can be embedded into OLE containers, during
which time a customer can set a zoom scale. This is stored in the file as a percentage called serverZoom.
©ISO/IEC 2016 – All rights reserved 4777\n\n--- Page 4788 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
An internationalized application might support configuring the editor to respect different screen
orientations. For example, in regions of the world where Complex Scripts are in use, it is customary to
orient the screen right-to-left. As such, a presentation can request the editor reconfigure itself for such
usage scenarios.
Finally, due to changes in the file format and functionality (e.g., graphics and text engines),
PresentationML introduces some end-user complexity when working collaboratively with other
customers using older versions. To help remedy this, an implementation might support a Compatibility
Mode, which restricts the functionality exposed by the editor to optimize the output for the best cross-
version collaboration story possible. As a result, each presentation needs to opt-into this mode.
L.3.1.3.2.4 Content-Related Properties
This set of properties is related to the actual content in the presentation.
End-users can define the starting slide number for numbered slides in each presentation. While it
typically starts at one, the user can select any positive number to begin slide numbering. The primary
user scenario is when compiling a mega-presentation that is a collection of multiple presentations. A
secondary user scenario is when including a presentation in the middle of or at the end of a printed
document where you want the slide/page numbers to continue.
Another content-related property controls whether or not header/footer placeholders are to be shown
on title slides. In many cases users use special shapes called header and footer placeholder that contain
built-in field codes that control the display of various sorts of information like the date/time and slide
number.
In most cases, users like to keep their title slides as simple as possible (much like in the printed world
where you want your first page to be clean and streamlined) and hence do not want data like
date/times and slide numbers to show up on such slides. This attribute defines this presentation-wide.
The final property relates to creating photo albums. The implementation has a feature that allows the
user to generate automatically a presentation based on a set of pictures. During this process, the user
can select from a variety of settings, including, but not limited to, what pictures to include, the layout of
the pictures on the slides (e.g., one picture per slide, two pictures per slide, etc.), what type of frame
shape to use, etc. All of this information is stored in the presentation for future photo album creation.
L.3.1.4 Presentation Properties
Those properties that apply to the presentation as a whole, and that are likely to be removed during
document sanitization, or are not going to invalidate a digital signature, are defined in the Presentation
Properties part. These properties can be grouped into three primary groupings.
 HTML Publish Properties
 Print Properties
 Slide Show Properties
 View Properties
4778 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 4789 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
In addition to this grouping, there are properties that define a Most Recently Used (“MRU”) list of colors
as well as providing for future extensibility. (The MRU is discussed in a DrawingML paper and the
extensibility is discussed in a similar paper.)
L.3.1.4.1 HTML Publish Properties
An implementation must have the ability to save (and publish) a presentation to a web-friendly format
like HTML or MHTML. Various parameters are used to configure the application for saving such formats
as well as to control what content gets generated. The parameters that configure the application are
the HTML Publish properties whereas the content properties are the Web Properties.
The HTML Publish properties provide the author with the ability to control what content gets displayed
in the browser when the resulting file—either HTML or MHTML—is viewed using that kind of an
application. For example, the speaker notes can either be displayed in the frameset or can be hidden
from view. This is particularly useful when a speaker’s notes are not necessarily in a customer-ready
format. It’s useful but not necessarily secure.
The author can also specify the title to be displayed in the browser. Although this defaults to the actual
file name, or if that is missing, to the content of the first slide’s title placeholder, it can be overridden by
the author.
Finally the author can specify a publish path to use when saving this file in this format. This is
particularly useful for two reasons.
First, because there is a transformation happening, it sometimes takes a few iterations of publishing to
get the browser-based experience to be exactly what you want. A classic example of this is the differing
animation capabilities between the implementation and certain browsers: it is important to verify that
the change in animation behavior continues to work after publishing; if you are not satisfied with the
experience, sometimes you need to change the animation in the implementation and republish.
The second reason storing the path is useful is that web server paths can be cumbersome and are often
not on the tip of each user’s tongue. This allows the user to specify the path once and then publish
using the same location without having to re-specify it. Naturally, being stored in the file format, this
allows this data to persist across session.
Indirectly, the HTML Publish properties can prime the Web Properties by defining a target web browser
generation (i.e., third, fourth or third and fourth). This is done by setting the appropriate
ST_HtmlPublishWebBrowserSupport attribute:
<xsd:complexType name="CT_HtmlPublishProperties">
<xsd:sequence>
<xsd:group ref="EG_SlideListChoice" minOccurs="1" maxOccurs="1">
</xsd:group>
</xsd:sequence>
©ISO/IEC 2016 – All rights reserved 4779\n\n--- Page 4790 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
<xsd:attribute name="showSpeakerNotes" type="xsd:boolean"
use="optional" default="true" />
<xsd:attribute name="pubBrowser"
type="ST_HtmlPublishWebBrowserSupport"
use="optional" default="v3v4" />
<xsd:attribute name="title" type="xsd:string" use="optional"
default="">
</xsd:attribute>
<xsd:attribute ref="r:id" use="required">
</xsd:attribute>
</xsd:complexType>
By providing a target generation, the Web Properties are set to a predefined package defined for the
specified browser generation. Naturally, the user can override the individual Web Property settings.
L.3.1.4.1.1 Web Properties
As mentioned in the previous subclause, these properties configure the output of the presentation
when saved using the HTML or MHTML formats. In this case, a number of parameters can be controlled.
In all multi-slide cases where the presentation is saved using one of these formats, the implementation
creates a frameset to bring the various parts of a presentation—the slide content, the speaker notes and
the outline—together as well as provide for simple navigation. The color of the HTML frames, the
background used and the user interface controls can be controlled to leverage browser settings, use
high contrast, etc.
The author can also control how much interactivity is exposed in the resulting output. For example, the
user might elect to disable slide animations and transitions and opt for a more static presentation.
Similarly, the author might elect to disable certain scripting features like the ability to resize dynamically
the output to match the size of the browser window.
Somewhat related to this is the ability to specify the target screen size which is especially important
when targeting the earlier browser generations or user environments where features like JavaScript are
disabled.
For an internationalized implementation, there is the ability to control the encoding of text used in the
generation of the HTML or MHTML output.
Finally there are a set of parameters that configure the on-disk storage of the resulting output. For
example, if the customer knows something about the machine configurations of her audience, she can
opt to use better raster graphic formats like PNG that support alpha transparency or elect to include
Vector Markup Language (“VML”) representations only for vector images.
The customer can also provide some indication as to how the output is used. If the customer knows
that the output is used like regular files (perhaps passed around on CDs or moved between file shares)
the user can elect to store the files in a folder to ensure that a straggling file is not lost; if, however, the
4780 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 4791 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
target scenario is to put the files on a web server, the user can skip the folder and save the individual
files in a flat directory. Similarly, if the customer knows that they are using a web server that only
handles “8.3” file names, they can configure the implementation to generate files using names that are
“8.3” compliant, as opposed to using long file names that might otherwise cause such web servers
problems.
L.3.1.4.2 Print Options Properties
There is also a set of properties that control the default print behavior for a presentation. The inclusion
of this information in the file format simply primes the Print dialog when this presentation is used. It
does not force options nor does it represent the last-used set of print options for a presentation.
Using these properties, the author can control the output printed. For example, in some cases, authors
need to print their slides (one slide per printed page) while in other cases, they want to provide printed
handouts for the audience on which to take their own notes (handout pages that can contain anywhere
from three to nine slides per printed page, as well as option lines for note taking). In other cases, the
author would like to print out notes where each printed page has one slide (anchored at the top) and a
text box (anchored at the bottom) with the speaker notes included or simply print the textual outline of
the presentation.
The author can also control whether or not hidden slides are included in the printed output, as well as
whether or not the output is sent to the printer in color, in grayscale, or in pure black and white.
There is also a set of properties that the author can set that determine if slides are framed on the
printed page, if the slides are scaled up to the printed page (e.g., consider non 4x3 aspect ratio slides),
etc.
L.3.1.4.3 Slide Show Properties
This set of presentation-level properties controls the default slide show.
Among the parameters that can be controlled is one that defines the type of slide show. Generally, the
classic slide show is characterized by a presenter presenting the presentation to an audience. The
presenter controls the flow of the presentation, etc. This is referred to as a “present” slide show. In
some cases, however, the presentation is distributed and individuals walk themselves through the slide
show. This is referred to as a “browse” slide show. Finally, there are cases where a slide show is
prepackaged and used as a kiosk; naturally, it is referred to as a “kiosk” slide show.
Furthermore, the customer can control which slides are to be included in the slide show, what color the
pen should be, etc.
Finally, the customer can control various interactivity settings that are to be used for the slide show.
This provides the customer the ability to configure their slide show outside the typical settings for a
particular slide show type. For example, the user can create a slide show that has a pre-configured
animation built with timings (i.e., the time between particular builds or the time between slide
transitions), even though she is going to be presenting the content to an audience.
©ISO/IEC 2016 – All rights reserved 4781\n\n--- Page 4792 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
L.3.1.4.4 View Properties
The View Properties part defines the properties on all of the views found in the implementation.
PresentationML supports the following views (§19.7.55):
 handout view
 normal slide view
 notes master view
 notes view
 outline view
 slide master view
 slide sorter view
 slide thumbnail view
The default view, normal slide viewAdditionally, the default view, Normal View, is a composite view that
pulls from three multiple view property sets.
In general, there is a significant amount of commonality among views. For example, each view contains
four common components:
Scale The zoom scale for the view
Origin The origin of the view
Variable Scaling A special zoom scale that configures the application to
fit the content of the view into whatever view size is
provided
Draft Mode Controls whether or not a view is in draft mode which
is a mode designed to provide the fastest
editing/redraw possible by dropping properties like
font face, certain colors, pictures, etc.
For those views based on a slide (e.g., slide master view) there are additional common components:
Guide List Represents the list of drawing guides for this view
Guide Properties Represents guide properties like direction and position
of each guide in the view
Guide Settings Determines if guides should be shown for this view
Snap Settings Determines if shapes should be snapped to the grid
and/or snapped to other shapes for this view
L.3.2 Slides, Masters, Layouts, and Placeholders
L.3.2.1 Introduction
This subclause provides a high-level overview of the content in the Slide Part.
4782 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 4793 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
The important aspects of the PresentationML Slides file format are introduced in the following order.
 Masters
 Presentation Slide
 Slide Notes
 Slide Layouts
This subclause provides a structured introduction to the slides portion of the PresentationML file
format. Other subclauses build on this foundation and explain more about topics such as animation,
comments, and the presentation object.
L.3.2.2 Masters
For slides the notion of hierarchy and inheritance applies. A master represents a common layout for the
page type in question. For instance, if a slide master had a background set to a gradient fill then all slides
referencing to that slide master would have the same background. In addition to setting common
attributes of the slides such as background and styling information, the slide master also provides
numerous layouts within itself in order to make a presentation that both follows a layout theme and
incorporates a high level of variety. The variety is supported through slide layouts which are discussed in
a later subclause.
L.3.2.2.1 Slide Master
A slide master is a master that is tied specifically to presentation slides. The presentation slides are
those that are shown during a presentation. These are discussed in more detail in a later section on the
Presentation Slide. Within a slide master are some common structural elements that should be
understood, namely:
 Common Data - Common properties that are inherited by the other slides as well as layout
information for presentation slides based on the master slide.
 Header and Footer - Header and footer properties for the presentation slides to inherit.
 Color Map - Color Mapping for the presentation slides to inherit.
 Text Styles - Text Styling information to be used within each placeholder on a presentation slide.
 Slide Layout List - A list of slide layouts that provide the variety needed within any presentation.
These are applied to a presentation slide which inherits both the layout of the slide layout in
addition to the slide design of the slide master.
 Timing Information - Common timing properties used for animation, controls, etc.
 Transition Information - Slide transitioning information to be inherited by each presentation
slide.
©ISO/IEC 2016 – All rights reserved 4783\n\n--- Page 4794 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Slides inheriting information from a slide master do have the ability to specify properties that override
those specified in the slide master.
L.3.2.2.2 Notes Master
A notes master is a master that specifies properties for slide notes pages. The notes page associated
with a presentation slide stores a thumbnail of the presentation slide as well as the presenter's notes
about the slide. These are discussed in more detail in a later section. Within a notes master the
important common structural elements are:
 Common Data - Common properties that are inherited by other notes pages as well as the
layout information for notes pages based on this master slide. The notes master serves as the
pattern for all notes pages.
 Color Map - Color Mapping for the notes pages to inherit.
4784 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 4795 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Notes pages inheriting information from a notes master do have the ability to specify properties that
override those specified in the notes master.
L.3.2.2.3 Handout Master
A handout master determines the layout for all handout pages. The handout pages consist of a place to
store a thumbnail of each slide with additional elements such as header, footer or graphical information.
These are discussed in more detail in a later section. Within a handout master are some common
structural elements that should be understood, namely the following.
 Common Slide Data - Common properties and layout information that are used by all handout
pages. The handout master represents how each handout page looks.
 Header and Footer - Header and footer properties for all handout pages.
 Color Map - Color Mapping for all handout pages.
©ISO/IEC 2016 – All rights reserved 4785\n\n--- Page 4796 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
L.3.2.3 Presentation Slide
A presentation slide is a slide that inherits slide properties from the corresponding slide master and
layout information from the corresponding slide layout. Each presentation slide has the ability to
override any of this information that it chooses by specifying local attribute values within the
presentation slide. Much like the master slide, the presentation slide contains some common structural
elements, namely the following.
 Common Slide Data - Common properties and layout information for this presentation slide.
Properties listed here that conflict with existing elements specified in the slide master override
those specified in the slide master.
 Color Map Override - Color Mapping that overrides the inherited color mapping for this
presentation slide.
 Timing Information - Common timing properties used for animation, controls, etc.
 Transition Information - Slide transitioning information for this presentation slide.
The above list defines the areas that can be used to override inherited components from the master
slide and the layout slide. That is, these can be specifically defined on a per-slide basis via the above
elements.
4786 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 4797 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
L.3.2.4 Notes Page
A notes page inherits slide properties from the corresponding notes master. The initial layout for a notes
page is defined by the single notes master slide. Each notes page has the ability to override any of this
information that it chooses by specifying local attribute values within the notes slide. Much like the
notes master, the notes page contains some common structural elements, namely the following.
 Common Slide Data - Common properties and layout information for this notes page.
 Color Map Override - Color Mapping to override the inherited color mapping for this notes page.
The above list defines the areas that can be used to override inherited components from the notes
master. That is, these can be specifically defined on a per-slide basis via the above elements.
©ISO/IEC 2016 – All rights reserved 4787\n\n--- Page 4798 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
L.3.2.5 Slide Layouts
A slide layout inherits slide properties from the corresponding slide master and sets layout information
for all presentation slides that utilize this layout. Each presentation slide has the ability to override any
of this information that it chooses by specifying local attribute values within the presentation slide.
Much like the slide master, the slide layout contains some common structural elements:
 Common Slide Data - Common properties and layout information that override properties set
within the slide master but are inherited by all presentation slides that utilize this layout.
 Color Map Override - Color Mapping that overrides the inherited color mapping from the slide
master but is inherited by all presentation slides that utilize this layout.
 Header and Footer - Header and footer properties that override properties set within the slide
master but are inherited by all presentation slides that utilize this layout.
 Timing Information - Common timing properties used for animation, controls, etc. These
override properties set within the slide master but are inherited by all presentation slides that
utilize this layout.
 Transition Information - Slide transitioning information to be inherited by each presentation
slide. These override properties set within the master slide but are inherited by all presentation
slides that utilize this layout
The above list defines the areas that can be used to override inherited components from the master
slide. That is, these can be specifically defined on a per-layout basis via the above elements.
L.3.3 Comments
L.3.3.1 Introduction
This document describes the commenting feature for presentations as expressed in PresentationML..
4788 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 4799 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
Note that it is important to keep in mind that comments are not shapes. The representation of them
within the document is left entirely up to the generating application and are thus implementation
specific.
L.3.3.2 Functional Overview
Readers of a presentation can provide feedback to the presentation author in the form of comments.
Comments can only be applied to slides; they cannot be applied to masters of any master type or to
notes slides.
At first glance, comments appear to be shapes on the slide surface; however, they are not. Comments
differ from regular shapes in two ways:
 Comments cannot be formatted or resized
 The text contained within a comment cannot be formatted
L.3.3.3 Comment Author List
Presentations contain a list of all authors who have comments in the presentation. This list is commonly
referred to as the Comment Author List (CAL). The CAL contains one entry for each author. Each entry is
made up of five pieces of data: ID, Author Name, Author Initials, Last Index, and Color Index.
Each author that comments on a presentation is assigned an ID, which is a simple integer. This ID is
unique within the presentation, and is assigned by the application itself.
The Author Name and Author Initials are taken from the application itself. If no initials are known to the
application, the comment author is prompted upon the insertion of the initial comment. Both the
Author Name and Author Initials are simple strings; that is, there is no association of the values with an
identity (from a security or authentication perspective).
The Last Index (lastIdx) is an integer that documents how many comments the associated author has
made in this presentation. When the author makes another comment, that comment is numbered using
the next integer, and then this value is updated once again.
The Color Index (clrIdx) is an integer into a color table that is used to provide the solid background fill
for the comment shape. The utility that this provides is that all of the comments by a particular author
share the same color.
Here is an example of such a CAL:
<p:cmAuthorLst>
<p:cmAuthor id="0" name="Shawn" initials="SV" lastIdx="3" clrIdx="0" />
<p:cmAuthor id="1" name="Brian" initials="BJ" lastIdx="7" clrIdx="1" />
</p:cmAuthorLst>
©ISO/IEC 2016 – All rights reserved 4789\n\n--- Page 4800 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
To determine if an author is already in the CAL, one must consider only the Author Name and Author
Initials data. If they both match an entry in the CAL, the author is already considered to be in the CAL;
otherwise, the author is considered unique, and a separate entry is added for that author in the CAL.
When the presentation is saved using PresentationML, a separate Comment Authors part is created that
contains the CAL.
L.3.3.4 Comment List
Each slide within a presentation can contain zero or more comments. Each slide with at least one
comment starts a list of comments for that slide. Each entry in that list is made up of the following
pieces of data:
 Author ID: This represents the ID of the author who created the comment. It matches an entry
in the CAL.
 Date/Time: This represents the date and time of the last modification of this particular
comment. Although expressed in UTC, its accuracy is dependent on the state of the machine
making the edits.
 Index: This is the number assigned to this particular comment, and is one of the comments
associated with the specified author. This number should be equal to, or less than, the Last
Index value for the author in the CAL. There cannot be duplicate Indexes for the same author.
 Position: This defines the 2D coordinate for the location at which the comment shows up on the
slide surface. This is the position of the upper left point of the comment shape.
 The Text data includes all of the text that makes up the body of the comment. Note that this
text is expressed differently than other text as expressed in DrawingML. As this text contains no
formatting, and is strictly limited to text input, there is no additional data that needs to be
stored.
Here is an example of a comment list for a slide:
<p:cmLst>
<p:cm authorId="0" dt="2006-01-30T22:45:13.597" idx="3">
<p:pos x="10" y="10" />
<p:text>Need to check with Mary on exact data values</p:text>
</p:cm>
<p:cm authorId="1" dt="2006-01-30T22:46:22.082" idx="1">
<p:pos x="106" y="106" />
<p:text>This chart is hard to read from afar</p:text>
</p:cm>
</p:cmLst>
When the presentation is saved using PresentationML, a separate Comments part is created for each
comment list.
4790 ©ISO/IEC 2016 – All rights reserved\n\n--- Page 4801 ---\nLicensed to Yatin Kare (yatin.kare@gmail.com)
ISO Store Order: OP-926892 license #1/ Downloaded: 2025-06-27
Single user licence only, copying and networking prohibited.
ISO/IEC 29500-1:2016(E)
L.3.4 Animation
L.3.4.1 Introduction
This subclause provides a high-level overview of the animation settings in PresentationML. This schema
is loosely based on the syntax and concepts from the Synchronized Multimedia Integration Language
(SMIL), a W3C Recommendation for describing multimedia presentations using XML.
The schema describes all the animations effects on that reside on a slide; it also describes the animation
that occurs when going from slide to slide (slide transition).
Animations on a slide are inherently time-based and consist of an animation effects on an object or text.
However, slide transitions do not follow this concept and always appear before any animation on a slide.
All elements described in this schema are contained within the slide XML file. More specifically, they are
in the transition and the timing element as shown below:
<p:sld>
<p:cSld> …
<p:clrMapOvr> …
<p:transition> …
<p:timing> …
</p:sld>
L.3.4.2 Slide Transitions
Slide transitions are the animation effects that displayed in between slides. They are specified in the
transition element in the slide XML file. For example, consider a slide with a "push" slide transition as
shown below:
©ISO/IEC 2016 – All rights reserved 4791\n