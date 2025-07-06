# `core.py` Documentation

This module defines the data structures (using `dataclasses`) that represent the parsed elements of a PowerPoint presentation. These models are used to store the extracted data in a structured way, making it easier to process and convert to other formats like HTML or JSON.

## Data Models

- **`Transform`**: Represents the position, size, rotation, and flip transformations of a slide element.
- **`SolidFill`**: Represents a solid color fill.
- **`GradientStop`**: Represents a single color stop in a gradient.
- **`GradientFill`**: Represents a gradient fill.
- **`BlipFill`**: Represents an image fill.
- **`PatternFill`**: Represents a pattern fill.
- **`Fill`**: A type alias for any of the fill types (`SolidFill`, `GradientFill`, `BlipFill`, `PatternFill`).
- **`Line`**: Represents the properties of a line or border.
- **`RunProperties`**: Represents the formatting properties of a text run (e.g., font size, bold, italic).
- **`TextRun`**: Represents a contiguous run of text with the same properties.
- **`ParagraphProperties`**: Represents the properties of a paragraph (e.g., alignment, indentation, bullet points).
- **`Paragraph`**: Represents a paragraph of text, composed of one or more text runs.
- **`TextFrame`**: Represents the text container within a shape.
- **`Hyperlink`**: Represents a hyperlink.
- **`CommonSlideData`**: Represents data common to all slides (e.g., background, slide dimensions).
- **`Picture`**: Represents a picture element.
- **`GroupShape`**: Represents a group of shapes.
- **`GraphicFrame`**: Represents a graphic frame (e.g., for charts, tables).
- **`Shape`**: Represents a shape element.
- **`LayoutPlaceholder`**: Represents a placeholder on a slide layout.
- **`SlideLayout`**: Represents a slide layout, including its placeholders and list styles.
- **`Slide`**: Represents a single slide in the presentation.
- **`JsonElement`**: A simplified data model for a JSON element.
- **`JsonSlide`**: A simplified data model for a JSON slide.
- **`JsonPresentation`**: A simplified data model for a JSON presentation.