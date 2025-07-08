# JSON Schema v2 Analysis - Version 0.2.5

## Current vs. v2 Schema Comparison

### Top-Level Structure

**Current Format:**
```json
{
  "id": "galaxy-001",
  "title": "Galaxy Presentation", 
  "slides": [...]
}
```

**v2 Required Format:**
```json
{
  "presentation": {
    "id": "galaxy-001",
    "title": "Galaxy Presentation",
    "slides": [...]
  }
}
```

**Required Change:** Add `presentation` wrapper object at top level.

### Slide Object Structure

**Current Format (Compliant):**
```json
{
  "id": "slide-1",
  "layout": "title-only",
  "elements": [...]
}
```

**v2 Format (Same):**
```json
{
  "id": "slide-1", 
  "layout": "title-only",
  "elements": [...]
}
```

**Status:** Already compliant.

### Element Types Analysis

#### 1. Title Element
**Current:** ✅ Compliant
```json
{
  "type": "title",
  "text": "Galaxy"
}
```

#### 2. Text-Box Element
**Current:** ✅ Mostly Compliant
```json
{
  "type": "text-box",
  "text": "Some text content",
  "style": {
    "bold": true,
    "italic": false,
    "fontSize": 18
  }
}
```

**v2 Requirement:** Same structure, but style properties are optional.

#### 3. Bullet-List Element
**Current:** ⚠️ Needs Enhancement
```json
{
  "type": "bullet-list",
  "items": [
    {
      "text": "Topic one"
    },
    {
      "text": "Topic two"
    }
  ]
}
```

**v2 Required:** Add support for `group`, `transcription`, `audioSrc`
```json
{
  "type": "bullet-list",
  "group": "optional_group_name",
  "items": [
    {
      "text": "Topic one",
      "transcription": "optional_transcription", 
      "audioSrc": "optional_audio_file"
    }
  ]
}
```

#### 4. Image Element
**Current:** ⚠️ Needs Enhancement
```json
{
  "type": "image",
  "src": "/ppt/media/image1.png"
}
```

**v2 Required:** Add `alt` attribute support
```json
{
  "type": "image", 
  "src": "/ppt/media/image1.png",
  "alt": "descriptive_text"
}
```

#### 5. Quote Element
**Current:** ❌ Missing
**v2 Required:** New element type
```json
{
  "type": "quote",
  "text": "Quote text",
  "attribution": "Author name"
}
```

#### 6. Chart-Placeholder Element
**Current:** ❌ Missing
**v2 Required:** New element type
```json
{
  "type": "chart-placeholder",
  "description": "Chart description"
}
```

### Layout Types Analysis

#### Current Layout Names (in use):
- `title-only` ✅ (compliant)
- `side-by-side` ❌ (not in v2 spec)
- `title-and-image` ❌ (not in v2 spec)
- `title-and-content` ✅ (compliant)
- `title-and-bullets` ❌ (not in v2 spec)
- `image-left` ❌ (not in v2 spec)

#### v2 Required Layout Names:
- `title-slide` ❌ (missing)
- `title-and-content` ✅ (exists)
- `section-header` ❌ (missing)
- `two-content` ❌ (missing)
- `comparison` ❌ (missing)
- `title-only` ✅ (exists)
- `blank` ❌ (missing)
- `content-with-caption` ❌ (missing)
- `picture-with-caption` ❌ (missing)

## Required Changes Summary

### 1. Top-Level Structure Changes
- **File:** `src/learnx_parser/models/core.py`
- **Action:** Modify `JsonPresentation` to be wrapped in `presentation` object
- **Impact:** Update `JsonWriter.write_presentation_json()` method

### 2. Element Type Enhancements
- **File:** `src/learnx_parser/models/core.py`, `src/learnx_parser/writers/json_writer.py`
- **Actions:**
  - Add `group`, `transcription`, `audioSrc` support to bullet-list items
  - Add `alt` attribute support to image elements
  - Add `quote` element type with `text` and `attribution` fields
  - Add `chart-placeholder` element type with `description` field

### 3. Layout Mapping Updates
- **File:** `src/learnx_parser/writers/json_writer.py`
- **Method:** `_map_layout_to_semantic_name()`
- **Actions:**
  - Replace non-compliant layout names with v2 equivalents
  - Add support for new layout types: `title-slide`, `section-header`, `two-content`, `comparison`, `blank`, `content-with-caption`, `picture-with-caption`
  - Update layout detection logic to match v2 semantics

### 4. Layout Mapping Strategy
```python
# Current → v2 Mappings
LAYOUT_MAPPINGS = {
    "title-and-bullets": "title-and-content",  # Bullets are content
    "side-by-side": "two-content",             # Two side-by-side elements  
    "title-and-image": "title-and-content",   # Image is content
    "image-left": "content-with-caption",     # Image with text caption
}

# New detection logic needed for:
# - title-slide: First slide with title + subtitle
# - section-header: Section divider slides
# - comparison: Two labeled content blocks
# - blank: No predefined elements
# - picture-with-caption: Large image + small caption
```

### 5. Data Model Updates Required

**JsonPresentation Update:**
```python
@dataclass
class JsonPresentationWrapper:
    presentation: JsonPresentation

# OR modify existing to wrap in presentation key during serialization
```

**JsonElement Enhancement:**
```python
@dataclass  
class JsonElement:
    type: str
    text: str | None = None
    style: dict[str, Any] | None = None
    items: list[dict[str, Any]] | None = None
    src: str | None = None
    alt: str | None = None                    # New for images
    attribution: str | None = None            # New for quotes  
    description: str | None = None            # New for chart-placeholder
    group: str | None = None                  # New for bullet-list
```

**Bullet List Item Enhancement:**
```python
# Update items structure to support:
{
    "text": str,
    "transcription": str | None,  # New
    "audioSrc": str | None        # New
}
```

## Implementation Priority

1. **High Priority (Required for v2 compliance):**
   - Top-level presentation wrapper
   - Layout name compliance
   - Image alt attribute support

2. **Medium Priority (New features):**
   - Quote element type
   - Chart-placeholder element type
   - Bullet-list group/audio support

3. **Low Priority (Enhanced detection):**
   - Advanced layout detection for new types
   - Content-aware layout classification

## Testing Strategy

1. **Schema Validation:** Create tests to validate v2 schema compliance
2. **Backward Compatibility:** Ensure existing functionality preserved
3. **Layout Detection:** Test layout mapping accuracy
4. **Element Types:** Test new element type generation
5. **Integration:** Full pipeline testing with Galaxy presentation