## Log: Map XML to Slide Elements

- **Prompt**: (Implicit) Continuation of the plan to understand the PPTX structure.
- **Issue**: The slide and relationship files are not sequentially numbered, so I had to pick one to analyze.

### What I did:

I analyzed the key XML files that define the presentation, its slides, and their relationships. This provides the foundational knowledge for how to parse the `.pptx` file.

### How I did it:

1.  **`ppt/presentation.xml`**: I read this file to understand how the overall presentation is structured. I identified the `<p:sldIdLst>` element, which contains a list of `<p:sldId>` elements. Each `<p:sldId>` has an `r:id` that points to a specific slide in the `ppt/slides` directory, defining the order of the presentation.

2.  **`ppt/slides/_rels/slide23.xml.rels`**: I examined this relationship file to see how a slide connects to other parts of the presentation. I found:
    -   A `Relationship` of type `http://.../image` that links to an image file in the `ppt/media` directory via the `Target` attribute.
    -   A `Relationship` of type `http://.../notesSlide` that links to the slide's notes.
    -   A `Relationship` of type `http://.../slideLayout` that links to a specific slide layout in `ppt/slideLayouts`.

3.  **`ppt/slides/slide23.xml`**: I analyzed the content of a slide file to identify the core elements:
    -   **`<p:sp>` (Shape)**: This seems to be a container for either text or other objects.
    -   **`<p:txBody>` (Text Body)**: This element within a `<p:sp>` contains the text of a shape.
    -   **`<a:t>` (Text Run)**: The actual text content is within this element.
    -   **`<p:pic>` (Picture)**: This element represents an image on the slide.
    -   **`<p:blipFill>`**: This element inside a `<p:pic>` contains the `<a:blip>` element.
    -   **`<a:blip r:embed>`**: This attribute contains the `r:id` that links to the image file in the `media` directory, as defined in the slide's `.rels` file.

### Future work:

Now that I have a basic understanding of the XML structure, I need to cross-reference this with the official ECMA-376 documentation to solidify my understanding and ensure I'm interpreting the tags correctly. I will then be ready to write the `schema_notes.md` file.
