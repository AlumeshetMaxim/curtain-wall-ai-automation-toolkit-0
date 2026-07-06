"""Template: export selected CAD text values to Excel.

Public sanitized version. Configure and extend it for your local AutoCAD or BricsCAD COM environment.
"""

from collections import Counter
from pathlib import Path

from openpyxl import Workbook

OUTPUT_EXCEL = Path("./reports/selected_text_count.xlsx")


def save_counter(counter: Counter[str], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "DATA"
    sheet.append(["Count", "Value"])
    for value, count in sorted(counter.items(), key=lambda item: (-item[1], item[0])):
        sheet.append([count, value])
    workbook.save(output_path)


def main() -> None:
    # Replace this sample list with TEXT/MTEXT values collected from CAD selection.
    sample_values = ["UNIT-01", "UNIT-01", "UNIT-02"]
    counter = Counter(sample_values)
    save_counter(counter, OUTPUT_EXCEL)
    print(f"Created: {OUTPUT_EXCEL}")


if __name__ == "__main__":
    main()
