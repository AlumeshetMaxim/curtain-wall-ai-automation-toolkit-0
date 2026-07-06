"""Convert PDF files to grayscale using Ghostscript."""

from __future__ import annotations

import argparse
import glob
import os
import shutil
import subprocess
from pathlib import Path


def find_ghostscript() -> str:
    for name in ["gs", "gswin64c", "gswin32c"]:
        path = shutil.which(name)
        if path:
            return path

    candidates = []
    candidates += glob.glob(r"C:\Program Files\gs\gs*\bin\gswin64c.exe")
    candidates += glob.glob(r"C:\Program Files (x86)\gs\gs*\bin\gswin32c.exe")
    for path in sorted(candidates, reverse=True):
        if os.path.exists(path):
            return path

    raise FileNotFoundError("Ghostscript was not found. Install it or pass --gs.")


def convert_to_grayscale(gs_exe: str, input_pdf: Path, output_pdf: Path) -> None:
    command = [
        gs_exe,
        "-dSAFER",
        "-dBATCH",
        "-dNOPAUSE",
        "-sDEVICE=pdfwrite",
        "-sColorConversionStrategy=Gray",
        "-dProcessColorModel=/DeviceGray",
        "-dOverrideICC=true",
        "-o",
        str(output_pdf),
        str(input_pdf),
    ]
    subprocess.run(command, check=True)


def main() -> None:
    parser = argparse.ArgumentParser(description="Convert a PDF file or folder of PDFs to grayscale.")
    parser.add_argument("input", help="Input PDF file or folder")
    parser.add_argument("--suffix", default="_grayscale")
    parser.add_argument("--overwrite", action="store_true")
    parser.add_argument("--gs", default=None, help="Path to Ghostscript executable")
    args = parser.parse_args()

    gs_exe = args.gs or find_ghostscript()
    input_path = Path(args.input)
    files = [input_path] if input_path.is_file() else sorted(input_path.glob("*.pdf"))

    for pdf_file in files:
        output_pdf = pdf_file.with_name(pdf_file.stem + args.suffix + pdf_file.suffix)
        if output_pdf.exists() and not args.overwrite:
            print(f"Skip existing: {output_pdf}")
            continue
        convert_to_grayscale(gs_exe, pdf_file, output_pdf)
        print(f"Created: {output_pdf}")


if __name__ == "__main__":
    main()
