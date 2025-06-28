import pdfplumber
import os
from pathlib import Path

# Path to the input PDF
pdf_path = "./ISO_IEC_29500-1_2016(en).pdf"

# Output directory
output_dir = Path("ecma_excerpt_blocks")
output_dir.mkdir(exist_ok=True)

# Define sections to extract (label, start_page, end_page)
sections = [
    ("13_PresentationML", 100, 130),
    ("19_PresentationML_Reference", 2515, 2719),
    ("20_DrawingML_Framework", 2719, 3180),
    ("Annex_K_Root_Elements", 4532, 4534),
    ("Annex_L3_Intro_PresentationML", 4769, 4801),
]

# Use pdfplumber to extract structured text
for label, start, end in sections:
    output_path = output_dir / f"{label}.md"
    with pdfplumber.open(pdf_path) as pdf, open(output_path, "w", encoding="utf-8") as out:
        for i in range(start - 1, end):  # 0-indexed
            page = pdf.pages[i]
            text_lines = page.extract_text().split("\\n")

            out.write(f"\\n--- Page {i + 1} ---\\n")
            for line in text_lines:
                if line.strip().startswith("<") or line.strip().endswith(">"):  # crude XML code detection
                    out.write(f"\\n```xml\\n{line.strip()}\\n```\n")
                elif line.strip().startswith("[Example:"):
                    out.write(f"\\n> {line.strip()}\\n")
                else:
                    out.write(line + "\\n")
    print(f"✔️ Extracted {label} to {output_path}")
