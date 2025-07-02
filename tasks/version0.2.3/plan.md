## Plan: Version 0.2.3 - JSON Cleaning and Generalization

### 🧠 Objective

1.  Remove all absolute positioning values in the JSON output, substituting them for better CSS-like properties.
2.  Adapt the cleanings from slide 2 and slide 5 from the previous version to all slides in the galaxy example presentation.

### Phase 1: JSON Output Refinement

*   **Task 1.1: Analyze JSON Output**
    *   **Subtask 1.1.1:** Examine the current JSON output for a representative slide to identify all instances of absolute positioning (`x`, `y`, `width`, `height`).
    *   **Subtask 1.1.2:** Cross-reference with the HTML/CSS generation to understand how these values are used and what CSS properties they correspond to.
*   **Task 1.2: Research and Design CSS-like JSON Structure**
    *   **Subtask 1.2.1:** Research best practices for representing layout and styling in a JSON structure in a way that is analogous to CSS.
    *   **Subtask 1.2.2:** Design a new JSON structure that replaces absolute pixel values with more flexible, CSS-like properties (e.g., `position`, `top`, `left`, `width`, `height` as percentages or other relative units, `transform`, etc.).
*   **Task 1.3: Implement JSON Writer Changes**
    *   **Subtask 1.3.1:** Modify the `JsonWriter` to implement the new, CSS-like JSON structure.
    *   **Subtask 1.3.2:** Update the `JsonWriter` to convert the absolute positioning values from the `Slide` data model into the new format.
*   **Task 1.4: Testing and Validation**
    *   **Subtask 1.4.1:** Create a new test in the `tests` directory to verify that the JSON output is correctly formatted according to the new structure.
    *   **Subtask 1.4.2:** Run the new test and all existing tests to ensure no regressions were introduced.
    *   **Subtask 1.4.3:** Perform "user testing" by running `main.py` and inspecting the generated JSON files to ensure the output is as expected.

### Phase 2: Generalize Slide Cleaning Logic

*   **Task 2.1: Analyze Existing Cleaning Logic**
    *   **Subtask 2.1.1:** Review the changes made for slides 2 and 5 in the previous version to fully understand the "cleaning" logic that was applied.
    *   **Subtask 2.1.2:** Identify the specific patterns in the slide data that the cleaning logic addresses.
*   **Task 2.2: Abstract and Generalize the Cleaning Logic**
    *   **Subtask 2.2.1:** Refactor the cleaning logic into a reusable function or class that can be applied to any slide.
    *   **Subtask 2.2.2:** The new logic should be able to identify and clean the targeted patterns on any slide, not just slides 2 and 5.
*   **Task 2.3: Integrate Generalized Cleaning into the Parser**
    *   **Subtask 2.3.1:** Integrate the new, generalized cleaning logic into the `SlideParser` so that it is applied to all slides as they are parsed.
*   **Task 2.4: Testing and Validation**
    *   **Subtask 2.4.1:** Update existing tests or create new ones to verify that the cleaning logic is correctly applied to all slides.
    *   **Subtask 2.4.2:** Run all tests to ensure no regressions were introduced.
    *   **Subtask 2.4.3:** Perform "user testing" by running `main.py` and inspecting the generated HTML/JSON for all slides to ensure the cleaning has been applied correctly and consistently.
