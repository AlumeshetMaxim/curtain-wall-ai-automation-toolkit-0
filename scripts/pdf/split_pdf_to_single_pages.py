"""Split a PDF into one PDF per page."""

from pathlib import Path

from cw_facade_toolkit.pdf_tools import split_pdf_to_single_pages

INPUT_PDF = Path("./examples/input.pdf")
OUTPUT_DIR = Path("./reports/single_pages")


def main() -> None:
    outputs = split_pdf_to_single_pages(INPUT_PDF, OUTPUT_DIR, prefix="page")
    for output in outputs:
        print(f"Created: {output}")


if __name__ == "__main__":
    main()
