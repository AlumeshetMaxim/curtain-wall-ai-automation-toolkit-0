"""Common helper functions for AutoCAD and BricsCAD automation examples."""

from __future__ import annotations

import re
from typing import Any


def safe_filename(value: str) -> str:
    """Return a Windows-safe file name."""
    return re.sub(r'[^A-Za-z0-9._ -]+', '_', (value or '').strip())


def bricscad_progids() -> list[str]:
    """Common BricsCAD COM ProgIDs from newest to generic."""
    return [
        'BricscadApp.AcadApplication.25',
        'BricscadApp.AcadApplication.24',
        'BricscadApp.AcadApplication.23',
        'BricscadApp.AcadApplication.22',
        'BricscadApp.AcadApplication.21',
        'BricscadApp.AcadApplication.20',
        'BricscadApp.AcadApplication',
    ]


def autocad_progids() -> list[str]:
    """Common AutoCAD COM ProgIDs."""
    return ['AutoCAD.Application']


def cad_progids() -> list[str]:
    """Common BricsCAD plus AutoCAD ProgIDs."""
    return bricscad_progids() + autocad_progids()


def attach_running_application(preferred_progids: list[str]) -> Any:
    """Attach to a running CAD application using pywin32."""
    import pythoncom
    import win32com.client

    pythoncom.CoInitialize()
    last_error: Exception | None = None
    for progid in preferred_progids:
        try:
            app = win32com.client.GetActiveObject(progid)
            _ = app.Documents
            return app
        except Exception as exc:
            last_error = exc
    raise RuntimeError(f'Could not attach to a running CAD application: {last_error}')


def get_active_document(app: Any) -> Any:
    """Return the active document or raise a clear error."""
    try:
        doc = app.ActiveDocument
        if doc is not None:
            return doc
    except Exception:
        pass
    raise RuntimeError('No active CAD document found. Open a DWG and try again.')
