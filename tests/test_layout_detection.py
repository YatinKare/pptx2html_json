"""Test cases for semantic layout detection features"""

import json
import os
import shutil


class TestLayoutDetection:
    """Test that PowerPoint layouts are mapped to semantic names"""

    def test_semantic_layout_names(self):
        """Test that layouts use semantic names instead of PowerPoint internal names"""
        from learnx_parser.services.document_parser import DocumentParser

        parser = DocumentParser("./temp_pptx", "./test_output_layout")
        parser.parse_presentation()

        # Read the generated JSON file
        json_file_path = os.path.join("./test_output_layout", "presentation.json")

        with open(json_file_path, "r") as f:
            json_data = json.load(f)

        # Test that layout uses semantic names
        semantic_layouts = [
            "title-only",
            "title-and-content",
            "title-and-bullets",
            "title-and-image",
            "image-left",
            "image-right",
            "side-by-side",
            "two-column-text",
            "quote-slide",
            "image-gallery",
            "custom",
        ]

        powerpoint_layouts = ["titleOnly", "picTx", "titlePic", "title", "obj"]

        for slide in json_data.get("slides", []):
            layout = slide.get("layout")
            assert layout in semantic_layouts, f"Layout '{layout}' is not semantic"
            assert layout not in powerpoint_layouts, (
                f"Layout '{layout}' is PowerPoint internal name"
            )

        # Clean up
        if os.path.exists("./test_output_layout"):
            shutil.rmtree("./test_output_layout")

    def test_specific_layout_mappings(self):
        """Test that specific slides get correct layout mappings"""
        from learnx_parser.services.document_parser import DocumentParser

        parser = DocumentParser("./temp_pptx", "./test_output_layout")
        parser.parse_presentation()

        # Read the generated JSON file
        json_file_path = os.path.join("./test_output_layout", "presentation.json")

        with open(json_file_path, "r") as f:
            json_data = json.load(f)

        slides = json_data.get("slides", [])

        # Check specific slides for correct layout mapping based on Galaxy presentation
        layout_expectations = {
            0: "title-only",  # Galaxy title slide (0-indexed)
            1: "side-by-side",  # Agenda with image and bullet list
            2: "title-and-image",  # The power of communication (title + image only)
            11: "title-only",  # Speaking engagement metrics (title only)
        }

        for slide_index, expected_layout in layout_expectations.items():
            if slide_index < len(slides):
                slide = slides[slide_index]
                actual_layout = slide.get("layout")
                assert actual_layout == expected_layout, (
                    f"Slide {slide_index + 1} should have layout '{expected_layout}', got '{actual_layout}'"
                )

        # Clean up
        if os.path.exists("./test_output_layout"):
            shutil.rmtree("./test_output_layout")

    def test_layout_consistency(self):
        """Test that layout detection is consistent with content"""
        from learnx_parser.services.document_parser import DocumentParser

        parser = DocumentParser("./temp_pptx", "./test_output_layout")
        parser.parse_presentation()

        # Read the generated JSON file
        json_file_path = os.path.join("./test_output_layout", "presentation.json")

        with open(json_file_path, "r") as f:
            json_data = json.load(f)

        for slide in json_data.get("slides", []):
            layout = slide.get("layout")
            elements = slide.get("elements", [])

            # Count element types
            title_count = sum(1 for el in elements if el.get("type") == "title")
            text_box_count = sum(1 for el in elements if el.get("type") == "text-box")
            bullet_list_count = sum(
                1 for el in elements if el.get("type") == "bullet-list"
            )
            image_count = sum(1 for el in elements if el.get("type") == "image")

            # Validate layout consistency with content
            if layout == "title-only":
                assert title_count == 1, (
                    f"title-only layout should have exactly 1 title"
                )
                assert text_box_count + bullet_list_count + image_count == 0, (
                    f"title-only layout should have no other elements"
                )

            elif layout == "title-and-bullets":
                assert title_count >= 1, (
                    f"title-and-bullets layout should have at least 1 title"
                )
                assert bullet_list_count >= 1, (
                    f"title-and-bullets layout should have at least 1 bullet list"
                )

            elif layout == "title-and-image":
                assert title_count >= 1, (
                    f"title-and-image layout should have at least 1 title"
                )
                assert image_count >= 1, (
                    f"title-and-image layout should have at least 1 image"
                )

            elif layout == "side-by-side":
                assert len(elements) >= 2, (
                    f"side-by-side layout should have at least 2 elements"
                )

        # Clean up
        if os.path.exists("./test_output_layout"):
            shutil.rmtree("./test_output_layout")
