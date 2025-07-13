import sys

from learnx_parser import parse_pptx


def main():
    """
    Main function to parse Galaxy presentation with positioning mode selection.

    Usage:
        python main.py              # Responsive positioning (default)
        python main.py --absolute   # Absolute positioning (pixel-perfect)

    Positioning Modes:
        - responsive: Flexbox-based layout that adapts to screen size
        - absolute: Fixed 1280x720 container with pixel-perfect positioning
    """
    pptx_file = "./Respiratory Ch 16_students.pptx"

    # Check if absolute positioning mode is requested
    if len(sys.argv) > 1 and sys.argv[1] == "--absolute":
        output_dir = "./output_presentation_absolute"
        positioning_mode = "absolute"
        print("🔄 Running with absolute positioning mode...")
        print("   - Fixed slide dimensions: 1280×720px (16:9 aspect ratio)")
        print("   - Pixel-perfect element positioning")
        print("   - CSS transform-based responsive scaling")
    else:
        output_dir = "./output_presentation_test"
        positioning_mode = "responsive"
        print("🔄 Running with responsive positioning mode...")
        print("   - Flexbox-based adaptive layout")
        print("   - Screen-size responsive design")

    # Parse the PPTX file
    parse_pptx(pptx_file, output_dir, positioning_mode)

    print(f"✅ Parsing complete. Check the '{output_dir}' directory.")
    print(f"📄 Generated slides with {positioning_mode} positioning.")
    print("🌐 Open any slide HTML file in a browser to view results.")


if __name__ == "__main__":
    main()
