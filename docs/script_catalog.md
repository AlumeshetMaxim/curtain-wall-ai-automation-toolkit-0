# Script Catalog

This catalog describes the public, sanitized automation scripts in this repository.

The original internal scripts were created for real facade, curtain wall and CAD/BIM workflows. For this public repository, company paths, project folders and confidential project data are removed or replaced with generic placeholders.

## CAD / BricsCAD / AutoCAD automation

| Script | Purpose |
|---|---|
| `scripts/cad/setup_layouts_by_frame.py` | Detects drawing frames in layouts and applies print/window settings. |
| `scripts/cad/auto_publish_active_dwg_hidden.py` | Publishes the active DWG using a hidden CAD instance workflow. |
| `scripts/cad/draw_glass_with_insert_pads.py` | Public placeholder for glass panel geometry from table data. |
| `scripts/cad/publish_dwgs_to_pdf_and_merge.py` | Batch-publishing workflow template for DWG to PDF packages. |
| `scripts/cad/mtext_to_text.py` | Cleans MTEXT formatting codes and supports MTEXT-to-TEXT workflows. |
| `scripts/cad/export_selected_text_count_to_excel.py` | Exports or summarizes selected text values to Excel. |
| `scripts/cad/publish_layouts_one_click.py` | Public placeholder for one-click layout export. |
| `scripts/cad/apply_standard_page_setup.py` | Page setup checklist/template for CAD layouts. |
| `scripts/cad/move_layouts_to_model.py` | Layout-to-model workflow notes. |
| `scripts/cad/select_dynamic_blocks_by_parameters.py` | Selects dynamic blocks by normalized parameter values. |
| `scripts/cad/select_blocks_by_attribute.py` | Finds blocks by attribute text matching logic. |

## DWG extraction / quantity workflows

| Script | Purpose |
|---|---|
| `scripts/dwg/count_units_from_floor_plans.py` | Counts unit names from floor-plan data. |
| `scripts/dwg/count_mullions_by_floor.py` | Counts selected facade/mullion block types by floor. |
| `scripts/dwg/extract_blocks_summary.py` | Creates a summary of block occurrences. |

## PDF workflows

| Script | Purpose |
|---|---|
| `scripts/pdf/split_pdf_by_page_groups.py` | Splits a PDF into files with a fixed number of pages per output file. |
| `scripts/pdf/split_pdf_to_single_pages.py` | Splits a PDF into one file per page. |
| `scripts/pdf/extract_selected_pages.py` | Extracts selected pages by 1-based page numbers. |
| `scripts/pdf/extract_pages_by_codes.py` | Extracts pages containing selected drawing or element codes. |
| `scripts/pdf/merge_first_pages_from_floor_plans.py` | Merges the first page from each floor-plan PDF into one package. |
| `scripts/pdf/merge_pdf_from_quantity_table.py` | Builds a merged PDF based on a quantity/id table. |
| `scripts/pdf/merge_pdfs_by_filename_search.py` | Searches for PDFs by filename codes and merges them in order. |
| `scripts/pdf/pdf_to_jpeg.py` | Public PDF-to-image workflow notes. |
| `scripts/pdf/render_pdf_pages_to_images.py` | PDF page rendering template. |
| `scripts/pdf/images_to_pdf.py` | Converts JPEG/PNG/TIFF images into a multi-page PDF. |
| `scripts/pdf/remove_pdf_comments.py` | Removes PDF annotations/comments. |
| `scripts/pdf/mark_text_with_red_circles.py` | Marks text occurrences with visible circle annotations. |
| `scripts/pdf/replace_text_with_overlay.py` | Replaces visible text by drawing an overlay and new text. |
| `scripts/pdf/delete_pages_by_title.py` | Removes PDF pages that contain selected drawing titles. |
| `scripts/pdf/convert_pdf_to_grayscale_ghostscript.py` | Converts PDF files to grayscale with Ghostscript. |

## Excel workflows

| Script | Purpose |
|---|---|
| `scripts/excel/color_matching_codes.py` | Colors Excel cells matching selected schedule/item codes. |

## File management workflows

| Script | Purpose |
|---|---|
| `scripts/file_management/replace_files_by_name.py` | Replaces files in target folders by matching file names. |
| `scripts/file_management/move_named_files_to_folder.py` | Moves selected named files into a target subfolder. |

## Checking / validation workflows

| Script | Purpose |
|---|---|
| `scripts/checking/check_stp_files_from_csv.py` | Checks whether CSV items exist as STP/STEP files and marks missing items in Excel. |
| `scripts/check_step_annotations.py` | Checks STEP files for PMI/annotation entities and text-height consistency. |

## Rhino workflows

| Script | Purpose |
|---|---|
| `scripts/rhino/count_blocks.py` | Counts Rhino block instances. |
| `scripts/rhino/step_to_make2d_dwg.py` | STEP-to-Make2D-to-DWG workflow template for Rhino. |

## SolidWorks workflows

| Script | Purpose |
|---|---|
| `scripts/solidworks/export_sheet_metal_flat_patterns.py` | Public notes for sheet-metal flat-pattern DXF export. |

## Trimble workflows

| Script | Purpose |
|---|---|
| `scripts/trimble/export_selected_to_excel.py` | Trimble selected-objects export workflow notes. |
| `scripts/trimble/access_trimble_notes.py` | Trimble access and safety notes. |

## Athena / profile extraction

| Script | Purpose |
|---|---|
| `scripts/athena/extract_profiles_joining_elements.py` | Experimental Athena/CAD automation for extracting or placing profile/joining-element data. |

## Safety rules

- Do not commit real project DWGs, PDFs, STEP files, client documents or internal production files.
- Keep examples generic and non-confidential.
- Replace company/project paths with `./examples`, `./input` or `./reports`.
- Use simplified sample data when demonstrating workflows.
