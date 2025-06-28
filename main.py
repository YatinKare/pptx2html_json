import os
from learnx_parser import parse_pptx

def main():
    pptx_file = "./example/Galaxy presentation.pptx"
    output_dir = "./output_presentation"

    # Parse the PPTX file
    parse_pptx(pptx_file, output_dir)

    print("Parsing complete. Check the 'output_presentation' directory.")

if __name__ == "__main__":
    main()