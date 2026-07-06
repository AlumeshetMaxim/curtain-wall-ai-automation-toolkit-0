"""Remove PDF pages that contain selected drawing titles."""

from pathlib import Path

import fitz

INPUT_PDF = Path("./examples/input.pdf")
OUTPUT_PDF = Path("./reports/without_selected_titles.pdf")
TITLES_TO_DELETE = ["DRAWING_A", "DRAWING_B"]


def delete_pages_by_title(input_pdf: Path, output_pdf: Path, titles: list[str]) -> list[int]:
    source = fitz.open(str(input_pdf))
    target = fitz.open()
    deleted_pages: list[int] = []

    for index in range(source.page_count):
        text = source.load_page(index).get_text("text") or ""
        if any(f"TITLE: {title}" in text for title in titles):
            deleted_pages.append(index + 1)
            continue
        target.insert_pdf(source, from_page=index, to_page=index)

    output_pdf.parent.mkdir(parents=True, exist_ok=True)
    target.save(str(output_pdf))
    target.close()
    source.close()
    return deleted_pages


def main() -> None:
    deleted = delete_pages_by_title(INPUT_PDF, OUTPUT_PDF, TITLES_TO_DELETE)
    print("Deleted pages:", deleted)
    print("Output:", OUTPUT_PDF)


if __name__ == "__main__":
    main()
