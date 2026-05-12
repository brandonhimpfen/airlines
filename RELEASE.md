# Release 1.0.0

Production-ready cleanup of the Airlines Dataset.

## Notes

- Reorganized files into `data/`, `schema/`, `scripts/`, and `docs/`.
- Added CSV, JSON, minified JSON, TSV, and names-only exports.
- Added JSON Schema and validation script.
- Added documentation, citation metadata, and Zenodo metadata.
- Preserved original identifiers and names while avoiding unsupported claims about active status or country.

## Validation

```bash
python scripts/validate.py
```

Expected result:

```text
OK: validated 555 airline records
```
