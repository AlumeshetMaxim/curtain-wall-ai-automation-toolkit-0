# Roadmap

The roadmap is focused on turning practical facade and curtain wall automation scripts into a structured open-source toolkit.

## Phase 1 — Public foundation

Status: in progress

- Create a public repository with a clear README, license and project purpose.
- Add sanitized examples of real CAD, PDF, DWG, STEP, Excel, Rhino, Trimble, SolidWorks and MTO automation scripts.
- Remove all confidential paths, project names, customer data and internal production files.
- Organize scripts into logical folders: CAD, PDF, DWG extraction, file management, Excel, checking, Rhino, Trimble, SolidWorks, Athena and STEP checking.
- Add a script catalog, extended overview and usage notes.

## Phase 2 — Script cleanup and configuration

- Replace hard-coded paths with CLI arguments or configuration files.
- Standardize input/output folders: `./input`, `./examples`, `./reports`, `./output`.
- Add consistent logging and error handling.
- Add `argparse` support to scripts that currently rely on constants.
- Add safer dry-run modes for scripts that modify DWG, PDF, Excel or production files.
- Add examples that can run without confidential project files.

## Phase 3 — Reusable Python package

- Move repeated CAD connection helpers into `cw_facade_toolkit.cad_com`.
- Move repeated PDF utilities into `cw_facade_toolkit.pdf_tools`.
- Move common Excel/MTO utilities into package modules.
- Add reusable helpers for file replacement, page extraction, PDF search and validation.
- Add unit tests for non-CAD parts such as PDF, CSV, Excel and file-management workflows.
- Add sample data for MTO, revision comparison and drawing-package workflows.

## Phase 4 — CAD / BIM automation templates

- Add BricsCAD and AutoCAD COM templates for layout publishing, page setup and data extraction.
- Add Rhino workflow examples for STEP import, Make2D and DWG export.
- Add SolidWorks workflow notes for sheet-metal flat-pattern DXF export.
- Add Trimble Connect workflow notes for model object selection and export.
- Add examples for glass naming, unit naming and drawing revision checking.
- Add practical tutorials for facade planners who are not full-time software developers.

## Phase 5 — Codex-assisted automation

- Add prompts and workflows showing how Codex can help create scripts from engineering requirements.
- Add examples of AI-assisted CAD automation: drawing checks, layer cleanup, BOM/MTO generation and revision comparison.
- Add examples for PDF package processing, page selection, drawing-code search and file replacement workflows.
- Build a bridge between engineering knowledge and software development for facade teams.
- Demonstrate how planners can automate tasks that previously required many hours or days of manual work.

## Phase 6 — Industry-ready toolkit

- Package the toolkit for easier installation.
- Add documentation for Windows CAD environments.
- Add stronger validation for DWG/PDF/Excel/STEP workflows.
- Add community contribution guidelines.
- Grow the project into a practical open-source toolkit for facade and construction automation in Israel and internationally.
