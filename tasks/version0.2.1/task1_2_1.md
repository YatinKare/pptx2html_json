## Log: Define New Data Structures for Semantic Layout

- **Prompt**: Define new data structures for semantic layout.
- **Issue**: None.

### What I did:
1.  Created `LayoutPlaceholder` dataclass to store placeholder type, index, and transform information.
2.  Created `SlideLayout` dataclass to store the layout name, type, and a list of `LayoutPlaceholder` objects.
3.  Updated the `Slide` dataclass to include an optional `slide_layout` field of type `SlideLayout`.

### How I did it:
- Modified `src/learnx_parser/data_models.py` using the `replace` tool to add the new dataclasses and update the `Slide` dataclass.

### What was challenging:
- None, this was a straightforward data modeling task.

### Future work:
- Implement the layout inference logic in `slide_layout_parser.py` to populate these new data structures.
