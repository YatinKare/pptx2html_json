# Outline

## Goals for this Version
  1. Background as a Single Image

  > This is a robust strategy to ensure visual fidelity by treating the entire slide
  > background as a single, static image. Instead of trying to replicate complex
  > gradients, theme colors, and background images with CSS, the parser will render the
  > final background of each slide into a PNG. This image will then be used as the
  > background-image for the main slide div, perfectly preserving the original look and
  > feel as seen in the HTML5Point example.

  2. Enhanced Text Formatting and Semantics

  > This goal focuses on achieving full text parity with the original presentation by
  > correctly implementing the complete OOXML inheritance model for all font properties.
  >  This includes not just font size and family, but also styles like bold, italics,
  > and underline. For special characters, such as the arrows in the Respiratory
  > presentation, the key is ensuring the correct font-family is applied in the final
  > HTML, as the issue is typically one of font rendering, not character encoding.


  3. Render Complex Shapes as Images
  > This is a highly effective method for handling complex DrawingML objects like
  > charts, diagrams, and custom icons without the immense overhead of parsing their
  > underlying data structures. Similar to the background image strategy, these
  > elements will be treated as "black boxes" and rendered as individual, transparent
  > PNG images. These images will then be absolutely positioned on the slide,
  > guaranteeing their appearance and location are preserved perfectly while
  > simplifying the parsing logic immensely.

## Pre-Project Workflow
Here are a list of things to check / setup before you start working:
1. Ensure /tasks/version{this-version}/ directory is created.
2. Ensure a plan.md is created in this version's tasks directory, it will be empty for now.
3. Read the previous's versions directory and its file such as plan.md and other files to understand the most up to date code.

## Project Workflow
We will implement a workflow ON TOP of the workflow already presented in {.gemini/GEMINI.md}. This workflow will be for both goals separately. 

1. Read the GEMINI.md file in its ENTIRETY to understand the standardizations for coding and the overall goal for this software.
2. Make sure you have read the previous version's directory and its files so that you have an understanding of what you're working with..
3. Make sure you have read the previous version's git commits and understood it.
4. Create a plan.md based on the goals that have phases, tasks and subtasks
    - You may look in the Gemini.md example or the previous version's plan.md for an example of the format, not the content.
5. Implement the task-by-task workflow stated in the GEMINI.md file.
    - Your first task will be reading documentation. It is HIGHLY important you do this thoroughly. If you are working with the open XML you should consult the docs/ directory as it has everything. DO NOT ASSUME OR MOVE ON. 
6. Continue code --> testing --> debug --> repeat. 
    - When coding / testing you should NEVER use anything that starts with `pip` or `python`. Everything should be used with the `uv` program like `uv run main.py` or `uv pytest`. 
    - For **EVERY** new feature you write, you **MUST** create a test case for its functionality. To write test cases examine the broken down powerpoint presentation of the galaxy presentation in temp_pptx/
    - Each test must be named according to its feature, nothing to do with its version.
7. Repeat 5 & 6 for each subtask within a task.
8. Perform "user testing"
    - Simulates what it would be like if a user would run the package.
    - Uses `main.py` to user test
    - Examine the output of the user test via the output folder (ex: the html/json file) and check if the outcome is desired.
    - If the desired has NOT been desired go back to step 6.
    - **IMPORTANT**: Please do not create extra scripts, if you do, remember to delete them after you are done.
9. Use `ruff` to check formating and lintting of the code. Make sure you fix all ruff callouts.
9. After a task has been completed. Create a task{N}.md file in the /tasks/version{this-version}/ directory and journal about this task as described in the GEMINI.md file.
10. Repeat steps 5-9 for each phase in plan.md

## Post-Project Workflow
1. After all phases have been achieved for this version. Clean up your code ( remove print statements and debug statements ).
2. Git add, commit and push your code to GitHub. 

## Notes
- you should should only use uv commands to test and user test no python commands.
- main.py is the only way you should user test.
- If you have trouble editing a file more than 3 times, provide me the edit and I will do it manually so you can continue.

* One Subtask at a Time: All work must strictly follow the plan.md hierarchy. Do not
  begin a new subtask until the current one is complete and verified. This prevents
  scope creep and ensures focus.
* Atomic Commits: Each commit to the repository must correspond to a single, completed
  subtask. The commit message should clearly state which subtask it resolves. This
  creates a clean and understandable project history.
* Mandatory Testing: After every code change, no matter how small, the 
  manual user test (uv run main.py) must be run to verify
  the change and check for regressions. Broken code should never be committed.
