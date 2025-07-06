# Outline

## Goals for this version
> Current problem: the files are so large that LLM's and even humans have trouble reading the code base and making edits. For LLM's, they have trouble holding the large file's in their context's. 
> Solution to try: Break up the code into smaller, explainable chunks

./html_writer.py: 530
./slide_layout_parser.py: 180
./slide_parser.py: 703
./pptx_parser.py: 131
./presentation_parser.py: 26
./data_models.py: 221
./json_writer.py: 118

1. Modularize the whole code base based on current python standards.
2. Use the ruff tool to lint and format code.

## Pre-project Workflow
> Here is a list of things to check / setup before you start working:

1. Ensure /tasks/version0.2.3.5/ directory is created.
2. Ensure a plan.md is created in this version's tasks directory, it will be empty for now.
3. Read the previous's versions directory and its file such as plan.md and other files to understand the most up to date code.

## Project Workflow

This project work flow **OVERRIDES** the GEMINI.md project workflow since this is a subversion. The goal of this version is to clean up the code while maintaining the FULL functionality.

I have a goal archticture in mind that I would like you to copy:

```
pptx_parser_project/
├── src/
│   └── pptx_parser/
│
│       ├── models/
│       │   └── core.py            # from data_models.py
│
│       ├── parsers/
│       │   ├── __init__.py
│       │   ├── slide/
│       │   │   ├── __init__.py
│       │   │   ├── base.py        # was slide_parser.py
│       │   │   ├── text.py
│       │   │   ├── tables.py
│       │   │   ├── shapes.py
│       │   │   └── charts.py
│       │   ├── layout.py          # from slide_layout_parser.py
│       │   ├── presentation.py    # from presentation_parser.py
│
│       ├── services/
│       │   └── document_parser.py # was pptx_parser.py, coordinates all parsing
│
│       ├── writers/
│       │   ├── html_writer.py
│       │   ├── json_writer.py
│       │   └── base_writer.py     # optional common interface
│
│       ├── utils/
│       │   └── xml_helpers.py     # for common XML ops
│
│       └── __init__.py
```

Please do you're best to eumulate this layout via the steps:

1. Load a file into your context by reading ONLY ONE FILE.
2. Look at the architecture and start building the blank files.
3. Transfer the code to each of the files in the architecture.
4. Create new tests with `uv pytest` for each of the functions/modular breakdown you created.
5. Once you have created new tests and it all works, use the `ruff` formatter & lintier tool with `uv` to format and lint the new code.
6. Once a file has been fully chunked and tested. Create a documentation file in this version's tasks/ directory that gives the signature of the file with explanations.
7. Do 1 "user test" where you do `uv run main.py` where you should not receive any errors.
8. Repeat 1-6 for each file in the src/ directory.
9. After all phases have been achieved for this version. Clean up your code ( remove print statements and debug statements ).
10. Git add, commit and push your code to GitHub. 
## Notes

- you should should only use uv commands to test and user test no python commands.
- main.py is the only way you should user test.
- If you have trouble editing a file more than 3 times, provide me the edit and I will do it manually so you can continue.
