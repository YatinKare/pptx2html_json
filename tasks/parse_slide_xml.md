## Log: Parse Slide XML

- **Prompt**: (Implicit) First task in Phase 3: Single Slide Parser Prototype.
- **Issue**: Initial `ModuleNotFoundError` due to incorrect import path and `pyproject.toml` configuration. Also, an incorrect image path in the test.

### What I did:

I implemented the initial version of the `SlideParser` class, which is responsible for parsing the XML content of a single slide and extracting its shapes, text, and image references. I also wrote and debugged unit tests to verify its functionality.

### How I did it:

1.  **Created `src/learnx_parser/slide_parser.py`**: This file contains the `SlideParser` class.
    -   The `__init__` method takes the paths to the slide XML and its corresponding relationships file.
    -   It uses `lxml` to parse the XML and store the root element.
    -   The `_parse_rels` method extracts the relationship IDs and their targets from the `.rels` file.
    -   The `extract_shapes_and_text` method iterates through `<p:sp>` elements and extracts text from `<a:t>` tags.
    -   The `extract_images` method finds `<p:pic>` elements, extracts the `r:embed` ID from `<a:blip>`, and resolves the image path using the parsed relationships.

2.  **Configured `pyproject.toml`**: I updated the `pyproject.toml` to include `lxml` as a dependency and configured `pytest` to correctly find the `learnx_parser` module.

3.  **Created `tests/test_slide_parser.py`**: This file contains unit tests for the `SlideParser`.
    -   A `pytest.fixture` provides an instance of `SlideParser` using the sample `slide23.xml` and its `.rels` file.
    -   `test_extract_shapes_and_text` asserts that shapes and expected text content are extracted.
    -   `test_extract_images` asserts that images are extracted and their paths are correctly resolved.

4.  **Debugging**: Encountered and resolved the following issues:
    -   `ModuleNotFoundError: No module named 'src'`: This was resolved by installing the package in editable mode (`uv pip install -e .`) and changing the import statement in the test file from `from src.learnx_parser.slide_parser import SlideParser` to `from learnx_parser.slide_parser import SlideParser`.
    -   Incorrect image path in test: The test initially expected `../media/image1.png` but the actual path in the `.rels` file was `/ppt/media/image1.png`. This was corrected in the test.

### Future work:

With the basic parsing of a single slide's XML complete, the next step is to extract the shapes and text in a more structured way, including their positions and styling information. This will be part of the `extract_shapes_and_text` task.
