# LearnX PowerPoint Parser

A robust, fully-tested Python package for parsing `.pptx` files and converting their content into structured HTML and JSON with flexible positioning modes.

## Features

- **📄 Full PPTX Parsing**: Directly reads and interprets the underlying OpenXML structure of `.pptx` files
- **🎨 Dual Output Formats**: Generates both HTML and JSON representations of your slides
- **📱 Flexible Positioning**: Choose between responsive (flexbox) or absolute (pixel-perfect) positioning modes
- **🖼️ Media Extraction**: Automatically extracts and organizes embedded images and media files
- **⚡ Fast & Reliable**: Built with performance in mind, includes comprehensive test coverage
- **🔧 Developer Friendly**: Easy to install, well-documented API, ready for production use

## Installation

Install using `uv` (recommended):

```bash
uv add learnx-parser
```

Or using `pip`:

```bash
pip install learnx-parser
```

## Quick Start

### Basic Usage

```python
from learnx_parser import parse_pptx

# Parse a PowerPoint file with default responsive positioning
parse_pptx("./presentation.pptx", "./output")
```

### Advanced Usage with Positioning Modes

```python
from learnx_parser import parse_pptx

# Responsive positioning (default) - flexbox-based, adapts to screen size
parse_pptx(
    pptx_file_path="./presentation.pptx",
    output_dir="./output_responsive",
    positioning_mode="responsive"
)

# Absolute positioning - pixel-perfect positioning in fixed 1280x720 container
parse_pptx(
    pptx_file_path="./presentation.pptx", 
    output_dir="./output_absolute",
    positioning_mode="absolute"
)

# Hybrid positioning - combines both approaches
parse_pptx(
    pptx_file_path="./presentation.pptx",
    output_dir="./output_hybrid", 
    positioning_mode="hybrid"
)
```

## Positioning Modes

### 🔄 Responsive Mode (Default)
- **Layout**: Flexbox-based adaptive layout
- **Behavior**: Elements flow and adapt to different screen sizes
- **Best for**: Web presentations, mobile-friendly displays
- **Output**: CSS flexbox with responsive design

### 📐 Absolute Mode
- **Layout**: Fixed 1280×720px container with pixel-perfect positioning
- **Behavior**: Elements positioned exactly as in original slides
- **Best for**: Preserving original design, presentations requiring exact layout
- **Output**: CSS absolute positioning with transform-based scaling

### 🔀 Hybrid Mode
- **Layout**: Combines responsive and absolute positioning strategies
- **Behavior**: Responsive container with precise element positioning
- **Best for**: Balancing design fidelity with adaptability

## Command Line Usage

The package includes a demo script for quick testing:

```bash
# Clone the repository to try the example
git clone https://github.com/yatink/pptx2html_json.git
cd pptx2html_json

# Run with responsive positioning (default)
uv run python main.py

# Run with absolute positioning
uv run python main.py --absolute
```

## Output Structure

After parsing, you'll find:

```
output_directory/
├── presentation.json          # Complete presentation metadata
├── slide1/
│   ├── slide1.html           # Individual slide HTML
│   └── media/                # Slide-specific media files
│       └── image1.png
├── slide2/
│   ├── slide2.html
│   └── media/
└── ...
```

### HTML Output
- Clean, semantic HTML structure
- Embedded CSS for styling and positioning
- Responsive or absolute positioning based on mode
- Media files referenced with relative paths

### JSON Output
- Structured representation of slide content
- Element-level metadata (text, positioning, styling)
- Media file references
- Layout information

## API Reference

### `parse_pptx(pptx_file_path, output_dir, positioning_mode)`

**Parameters:**
- `pptx_file_path` (str): Path to the .pptx file to parse
- `output_dir` (str, optional): Output directory for generated files. Default: `"./output"`
- `positioning_mode` (str, optional): Positioning mode. Options: `"responsive"`, `"absolute"`, `"hybrid"`. Default: `"responsive"`

**Raises:**
- `FileNotFoundError`: If the specified .pptx file doesn't exist
- `zipfile.BadZipFile`: If the file is not a valid .pptx file

## Development

### Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yatink/pptx2html_json.git
   cd pptx2html_json
   ```

2. **Install dependencies:**
   ```bash
   uv sync
   ```

### Running Tests

```bash
# Run all tests
uv run pytest tests/

# Run tests with coverage
uv run pytest tests/ --cov=src/learnx_parser

# Run specific test file
uv run pytest tests/test_html_writer.py -v
```

### Building the Package

```bash
uv build
```

Built packages will be in the `dist/` directory.

## Project Structure

```
pptx2html_json/
├── src/
│   └── learnx_parser/
│       ├── __init__.py              # Public API
│       ├── models/
│       │   └── core.py              # Data models
│       ├── parsers/
│       │   ├── presentation.py      # Presentation-level parsing
│       │   ├── layout.py            # Layout detection
│       │   └── slide/               # Slide-level parsers
│       ├── services/
│       │   └── document_parser.py   # Main orchestrator
│       ├── writers/
│       │   ├── html_writer.py       # HTML generation
│       │   ├── json_writer.py       # JSON generation
│       │   └── css_utils.py         # CSS utilities
│       └── utils/
│           └── xml_helpers.py       # XML parsing utilities
├── tests/                           # Comprehensive test suite
├── example/                         # Sample files
├── main.py                          # Demo script
├── pyproject.toml                   # Project configuration
└── README.md                        # This file
```

## Requirements

- Python 3.10+
- Dependencies: `lxml`, `jsonschema`, `htpy`, `pytest`

## Contributing

1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Ensure all tests pass: `uv run pytest tests/`
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
