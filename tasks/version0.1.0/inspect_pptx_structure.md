## Log: Inspect PPTX Structure

- **Prompt**: I have given you an example .pptx file: @example/Galaxy presentation.pptx
- **Issue**: None.

### What I did:

I unzipped the provided `.pptx` file and listed its contents to understand the basic structure of a PowerPoint file.

### How I did it:

1.  I used the `unzip` command to extract the `.pptx` file's contents into a temporary directory (`/tmp/pptx_unpacked`).
2.  I then used `ls -R` to recursively list the files and directories within the unpacked folder.

### Key Findings (High-Level Structure):

-   **`[Content_Types].xml`**: An XML file that defines the content types of all the different parts within the `.pptx` package.
-   **`_rels/`**: This directory contains relationship files (`.rels`). The main `.rels` file defines the relationships for the entire package, such as the main presentation file.
-   **`docProps/`**: Contains metadata about the document.
    -   `app.xml`: Application-specific properties.
    -   `core.xml`: Core properties like author, title, etc.
    -   `custom.xml`: Custom user-defined properties.
    -   `thumbnail.jpeg`: A thumbnail image of the presentation's first slide.
-   **`ppt/`**: The core directory containing the presentation's content.
    -   **`presentation.xml`**: The main XML file that defines the overall presentation, including the order of the slides.
    -   **`slides/`**: Contains one XML file for each slide in the presentation (e.g., `slide1.xml`, `slide2.xml`).
    -   **`slideLayouts/`**: XML files that define the layout and structure for different types of slides.
    -   **`slideMasters/`**: XML files for the master slides, which control the overall theme and default layout.
    -   **`theme/`**: Contains XML files defining the visual theme (colors, fonts, effects).
    -   **`media/`**: Stores all the media files embedded in the presentation, such as images.
    -   **`notesSlides/`**: Contains XML files for the speaker notes for each slide.
    -   **`_rels/`**: A subdirectory containing relationship files specific to the presentation, linking slides, media, and other resources.

### Future work:

Now that I have a high-level overview, the next step is to dive deeper into the XML files themselves to understand how they define the content and structure of the slides. I will proceed with the `map_xml_to_slide_elements` task.
