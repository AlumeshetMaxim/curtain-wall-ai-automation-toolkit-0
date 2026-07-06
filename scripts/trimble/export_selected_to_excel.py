"""Trimble Connect selected-objects export workflow notes.

Public placeholder. The private/local version can connect to Trimble Connect Desktop API and export selected model objects to Excel.
"""

from pathlib import Path

OUTPUT_XLSX = Path("./reports/trimble_selected_objects.xlsx")


def main() -> None:
    print("Trimble selected objects export workflow")
    print("Output:", OUTPUT_XLSX)
    print("Connect to Trimble Connect Desktop API in your local environment.")


if __name__ == "__main__":
    main()
