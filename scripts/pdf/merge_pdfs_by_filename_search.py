"""Search a folder tree for PDFs by code and merge matches in requested order."""

from pathlib import Path

from PyPDF2 import PdfMerger

BASE_DIR = Path("./examples/pdf_search")
OUTPUT_PDF = Path("./reports/merged_by_search.pdf")
TARGET_CODES = ["A01", "B02", "C03"]


def find_pdfs_by_codes(base_dir: Path, codes: list[str]) -> dict[str, list[Path]]:
    result = {code: [] for code in codes}
    for path in base_dir.rglob("*.pdf"):
        name = path.stem.lower()
        for code in codes:
            if code.lower() in name:
                result[code].append(path)
    return result


def main() -> None:
    matches = find_pdfs_by_codes(BASE_DIR, TARGET_CODES)
    ordered_files = []
    used = set()
    for code in TARGET_CODES:
        files = matches[code]
        if not files:
            print(f"Not found: {code}")
            continue
        selected = sorted(files)[0]
        if selected not in used:
            ordered_files.append(selected)
            used.add(selected)

    if not ordered_files:
        print("No files to merge.")
        return

    OUTPUT_PDF.parent.mkdir(parents=True, exist_ok=True)
    merger = PdfMerger()
    try:
        for path in ordered_files:
            merger.append(str(path))
        merger.write(str(OUTPUT_PDF))
    finally:
        merger.close()
    print(f"Created: {OUTPUT_PDF}")


if __name__ == "__main__":
    main()
