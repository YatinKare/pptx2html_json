## Log: Define parse_pptx entrypoint

### What I did:
1.  Created a new function `parse_pptx` in `learnx_parser/__init__.py` to serve as the main API entry point for parsing PPTX files.
2.  Moved the PPTX unpacking logic (using `zipfile` and `shutil`) into this `parse_pptx` function.
3.  Modified `main.py` to import and use the new `parse_pptx` function, simplifying the main script.

### How I did it:
1.  Created `src/learnx_parser/__init__.py` and added the `parse_pptx` function, which takes `pptx_file_path` and `output_dir` as arguments.
2.  Implemented the unpacking logic within `parse_pptx`, including creating a temporary directory for unpacked content and cleaning it up afterwards.
3.  Instantiated `PptxParser` within `parse_pptx` and called `parse_presentation()`.
4.  Updated `main.py` to import `parse_pptx` and call it with the appropriate arguments.
5.  Ran `uv run python main.py` to verify the functionality.

### What was challenging:
None for this step.

### Future work:
Add tests for the new `parse_pptx` entry point.