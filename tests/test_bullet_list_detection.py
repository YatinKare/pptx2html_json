"""Test cases for bullet list detection features"""

import json
import os
import shutil


class TestBulletListDetection:
    """Test improved bullet list detection functionality"""

    def test_agenda_items_as_bullet_list(self):
        """Test that agenda items are correctly detected as bullet-list"""
        from learnx_parser.services.document_parser import DocumentParser

        parser = DocumentParser("./temp_pptx", "./test_output_bullets")
        parser.parse_presentation()

        # Read the generated JSON file
        json_file_path = os.path.join("./test_output_bullets", "presentation.json")

        with open(json_file_path, "r") as f:
            json_data = json.load(f)

        # Find the agenda slide
        agenda_slide = None
        slides = json_data.get("slides", [])
        for slide in slides:
            for element in slide.get("elements", []):
                if element.get("type") == "title" and "Agenda" in element.get(
                    "text", ""
                ):
                    agenda_slide = slide
                    break

        assert agenda_slide is not None, "Could not find agenda slide"

        # Check that agenda items are detected as bullet-list
        bullet_lists = [
            el
            for el in agenda_slide.get("elements", [])
            if el.get("type") == "bullet-list"
        ]
        assert len(bullet_lists) > 0, "Agenda items should be detected as bullet-list"

        # Check that bullet list contains expected items
        agenda_bullet_list = bullet_lists[0]
        assert "items" in agenda_bullet_list, "Bullet list should have items"
        assert len(agenda_bullet_list["items"]) >= 3, (
            "Should have multiple agenda items"
        )

        # Check for topic items
        topic_items = [
            item
            for item in agenda_bullet_list["items"]
            if "Topic" in item.get("text", "")
        ]
        assert len(topic_items) >= 3, "Should detect multiple topic items"

        # Clean up
        if os.path.exists("./test_output_bullets"):
            shutil.rmtree("./test_output_bullets")

    def test_explicit_bullet_detection(self):
        """Test that explicitly marked bullets are detected"""
        from learnx_parser.services.document_parser import DocumentParser

        parser = DocumentParser("./temp_pptx", "./test_output_bullets")
        parser.parse_presentation()

        # Read the generated JSON file
        json_file_path = os.path.join("./test_output_bullets", "presentation.json")

        with open(json_file_path, "r") as f:
            json_data = json.load(f)

        # Count total bullet lists found
        total_bullet_lists = 0
        for slide in json_data.get("slides", []):
            bullet_lists = [
                el
                for el in slide.get("elements", [])
                if el.get("type") == "bullet-list"
            ]
            total_bullet_lists += len(bullet_lists)

        # Should find some bullet lists in the presentation
        assert total_bullet_lists > 0, (
            "Should detect some bullet lists in the presentation"
        )

        # Clean up
        if os.path.exists("./test_output_bullets"):
            shutil.rmtree("./test_output_bullets")

    def test_bullet_list_item_structure(self):
        """Test that bullet list items have correct structure"""
        from learnx_parser.services.document_parser import DocumentParser

        parser = DocumentParser("./temp_pptx", "./test_output_bullets")
        parser.parse_presentation()

        # Read the generated JSON file
        json_file_path = os.path.join("./test_output_bullets", "presentation.json")

        with open(json_file_path, "r") as f:
            json_data = json.load(f)

        # Find bullet lists and validate their structure
        bullet_lists_found = 0
        for slide in json_data.get("slides", []):
            for element in slide.get("elements", []):
                if element.get("type") == "bullet-list":
                    bullet_lists_found += 1

                    # Check that bullet list has items
                    assert "items" in element, (
                        "Bullet list should have 'items' property"
                    )
                    assert isinstance(element["items"], list), (
                        "Bullet list items should be an array"
                    )

                    # Check structure of individual items
                    for item in element["items"]:
                        assert isinstance(item, dict), (
                            "Bullet list item should be an object"
                        )
                        assert "text" in item, (
                            "Bullet list item should have 'text' property"
                        )
                        assert isinstance(item["text"], str), (
                            "Bullet list item text should be a string"
                        )

                        # If style is present, validate it
                        if "style" in item:
                            style = item["style"]
                            assert isinstance(style, dict), "Style should be an object"
                            valid_style_props = [
                                "bold",
                                "italic",
                                "fontSize",
                                "underline",
                            ]
                            for prop in style.keys():
                                assert prop in valid_style_props, (
                                    f"Invalid style property: {prop}"
                                )

        assert bullet_lists_found > 0, (
            "Should find at least one bullet list to validate"
        )

        # Clean up
        if os.path.exists("./test_output_bullets"):
            shutil.rmtree("./test_output_bullets")

    def test_heuristic_bullet_detection(self):
        """Test heuristic bullet detection for list-like content"""
        from learnx_parser.services.document_parser import DocumentParser

        parser = DocumentParser("./temp_pptx", "./test_output_bullets")
        parser.parse_presentation()

        # Read the generated JSON file
        json_file_path = os.path.join("./test_output_bullets", "presentation.json")

        with open(json_file_path, "r") as f:
            json_data = json.load(f)

        # Look for slides that should have heuristically detected bullets
        slides_with_bullets = []
        for slide in json_data.get("slides", []):
            bullet_lists = [
                el
                for el in slide.get("elements", [])
                if el.get("type") == "bullet-list"
            ]
            if bullet_lists:
                slides_with_bullets.append(slide)

        # Should detect bullets in agenda slide and potentially others
        assert len(slides_with_bullets) >= 1, "Should detect bullets through heuristics"

        # Verify that detected bullets contain reasonable content
        for slide in slides_with_bullets:
            bullet_lists = [
                el
                for el in slide.get("elements", [])
                if el.get("type") == "bullet-list"
            ]
            for bullet_list in bullet_lists:
                items = bullet_list.get("items", [])
                assert len(items) >= 1, (
                    "Heuristically detected bullet lists should have at least one item"
                )

                # Check that items have reasonable length (not too long for bullets)
                for item in items:
                    text = item.get("text", "")
                    assert len(text) < 200, (
                        f"Bullet item text too long: {len(text)} chars"
                    )

        # Clean up
        if os.path.exists("./test_output_bullets"):
            shutil.rmtree("./test_output_bullets")
