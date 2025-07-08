# PowerPoint XML Coordinate System Analysis

## Presentation Dimensions

**From presentation.xml:**
- Slide canvas: `<p:sldSz cx="12192000" cy="6858000"/>`
- EMU to pixels: 1280px × 720px
- Conversion factor: 1 EMU = 1/9525 pixel

**Current project conversion:**
```python
def emu_to_px(emu):
    return round(emu / 9525)
```

## Element Positioning Analysis

### Slide 1 (Title Slide) - slide16.xml

**Title Element Transform:**
```xml
<a:xfrm>
  <a:off x="1280159" y="357809"/>
  <a:ext cx="7983110" cy="3080335"/>
</a:xfrm>
```

**Converted to pixels:**
- Position: (134.4px, 37.6px)
- Size: 838.4px × 323.6px
- Relative to slide: 10.5% from left, 5.2% from top
- Size relative to slide: 65.5% width, 44.9% height

### Slide 2 (Agenda) - slide23.xml

**Title Element (no explicit transform - inherits from layout):**
- Uses layout placeholder positioning
- Layout reference: slideLayout26.xml

**Picture Element (placeholder with layout position):**
```xml
<p:nvPr><p:ph type="pic" sz="quarter" idx="14"/></p:nvPr>
```

**Text Element (placeholder with layout position):**
```xml
<p:nvPr><p:ph type="body" sz="quarter" idx="17"/></p:nvPr>
```

### Layout Positioning (slideLayout26.xml)

**Title Placeholder:**
```xml
<a:xfrm>
  <a:off x="5116544" y="614202"/>
  <a:ext cx="5918072" cy="2276856"/>
</a:xfrm>
```
- Position: (537.1px, 64.5px)
- Size: 621.2px × 239.1px

**Picture Placeholder:**
```xml
<a:xfrm>
  <a:off x="1280160" y="2530058"/>
  <a:ext cx="3707972" cy="3707971"/>
</a:xfrm>
```
- Position: (134.4px, 265.9px)
- Size: 389.4px × 389.4px

**Text Placeholder:**
```xml
<a:xfrm>
  <a:off x="5116548" y="3161752"/>
  <a:ext cx="5918068" cy="3144965"/>
</a:xfrm>
```
- Position: (537.1px, 332.0px)
- Size: 621.2px × 330.2px

## Coordinate System Key Points

### 1. EMU (English Metric Units)
- **Definition**: 1 EMU = 1/914400 inch
- **Pixel Conversion**: 1 EMU = 1/9525 pixel (at 96 DPI)
- **Precision**: EMU provides very high precision for positioning

### 2. Coordinate Origin
- **Origin**: Top-left corner (0,0)
- **X-axis**: Increases to the right
- **Y-axis**: Increases downward
- **Units**: All coordinates in EMU

### 3. Transform Structure
```xml
<a:xfrm>
  <a:off x="X_EMU" y="Y_EMU"/>          <!-- Position -->
  <a:ext cx="WIDTH_EMU" cy="HEIGHT_EMU"/> <!-- Size -->
</a:xfrm>
```

### 4. Placeholder System
- **Slide elements**: May inherit positioning from layout placeholders
- **Layout inheritance**: Elements without explicit transforms use layout positions
- **Placeholder types**: title, body, pic, ftr, sldNum, etc.

## Absolute Positioning Requirements

### 1. Direct Coordinate Extraction
```python
def extract_absolute_position(element):
    """Extract absolute position from XML element."""
    transform = element.find('.//a:xfrm')
    if transform is not None:
        off = transform.find('a:off')
        ext = transform.find('a:ext')
        if off is not None and ext is not None:
            x = int(off.get('x', 0))
            y = int(off.get('y', 0))
            width = int(ext.get('cx', 0))
            height = int(ext.get('cy', 0))
            return {
                'x': emu_to_px(x),
                'y': emu_to_px(y),
                'width': emu_to_px(width),
                'height': emu_to_px(height)
            }
    return None
```

### 2. Layout Placeholder Resolution
```python
def resolve_placeholder_position(slide_element, layout):
    """Resolve position from layout placeholder."""
    ph_type = slide_element.find('.//p:ph').get('type')
    ph_idx = slide_element.find('.//p:ph').get('idx')
    
    # Find corresponding placeholder in layout
    for layout_element in layout.findall('.//p:sp'):
        layout_ph = layout_element.find('.//p:ph')
        if (layout_ph.get('type') == ph_type and 
            layout_ph.get('idx') == ph_idx):
            return extract_absolute_position(layout_element)
    
    return None
```

### 3. CSS Generation for Absolute Positioning
```python
def generate_absolute_css(position):
    """Generate CSS for absolute positioning."""
    return f"""
    position: absolute;
    left: {position['x']}px;
    top: {position['y']}px;
    width: {position['width']}px;
    height: {position['height']}px;
    """
```

## Comparison with Current System

### Current Approach (Responsive)
- Uses flexbox layouts with relative positioning
- Infers layout patterns from element types
- Responsive design with percentage-based sizing
- Layout handlers for different slide types

### Proposed Absolute Approach
- Direct EMU-to-pixel conversion
- Absolute positioning from XML coordinates
- Fixed slide dimensions (1280px × 720px)
- Pixel-perfect reproduction of PowerPoint layout

## Implementation Strategy

### 1. Coordinate Extraction Enhancement
- Extract precise positions from XML transforms
- Handle placeholder inheritance from layouts
- Support grouped elements with nested coordinates

### 2. CSS Generation Update
- Generate absolute positioning CSS
- Add transform-origin for scaling
- Include z-index for element layering

### 3. Container Design
- Fixed slide container dimensions
- CSS transforms for responsive scaling
- Overflow handling for content clipping

### 4. Backward Compatibility
- Configuration option for positioning mode
- Maintain existing responsive layout system
- Allow switching between modes