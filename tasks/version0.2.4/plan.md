# Version 0.2.4 Plan

## Goals
1. Clean up the JSON format to follow the json_schema.md
2. Add text semantics (bold, italics, underline, font sizes)

## Phase 1: Planning and Documentation

### Task 1.1: Understand Current JSON Output Format
- **Subtask 1.1.1:** Analyze current JSON writer implementation in src/pptx_parser/writers/json_writer.py
- **Subtask 1.1.2:** Run current implementation on galaxy presentation to understand current output format
- **Subtask 1.1.3:** Compare current output with json_schema.md target format
- **Subtask 1.1.4:** Document gaps between current and target formats

### Task 1.2: Understand Text Parsing Capabilities
- **Subtask 1.2.1:** Analyze current text parsing in src/pptx_parser/parsers/slide/text.py
- **Subtask 1.2.2:** Examine temp_pptx/ directory to understand text formatting in XML
- **Subtask 1.2.3:** Document current text semantic extraction capabilities
- **Subtask 1.2.4:** Identify missing text semantic features (bold, italic, underline, font sizes)

## Phase 2: Implement JSON Schema Compliance

### Task 2.1: Refactor JSON Writer Structure
- **Subtask 2.1.1:** Update JSON writer to output top-level presentation structure
- **Subtask 2.1.2:** Implement slide object structure with id, layout, and elements
- **Subtask 2.1.3:** Add layout detection logic for different slide types
- **Subtask 2.1.4:** Implement element type classification (title, text-box, bullet-list, image, quote)
- **Subtask 2.1.5:** Remove absolute positioning data (x, y, width, height) from JSON output

### Task 2.2: Implement Element Type Detection
- **Subtask 2.2.1:** Create logic to identify title elements
- **Subtask 2.2.2:** Create logic to identify text-box elements
- **Subtask 2.2.3:** Create logic to identify bullet-list elements
- **Subtask 2.2.4:** Create logic to identify image elements
- **Subtask 2.2.5:** Create logic to identify quote/callout elements

### Task 2.3: Implement Layout Detection
- **Subtask 2.3.1:** Analyze slide element arrangements to determine layout types
- **Subtask 2.3.2:** Implement title-only layout detection
- **Subtask 2.3.3:** Implement title-and-content layout detection
- **Subtask 2.3.4:** Implement title-and-bullets layout detection
- **Subtask 2.3.5:** Implement image-left and image-right layout detection
- **Subtask 2.3.6:** Add fallback layout classification for unrecognized patterns

## Phase 3: Implement Text Semantics

### Task 3.1: Extract Text Formatting from XML
- **Subtask 3.1.1:** Parse bold formatting from a:rPr b="1" attribute
- **Subtask 3.1.2:** Parse italic formatting from a:rPr i="1" attribute  
- **Subtask 3.1.3:** Parse underline formatting from a:rPr u attribute
- **Subtask 3.1.4:** Parse font size from a:rPr sz attribute
- **Subtask 3.1.5:** Update text.py parser to extract and store these properties

### Task 3.2: Update Data Models for Text Semantics
- **Subtask 3.2.1:** Add style properties to TextRun data model
- **Subtask 3.2.2:** Update TextElement to include formatting information
- **Subtask 3.2.3:** Ensure compatibility with existing parsing pipeline

### Task 3.3: Integrate Text Semantics into JSON Output
- **Subtask 3.3.1:** Add style object to text-box elements with bold, italic, fontSize properties
- **Subtask 3.3.2:** Apply text formatting to bullet-list items
- **Subtask 3.3.3:** Apply text formatting to title elements
- **Subtask 3.3.4:** Test that semantic formatting is preserved in JSON output

## Phase 4: Testing and Validation

### Task 4.1: Unit Testing
- **Subtask 4.1.1:** Create tests for JSON schema compliance
- **Subtask 4.1.2:** Create tests for text semantic extraction
- **Subtask 4.1.3:** Create tests for layout detection logic
- **Subtask 4.1.4:** Create tests for element type classification

### Task 4.2: Integration Testing
- **Subtask 4.2.1:** Test complete pipeline with galaxy presentation
- **Subtask 4.2.2:** Validate JSON output matches schema requirements
- **Subtask 4.2.3:** Verify text semantics are correctly captured
- **Subtask 4.2.4:** Test with additional PPTX files if available

### Task 4.3: User Testing
- **Subtask 4.3.1:** Run main.py with galaxy presentation
- **Subtask 4.3.2:** Examine JSON output files
- **Subtask 4.3.3:** Verify no errors occur during execution
- **Subtask 4.3.4:** Validate output matches expected schema format

## Phase 5: Code Cleanup and Documentation

### Task 5.1: Code Quality
- **Subtask 5.1.1:** Run ruff linter on modified files
- **Subtask 5.1.2:** Fix any linting issues
- **Subtask 5.1.3:** Remove debug print statements
- **Subtask 5.1.4:** Add appropriate comments and docstrings

### Task 5.2: Documentation
- **Subtask 5.2.1:** Update README if needed
- **Subtask 5.2.2:** Document new JSON schema format
- **Subtask 5.2.3:** Document text semantic capabilities
- **Subtask 5.2.4:** Create task completion logs

### Task 5.3: Final Validation
- **Subtask 5.3.1:** Run complete test suite with uv pytest
- **Subtask 5.3.2:** Perform final user test with main.py
- **Subtask 5.3.3:** Commit and push changes to GitHub