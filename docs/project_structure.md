# Project Structure

This repository is organized by workflow area. The goal is to keep public examples easy to find and safe to share.

```text
cw_facade_toolkit/          Reusable Python helper modules
scripts/cad/               AutoCAD and BricsCAD workflow templates
scripts/dwg/               DWG extraction and quantity workflows
scripts/pdf/               PDF drawing-package tools
scripts/excel/             Excel schedule and highlighting workflows
scripts/file_management/   File replacement, sorting and moving workflows
scripts/checking/          Validation and checking workflows
scripts/rhino/             Rhino and Make2D workflow templates
scripts/solidworks/        SolidWorks sheet-metal workflow notes
scripts/trimble/           Trimble Connect workflow notes
scripts/athena/            Athena/profile workflow notes
examples/                  Public sample CSV/input data
reports/                   Local output folder, not intended for committed production files
docs/                      Project documentation
```

## Naming rules

- Use lowercase file names where possible.
- Use clear workflow names, for example `extract_pages_by_codes.py` instead of a temporary file name.
- Keep real project names out of public file names.
- Keep reusable logic in `cw_facade_toolkit/` and workflow entry points in `scripts/`.

## Public repository rule

Only generic, non-confidential scripts and examples belong here. Real DWG/PDF/STEP/Excel/project data should stay outside the repository.
