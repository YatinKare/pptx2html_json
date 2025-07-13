# Version 0.2.7 Plan: Element Overflow Prevention, Background Images, and Font Styling

## Goal
Implement three key enhancements to create pixel-perfect PowerPoint reproduction:
1. Ensure all elements fit within visible viewport without overflow
2. Extract and implement background images from slide masters
3. Extract and apply font families, colors, and styling from PPTX themes and content

## Phase 1: Analysis and Documentation

### Task 1.1: Analyze Current State and Overflow Issues
- **Subtask 1.1.1:** Test current `uv run main.py --absolute` output and identify overflow issues
- **Subtask 1.1.2:** Compare current output structure with HTML5Point_output.html reference
- **Subtask 1.1.3:** Document current element rendering and positioning approach
- **Subtask 1.1.4:** Identify specific elements that may cause overflow (large shapes, positioned text, images)

### Task 1.2: Research Background Implementation Requirements
- **Subtask 1.2.1:** Examine presentation.xml and slide master XML for background properties
- **Subtask 1.2.2:** Study HTML5Point_output.html background implementation approach
- **Subtask 1.2.3:** Analyze OpenXML documentation for slide backgrounds in docs/ directory
- **Subtask 1.2.4:** Cross-reference background properties in temp_pptx/ Galaxy presentation

### Task 1.3: Research Font and Color Extraction Requirements
- **Subtask 1.3.1:** Study theme.xml files in temp_pptx/ppt/theme/ for color schemes and fonts
- **Subtask 1.3.2:** Analyze text run properties in slide XML for font families and colors
- **Subtask 1.3.3:** Examine HTML5Point_output.html font rendering approach
- **Subtask 1.3.4:** Document required OpenXML elements for font and color extraction

## Phase 2: Element Overflow Prevention

### Task 2.1: Implement Enhanced Element Validation
- **Subtask 2.1.1:** Create element bounds checking system for slide container (1280×720px)
- **Subtask 2.1.2:** Add overflow detection for shapes, text, and images
- **Subtask 2.1.3:** Implement element clipping and scaling strategies
- **Subtask 2.1.4:** Create comprehensive test cases for overflow scenarios

### Task 2.2: Fix Element Positioning and Sizing
- **Subtask 2.2.1:** Validate EMU-to-pixel conversion accuracy against PowerPoint dimensions
- **Subtask 2.2.2:** Fix text content rendering within shape boundaries
- **Subtask 2.2.3:** Ensure image scaling and cropping preserves aspect ratio
- **Subtask 2.2.4:** Implement proper z-index ordering to prevent element stacking issues

### Task 2.3: Enhanced Container Management
- **Subtask 2.3.1:** Verify slide container scaling maintains aspect ratio
- **Subtask 2.3.2:** Add container overflow:hidden enforcement
- **Subtask 2.3.3:** Implement responsive scaling validation for different screen sizes
- **Subtask 2.3.4:** Test element visibility across browser viewport sizes

## Phase 3: Background Image Implementation

### Task 3.1: Extract Background Properties from XML
- **Subtask 3.1.1:** Parse slide master background properties (p:bg, a:blipFill)
- **Subtask 3.1.2:** Extract background images from master and layout relationships
- **Subtask 3.1.3:** Parse individual slide background overrides
- **Subtask 3.1.4:** Handle gradient and solid color backgrounds alongside images

### Task 3.2: Implement Background Rendering
- **Subtask 3.2.1:** Add background image extraction to media processing pipeline
- **Subtask 3.2.2:** Generate CSS background-image properties for slide containers
- **Subtask 3.2.3:** Implement background sizing and positioning (cover, contain, repeat)
- **Subtask 3.2.4:** Add background layering support (master + slide specific)

### Task 3.3: Background Integration with HTML Writer
- **Subtask 3.3.1:** Update HtmlWriter to include background CSS in slide container
- **Subtask 3.3.2:** Ensure background images don't interfere with element positioning
- **Subtask 3.3.3:** Add background image path resolution and media organization
- **Subtask 3.3.4:** Test background rendering with HTML5Point_output.html reference

## Phase 4: Font and Color Extraction

### Task 4.1: Extract Theme Colors and Fonts
- **Subtask 4.1.1:** Parse theme.xml color scheme (a:clrScheme) for primary colors
- **Subtask 4.1.2:** Extract font scheme (a:fontScheme) for major and minor fonts
- **Subtask 4.1.3:** Parse color definitions and theme color references
- **Subtask 4.1.4:** Create theme color and font mapping system

### Task 4.2: Extract Text-Level Font Properties
- **Subtask 4.2.1:** Parse text run properties (a:rPr) for font families, sizes, colors
- **Subtask 4.2.2:** Extract paragraph properties (a:pPr) for text alignment and spacing
- **Subtask 4.2.3:** Handle font fallbacks and web-safe font alternatives
- **Subtask 4.2.4:** Parse character-level formatting (bold, italic, underline)

### Task 4.3: Implement Font and Color Rendering
- **Subtask 4.3.1:** Generate CSS font-family declarations with fallbacks
- **Subtask 4.3.2:** Convert theme colors to CSS color values (RGB, hex)
- **Subtask 4.3.3:** Apply font sizing with accurate EMU-to-pixel conversion
- **Subtask 4.3.4:** Implement text styling (weight, style, decoration)

## Phase 5: Integration and Element Content Enhancement

### Task 5.1: Enhanced Element Content Rendering
- **Subtask 5.1.1:** Replace placeholder colored divs with actual text content
- **Subtask 5.1.2:** Implement proper image rendering with src attributes
- **Subtask 5.1.3:** Add shape content rendering (text frames, bullets)
- **Subtask 5.1.4:** Integrate font and color styling with element content

### Task 5.2: Content Validation and Quality
- **Subtask 5.2.1:** Ensure text content fits within shape boundaries
- **Subtask 5.2.2:** Validate image aspect ratios and scaling
- **Subtask 5.2.3:** Test font rendering across different elements
- **Subtask 5.2.4:** Verify color accuracy against PowerPoint original

### Task 5.3: Performance and Output Optimization
- **Subtask 5.3.1:** Optimize CSS generation for large presentations
- **Subtask 5.3.2:** Minimize redundant styling and improve CSS efficiency
- **Subtask 5.3.3:** Ensure media file organization remains clean
- **Subtask 5.3.4:** Validate output structure matches expected format

## Phase 6: Testing and Validation

### Task 6.1: Unit Testing for New Features
- **Subtask 6.1.1:** Create tests for element overflow detection and prevention
- **Subtask 6.1.2:** Add tests for background image extraction and rendering
- **Subtask 6.1.3:** Test font and color extraction accuracy
- **Subtask 6.1.4:** Create comprehensive integration tests for absolute positioning mode

### Task 6.2: User Testing and Real-World Validation
- **Subtask 6.2.1:** Run `uv run main.py --absolute` and validate Galaxy presentation output
- **Subtask 6.2.2:** Compare output visually with PowerPoint original and HTML5Point reference
- **Subtask 6.2.3:** Test viewport scaling and element visibility across screen sizes
- **Subtask 6.2.4:** Validate all 13 slides for proper rendering and no overflow

### Task 6.3: Cross-Browser and Compatibility Testing
- **Subtask 6.3.1:** Test output in Chrome, Firefox, Safari, and Edge
- **Subtask 6.3.2:** Validate responsive scaling on mobile and tablet viewports
- **Subtask 6.3.3:** Ensure font fallbacks work correctly across platforms
- **Subtask 6.3.4:** Test background image rendering across browsers

## Phase 7: Documentation and Cleanup

### Task 7.1: Code Quality and Documentation
- **Subtask 7.1.1:** Run ruff linter on all modified files and fix issues
- **Subtask 7.1.2:** Add comprehensive docstrings for new functions and classes
- **Subtask 7.1.3:** Update README with new features (backgrounds, fonts, overflow prevention)
- **Subtask 7.1.4:** Remove debug statements and clean up test output

### Task 7.2: Final Integration and Testing
- **Subtask 7.2.1:** Run complete test suite with `uv run pytest tests/`
- **Subtask 7.2.2:** Perform comprehensive user testing with main.py
- **Subtask 7.2.3:** Validate backward compatibility with responsive mode
- **Subtask 7.2.4:** Create completion summary and task documentation

### Task 7.3: Version Release Preparation
- **Subtask 7.3.1:** Update version number in pyproject.toml to 0.2.7
- **Subtask 7.3.2:** Create comprehensive change log for version 0.2.7
- **Subtask 7.3.3:** Ensure all tests pass and output quality meets standards
- **Subtask 7.3.4:** Commit changes and prepare for production release

## Success Criteria

### Goal 1: Element Overflow Prevention ✅
- All elements visible within browser viewport at any screen size
- Slide container maintains 16:9 aspect ratio
- No horizontal or vertical scrollbars required
- Elements properly clipped or scaled to fit

### Goal 2: Background Images ✅  
- Master slide backgrounds extracted and rendered
- Background images display correctly as CSS backgrounds
- Background sizing and positioning matches PowerPoint
- No interference with foreground element positioning

### Goal 3: Font and Color Styling ✅
- Theme colors accurately extracted and applied
- Font families, sizes, and styles match PowerPoint
- Web font fallbacks implemented for missing fonts
- Character-level formatting (bold, italic, color) preserved

### Overall Quality ✅
- Output visually matches PowerPoint original
- HTML structure clean and semantic
- Performance maintained for 13-slide presentations
- Backward compatibility with responsive mode preserved