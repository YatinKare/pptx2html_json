## Log: Parse Presentation Order

- **Prompt**: (Implicit) First task in Phase 5: Scale to Full Presentation.
- **Issue**: None.

### What I did:

I implemented the `PresentationParser` class, which is responsible for parsing the `ppt/presentation.xml` file to extract the order of slides in the presentation. This is a crucial step for processing multi-slide presentations.

### How I did it:

1.  **Created `src/learnx_parser/presentation_parser.py`:**
    -   Defined the `PresentationParser` class with an `__init__` method that takes the path to `presentation.xml`.
    -   Implemented `get_slide_order` to:
        -   Parse the `presentation.xml` using `lxml`.
        -   Find the `<p:sldIdLst>` element.
        -   Iterate through each `<p:sldId>` element within `sldIdLst`.
        -   Extract the `r:id` attribute from each `sldId`, which corresponds to the relationship ID of a slide.
        -   Return a list of these slide IDs in the order they appear in the XML.

2.  **Created `tests/test_presentation_parser.py`:**
    -   Created a `pytest.fixture` for `presentation_parser` using the sample `presentation.xml`.
    -   Implemented `test_get_slide_order` to:
        -   Assert that the returned `slide_order` is a list and is not empty.
        -   Assert that a known slide ID (`rId2`) from the sample presentation is present in the list.

### Future work:

With the ability to get the slide order, the next task is `iterate_over_all_slides`. This will involve using the `PresentationParser` to get the slide order and then iterating through each slide, parsing it with the `SlideParser`, and generating output using the `HtmlWriter` and `JsonWriter`.
