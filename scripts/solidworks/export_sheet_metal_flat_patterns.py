"""SolidWorks sheet-metal DXF export workflow notes.

Public placeholder. The local/private version can open SLDPRT files, update sheet-metal parameters and export flat-pattern DXF files.
"""

from pathlib import Path

INPUT_DIR = Path("./examples/sldprt")
OUTPUT_DIR = Path("./reports/dxf")
THICKNESS_MM = 2.0
BEND_RADIUS_MM = 6.0
K_FACTOR = 0.275


def main() -> None:
    print("SolidWorks sheet-metal DXF export workflow")
    print("Input:", INPUT_DIR)
    print("Output:", OUTPUT_DIR)
    print("Thickness:", THICKNESS_MM)
    print("Bend radius:", BEND_RADIUS_MM)
    print("K-factor:", K_FACTOR)
    print("Connect to SolidWorks COM locally; do not commit private model files.")


if __name__ == "__main__":
    main()
