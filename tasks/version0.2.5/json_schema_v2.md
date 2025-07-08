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
* `layout`: A string representing the slide layout type (see standardized layout list).
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

---

## Standardized Layout Naming and Semantics

To ensure consistency, the `layout` field must conform to predefined, semantically named values. These names align with Microsoft's native PowerPoint layout types but are normalized for frontend-friendly naming.

### Naming Convention

Use lowercase, dash-separated strings. Follow the naming and intent of native PowerPoint layouts to maximize semantic clarity and UI mapping.

### Layout Types and Descriptions

1. `title-slide`: Includes a main `title` and optional `subtitle`. Used for presentation openers.
2. `title-and-content`: Includes `title` followed by `text-box`, `bullet-list`, `image`, `chart-placeholder`, or other supported types.
3. `section-header`: A `title` and optional `subtitle`, used to divide sections.
4. `two-content`: A `title` followed by two content blocks (side-by-side `text-box`, `image`, or `bullet-list`).
5. `comparison`: Like `two-content`, but each block includes a labeled subheading.
6. `title-only`: A single centered `title`.
7. `blank`: No predefined elements. Reserved for highly custom slide renderings.
8. `content-with-caption`: Content (usually `image`) with smaller explanatory `text-box` beside it.
9. `picture-with-caption`: A large image with a small caption under or beside it.

### Examples

#### title-slide

```json
{
  "layout": "title-slide",
  "elements": [
    { "type": "title", "text": "Welcome to the Galaxy" },
    { "type": "text-box", "text": "By Brita Tamm" }
  ]
}
```

#### two-content

```json
{
  "layout": "two-content",
  "elements": [
    { "type": "text-box", "text": "Pros of Feature A" },
    { "type": "text-box", "text": "Cons of Feature A" }
  ]
}
```

#### comparison

```json
{
  "layout": "comparison",
  "elements": [
    { "type": "text-box", "text": "Feature A", "group": "Pros" },
    { "type": "text-box", "text": "Feature B", "group": "Cons" }
  ]
}
```

#### content-with-caption

```json
{
  "layout": "content-with-caption",
  "elements": [
    { "type": "image", "src": "/images/chart1.png" },
    { "type": "text-box", "text": "Chart shows 2023 engagement growth" }
  ]
}
```

