"""Test cases for JSON schema compliance features"""

import json
import os
import shutil


class TestJsonSchemaCompliance:
    """Test that JSON output follows the target schema structure"""

    def test_top_level_structure(self):
        """Test that JSON output has correct top-level structure"""
        from learnx_parser.services.document_parser import DocumentParser

        parser = DocumentParser("./temp_pptx", "./test_output_schema")
        parser.parse_presentation()

        # Read the generated JSON file
        json_file_path = os.path.join("./test_output_schema", "presentation.json")
        assert os.path.exists(json_file_path), "JSON output file should exist"

        with open(json_file_path, "r") as f:
            json_data = json.load(f)

        # Test top-level structure matches schema
        required_fields = ["id", "title", "slides"]
        for field in required_fields:
            assert field in json_data, f"Missing required field: {field}"

        assert isinstance(json_data["slides"], list), "slides should be an array"

        # Clean up
        if os.path.exists("./test_output_schema"):
            shutil.rmtree("./test_output_schema")

    def test_slide_object_structure(self):
        """Test that slide objects have correct structure"""
        from learnx_parser.services.document_parser import DocumentParser

        parser = DocumentParser("./temp_pptx", "./test_output_schema")
        parser.parse_presentation()

        # Read the generated JSON file
        json_file_path = os.path.join("./test_output_schema", "presentation.json")

        with open(json_file_path, "r") as f:
            json_data = json.load(f)

        # Test slide structure
        slides = json_data.get("slides", [])
        assert len(slides) > 0, "Should have at least one slide"

        for slide in slides:
            required_slide_fields = ["id", "layout", "elements"]
            for field in required_slide_fields:
                assert field in slide, f"Slide missing required field: {field}"

            assert slide["id"].startswith("slide-"), (
                "Slide ID should start with 'slide-'"
            )
            assert isinstance(slide["elements"], list), "elements should be an array"

        # Clean up
        if os.path.exists("./test_output_schema"):
            shutil.rmtree("./test_output_schema")

    def test_element_types(self):
        """Test that elements have valid types"""
        from learnx_parser.services.document_parser import DocumentParser

        parser = DocumentParser("./temp_pptx", "./test_output_schema")
        parser.parse_presentation()

        # Read the generated JSON file
        json_file_path = os.path.join("./test_output_schema", "presentation.json")

        with open(json_file_path, "r") as f:
            json_data = json.load(f)

        # Test element types
        valid_types = [
            "title",
            "text-box",
            "bullet-list",
            "image",
            "quote",
            "chart-placeholder",
        ]

        for slide in json_data.get("slides", []):
            for element in slide.get("elements", []):
                assert "type" in element, "Element should have a type"
                assert element["type"] in valid_types, (
                    f"Invalid element type: {element['type']}"
                )

        # Clean up
        if os.path.exists("./test_output_schema"):
            shutil.rmtree("./test_output_schema")

    def test_no_absolute_positioning(self):
        """Test that JSON output contains no absolute positioning data"""
        from learnx_parser.services.document_parser import DocumentParser

        parser = DocumentParser("./temp_pptx", "./test_output_schema")
        parser.parse_presentation()

        # Read the generated JSON file
        json_file_path = os.path.join("./test_output_schema", "presentation.json")

        with open(json_file_path, "r") as f:
            json_data = json.load(f)

        def check_no_positioning(obj, path=""):
            """Recursively check that no positioning properties exist"""
            if isinstance(obj, dict):
                forbidden_props = ["x", "y", "width", "height", "left", "top"]
                for prop in forbidden_props:
                    assert prop not in obj, (
                        f"Found forbidden positioning property '{prop}' at {path}"
                    )

                for key, value in obj.items():
                    check_no_positioning(value, f"{path}.{key}")
            elif isinstance(obj, list):
                for i, item in enumerate(obj):
                    check_no_positioning(item, f"{path}[{i}]")

        check_no_positioning(json_data)

        # Clean up
        if os.path.exists("./test_output_schema"):
            shutil.rmtree("./test_output_schema")
