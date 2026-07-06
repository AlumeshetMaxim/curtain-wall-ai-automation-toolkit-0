"""Check STEP files for PMI dimensions and annotation text-height consistency.

This public version is based on a real facade/CW workflow, but it does not
contain project-specific paths or confidential project data.

Usage:
    python scripts/check_step_annotations.py --folder ./step_files --output ./reports/step_dimension_check.csv
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from collections import Counter
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

STRICT_DIMENSION_KEYWORDS = [
    "DIMENSIONAL_SIZE",
    "DIMENSIONAL_LOCATION",
    "DIMENSIONAL_CHARACTERISTIC_REPRESENTATION",
    "SHAPE_DIMENSION_REPRESENTATION",
    "ANGULAR_SIZE",
    "CURVE_DISTANCE_GEOMETRIC_CONSTRAINT",
    "LENGTH_MEASURE",
    "DATUM",
    "DATUM_FEATURE",
    "DATUM_REFERENCE",
    "DATUM_SYSTEM",
]

ANNOTATION_DIMENSION_KEYWORDS = [
    "ANNOTATION_OCCURRENCE",
    "ANNOTATION_CURVE_OCCURRENCE",
    "ANNOTATION_TEXT_OCCURRENCE",
    "TESSELLATED_ANNOTATION_OCCURRENCE",
    "DRAUGHTING_CALLOUT",
    "DRAUGHTING_MODEL",
    "DIMENSION_CURVE",
    "DIMENSION_CURVE_TERMINATOR",
    "TERMINATOR_SYMBOL",
    "PROJECTION_CURVE",
    "LEADER_CURVE",
    "TEXT_LITERAL",
    "TEXT_LITERAL_WITH_EXTENT",
    "COMPOSITE_TEXT",
    "COMPOSITE_TEXT_WITH_EXTENT",
    "TEXT_STYLE",
    "TEXT_STYLE_FOR_DEFINED_FONT",
    "TEXT_STYLE_WITH_BOX_CHARACTERISTICS",
    "CHARACTERIZED_OBJECT",
    "PLANAR_BOX",
]

READABLE_TEXT_HEIGHT_MIN = 1.5
READABLE_TEXT_HEIGHT_MAX = 10.0
TEXT_HEIGHT_ABSOLUTE_TOLERANCE = 0.25
TEXT_HEIGHT_RELATIVE_TOLERANCE = 0.10
STEP_ID_RE = re.compile(r"^\s*#(\d+)\s*=")
STEP_NUMBER_RE = r"[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[Ee][-+]?\d+)?"
STEP_POINT_RE = re.compile(
    r"\(\s*(" + STEP_NUMBER_RE + r")\s*,\s*("
    + STEP_NUMBER_RE + r")\s*,\s*("
    + STEP_NUMBER_RE + r")\s*\)"
)
TESSELLATED_CURVE_COORD_RE = re.compile(
    r"TESSELLATED_CURVE_SET\([^,]*,\s*#(\d+)\s*,",
    re.IGNORECASE,
)


def load_step_records(step_path: Path) -> tuple[list[str], str]:
    """Load a STEP file and combine multiline records until ';'."""
    records: list[str] = []
    schema_line = ""

    with step_path.open("r", encoding="utf-8", errors="ignore") as file:
        buffer = ""

        for line in file:
            line_stripped = line.strip()
            if not line_stripped:
                continue

            upper_line = line_stripped.upper()
            if "FILE_SCHEMA" in upper_line:
                schema_line = upper_line.strip()

            buffer += " " + line_stripped
            if ";" in line_stripped:
                records.append(buffer.strip())
                buffer = ""

    return records, schema_line


def build_step_record_map(records: list[str]) -> dict[int, str]:
    result: dict[int, str] = {}
    for record in records:
        match = STEP_ID_RE.match(record)
        if match:
            result[int(match.group(1))] = record
    return result


def parse_coordinate_points(record: str) -> list[tuple[float, float, float]]:
    return [(float(x), float(y), float(z)) for x, y, z in STEP_POINT_RE.findall(record)]


def is_probable_text_size(value: float) -> bool:
    return 0.5 <= value <= 50.0


def extract_tessellated_text_heights(records: list[str]) -> list[float]:
    """Extract probable text heights from AP242 tessellated annotation curves."""
    record_map = build_step_record_map(records)
    text_heights: list[float] = []

    for record in record_map.values():
        if "TESSELLATED_CURVE_SET" not in record.upper():
            continue

        coord_match = TESSELLATED_CURVE_COORD_RE.search(record)
        if not coord_match:
            continue

        coord_record = record_map.get(int(coord_match.group(1)), "")
        points = parse_coordinate_points(coord_record)
        if len(points) <= 18:
            continue

        glyph_points = points[18:]
        min_y = min(y for _, y, _ in glyph_points)
        max_y = max(y for _, y, _ in glyph_points)
        height = round(max_y - min_y, 4)

        if is_probable_text_size(height):
            text_heights.append(height)

    return text_heights


def extract_numbers_from_record(record: str) -> list[float]:
    """Extract numeric values, ignoring STEP ids and text literals."""
    record = re.sub(r"#\d+", " ", record)
    record = re.sub(r"'(?:[^']|'')*'", " ", record)

    numbers = re.findall(r"[-+]?\d*\.\d+|[-+]?\d+", record)
    result: list[float] = []
    for number in numbers:
        try:
            result.append(float(number))
        except ValueError:
            pass
    return result


def format_size(value: float | str | None) -> str:
    if value in ("", None):
        return ""
    try:
        return f"{float(value):g}"
    except ValueError:
        return str(value)


def safe_float(value: str | float | int | None) -> float | None:
    if value in ("", None):
        return None
    try:
        return float(value)
    except ValueError:
        return None


def parse_size_string(size_string: str) -> list[float]:
    if not size_string:
        return []
    values: list[float] = []
    for part in str(size_string).split(";"):
        value = safe_float(part.strip())
        if value is not None:
            values.append(value)
    return sorted(values)


def analyze_annotation_sizes(records: list[str]) -> dict[str, str | int | list[float]]:
    annotation_found_keywords: set[str] = set()
    text_size_candidates: list[float] = []
    tessellated_text_heights = extract_tessellated_text_heights(records)

    if tessellated_text_heights:
        annotation_found_keywords.add("TESSELLATED_CURVE_SET_TEXT_HEIGHT")
        text_size_candidates.extend(tessellated_text_heights)

    for index, record in enumerate(records):
        upper_record = record.upper()
        matched_annotation = False

        for keyword in ANNOTATION_DIMENSION_KEYWORDS:
            if keyword in upper_record:
                annotation_found_keywords.add(keyword)
                matched_annotation = True

        if not matched_annotation:
            continue

        numbers = extract_numbers_from_record(record)
        nearby_records = records[max(0, index - 5): min(len(records), index + 6)]

        for nearby_record in nearby_records:
            nearby_upper = nearby_record.upper()
            if any(
                token in nearby_upper
                for token in [
                    "TEXT",
                    "FONT",
                    "STYLE",
                    "PLANAR_BOX",
                    "CHARACTERIZED_OBJECT",
                    "ANNOTATION_TEXT",
                    "TEXT_LITERAL",
                    "COMPOSITE_TEXT",
                ]
            ):
                numbers.extend(extract_numbers_from_record(nearby_record))

        for value in numbers:
            if is_probable_text_size(value):
                text_size_candidates.append(round(value, 4))

    unique_sizes = sorted(set(text_size_candidates))
    size_counter = Counter(text_size_candidates)
    dominant_size = size_counter.most_common(1)[0][0] if size_counter else ""

    return {
        "has_annotation_dimensions": "YES" if annotation_found_keywords else "NO",
        "annotation_found_keywords": "; ".join(sorted(annotation_found_keywords)),
        "annotation_text_sizes_list": unique_sizes,
        "annotation_text_sizes": "; ".join(str(x) for x in unique_sizes),
        "annotation_text_size_count": len(unique_sizes),
        "annotation_text_height_min": format_size(unique_sizes[0]) if unique_sizes else "",
        "annotation_text_height_max": format_size(unique_sizes[-1]) if unique_sizes else "",
        "annotation_dominant_text_size": format_size(dominant_size),
    }


def analyze_real_dimensions(records: list[str]) -> dict[str, str]:
    found: set[str] = set()
    for record in records:
        upper_record = record.upper()
        for keyword in STRICT_DIMENSION_KEYWORDS:
            if keyword in upper_record:
                found.add(keyword)

    return {
        "has_real_dimensions": "YES" if found else "NO",
        "found_keywords": "; ".join(sorted(found)),
    }


def analyze_step_file(step_path: Path) -> dict[str, str | int]:
    try:
        records, schema_line = load_step_records(step_path)
        real_result = analyze_real_dimensions(records)
        annotation_result = analyze_annotation_sizes(records)

        return {
            "file": str(step_path),
            "file_name": step_path.name,
            "schema": schema_line,
            "has_real_dimensions": real_result["has_real_dimensions"],
            "found_keywords": real_result["found_keywords"],
            "has_annotation_dimensions": annotation_result["has_annotation_dimensions"],
            "annotation_found_keywords": annotation_result["annotation_found_keywords"],
            "annotation_text_sizes": annotation_result["annotation_text_sizes"],
            "annotation_text_size_count": annotation_result["annotation_text_size_count"],
            "annotation_text_height_min": annotation_result["annotation_text_height_min"],
            "annotation_text_height_max": annotation_result["annotation_text_height_max"],
            "annotation_dominant_text_size": annotation_result["annotation_dominant_text_size"],
            "annotation_text_height_status": "",
            "annotation_text_height_reason": "",
            "reference_annotation_text_height_min": "",
            "reference_annotation_text_height_max": "",
        }
    except Exception as exc:  # noqa: BLE001 - CLI report should continue on bad files.
        return {
            "file": str(step_path),
            "file_name": step_path.name,
            "schema": "",
            "has_real_dimensions": "ERROR",
            "found_keywords": f"READ_ERROR: {exc}",
            "has_annotation_dimensions": "ERROR",
            "annotation_found_keywords": f"READ_ERROR: {exc}",
            "annotation_text_sizes": "",
            "annotation_text_size_count": 0,
            "annotation_text_height_min": "",
            "annotation_text_height_max": "",
            "annotation_dominant_text_size": "",
            "annotation_text_height_status": "NOT OK",
            "annotation_text_height_reason": f"READ_ERROR: {exc}",
            "reference_annotation_text_height_min": "",
            "reference_annotation_text_height_max": "",
        }


def add_annotation_text_height_check(results: list[dict[str, str | int]]) -> list[dict[str, str | int]]:
    all_text_heights: list[float] = []
    for result in results:
        all_text_heights.extend(parse_size_string(str(result.get("annotation_text_sizes", ""))))

    if not all_text_heights:
        for result in results:
            result["annotation_text_height_status"] = "NOT OK"
            result["annotation_text_height_reason"] = "NO_ANNOTATION_SIZE_FOUND"
        return results

    reference_min = min(all_text_heights)
    reference_max = max(all_text_heights)

    for result in results:
        heights = parse_size_string(str(result.get("annotation_text_sizes", "")))
        reasons: list[str] = []
        result["reference_annotation_text_height_min"] = format_size(reference_min)
        result["reference_annotation_text_height_max"] = format_size(reference_max)

        if not heights:
            reasons.append("NO_TEXT_HEIGHT")
        else:
            file_min = min(heights)
            file_max = max(heights)
            result["annotation_text_height_min"] = format_size(file_min)
            result["annotation_text_height_max"] = format_size(file_max)

            if file_min < reference_min - TEXT_HEIGHT_ABSOLUTE_TOLERANCE:
                reasons.append(f"MIN_BELOW_REFERENCE({format_size(file_min)})")
            if file_max > reference_max + TEXT_HEIGHT_ABSOLUTE_TOLERANCE:
                reasons.append(f"MAX_ABOVE_REFERENCE({format_size(file_max)})")

        if reasons:
            result["annotation_text_height_status"] = "NOT OK"
            result["annotation_text_height_reason"] = "; ".join(reasons)
        else:
            result["annotation_text_height_status"] = "OK"
            result["annotation_text_height_reason"] = (
                f"OK_REFERENCE_RANGE({format_size(reference_min)} - {format_size(reference_max)})"
            )

    return results


def find_step_files(folder: Path) -> list[Path]:
    return sorted(list(folder.rglob("*.stp")) + list(folder.rglob("*.step")))


def write_csv_report(results: list[dict[str, str | int]], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "file",
        "file_name",
        "schema",
        "has_real_dimensions",
        "found_keywords",
        "has_annotation_dimensions",
        "annotation_found_keywords",
        "annotation_text_sizes",
        "annotation_text_size_count",
        "annotation_text_height_min",
        "annotation_text_height_max",
        "annotation_dominant_text_size",
        "annotation_text_height_status",
        "annotation_text_height_reason",
        "reference_annotation_text_height_min",
        "reference_annotation_text_height_max",
    ]

    with output_path.open("w", newline="", encoding="utf-8-sig") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(results)


def main() -> int:
    parser = argparse.ArgumentParser(description="Check STEP files for PMI and annotation text-height consistency.")
    parser.add_argument("--folder", required=True, help="Folder containing STEP files.")
    parser.add_argument("--output", required=True, help="Output CSV report path.")
    args = parser.parse_args()

    folder = Path(args.folder)
    output_path = Path(args.output)

    if not folder.exists():
        print(f"Folder not found: {folder}")
        return 1

    step_files = find_step_files(folder)
    if not step_files:
        print("No STEP files found.")
        return 1

    print("Checking STEP files...\n")
    results: list[dict[str, str | int]] = []

    for step_file in step_files:
        result = analyze_step_file(step_file)
        results.append(result)
        print(
            f"[PMI: {result['has_real_dimensions']}] "
            f"[ANNOT: {result['has_annotation_dimensions']}] "
            f"[TEXT_MIN: {result['annotation_text_height_min'] or '-'}] "
            f"[TEXT_MAX: {result['annotation_text_height_max'] or '-'}] "
            f"{step_file.name}"
        )

    results = add_annotation_text_height_check(results)
    write_csv_report(results, output_path)

    print("\nDone.")
    print("Report:", output_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
