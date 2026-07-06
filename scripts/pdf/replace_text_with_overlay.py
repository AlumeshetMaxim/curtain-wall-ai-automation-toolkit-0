"""Replace visible PDF text by drawing a white overlay and new text.

Generic public version. This is useful when a drawing package contains repeated placeholder text.
"""

from pathlib import Path

import pdfplumber
from reportlab.pdfgen import canvas
from PyPDF2 import PdfReader, PdfWriter

INPUT_PDF = Path("./examples/input.pdf")
OUTPUT_PDF = Path("./reports/replaced_text.pdf")
OLD_TEXT = "TBD"
NEW_TEXT = "7016"


def collect_word_boxes(input_pdf: Path, word: str) -> list[list[tuple[float, float, float, float]]]:
    boxes_by_page = []
    with pdfplumber.open(str(input_pdf)) as pdf:
        for page in pdf.pages:
            height = page.height
            boxes = []
            for item in page.extract_words():
                if item.get("text", "").strip().upper() == word.upper():
                    x0, x1 = item["x0"], item["x1"]
                    y0 = height - item["bottom"]
                    y1 = height - item["top"]
                    boxes.append((x0, y0, x1, y1))
            boxes_by_page.append(boxes)
    return boxes_by_page


def make_overlay(input_pdf: Path, boxes_by_page: list[list[tuple[float, float, float, float]]], overlay_pdf: Path) -> None:
    reader = PdfReader(str(input_pdf))
    c = canvas.Canvas(str(overlay_pdf))
    for page_index, page in enumerate(reader.pages):
        width = float(page.mediabox.width)
        height = float(page.mediabox.height)
        c.setPageSize((width, height))
        for x0, y0, x1, y1 in boxes_by_page[page_index]:
            c.setFillColorRGB(1, 1, 1)
            c.rect(x0 - 1, y0 - 1, (x1 - x0) + 2, (y1 - y0) + 2, stroke=0, fill=1)
            c.setFillColorRGB(0, 0, 0)
            c.setFont("Helvetica", max((y1 - y0) * 0.8, 6))
            c.drawCentredString((x0 + x1) / 2, y0, NEW_TEXT)
        c.showPage()
    c.save()


def merge_overlay(input_pdf: Path, overlay_pdf: Path, output_pdf: Path) -> None:
    base = PdfReader(str(input_pdf))
    overlay = PdfReader(str(overlay_pdf))
    writer = PdfWriter()
    for index in range(len(base.pages)):
        page = base.pages[index]
        page.merge_page(overlay.pages[index])
        writer.add_page(page)
    output_pdf.parent.mkdir(parents=True, exist_ok=True)
    with output_pdf.open("wb") as file:
        writer.write(file)


def main() -> None:
    temp_overlay = OUTPUT_PDF.with_suffix(".overlay.pdf")
    boxes = collect_word_boxes(INPUT_PDF, OLD_TEXT)
    make_overlay(INPUT_PDF, boxes, temp_overlay)
    merge_overlay(INPUT_PDF, temp_overlay, OUTPUT_PDF)
    temp_overlay.unlink(missing_ok=True)
    print(f"Created: {OUTPUT_PDF}")


if __name__ == "__main__":
    main()
