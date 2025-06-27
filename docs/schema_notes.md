# PPTX OpenXML Schema Notes

This document outlines the key findings from analyzing the `.pptx` file format, grounded in the ECMA-376 standard. It will serve as the technical reference for building the parser.

## 1. Core File Structure

A `.pptx` file is a ZIP archive containing a collection of XML files and other resources. The primary directory of interest is `ppt/`.

-   **`ppt/presentation.xml`**: The main file defining the presentation. It contains the slide master list, notes master list, and the slide ID list (`<p:sldIdLst>`), which dictates the order of the slides.
-   **`ppt/slides/`**: Contains the individual slide XML files (e.g., `slide1.xml`).
-   **`ppt/slides/_rels/`**: Contains relationship files for each slide. For example, `slide1.xml.rels` defines the relationships from `slide1.xml` to other resources like images, notes, and layouts.
-   **`ppt/media/`**: Stores all embedded media files (images, audio, etc.).
-   **`ppt/slideLayouts/`**: Defines the structure and placeholders for different slide layouts.
-   **`ppt/slideMasters/`**: Defines the overall theme and master layout for the presentation.

## 2. Slide Content Breakdown (`ppt/slides/slideN.xml`)

Each slide XML file contains a `<p:cSld>` (common slide data) element, which in turn contains a `<p:spTree>` (shape tree). The shape tree holds all the visible elements on the slide.

### Key Elements:

-   **`<p:sp>` (Shape):** The fundamental container for content.
    -   It has a `<p:nvSpPr>` (non-visual shape properties) section for ID, name, etc.
    -   It has a `<p:spPr>` (shape properties) section defining its position, size, and style.

-   **`<p:txBody>` (Text Body):** Found within a `<p:sp>`, this element contains the text.
    -   It contains one or more `<a:p>` (paragraph) elements.
    -   Each `<a:p>` contains one or more `<a:r>` (run) elements.
    -   Each `<a:r>` contains the actual text in an **`<a:t>`** element.

-   **`<p:pic>` (Picture):** Represents an image.
    -   It contains a `<p:blipFill>` element.
    -   The `<p:blipFill>` contains an **`<a:blip>`** element.
    -   The `<a:blip>` element has an `r:embed` attribute with a relationship ID (e.g., `"rId2"`).

## 3. Relationships (`.rels` files)

Relationships are crucial for resolving links between different parts of the presentation.

-   The `r:embed` ID from an `<a:blip>` element in `slideN.xml` is resolved by looking in `ppt/slides/_rels/slideN.xml.rels`.
-   In the `.rels` file, a `Relationship` element with the matching `Id` will have a `Target` attribute pointing to the actual media file in the `ppt/media/` directory (e.g., `Target="../media/image1.png"`).

## 4. Parsing Workflow

1.  Unzip the `.pptx` file.
2.  Parse `ppt/presentation.xml` to get the list and order of slide IDs.
3.  For each slide ID:
    a.  Open the corresponding `ppt/slides/slideN.xml` file.
    b.  Parse the `<p:spTree>` to find all shapes (`<p:sp>`) and pictures (`<p:pic>`).
    c.  For each shape, extract the text from `<p:txBody>` -> `<a:p>` -> `<a:r>` -> `<a:t>`.
    d.  For each picture, get the `r:embed` ID from the `<a:blip>` element.
    e.  Open the corresponding `ppt/slides/_rels/slideN.xml.rels` file.
    f.  Find the `Relationship` with the matching `Id` to get the `Target` path to the image file in `ppt/media/`.
4.  Copy the media files to the output directory.
5.  Generate the final HTML or JSON output.
