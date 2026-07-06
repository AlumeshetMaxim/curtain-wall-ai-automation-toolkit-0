"""Template: select dynamic CAD blocks by matching parameter values.

Public sanitized version. Connect to AutoCAD/BricsCAD COM locally.
"""

MATCH_KEYS = ["WIDTH", "HEIGHT"]
TOLERANCE = 1e-6
SELECTION_SET_NAME = "SS_SAME_DYNAMIC"


def normalize_value(value):
    try:
        return float(str(value).replace(",", "."))
    except Exception:
        return str(value).strip().upper()


def values_equal(left, right) -> bool:
    left_norm = normalize_value(left)
    right_norm = normalize_value(right)
    if isinstance(left_norm, float) and isinstance(right_norm, float):
        return abs(left_norm - right_norm) <= TOLERANCE
    return left_norm == right_norm


def main() -> None:
    print("Dynamic block selection template")
    print("Compare keys:", MATCH_KEYS)
    print("Selection set:", SELECTION_SET_NAME)


if __name__ == "__main__":
    main()
