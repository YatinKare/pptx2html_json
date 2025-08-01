import os
import shutil
import tempfile
import zipfile

from learnx_parser.services.document_parser import DocumentParser


def parse_pptx(pptx_file_path, output_dir="./output"):
    """
    Parses a .pptx file and converts its content to HTML and JSON using absolute positioning.

    Args:
        pptx_file_path (str): The absolute path to the .pptx file.
        output_dir (str): The directory where the HTML and JSON output will be saved.
    """
    if not os.path.exists(pptx_file_path):
        raise FileNotFoundError(f"PPTX file not found: {pptx_file_path}")

    # Create a temporary directory for unpacking the PPTX using system temp directory
    # This avoids cluttering the output directory and ensures consistent behavior
    temp_unpacked_dir = tempfile.mkdtemp(prefix="pptx_unpacked_")
    os.makedirs(temp_unpacked_dir, exist_ok=True)

    try:
        # Unzip the PPTX file
        with zipfile.ZipFile(pptx_file_path, "r") as zip_ref:
            zip_ref.extractall(temp_unpacked_dir)

        # Initialize and run the DocumentParser with absolute positioning
        parser = DocumentParser(temp_unpacked_dir, output_dir)
        parser.parse_presentation()

    finally:
        # Clean up the temporary unpacked directory
        if os.path.exists(temp_unpacked_dir):
            shutil.rmtree(temp_unpacked_dir)
