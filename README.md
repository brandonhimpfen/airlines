# Airlines Dataset

[![Support Open Work](https://img.shields.io/badge/Support-Open%20Work-0A0A0A?style=flat&logo=github)](https://github.com/brandonhimpfen/support) 
[![DOI](https://zenodo.org/badge/361875893.svg)](https://doi.org/10.5281/zenodo.20127510)

A lightweight, reusable dataset of airline identifiers and airline names.

This repository provides airline data in CSV, JSON, minified JSON, TSV, and plain text formats.

## What is included

- `data/airlines.csv` — canonical dataset
- `data/airlines.json` — JSON export
- `data/airlines.min.json` — compact JSON export
- `data/airlines.tsv` — tab-separated export
- `data/airlines.txt` — airline names only
- `schema/airlines.schema.json` — JSON Schema for the dataset
- `scripts/validate.py` — validation script
- `docs/data-dictionary.md` — field definitions

## Dataset status

This release contains **555 airline records**.

## Fields

| Field | Description |
|---|---|
| `airline_id` | Original airline identifier from the source dataset. |
| `name` | Airline name. |
| `code_type` | `iata` for two-character codes, `legacy_or_icao_like` for longer legacy identifiers. |
| `iata_code` | Two-character IATA-style code when applicable. |
| `icao_code` | Three-character or legacy code when applicable. |
| `country` | Airline country, blank until verified. |
| `region` | Geographic region, blank until verified. |
| `status` | Current known status. Defaults to `unknown`. |
| `active` | Boolean active flag once verified. Blank while unknown. |
| `website` | Official website once verified. |
| `wikidata_id` | Wikidata identifier once verified. |
| `notes` | Notes about import status, ambiguity, or enrichment. |

## Usage

```python
import csv

with open("data/airlines.csv", newline="", encoding="utf-8") as f:
    airlines = list(csv.DictReader(f))

print(airlines[0])
```

## Validate the dataset

```bash
python scripts/validate.py
```

Expected output:

```text
OK: validated 555 airline records
```

## License

This dataset is released under the license included in this repository.

## Citation

Citation metadata is available in `CITATION.cff` and `.zenodo.json`.
