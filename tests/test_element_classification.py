"""Test cases for element type classification features"""

import json
import os
import shutil


class TestElementClassification:
    """Test proper classification of slide elements into types"""

    def test_title_element_detection(self):
        """Test that title elements are correctly identified"""
        from learnx_parser.services.document_parser import DocumentParser

        parser = DocumentParser("./temp_pptx", "./test_output_elements")
        parser.parse_presentation()

        # Read the generated JSON file
        json_file_path = os.path.join("./test_output_elements", "presentation.json")

        with open(json_file_path, "r") as f:
            json_data = json.load(f)

        # Check that each slide has appropriate title elements
        slides = json_data.get("slides", [])
        title_slides_count = 0

        for slide in slides:
            title_elements = [
                el for el in slide.get("elements", []) if el.get("type") == "title"
            ]

            # Most slides should have at least one title
            if title_elements:
                title_slides_count += 1

                # Validate title element structure
                for title_el in title_elements:
                    assert "text" in title_el, "Title element should have text"
                    assert isinstance(title_el["text"], str), (
                        "Title text should be string"
                    )
                    assert len(title_el["text"].strip()) > 0, (
                        "Title should not be empty"
                    )

        # Should find titles on most slides
        assert title_slides_count >= len(slides) * 0.8, "Most slides should have titles"

        # Clean up
        if os.path.exists("./test_output_elements"):
            shutil.rmtree("./test_output_elements")

    def test_image_element_detection(self):
        """Test that image elements are correctly identified"""
        from learnx_parser.services.document_parser import DocumentParser

        parser = DocumentParser("./temp_pptx", "./test_output_elements")
        parser.parse_presentation()

        # Read the generated JSON file
        json_file_path = os.path.join("./test_output_elements", "presentation.json")

        with open(json_file_path, "r") as f:
            json_data = json.load(f)

        # Count image elements
        image_elements = []
        for slide in json_data.get("slides", []):
            for element in slide.get("elements", []):
                if element.get("type") == "image":
                    image_elements.append(element)

        # Should find some images in the Galaxy presentation
        assert len(image_elements) > 0, "Should detect image elements in presentation"

        # Validate image element structure
        for img_el in image_elements:
            assert "src" in img_el, "Image element should have src property"
            assert isinstance(img_el["src"], str), "Image src should be string"
            assert len(img_el["src"]) > 0, "Image src should not be empty"

            # Should point to media files
            assert "media/" in img_el["src"] or "image" in img_el["src"], (
                "Image src should reference media files"
            )

        # Clean up
        if os.path.exists("./test_output_elements"):
            shutil.rmtree("./test_output_elements")

    def test_text_box_vs_bullet_list_classification(self):
        """Test that text content is properly classified as text-box vs bullet-list"""
        from learnx_parser.services.document_parser import DocumentParser

        parser = DocumentParser("./temp_pptx", "./test_output_elements")
        parser.parse_presentation()

        # Read the generated JSON file
        json_file_path = os.path.join("./test_output_elements", "presentation.json")

        with open(json_file_path, "r") as f:
            json_data = json.load(f)

        # Count different text element types
        text_boxes = []
        bullet_lists = []

        for slide in json_data.get("slides", []):
            for element in slide.get("elements", []):
                if element.get("type") == "text-box":
                    text_boxes.append(element)
                elif element.get("type") == "bullet-list":
                    bullet_lists.append(element)

        # Should have both types
        assert len(text_boxes) > 0, "Should find text-box elements"
        assert len(bullet_lists) > 0, "Should find bullet-list elements"

        # Validate text-box structure
        for text_box in text_boxes:
            assert "text" in text_box, "Text box should have text property"
            assert isinstance(text_box["text"], str), "Text box text should be string"

        # Validate bullet-list structure
        for bullet_list in bullet_lists:
            assert "items" in bullet_list, "Bullet list should have items property"
            assert isinstance(bullet_list["items"], list), (
                "Bullet list items should be array"
            )
            assert len(bullet_list["items"]) > 0, (
                "Bullet list should have at least one item"
            )

            for item in bullet_list["items"]:
                assert "text" in item, "Bullet item should have text"
                assert isinstance(item["text"], str), (
                    "Bullet item text should be string"
                )

        # Clean up
        if os.path.exists("./test_output_elements"):
            shutil.rmtree("./test_output_elements")

    def test_element_content_quality(self):
        """Test that elements contain meaningful content"""
        from learnx_parser.services.document_parser import DocumentParser

        parser = DocumentParser("./temp_pptx", "./test_output_elements")
        parser.parse_presentation()

        # Read the generated JSON file
        json_file_path = os.path.join("./test_output_elements", "presentation.json")

        with open(json_file_path, "r") as f:
            json_data = json.load(f)

        for slide in json_data.get("slides", []):
            for element in slide.get("elements", []):
                element_type = element.get("type")

                if element_type == "title":
                    text = element.get("text", "")
                    assert len(text.strip()) > 0, "Title should not be empty"
                    assert len(text) < 200, "Title should be reasonably short"

                elif element_type == "text-box":
                    text = element.get("text", "")
                    assert len(text.strip()) > 0, "Text box should not be empty"

                elif element_type == "bullet-list":
                    items = element.get("items", [])
                    assert len(items) > 0, "Bullet list should have items"

                    for item in items:
                        item_text = item.get("text", "")
                        assert len(item_text.strip()) > 0, (
                            "Bullet item should not be empty"
                        )

                elif element_type == "image":
                    src = element.get("src", "")
                    assert len(src.strip()) > 0, "Image should have src"
                    assert not src.startswith("http"), (
                        "Should use local paths, not URLs"
                    )

        # Clean up
        if os.path.exists("./test_output_elements"):
            shutil.rmtree("./test_output_elements")

    def test_element_ordering(self):
        """Test that elements maintain logical ordering within slides"""
        from learnx_parser.services.document_parser import DocumentParser

        parser = DocumentParser("./temp_pptx", "./test_output_elements")
        parser.parse_presentation()

        # Read the generated JSON file
        json_file_path = os.path.join("./test_output_elements", "presentation.json")

        with open(json_file_path, "r") as f:
            json_data = json.load(f)

        for slide in json_data.get("slides", []):
            elements = slide.get("elements", [])

            if len(elements) > 1:
                # Check for logical ordering patterns
                title_indices = []
                for i, element in enumerate(elements):
                    if element.get("type") == "title":
                        title_indices.append(i)

                # If there are titles, they should generally come first
                if title_indices:
                    first_title_index = min(title_indices)
                    # Allow some flexibility, but title should be in first half
                    assert first_title_index < len(elements) / 2, (
                        "Title should appear early in element order"
                    )

        # Clean up
        if os.path.exists("./test_output_elements"):
            shutil.rmtree("./test_output_elements")
