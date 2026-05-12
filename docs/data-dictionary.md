# Data Dictionary

## Canonical file

The canonical dataset is `data/airlines.csv`.

## Fields

| Field | Type | Required | Description |
|---|---:|---:|---|
| `airline_id` | string | yes | Original airline identifier from the source dataset. |
| `name` | string | yes | Airline name. |
| `code_type` | string | yes | `iata` for two-character codes, `legacy_or_icao_like` for longer identifiers. |
| `iata_code` | string | no | Two-character IATA-style code when applicable. |
| `icao_code` | string | no | Three-character or legacy code when applicable. |
| `country` | string | no | Airline country. Blank until verified. |
| `region` | string | no | Geographic region. Blank until verified. |
| `status` | string | yes | One of `active`, `inactive`, `defunct`, `merged`, `renamed`, or `unknown`. |
| `active` | boolean/string | no | Boolean once verified. Blank while unknown. |
| `website` | string | no | Official website once verified. |
| `wikidata_id` | string | no | Wikidata identifier once verified. |
| `notes` | string | no | Notes about import status, ambiguity, or enrichment. |

## Controlled values

The `status` field uses the following controlled vocabulary:

- `active`
- `inactive`
- `defunct`
- `merged`
- `renamed`
- `unknown`
