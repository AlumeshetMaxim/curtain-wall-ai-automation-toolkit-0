"""Template: setup CAD layouts by detecting drawing frames.

Workflow:
1. Open a DWG in AutoCAD or BricsCAD.
2. Detect frame geometry in each layout.
3. Set plot window to the frame bounding box.
4. Apply plotter, paper size, CTB and scale-to-fit.

This file is a public sanitized template based on a real internal automation script.
"""

FRAME_LAYERS_HINT = ["FRAME", "BORDER", "TITLE", "TB_FRAME"]
PLOTTER_NAME = "DWG To PDF.pc3"
CTB_NAME = "monochrome.ctb"
MARGIN_MM = 2.0


def main() -> None:
    print("Layout setup template")
    print("Frame layers:", FRAME_LAYERS_HINT)
    print("Plotter:", PLOTTER_NAME)
    print("CTB:", CTB_NAME)
    print("Margin:", MARGIN_MM, "mm")
    print("Add CAD COM frame detection logic for your local environment.")


if __name__ == "__main__":
    main()
