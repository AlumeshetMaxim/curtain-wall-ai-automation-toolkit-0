"""Mark text occurrences in a PDF with visible circle annotations.

Generic public version. Useful for review workflows such as marking TBD items.
"""

from pathlib import Path

import fitz

INPUT_PDF = Path("./examples/input.pdf")
OUTPUT_PDF = Path("./reports/marked_text.pdf")
SEARCH_TEXT = "TBD"
RADIUS_MM = 5.0


def mm_to_points(value_mm: float) -> float:
    return value_mm / 25.4 * 72.0


def mark_text_with_circles(input_pdf: Path, output_pdf: Path, search_text: str, radius_mm: float) -> int:
    output_pdf.parent.mkdir(parents=True, exist_ok=True)
    radius = mm_to_points(radius_mm)
    document = fitz.open(str(input_pdf))
    count = 0

    for page in document:
        for rect in page.search_for(search_text):
            cx = (rect.x0 + rect.x1) / 2
            cy = (rect.y0 + rect.y1) / 2
            circle_rect = fitz.Rect(cx - radius, cy - radius, cx + radius, cy + radius)
            annot = page.add_circle_annot(circle_rect)
            annot.set_colors(stroke=(1, 0, 0))
            annot.set_border(width=1.0)
            annot.update()
            count += 1

    document.save(str(output_pdf), incremental=False, deflate=True)
    document.close()
    return count


def main() -> None:
    count = mark_text_with_circles(INPUT_PDF, OUTPUT_PDF, SEARCH_TEXT, RADIUS_MM)
    print(f"Marked {count} occurrences. Output: {OUTPUT_PDF}")


if __name__ == "__main__":
    main()
