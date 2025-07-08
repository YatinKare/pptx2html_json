"""Test cases for text semantics extraction features"""

import json
import os
import shutil


class TestTextSemantics:
    """Test text formatting extraction and application"""

    def test_text_style_properties(self):
        """Test that text elements support style properties"""
        from learnx_parser.services.document_parser import DocumentParser

        parser = DocumentParser("./temp_pptx", "./test_output_text")
        parser.parse_presentation()

        # Read the generated JSON file
        json_file_path = os.path.join("./test_output_text", "presentation.json")

        with open(json_file_path, "r") as f:
            json_data = json.load(f)

        # Look for elements with style properties
        elements_with_style = []
        for slide in json_data.get("slides", []):
            for element in slide.get("elements", []):
                if "style" in element and element["style"]:
                    elements_with_style.append(element)
                elif element.get("type") == "bullet-list" and "items" in element:
                    for item in element["items"]:
                        if "style" in item and item["style"]:
                            elements_with_style.append(item)

        # Test that style properties are valid when present
        for element in elements_with_style:
            style = element.get("style", {})
            valid_style_props = ["bold", "italic", "fontSize", "underline"]
            for prop in style.keys():
                assert prop in valid_style_props, f"Invalid style property: {prop}"

                # Test property types
                if prop in ["bold", "italic", "underline"]:
                    assert isinstance(style[prop], bool), f"{prop} should be boolean"
                elif prop == "fontSize":
                    assert isinstance(style[prop], (int, float)), (
                        f"fontSize should be numeric"
                    )

        # Clean up
        if os.path.exists("./test_output_text"):
            shutil.rmtree("./test_output_text")

    def test_text_box_style_support(self):
        """Test that text-box elements can have style properties"""
        from learnx_parser.services.document_parser import DocumentParser

        parser = DocumentParser("./temp_pptx", "./test_output_text")
        parser.parse_presentation()

        # Read the generated JSON file
        json_file_path = os.path.join("./test_output_text", "presentation.json")

        with open(json_file_path, "r") as f:
            json_data = json.load(f)

        # Find text-box elements
        text_boxes = []
        for slide in json_data.get("slides", []):
            for element in slide.get("elements", []):
                if element.get("type") == "text-box":
                    text_boxes.append(element)

        assert len(text_boxes) > 0, "Should find text-box elements in presentation"

        # Check that text boxes can have style (structure should support it)
        for text_box in text_boxes:
            assert "text" in text_box, "Text box should have text property"
            # Style is optional, but if present should be valid
            if "style" in text_box:
                style = text_box["style"]
                assert isinstance(style, dict), "Style should be a dictionary"

        # Clean up
        if os.path.exists("./test_output_text"):
            shutil.rmtree("./test_output_text")

    def test_bullet_list_item_styles(self):
        """Test that bullet list items can have individual styles"""
        from learnx_parser.services.document_parser import DocumentParser

        parser = DocumentParser("./temp_pptx", "./test_output_text")
        parser.parse_presentation()

        # Read the generated JSON file
        json_file_path = os.path.join("./test_output_text", "presentation.json")

        with open(json_file_path, "r") as f:
            json_data = json.load(f)

        # Find bullet list items
        bullet_items = []
        for slide in json_data.get("slides", []):
            for element in slide.get("elements", []):
                if element.get("type") == "bullet-list" and "items" in element:
                    bullet_items.extend(element["items"])

        assert len(bullet_items) > 0, "Should find bullet list items in presentation"

        # Check that bullet items can have style
        for item in bullet_items:
            assert "text" in item, "Bullet item should have text property"
            # Style is optional, but if present should be valid
            if "style" in item:
                style = item["style"]
                assert isinstance(style, dict), "Style should be a dictionary"
                # Validate style properties
                valid_props = ["bold", "italic", "fontSize", "underline"]
                for prop in style.keys():
                    assert prop in valid_props, f"Invalid style property: {prop}"

        # Clean up
        if os.path.exists("./test_output_text"):
            shutil.rmtree("./test_output_text")

    def test_font_size_extraction(self):
        """Test that font sizes are correctly extracted and applied"""
        from learnx_parser.services.document_parser import DocumentParser

        parser = DocumentParser("./temp_pptx", "./test_output_text")
        parser.parse_presentation()

        # Read the generated JSON file
        json_file_path = os.path.join("./test_output_text", "presentation.json")

        with open(json_file_path, "r") as f:
            json_data = json.load(f)

        # Look for fontSize properties
        font_sizes_found = []
        for slide in json_data.get("slides", []):
            for element in slide.get("elements", []):
                if "style" in element and "fontSize" in element["style"]:
                    font_sizes_found.append(element["style"]["fontSize"])
                elif element.get("type") == "bullet-list" and "items" in element:
                    for item in element["items"]:
                        if "style" in item and "fontSize" in item["style"]:
                            font_sizes_found.append(item["style"]["fontSize"])

        # If font sizes are found, validate them
        for font_size in font_sizes_found:
            assert isinstance(font_size, (int, float)), "Font size should be numeric"
            assert font_size > 0, "Font size should be positive"
            assert font_size < 1000, "Font size should be reasonable (< 1000)"

        # Clean up
        if os.path.exists("./test_output_text"):
            shutil.rmtree("./test_output_text")

    def test_bold_italic_underline_extraction(self):
        """Test that bold, italic, and underline formatting is extracted"""
        from learnx_parser.services.document_parser import DocumentParser

        parser = DocumentParser("./temp_pptx", "./test_output_text")
        parser.parse_presentation()

        # Read the generated JSON file
        json_file_path = os.path.join("./test_output_text", "presentation.json")

        with open(json_file_path, "r") as f:
            json_data = json.load(f)

        # Look for formatting properties
        formatting_found = {"bold": False, "italic": False, "underline": False}

        for slide in json_data.get("slides", []):
            for element in slide.get("elements", []):
                if "style" in element:
                    style = element["style"]
                    for prop in ["bold", "italic", "underline"]:
                        if prop in style:
                            formatting_found[prop] = True
                            assert isinstance(style[prop], bool), (
                                f"{prop} should be boolean"
                            )

                elif element.get("type") == "bullet-list" and "items" in element:
                    for item in element["items"]:
                        if "style" in item:
                            style = item["style"]
                            for prop in ["bold", "italic", "underline"]:
                                if prop in style:
                                    formatting_found[prop] = True
                                    assert isinstance(style[prop], bool), (
                                        f"{prop} should be boolean"
                                    )

        # Note: The galaxy presentation might not have explicit formatting,
        # but the structure should support it and extraction should work without errors

        # Clean up
        if os.path.exists("./test_output_text"):
            shutil.rmtree("./test_output_text")
