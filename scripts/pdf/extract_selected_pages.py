"""Extract selected pages from a PDF by 1-based page numbers."""

from pathlib import Path

from pypdf import PdfReader, PdfWriter

INPUT_PDF = Path("./examples/input.pdf")
OUTPUT_PDF = Path("./reports/selected_pages.pdf")
PAGES_1_BASED = [1, 2, 3]


def extract_pages(input_pdf: Path, output_pdf: Path, pages_1_based: list[int]) -> Path:
    reader = PdfReader(str(input_pdf))
    writer = PdfWriter()
    total = len(reader.pages)

    for page_number in pages_1_based:
        if 1 <= page_number <= total:
            writer.add_page(reader.pages[page_number - 1])
        else:
            print(f"Page out of range: {page_number}")

    output_pdf.parent.mkdir(parents=True, exist_ok=True)
    with output_pdf.open("wb") as file:
        writer.write(file)
    return output_pdf


def main() -> None:
    output = extract_pages(INPUT_PDF, OUTPUT_PDF, PAGES_1_BASED)
    print(f"Created: {output}")


if __name__ == "__main__":
    main()
