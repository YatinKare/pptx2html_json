# JSON Format Specification for Simplified PowerPoint Representation

## Top-Level Structure

```json
{
  "presentation": {
    "id": string,
    "title": string,
    "slides": [ SlideObject, ... ]
  }
}
```

### Field Descriptions

* `id`: Unique identifier for the presentation.
* `title`: Presentation title.
* `slides`: An array of slide objects, each representing a single slide.

---

## Slide Object Structure

```json
{
  "id": string,
  "layout": string, // Defines which template/layout to use
  "elements": [ ElementObject, ... ]
}
```

### Field Descriptions

* `id`: Unique slide identifier.
* `layout`: A string representing the slide layout type (e.g., `"title-and-content"`, `"image-left"`, `"two-column"`). This can be mapped to a Svelte component.
* `elements`: A list of content blocks (text, image, title, etc.).

---

## ElementObject Types

Each element has a `type` field that defines the structure of its content. Below are the supported types:

### 1. Title

```json
{
  "type": "title",
  "text": string
}
```

### 2. Text Box

```json
{
  "type": "text-box",
  "text": string,
  "style"?: {
    "bold"?: boolean,
    "italic"?: boolean,
    "fontSize"?: number
  }
}
```

### 3. Bullet List

```json
{
  "type": "bullet-list",
  "group"?: string,
  "items": [
    {
      "text": string,
      "transcription"?: string,
      "audioSrc"?: string
    },
    ...
  ]
}
```

### 4. Image

```json
{
  "type": "image",
  "src": string, // File path or URL
  "alt"?: string
}
```

### 5. Quote / Callout

```json
{
  "type": "quote",
  "text": string,
  "attribution"?: string
}
```

### 6. Chart Placeholder

```json
{
  "type": "chart-placeholder",
  "description"?: string
}
```
---

## Design Principle: Relative Layouts Only

All positioning is managed via **relative layout logic** (e.g., flexbox on the frontend). The JSON structure **should not include any absolute** `x`, `y`, `width`, or `height` values. Layout and element arrangement are inferred from:

* The `layout` field at the slide level
* The `order` of elements within the `elements` array

This ensures that:

* The backend can remain simple and focused on semantics rather than spatial design.

---

## Notes for Frontend Consumers

* Layout type controls how to render elements spatially.
* Elements should be rendered in the order they appear.
* Unknown `type` values should be ignored or logged.

---

## Standardized Layout Naming and Semantics

To ensure consistency, the `layout` field must conform to predefined, semantically named values. These should align with how the frontend arranges elements using flexbox.

### Naming Convention

Use lowercase, dash-separated layout strings. Each layout describes both **structure** and **intended content types**.

### Layout Examples

1. `title-only`: A single `title` element centered on the slide.
2. `title-and-content`: A `title` followed by a `text-box` or `bullet-list` stacked vertically.
3. `image-left`: A `image` element on the left and a `text-box` on the right, rendered in a horizontal flex container.
4. `image-right`: A `text-box` on the left and an `image` on the right, rendered horizontally.
5. `title-and-image`: A `title` on top and an `image` below.
6. `two-column-text`: Two `text-box` elements side by side.
7. `quote-slide`: A single `quote` element, often centered or emphasized.
8. `image-gallery`: Multiple `image` elements displayed in a responsive flex row.
9. `title-and-bullets`: A `title` followed by a `bullet-list`.
10. `side-by-side`: A flexible layout with any two elements side by side (e.g., `image` and `bullet-list`).

---

## Example
Here is a sample JSON file that applies your finalized schema to 3 specific slides from the Galaxy presentation: the cover slide, Agenda, and Engaging the audience:

```json
{
  "presentation": {
    "id": "galaxy-001",
    "title": "Galaxy Presentation",
    "slides": [
      {
        "id": "slide-1",
        "layout": "title-only",
        "elements": [
          {
            "type": "title",
            "text": "Galaxy"
          }
        ]
      },
      {
        "id": "slide-2",
        "layout": "title-and-bullets",
        "elements": [
          {
            "type": "title",
            "text": "Agenda"
          },
          {
            "type": "bullet-list",
            "items": [
              { "text": "Topic one" },
              { "text": "Topic two" },
              { "text": "Topic three" },
              { "text": "Topic four" }
            ]
          }
        ]
      },
      {
        "id": "slide-3",
        "layout": "title-and-bullets",
        "elements": [
          {
            "type": "title",
            "text": "Engaging the audience"
          },
          {
            "type": "bullet-list",
            "items": [
              {
                "text": "Make eye contact with your audience to create a sense of intimacy and involvement"
              },
              {
                "text": "Weave relatable stories into your presentation using narratives that make your message memorable and impactful"
              },
              {
                "text": "Encourage questions and provide thoughtful responses to enhance audience participation"
              },
              {
                "text": "Use live polls or surveys to gather audience opinions, promoting engagement and making sure the audience feel involved"
              }
            ]
          }
        ]
      }
    ]
  }
}
```
