# CW Facade Automation Toolkit

Open-source automation toolkit for CAD, BIM, facade engineering and curtain wall workflows.

This project focuses on automating repetitive tasks in facade and cladding planning, including CAD drawing processing, glass and profile naming, MTO/BOM generation, revision comparison, PDF publishing, viewport creation and fabrication package checking.

The toolkit is based on Python, CAD APIs, Excel workflows, Visual Studio / VS Code and AI-assisted development with Codex.

See also: [Extended overview](README_EXTENDED.md), [Script catalog](docs/script_catalog.md), [Roadmap](docs/roadmap.md), and [Privacy/Sanitization](docs/privacy_and_sanitization.md).

## Why this project exists

Facade and curtain wall engineering teams often work under tight deadlines while handling large amounts of drawing data, fabrication information, Excel schedules, profile lists, glass names and revision changes.

Many of these tasks are still done manually. Manual work can take many hours or days, and it can introduce mistakes during production, ordering or installation preparation.

Codex and AI-assisted development make it possible to turn practical engineering knowledge into working scripts and tools much faster. This project is intended to demonstrate how planners and engineers can use automation to improve real construction workflows.

## Project goals

- Automate repetitive CAD and BIM-related tasks for facade planning.
- Help generate and validate MTO/BOM data from drawings and schedules.
- Support glass, profile and unit naming workflows.
- Assist with revision comparison and production package checks.
- Provide examples for AutoCAD, BricsCAD, Rhino/Grasshopper and Excel-based workflows.
- Make practical automation accessible to facade planners and engineers who are not full-time software developers.

## Example automation areas

- CAD drawing processing and layer cleanup.
- Automatic glass naming and dimension extraction.
- Viewport creation and PDF publishing.
- Quantity take-off and MTO/BOM generation.
- Revision comparison between drawing packages.
- Fabrication package validation.
- Excel schedule processing.
- AI-assisted script generation for construction workflows.

## Current modules

- `cw_facade_toolkit.excel_mto` - example utilities for reading simplified facade schedules and creating MTO summaries.
- `cw_facade_toolkit.revision_compare` - example utilities for comparing two CSV-based drawing or fabrication schedules.
- `cw_facade_toolkit.pdf_tools` - reusable PDF helpers for public drawing package workflows.
- `cw_facade_toolkit.cad_com` - small helper utilities for CAD examples.

These modules use simplified, non-confidential sample data. They are intended as a public starting point for real CAD/BIM automation workflows.

## Technology stack

- Python
- Visual Studio / VS Code
- AutoCAD / BricsCAD APIs
- Rhino / Grasshopper workflows
- Excel / CSV data processing
- OpenAI / Codex-assisted development

## Status

This repository is in the early stage. The first goal is to collect and publish general, non-confidential examples of automation workflows for facade and curtain wall engineering.

No private company drawings, confidential project files, client documents or production data should be committed to this repository.

## Quick start

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the sample MTO script:

```bash
python scripts/example_mto_from_csv.py
```

Run the sample revision comparison script:

```bash
python scripts/example_revision_compare.py
```

Run STEP annotation check:

```bash
python scripts/check_step_annotations.py --folder ./examples/step --output ./reports/step_dimension_check.csv
```

## Open-source purpose

The long-term goal is to build a practical open-source toolkit that can help facade planners, engineers, CAD users and construction companies automate complex work not only in Israel, but also internationally.

## Roadmap

See the detailed roadmap: [docs/roadmap.md](docs/roadmap.md).

## License

This project is licensed under the MIT License.
