Goal

  The primary goal is to completely refactor the bullet point and mixed-content
  rendering system. We will replace the current fragile, stateful renderer with a
  simple, linear one and fix the broken style inheritance logic. This will ensure that
  text boxes with a mix of bulleted and non-bulleted paragraphs, like in slide 5 of the
   "Respiratory" presentation, are rendered correctly in both HTML and JSON outputs, as
   outlined in the report.md.

  Strategies & Information Needed

   1. The Core Problem: The current system, particularly in element_renderers.py, uses a
      list_stack to manage list nesting. This is the root of all evil here. It cannot
      handle transitions between bulleted and plain text paragraphs within the same text
      box, leading to incorrect HTML nesting. The json_writer.py has a similar flawed
      logic.

   2. The New Rendering Strategy: We will implement a simple, linear-pass renderer. This
      approach iterates through paragraphs one by one and decides whether to open a list,
      close a list, add an item to an existing list, or just render a plain paragraph.
      It's a basic state machine that only needs to know if it's currently inside a list
      or not. This is a far more robust and less error-prone method, as suggested by the
      analysis in report.md.

   3. Bullet Property Resolution: The logic for determining a paragraph's style is
      scattered and incomplete. The StyleResolver is the correct place for this, but its
      implementation is flawed. We will centralize all bullet and style resolution within
      StyleResolver and make it follow the correct OOXML inheritance hierarchy: Paragraph
      -> Layout -> Master -> Presentation Defaults. The old, confusing logic in text.py
      will be completely removed.

   4. Defining a "Bullet Paragraph": For all tasks below, the definition of a "bullet
      paragraph" is strict and simple. A paragraph is considered a bullet item if, after
      style resolution, its properties.bullet_type is not None and is not 'none'. Any
      other paragraph is considered plain text. The junior dev must use this precise
      definition.

---

Task List for Claude Code

Part 1: Rewrite the Goddamn HTML Renderer

File to Modify: src/learnx_parser/writers/element_renderers.py

- [x] Task 1: Overhaul render_text_frame_html
  - [x] Subtask 1.1: Rip out the existing logic. Delete the list_stack variable and the
        entire loop that uses it. We're starting fresh.
  - [x] Subtask 1.2: Implement the new linear rendering logic.
    - [x] Initialize a new list to hold the final HTML elements (e.g., html_elements =
          []).
    - [x] Initialize a simple state tracker for lists. You'll need a list to hold the
          current list items (e.g., current_list_items = []) and the current list
          level (e.g., current_list_level = -1).
    - [x] Loop through each para in text_frame.paragraphs.
    - [x] Inside the loop, use the following logic:
      - [x] Determine if the current paragraph is a bullet item using the
            definition from the "Strategies" section above.
      - [x] Get the paragraph's level (para.properties.level). Treat a None level
            as 0.
      - [x] If the paragraph IS a bullet item:
        - [x] If there is an open list (current_list_items is not empty) but the
              level is different from current_list_level, you must first close the
              existing list, add it to html_elements, and clear current_list_items.
        - [x] Render the paragraph's content (its runs) into an HTML string.
        - [x] Add this rendered content as a new item to the current_list_items
              list.
        - [x] Update current_list_level to the current paragraph's level.
      - [x] If the paragraph IS NOT a bullet item:
        - [x] If there is an open list (current_list_items is not empty), you must
              close it. This means wrapping current_list_items in the appropriate
              <ul> or <ol> tags, adding the result to html_elements, and then
              clearing current_list_items and resetting current_list_level.
        - [x] Render the paragraph as a standard <p> tag and add it directly to
              html_elements.
  - [x] Subtask 1.3: After the loop finishes, check if current_list_items still contains
        items. If it does, it means the text box ended with a list. You must close this
        final list and add it to html_elements.
  - [x] Subtask 1.4: Join the html_elements list into a single string and return it.
  - [x] Subtask 1.5: Remove the now-unused helper functions _render_as_regular_text,
        _render_as_bullet_list, _build_nested_list, _get_list_style_for_level, and
        _get_list_type_for_paragraph. They are part of the old, broken system.

Part 2: Fix the Broken Style Resolution

File to Modify: src/learnx_parser/services/style_resolver.py

- [x] Task 2: Refactor resolve_paragraph_properties
  - [x] Subtask 2.1: The current implementation is a disaster. Rewrite it to follow the
        correct, simple inheritance hierarchy for bullet properties as documented in
        report.md.
  - [x] Subtask 2.2: The function should perform a search in the following strict order:
    - [x] Paragraph Properties: Check the paragraph's own <a:pPr> element first. If it
          contains <a:buNone>, the bullet type is 'none' and the search stops. If it
          contains <a:buChar>, <a:buAutoNum>, etc., use that and stop.
    - [x] Layout List Styles: If no bullet property is found on the paragraph, check
          the list_styles of the slide_layout for the paragraph's level (p_level). If
          a style is found, use it and stop.
    - [x] Master List Styles: If nothing is found on the layout, check the list_styles
          of the slide_master (accessible via slide_layout.slide_master) for the
          paragraph's level. If a style is found, use it and stop.
    - [x] Presentation Defaults: If the master provides no style, check the
          presentation_defaults.
    - [x] No Bullet: If no bullet style is found after checking all levels, the
          paragraph does not have a bullet. bullet_type should remain None.
  - [x] Subtask 2.3: Ensure the function correctly handles paragraphs that have a lvl
        attribute but no explicit bullet definition; it must inherit the style from a
        higher level (layout, master, etc.).

File to Modify: src/learnx_parser/parsers/slide/text.py

- [x] Task 3: Remove Obsolete Bullet Logic
  - [x] Subtask 3.1: Delete the entire _resolve_bullet_properties_intelligently
        function and all of its helper functions (_check_bullet_properties_in_element,
        _apply_bullet_result, _get_layout_bullet_properties,
        _get_master_bullet_properties, _get_presentation_bullet_properties). They are
        redundant and incorrect.
  - [x] Subtask 3.2: In the extract_paragraph_properties function, remove any fallback
        logic. It should only call style_resolver.resolve_paragraph_properties to get
        the paragraph's properties. No more, no less.

Part 3: Clean up
- [ ] Task 4: Replace Flawed Bullet Detection
  - [ ] Subtask 5.1: Delete the _is_bullet_paragraph helper function. Its
        heuristic-based approach is garbage.
  - [ ] Subtask 5.2: In its place, use the same, simple definition: a paragraph is a
        bullet if paragraph.properties.bullet_type is not None and
        paragraph.properties.bullet_type != 'none'.

