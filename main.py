from learnx_parser import parse_pptx


def main():
    """
    Main function to parse Galaxy presentation with absolute positioning.

    Uses absolute positioning with fixed 1280x720 container for pixel-perfect rendering.
    """
    pptx_file = "./Respiratory Ch 16_students.pptx"
    output_dir = "./output_presentation"

    print("🔄 Running with absolute positioning mode...")
    print("   - Fixed slide dimensions: 1280×720px (16:9 aspect ratio)")
    print("   - Pixel-perfect element positioning")
    print("   - CSS transform-based responsive scaling")

    # Parse the PPTX file with absolute positioning
    parse_pptx(pptx_file, output_dir)

    print(f"✅ Parsing complete. Check the '{output_dir}' directory.")
    print("📄 Generated slides with absolute positioning.")
    print("🌐 Open any slide HTML file in a browser to view results.")


if __name__ == "__main__":
    main()
