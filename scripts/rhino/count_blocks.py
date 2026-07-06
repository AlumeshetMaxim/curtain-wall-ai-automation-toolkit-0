"""Rhino script: count block instances in the current document.

Run inside Rhino Python environment.
"""

try:
    import rhinoscriptsyntax as rs
except ImportError:  # Allows importing outside Rhino for docs/tests.
    rs = None


def count_blocks() -> None:
    if rs is None:
        print("Run this script inside Rhino.")
        return

    object_ids = rs.AllObjects(select=False)
    if not object_ids:
        print("No objects in document.")
        return

    counts = {}
    for object_id in object_ids:
        if rs.IsBlockInstance(object_id):
            name = rs.BlockInstanceName(object_id)
            if name:
                counts[name] = counts.get(name, 0) + 1

    total = sum(counts.values())
    for name in sorted(counts):
        print(f"{name}\t{counts[name]}")
    print(f"TOTAL\t{total}")


def main() -> None:
    count_blocks()


if __name__ == "__main__":
    main()
