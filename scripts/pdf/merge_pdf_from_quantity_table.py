"""Merge PDFs according to a quantity / drawing-id table."""

from pathlib import Path

from cw_facade_toolkit.pdf_tools import files_from_quantity_table, merge_pdfs

PDF_DIR = Path("./examples/pdf_parts")
OUTPUT_PDF = Path("./reports/merged_from_quantity_table.pdf")

# Public sample data: quantity, drawing_id without .pdf
ITEMS = [
    (1, "PART_A"),
    (2, "PART_B"),
    (1, "PART_C"),
]


def main() -> None:
    files = files_from_quantity_table(PDF_DIR, ITEMS)
    missing = [path for path in files if not path.exists()]
    if missing:
        print("Missing input PDFs:")
        for path in missing:
            print(" -", path)
        return
    output = merge_pdfs(files, OUTPUT_PDF)
    print(f"Created: {output}")


if __name__ == "__main__":
    main()
