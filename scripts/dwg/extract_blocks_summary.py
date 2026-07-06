"""Template: create a summary of block occurrences extracted from DWG files."""

from collections import Counter
from pathlib import Path

import pandas as pd

OUTPUT_CSV = Path("./reports/block_summary.csv")


def summarize_blocks(block_names: list[str]) -> pd.DataFrame:
    counter = Counter(block_names)
    return pd.DataFrame(
        [{"block_name": name, "count": count} for name, count in sorted(counter.items())]
    )


def main() -> None:
    sample_blocks = ["UNIT-01", "UNIT-01", "MULLION_A", "BRACKET_01"]
    summary = summarize_blocks(sample_blocks)
    OUTPUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    summary.to_csv(OUTPUT_CSV, index=False)
    print(summary)
    print(f"Created: {OUTPUT_CSV}")


if __name__ == "__main__":
    main()
