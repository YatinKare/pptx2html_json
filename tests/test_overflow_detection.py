"""Test cases for element overflow detection in absolute positioning mode."""

import os
import re


def test_element_overflow_detection():
    """Test that all elements fit within the 1280x720 slide container."""

    # Container dimensions
    CONTAINER_WIDTH = 1280
    CONTAINER_HEIGHT = 720

    output_dir = "./output_presentation_absolute"
    overflow_issues = []

    # Check all generated slides
    for slide_num in range(1, 14):  # Galaxy presentation has 13 slides
        slide_file = os.path.join(
            output_dir, f"slide{slide_num}", f"slide{slide_num}.html"
        )

        if not os.path.exists(slide_file):
            continue

        with open(slide_file) as f:
            content = f.read()

        # Find all style attributes with positioning
        style_pattern = r'style="([^"]*(?:left:|top:|width:|height:)[^"]*)"'
        style_matches = re.findall(style_pattern, content)

        for i, style in enumerate(style_matches):
            # Extract position and size values
            left_match = re.search(r"left:\s*(\d+)px", style)
            top_match = re.search(r"top:\s*(\d+)px", style)
            width_match = re.search(r"width:\s*(\d+)px", style)
            height_match = re.search(r"height:\s*(\d+)px", style)

            if all([left_match, top_match, width_match, height_match]):
                left = int(left_match.group(1))
                top = int(top_match.group(1))
                width = int(width_match.group(1))
                height = int(height_match.group(1))

                # Calculate element bounds
                right = left + width
                bottom = top + height

                # Check for overflow
                overflow_right = max(0, right - CONTAINER_WIDTH)
                overflow_bottom = max(0, bottom - CONTAINER_HEIGHT)

                if overflow_right > 0 or overflow_bottom > 0:
                    # Determine element type from class
                    element_type = "unknown"
                    if (
                        "shape" in style
                        or "shape"
                        in content[
                            max(0, content.find(style) - 100) : content.find(style)
                            + 100
                        ]
                    ):
                        element_type = "shape"
                    elif (
                        "image" in style
                        or "img"
                        in content[
                            max(0, content.find(style) - 100) : content.find(style)
                            + 100
                        ]
                    ):
                        element_type = "image"

                    overflow_issues.append(
                        {
                            "slide": slide_num,
                            "element": element_type,
                            "left": left,
                            "top": top,
                            "width": width,
                            "height": height,
                            "right": right,
                            "bottom": bottom,
                            "overflow_right": overflow_right,
                            "overflow_bottom": overflow_bottom,
                        }
                    )

    # Report findings
    if overflow_issues:
        print(f"Found {len(overflow_issues)} overflow issues:")
        for issue in overflow_issues:
            print(f"  Slide {issue['slide']}: {issue['element']} element")
            print(f"    Position: ({issue['left']}, {issue['top']})")
            print(f"    Size: {issue['width']}x{issue['height']}")
            print(f"    Bounds: right={issue['right']}, bottom={issue['bottom']}")
            print(
                f"    Overflow: right={issue['overflow_right']}px, bottom={issue['overflow_bottom']}px"
            )
            print()
    else:
        print(
            "✅ No overflow issues detected - all elements fit within container bounds"
        )

    # Test assertion
    assert len(overflow_issues) == 0, (
        f"Found {len(overflow_issues)} elements with overflow issues"
    )


if __name__ == "__main__":
    test_element_overflow_detection()
