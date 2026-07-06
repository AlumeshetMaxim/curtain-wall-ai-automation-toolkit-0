"""Utilities for simplified facade MTO/BOM schedule processing.

The functions in this module work with public, simplified CSV/Excel-style data.
They do not require confidential project files and are intended as examples for
facade and curtain wall automation workflows.
"""

from __future__ import annotations

from pathlib import Path
from typing import Iterable

import pandas as pd

REQUIRED_COLUMNS = {"unit", "item_type", "part_name", "quantity"}


def read_schedule(path: str | Path) -> pd.DataFrame:
    """Read a simplified facade schedule from CSV or Excel.

    Required columns:
    - unit
    - item_type
    - part_name
    - quantity
    """
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Schedule file not found: {path}")

    if path.suffix.lower() in {".xlsx", ".xlsm", ".xls"}:
        df = pd.read_excel(path)
    elif path.suffix.lower() == ".csv":
        df = pd.read_csv(path)
    else:
        raise ValueError("Unsupported file type. Use CSV or Excel.")

    missing = REQUIRED_COLUMNS - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {', '.join(sorted(missing))}")

    df = df.copy()
    df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce").fillna(0)
    return df


def summarize_mto(df: pd.DataFrame, group_by: Iterable[str] | None = None) -> pd.DataFrame:
    """Create a summarized MTO table from a simplified schedule."""
    if group_by is None:
        group_by = ["item_type", "part_name"]

    group_by = list(group_by)
    missing = set(group_by) - set(df.columns)
    if missing:
        raise ValueError(f"Cannot group by missing columns: {', '.join(sorted(missing))}")

    summary = (
        df.groupby(group_by, dropna=False, as_index=False)["quantity"]
        .sum()
        .sort_values(group_by)
        .reset_index(drop=True)
    )
    return summary


def export_summary(summary: pd.DataFrame, output_path: str | Path) -> Path:
    """Export an MTO summary to CSV or Excel based on the output suffix."""
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    if output_path.suffix.lower() == ".csv":
        summary.to_csv(output_path, index=False)
    elif output_path.suffix.lower() in {".xlsx", ".xlsm"}:
        summary.to_excel(output_path, index=False)
    else:
        raise ValueError("Unsupported output type. Use CSV or XLSX.")

    return output_path
