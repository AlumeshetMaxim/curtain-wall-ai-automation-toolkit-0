"""Example: compare two simplified facade schedules."""

from pathlib import Path

from cw_facade_toolkit.revision_compare import compare_schedules

BASE_DIR = Path(__file__).resolve().parents[1]
OLD_FILE = BASE_DIR / "examples" / "sample_schedule_rev01.csv"
NEW_FILE = BASE_DIR / "examples" / "sample_schedule_rev02.csv"
OUTPUT = BASE_DIR / "reports" / "sample_revision_compare.csv"


def main() -> None:
    comparison = compare_schedules(OLD_FILE, NEW_FILE)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    comparison.to_csv(OUTPUT, index=False)
    print(f"Revision comparison exported to: {OUTPUT}")
    print(comparison)


if __name__ == "__main__":
    main()
