## Plan: Version 0.2.4 - JSON Schema Alignment and Text Semantics

### 🧠 Objective

1.  Clean up the JSON format to follow the `json_schema.md`.
2.  Add text semantics, including bold, italics, underline, and font sizes.

### Phase 1: JSON Schema Alignment

*   **Task 1.1: Analyze `json_schema.md`**
    *   **Subtask 1.1.1:** Read and understand the specified JSON schema in `json_schema.md`.
    *   **Subtask 1.1.2:** Compare the current JSON output with the example in `json_schema.md` to identify differences.
*   **Task 1.2: Refactor `JsonWriter`**
    *   **Subtask 1.2.1:** Modify the `JsonWriter` to produce JSON that conforms to the `json_schema.md`.
    *   **Subtask 1.2.2:** Update the `data_models.py` if necessary to support the new JSON structure.
*   **Task 1.3: Testing and Validation**
    *   **Subtask 1.3.1:** Create a new test to validate the new JSON output against the `json_schema.md`.
    *   **Subtask 1.3.2:** Run all tests to ensure no regressions.
    *   **Subtask 1.3.3:** "User test" by running `main.py` and inspecting the output.

### Phase 2: Text Semantics

*   **Task 2.1: Documentation and Research**
    *   **Subtask 2.1.1:** Research how to extract text formatting (bold, italics, underline, font size) from the `drawingML` and `presentationML` parts of the OOXML specification.
    *   **Subtask 2.1.2:** Document findings in a new file: `docs/text_formatting.md`.
*   **Task 2.2: Update `SlideParser`**
    *   **Subtask 2.2.1:** Modify the `SlideParser` to extract text formatting information.
    *   **Subtask 2.2.2:** Update `data_models.py` to store the extracted formatting information.
*   **Task 2.3: Update `JsonWriter`**
    *   **Subtask 2.3.1:** Modify the `JsonWriter` to include the text formatting information in the JSON output.
*   **Task 2.4: Testing and Validation**
    *   **Subtask 2.4.1:** Create a new test to verify that text formatting is correctly extracted and represented in the JSON output.
    *   **Subtask 2.4.2:** Run all tests to ensure no regressions.
    *   **Subtask 2.4.3:** "User test" by running `main.py` and inspecting the output.
