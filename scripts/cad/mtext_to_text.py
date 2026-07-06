"""Workflow template: convert MTEXT to plain TEXT in CAD drawings.

The original internal workflow cleaned MTEXT formatting codes and created
plain TEXT entities. This public file keeps the text-cleaning logic generic.
"""

import re


def clean_mtext(value: str) -> str:
    if not value:
        return ""
    value = value.replace("\\P", "\n").replace("\\p", "\n").replace("\\~", " ")
    value = re.sub(r"\\S([^;]*);", lambda m: m.group(1).replace("#", "/").replace("^", "/"), value)
    value = re.sub(r"\\[A-Za-z][^;]*;", "", value)
    value = value.replace("{", "").replace("}", "")
    return value.strip()


def main() -> None:
    sample = r"{\\fArial|b0|i0;GL-01}\\P1200x2400"
    print(clean_mtext(sample))
    print("Connect this cleaner to your CAD selection/conversion routine locally.")


if __name__ == "__main__":
    main()
