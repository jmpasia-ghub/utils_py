import sys
try:
    from PyPDF2 import PdfMerger
except ImportError:
    print("Missing dependency 'PyPDF2'. Please install it with:\n  python -m pip install PyPDF2\nOr create/activate a virtual environment and install dependencies from requirements.txt.")
    sys.exit(1)
from pathlib import Path
import argparse
from datetime import datetime

# Folders
INPUT_DIR = Path("input")
OUTPUT_DIR = Path("output")

parser = argparse.ArgumentParser(description="Merge PDF files located in the `input/` folder.")
parser.add_argument("files", nargs="+", help="PDF filenames (in `input/`) to merge, separated by spaces. Only PDF files are supported.")
args = parser.parse_args()

# Require input directory
if not INPUT_DIR.exists():
    print(f"Input directory '{INPUT_DIR}' does not exist. Create it and add your PDF files before running the script.")
    sys.exit(1)

# Resolve and validate files inside input/
resolved = []
for name in args.files:
    p = INPUT_DIR / name
    if not p.exists():
        print(f"File not found in '{INPUT_DIR}': {name}")
        sys.exit(1)
    resolved.append(p)

if not resolved:
    print("No PDF files to merge.")
    sys.exit(1)

# Ensure output directory exists
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

merger = PdfMerger()
for pdf_path in resolved:
    print(f"Appending: {pdf_path.name}")
    merger.append(str(pdf_path))

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
output_path = OUTPUT_DIR / f"output_{timestamp}.pdf"
merger.write(str(output_path))
merger.close()

print(f"Merged {len(resolved)} files into '{output_path}'")
