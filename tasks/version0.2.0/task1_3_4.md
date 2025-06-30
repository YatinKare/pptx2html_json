# Task 1.3.4: Adjust expected values in `test_flexbox_layout.py` and `test_html_writer.py` to account for rounding in `_emu_to_px`

**Status:** Completed

**Description:**
Modified the expected pixel values in the assertions within `tests/test_flexbox_layout.py` and `tests/test_html_writer.py`. This adjustment accounts for the rounding behavior of the `_emu_to_px` conversion function, ensuring that tests pass consistently despite minor floating-point discrepancies.
