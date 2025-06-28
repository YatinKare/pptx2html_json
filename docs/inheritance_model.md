# PPTX Property Inheritance Model

This document outlines the property inheritance rules within a PowerPoint (.pptx) file, crucial for accurately rendering slide content. Properties are resolved by looking up values in a specific hierarchy, from the most specific (slide element) to the most general (theme).

## 1. Inheritance Hierarchy (General to Specific)

Properties are typically inherited in the following order, with more specific definitions overriding more general ones:

1.  **Theme (`ppt/theme/theme*.xml`)**:
    -   Defines global default styles, colors, fonts, and effects for the entire presentation.
    -   Provides base properties for text, shapes, and backgrounds.

2.  **Presentation Properties (`ppt/presProps.xml`, `ppt/viewProps.xml`)**:
    -   Contains presentation-wide settings, though less directly involved in individual element styling than themes.

3.  **Slide Master (`ppt/slideMasters/slideMaster*.xml`)**:
    -   Defines the overall design and layout for a set of slides.
    -   Properties defined here (e.g., default text styles for title, body) override theme properties.
    -   Includes placeholder (`<p:ph>`) definitions that can carry default properties.

4.  **Slide Layout (`ppt/slideLayouts/slideLayout*.xml`)**:
    -   Defines the structure and positioning of content on a specific type of slide (e.g., Title Slide, Title and Content).
    -   Properties defined here override those from the slide master.
    -   Placeholders in the layout (`<p:ph>`) inherit from corresponding placeholders in the master.

5.  **Individual Slide (`ppt/slides/slide*.xml`)**:
    -   Contains the actual content of each slide.
    -   Properties explicitly defined on shapes (`<p:sp>`), text runs (`<a:rPr>`), or pictures (`<p:pic>`) directly within the slide XML override all inherited properties.

## 2. Key XML Files and Their Roles

-   **`ppt/theme/theme*.xml`**: Contains `<a:theme>` element. Look for `<a:fontScheme>`, `<a:fmtScheme>`, `<a:clrScheme>` for default fonts, effects, and colors. Text styles are often defined within `<a:txStyles>`. 
-   **`ppt/slideMasters/slideMaster*.xml`**: Contains `<p:sldMaster>` element. Defines common elements and formatting for slides based on this master. Placeholders (`<p:ph>`) within `<p:spTree>` define default properties for content areas.
-   **`ppt/slideLayouts/slideLayout*.xml`**: Contains `<p:sldLayout>` element. Defines the arrangement of placeholders and other elements for a specific layout. Placeholders here also have `<p:ph>` elements.
-   **`ppt/slides/slide*.xml`**: Contains `<p:sld>` element. Individual shapes (`<p:sp>`) and pictures (`<p:pic>`) have their own properties (`<p:spPr>`, `<p:txBody>`, `<a:rPr>`) that can override inherited values.
-   **`ppt/presProps.xml`**: Contains presentation-wide properties like default slide size (`<p:sldSz>`).
-   **`ppt/viewProps.xml`**: Contains properties related to how the presentation is viewed (e.g., zoom level), less relevant for content rendering.

## 3. Property Resolution Example (Text)

To determine the effective font size of a piece of text:

1.  Check the `<a:rPr>` (run properties) of the specific `<a:t>` (text run) in `slide*.xml`.
2.  If not found, check the paragraph properties (`<a:pPr>`) of the containing `<a:p>` (paragraph).
3.  If not found, check the text body properties (`<a:bodyPr>`) of the containing `<p:txBody>`.
4.  If not found, check the properties of the placeholder (`<p:ph>`) in `slide*.xml` (if the text is in a placeholder).
5.  If not found, check the corresponding placeholder in the `slideLayout*.xml`.
6.  If not found, check the corresponding placeholder in the `slideMaster*.xml`.
7.  Finally, if still not found, fall back to the default text styles defined in the `theme*.xml`.

This hierarchical lookup applies to various properties, including position, size, fill color, line style, etc.
