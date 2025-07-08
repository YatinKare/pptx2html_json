# Version 0.2.5 Plan

## Goals
1. Remove ALL 'f-strings' for HTML generation → replacing them with htpy library syntax
2. Apply json_schema_v2.md to JSON generation for better output structure

## Phase 1: Planning and Documentation

### Task 1.1: Analyze Current F-String Usage in HTML Generation
- **Subtask 1.1.1:** Examine f-string usage in src/learnx_parser/writers/html_writer.py
- **Subtask 1.1.2:** Examine f-string usage in src/learnx_parser/writers/layout_handlers.py
- **Subtask 1.1.3:** Examine f-string usage in src/learnx_parser/writers/element_renderers.py
- **Subtask 1.1.4:** Document all f-string patterns that need conversion to htpy

### Task 1.2: Analyze Test Files for F-String Usage
- **Subtask 1.2.1:** Examine f-string usage in tests/test_html_writer.py
- **Subtask 1.2.2:** Examine f-string usage in tests/test_pptx_parser.py
- **Subtask 1.2.3:** Document test-specific f-string patterns that need conversion

### Task 1.3: Understand JSON Schema v2 Requirements
- **Subtask 1.3.1:** Compare json_schema_v2.md with current JSON output format
- **Subtask 1.3.2:** Identify structural changes needed for v2 compliance
- **Subtask 1.3.3:** Document required changes to element types and layouts

## Phase 2: Replace F-Strings with htpy in HTML Writers

### Task 2.1: Convert html_writer.py to htpy
- **Subtask 2.1.1:** Install htpy dependency in pyproject.toml
- **Subtask 2.1.2:** Import htpy elements in html_writer.py
- **Subtask 2.1.3:** Convert f-string HTML generation to htpy syntax
- **Subtask 2.1.4:** Update method signatures to return htpy Renderable objects
- **Subtask 2.1.5:** Test HTML output matches previous format

### Task 2.2: Convert layout_handlers.py to htpy
- **Subtask 2.2.1:** Import htpy elements in layout_handlers.py
- **Subtask 2.2.2:** Convert layout generation f-strings to htpy syntax
- **Subtask 2.2.3:** Update layout handler methods to return htpy objects
- **Subtask 2.2.4:** Test layout generation with htpy

### Task 2.3: Convert element_renderers.py to htpy
- **Subtask 2.3.1:** Import htpy elements in element_renderers.py
- **Subtask 2.3.2:** Convert element rendering f-strings to htpy syntax
- **Subtask 2.3.3:** Update element renderer methods to return htpy objects
- **Subtask 2.3.4:** Test element rendering with htpy

## Phase 3: Update Tests to Use htpy Instead of F-Strings

### Task 3.1: Convert test_html_writer.py to htpy
- **Subtask 3.1.1:** Import htpy elements in test_html_writer.py
- **Subtask 3.1.2:** Replace f-string HTML creation with htpy syntax
- **Subtask 3.1.3:** Update test assertions to work with htpy output
- **Subtask 3.1.4:** Run tests to ensure they pass with htpy

### Task 3.2: Convert test_pptx_parser.py to htpy
- **Subtask 3.2.1:** Import htpy elements in test_pptx_parser.py
- **Subtask 3.2.2:** Replace f-string HTML creation with htpy syntax
- **Subtask 3.2.3:** Update test assertions to work with htpy output
- **Subtask 3.2.4:** Run tests to ensure they pass with htpy

## Phase 4: Implement JSON Schema v2 Compliance

### Task 4.1: Update JSON Writer Structure
- **Subtask 4.1.1:** Modify JSON writer to use json_schema_v2.md structure
- **Subtask 4.1.2:** Update top-level presentation object format
- **Subtask 4.1.3:** Update slide object structure for v2 compliance
- **Subtask 4.1.4:** Update element object types for v2 compliance

### Task 4.2: Implement New Layout Types
- **Subtask 4.2.1:** Add support for title-slide layout
- **Subtask 4.2.2:** Add support for section-header layout
- **Subtask 4.2.3:** Add support for two-content layout
- **Subtask 4.2.4:** Add support for comparison layout
- **Subtask 4.2.5:** Add support for content-with-caption layout
- **Subtask 4.2.6:** Add support for picture-with-caption layout
- **Subtask 4.2.7:** Add support for blank layout

### Task 4.3: Update Element Types for v2
- **Subtask 4.3.1:** Add support for quote element type
- **Subtask 4.3.2:** Add support for chart-placeholder element type
- **Subtask 4.3.3:** Update bullet-list with group and audio support
- **Subtask 4.3.4:** Update image elements with alt text support

## Phase 5: Testing and Validation

### Task 5.1: Unit Testing
- **Subtask 5.1.1:** Create tests for htpy HTML generation
- **Subtask 5.1.2:** Create tests for JSON schema v2 compliance
- **Subtask 5.1.3:** Create tests for new layout types
- **Subtask 5.1.4:** Create tests for new element types

### Task 5.2: Integration Testing
- **Subtask 5.2.1:** Test complete pipeline with galaxy presentation
- **Subtask 5.2.2:** Validate HTML output uses htpy instead of f-strings
- **Subtask 5.2.3:** Validate JSON output matches schema v2 format
- **Subtask 5.2.4:** Test with uv pytest to ensure all tests pass

### Task 5.3: User Testing
- **Subtask 5.3.1:** Run main.py with galaxy presentation
- **Subtask 5.3.2:** Examine HTML output files for htpy-generated content
- **Subtask 5.3.3:** Examine JSON output files for v2 schema compliance
- **Subtask 5.3.4:** Verify no errors occur during execution

## Phase 6: Code Cleanup and Documentation

### Task 6.1: Code Quality
- **Subtask 6.1.1:** Run ruff linter on all modified files
- **Subtask 6.1.2:** Fix any linting issues
- **Subtask 6.1.3:** Remove debug print statements
- **Subtask 6.1.4:** Add appropriate comments and docstrings

### Task 6.2: Final Validation
- **Subtask 6.2.1:** Run complete test suite with uv pytest
- **Subtask 6.2.2:** Perform final user test with main.py
- **Subtask 6.2.3:** Verify all f-strings for HTML generation are removed
- **Subtask 6.2.4:** Verify JSON output matches schema v2 requirements
- **Subtask 6.2.5:** Commit and push changes to GitHub
