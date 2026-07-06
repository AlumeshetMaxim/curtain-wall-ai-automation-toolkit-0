"""Template: publish the active DWG using a separate hidden CAD instance.

This public version keeps the workflow structure without exposing internal paths.
"""

from pathlib import Path

OUTPUT_DIR = Path("./reports/published")
PDF_PLOTTERS = ["DWG To PDF.pc3", "Print as PDF.pc3", "Publish to PDF.pc3"]


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    print("Hidden publish workflow template")
    print("Output folder:", OUTPUT_DIR)
    print("PDF plotter candidates:", PDF_PLOTTERS)
    print("Connect this template to AutoCAD/BricsCAD COM in your local environment.")


if __name__ == "__main__":
    main()
