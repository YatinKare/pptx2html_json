# LearnX PowerPoint Parser

A robust, fully-tested Python package for parsing `.pptx` files and converting their content into structured HTML or JSON.

>[!NOTE] This package was fully developed by gemini-cli. See here how it was done: {will put a link here}

## Features

-   **Parses OpenXML Structure**: Directly reads and interprets the underlying XML components of `.pptx` files.
-   **HTML Output**: Converts slides into cleanly structured HTML, preserving layout, text position, and basic styling.
-   **JSON Output**: Provides an alternate JSON representation for programmatic access to slide content.
-   **Media Extraction**: Extracts and organizes embedded media files (images, etc.) alongside the generated output.
-   **Installable**: Designed to be easily installed via `uv add` and suitable for PyPI publication.

## Installation

To install the `learnx-parser` package, you can use `uv`:

```bash
uv add learnx-parser
```

## Usage

Here's a basic example of how to use the `learnx-parser` to convert a `.pptx` file:

```python
import os
from learnx_parser import parse_pptx

# Define the path to your .pptx file
pptx_file = "./path/to/your/presentation.pptx"

# Define the output directory for HTML, JSON, and media files
output_directory = "./output_slides"

# Ensure the output directory exists
os.makedirs(output_directory, exist_ok=True)

# Parse the .pptx file
parse_pptx(pptx_file, output_dir=output_directory)

print(f"Successfully parsed {pptx_file} and saved output to {output_directory}")

# You can now find slide1.html, slide1.json, etc., in the output_slides directory.
# Media files will be in output_slides/media/.
```

## Development

### Setup

1.  Clone the repository:
    ```bash
    git clone https://github.com/yatink/pptx2html_json.git
    cd pptx2html_json
    ```
2.  Create and activate a virtual environment using `uv`:
    ```bash
    uv venv
    source .venv/bin/activate
    ```
3.  Install development dependencies:
    ```bash
    uv pip install -e . pytest
    ```

### Running Tests

```bash
uv run pytest
```

### Building the Package

To build the distributable package (wheel and sdist):

```bash
uv build
```

The built packages will be located in the `dist/` directory.

## Project Structure

```
pptx2html_json/
├── src/
│   └── learnx_parser/
│       ├── __init__.py         # Public API entrypoint (parse_pptx)
│       ├── html_writer.py      # Generates HTML output
│       ├── json_writer.py      # Generates JSON output
│       ├── pptx_parser.py      # Orchestrates the parsing process
│       ├── presentation_parser.py # Parses presentation.xml for slide order
│       └── slide_parser.py     # Parses individual slide XMLs
├── tests/                    # Unit and integration tests
├── docs/                     # Project documentation (e.g., schema_notes.md)
├── tasks/                    # Task journals (for Gemini)
├── pyproject.toml            # Project metadata and dependencies
├── README.md                 # This file
└── ...
```

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.
