#!/usr/bin/env python3
"""Validate the airlines dataset.

Checks:
- required columns exist
- identifiers and names are present
- identifiers are unique
- code_type matches identifier shape
- status values are from the controlled vocabulary
- JSON export matches CSV row count
"""
from __future__ import annotations

import csv
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "data" / "airlines.csv"
JSON_PATH = ROOT / "data" / "airlines.json"
REQUIRED_COLUMNS = [
    "airline_id", "name", "code_type", "iata_code", "icao_code", "country",
    "region", "status", "active", "website", "wikidata_id", "notes"
]
STATUSES = {"active", "inactive", "defunct", "merged", "renamed", "unknown"}

def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)

def main() -> None:
    with CSV_PATH.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames != REQUIRED_COLUMNS:
            fail(f"Unexpected CSV columns: {reader.fieldnames}")
        rows = list(reader)

    if not rows:
        fail("Dataset is empty")

    seen = set()
    for i, row in enumerate(rows, start=2):
        airline_id = row["airline_id"].strip()
        name = row["name"].strip()
        if not airline_id:
            fail(f"Missing airline_id on CSV line {i}")
        if not name:
            fail(f"Missing name on CSV line {i}")
        if airline_id in seen:
            fail(f"Duplicate airline_id {airline_id!r} on CSV line {i}")
        seen.add(airline_id)
        expected_type = "iata" if re.fullmatch(r"[A-Z0-9]{2}", airline_id) else "legacy_or_icao_like"
        if row["code_type"] != expected_type:
            fail(f"code_type mismatch for {airline_id!r}: expected {expected_type}")
        if row["status"] not in STATUSES:
            fail(f"Invalid status {row['status']!r} on CSV line {i}")

    with JSON_PATH.open(encoding="utf-8") as f:
        data = json.load(f)
    if len(data) != len(rows):
        fail(f"JSON row count {len(data)} does not match CSV row count {len(rows)}")

    print(f"OK: validated {len(rows)} airline records")

if __name__ == "__main__":
    main()
