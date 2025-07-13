# Outline

## Goals for this Version
1. Make sure all elements fit into 1 visible page, there should be no overflow of any elements off screen.
2. Get the background picture(s) (look into the docs/ directory and the HTML5point.html example)
3. Get the fonts/ font colors styles.

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
