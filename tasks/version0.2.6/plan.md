# Version 0.2.6 Plan: Absolute Positioning Implementation

## Goal
Implement absolute positioning system similar to HTML5Point to create pixel-perfect PowerPoint slide reproduction while maintaining htpy-based HTML generation.

## Phase 1: Analysis and Design

### Task 1.1: Analyze HTML5Point Architecture
- **Subtask 1.1.1:** Study HTML5Point reverse engineering report thoroughly
- **Subtask 1.1.2:** Analyze current project's positioning system vs HTML5Point approach
- **Subtask 1.1.3:** Identify key differences in coordinate systems and scaling
- **Subtask 1.1.4:** Document requirements for absolute positioning implementation

### Task 1.2: Analyze PowerPoint XML Coordinate System
- **Subtask 1.2.1:** Examine presentation.xml slide dimensions and EMU units
- **Subtask 1.2.2:** Analyze shape transform data (`a:xfrm`) in multiple slides
- **Subtask 1.2.3:** Document EMU to pixel conversion requirements
- **Subtask 1.2.4:** Cross-reference XML coordinates with current HTML output

### Task 1.3: Design Absolute Positioning System
- **Subtask 1.3.1:** Design fixed slide container dimensions (like HTML5Point)
- **Subtask 1.3.2:** Design EMU-to-pixel conversion system
- **Subtask 1.3.3:** Design CSS transform-based scaling for responsiveness
- **Subtask 1.3.4:** Design configuration system for absolute vs responsive modes

## Phase 2: Core Positioning Implementation

### Task 2.1: Implement EMU-to-Pixel Conversion
- **Subtask 2.1.1:** Create EMU conversion utility functions
- **Subtask 2.1.2:** Add coordinate transformation methods to core models
- **Subtask 2.1.3:** Update shape parsing to extract precise positioning data
- **Subtask 2.1.4:** Test EMU conversion accuracy with sample XML data

### Task 2.2: Implement Fixed Slide Container
- **Subtask 2.2.1:** Update HtmlWriter to use fixed slide dimensions
- **Subtask 2.2.2:** Create slide container with absolute positioning context
- **Subtask 2.2.3:** Implement CSS transform-based scaling system
- **Subtask 2.2.4:** Add responsive scaling logic for different screen sizes

### Task 2.3: Update Element Renderers for Absolute Positioning
- **Subtask 2.3.1:** Modify shape rendering to use absolute positioning
- **Subtask 2.3.2:** Update text element rendering with precise coordinates
- **Subtask 2.3.3:** Modify image rendering for absolute placement
- **Subtask 2.3.4:** Update group shape rendering with nested absolute positioning

## Phase 3: Layout System Enhancement

### Task 3.1: Implement Absolute Layout Handlers
- **Subtask 3.1.1:** Create absolute positioning versions of layout handlers
- **Subtask 3.1.2:** Remove flexbox layouts in favor of absolute positioning
- **Subtask 3.1.3:** Implement z-index management for element layering
- **Subtask 3.1.4:** Handle element overflow and clipping with absolute positioning

### Task 3.2: Font and Typography Precision
- **Subtask 3.2.1:** Implement precise font size conversion from PowerPoint units
- **Subtask 3.2.2:** Add support for exact character spacing and line height
- **Subtask 3.2.3:** Implement text baseline and alignment precision
- **Subtask 3.2.4:** Test typography accuracy against PowerPoint original

### Task 3.3: Advanced Shape Positioning
- **Subtask 3.3.1:** Implement rotation transforms for shapes
- **Subtask 3.3.2:** Add support for shape flipping and scaling
- **Subtask 3.3.3:** Handle complex shape geometries with absolute positioning
- **Subtask 3.3.4:** Implement shape grouping with nested coordinate systems

## Phase 4: Configuration and Modes

### Task 4.1: Implement Positioning Mode Configuration
- **Subtask 4.1.1:** Add configuration options for absolute vs responsive positioning
- **Subtask 4.1.2:** Create mode-specific rendering logic in HtmlWriter
- **Subtask 4.1.3:** Add command-line arguments for positioning mode selection
- **Subtask 4.1.4:** Update documentation for positioning mode options

### Task 4.2: Maintain Backward Compatibility
- **Subtask 4.2.1:** Ensure existing responsive mode continues to work
- **Subtask 4.2.2:** Add tests for both positioning modes
- **Subtask 4.2.3:** Validate JSON output remains unchanged
- **Subtask 4.2.4:** Test mode switching functionality

## Phase 5: CSS and Styling Enhancements

### Task 5.1: Implement Transform-Based Scaling
- **Subtask 5.1.1:** Add CSS transform origin settings for scaling
- **Subtask 5.1.2:** Implement viewport-based scaling calculations
- **Subtask 5.1.3:** Add media queries for responsive scaling
- **Subtask 5.1.4:** Test scaling behavior across different screen sizes

### Task 5.2: Enhanced CSS Generation
- **Subtask 5.2.1:** Generate CSS for absolute positioning with htpy
- **Subtask 5.2.2:** Add CSS for transform-based scaling
- **Subtask 5.2.3:** Implement CSS for element layering (z-index)
- **Subtask 5.2.4:** Optimize CSS output for absolute positioning

### Task 5.3: Style Precision Improvements
- **Subtask 5.3.1:** Implement exact color matching from PowerPoint
- **Subtask 5.3.2:** Add support for precise border and outline styles
- **Subtask 5.3.3:** Implement shadow and effect positioning
- **Subtask 5.3.4:** Test style accuracy against PowerPoint original

## Phase 6: Testing and Validation

### Task 6.1: Unit Testing for Absolute Positioning
- **Subtask 6.1.1:** Create tests for EMU-to-pixel conversion
- **Subtask 6.1.2:** Add tests for absolute positioning calculations
- **Subtask 6.1.3:** Test coordinate transformation accuracy
- **Subtask 6.1.4:** Create tests for both positioning modes

### Task 6.2: Integration Testing
- **Subtask 6.2.1:** Test complete pipeline with absolute positioning
- **Subtask 6.2.2:** Validate HTML output matches HTML5Point structure
- **Subtask 6.2.3:** Test responsive scaling functionality
- **Subtask 6.2.4:** Ensure all existing tests pass with new system

### Task 6.3: User Testing and Validation
- **Subtask 6.3.1:** Run main.py with absolute positioning mode
- **Subtask 6.3.2:** Compare HTML output visually with PowerPoint original
- **Subtask 6.3.3:** Test different slide types and layouts
- **Subtask 6.3.4:** Validate scaling behavior in browser

## Phase 7: Documentation and Cleanup

### Task 7.1: Code Quality and Documentation
- **Subtask 7.1.1:** Run ruff linter on all modified files
- **Subtask 7.1.2:** Add comprehensive docstrings for new functions
- **Subtask 7.1.3:** Update README with positioning mode documentation
- **Subtask 7.1.4:** Remove debug statements and clean up code

### Task 7.2: Performance Optimization
- **Subtask 7.2.1:** Profile absolute positioning performance
- **Subtask 7.2.2:** Optimize coordinate calculations
- **Subtask 7.2.3:** Minimize CSS generation overhead
- **Subtask 7.2.4:** Test performance with large presentations

### Task 7.3: Final Validation
- **Subtask 7.3.1:** Run complete test suite with uv pytest
- **Subtask 7.3.2:** Perform comprehensive user testing
- **Subtask 7.3.3:** Validate pixel-perfect positioning accuracy
- **Subtask 7.3.4:** Commit and document changes