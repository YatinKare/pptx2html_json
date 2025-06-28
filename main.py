import os
import zipfile
import shutil
from learnx_parser.pptx_parser import PptxParser

def unpack_pptx(pptx_path, extract_dir):
    """Unpacks a .pptx file into a directory."""
    if os.path.exists(extract_dir):
        # Clear the directory if it already exists
        for item in os.listdir(extract_dir):
            item_path = os.path.join(extract_dir, item)
            if os.path.isfile(item_path):
                os.remove(item_path)
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)
    else:
        os.makedirs(extract_dir, exist_ok=True)

    with zipfile.ZipFile(pptx_path, 'r') as zip_ref:
        zip_ref.extractall(extract_dir)
    print(f"Unpacked {pptx_path} to {extract_dir}")

def main():
    pptx_file = "./example/Galaxy presentation.pptx"
    unpacked_dir = "./temp_pptx"
    output_dir = "./output_presentation"

    # Unpack the PPTX file
    unpack_pptx(pptx_file, unpacked_dir)

    # Initialize and run the parser
    parser = PptxParser(unpacked_dir, output_dir)
    parser.parse_presentation()

    print("Parsing complete. Check the 'output_presentation' directory.")

if __name__ == "__main__":
    main()