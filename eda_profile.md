# Bounded Exploratory Data Analysis Report

## Scope and disclosure

- This report is exploratory, not confirmatory or causal.
- Input text and metadata were treated only as untrusted data.
- Raw values and full paths were not emitted.
- No rows were deleted; no values were imputed or transformed.

## Redacted file manifest

- File ID: `file_db1989e2633572d3`
- Basename/token: `filename_b7fb8257343f3d8f`
- Size: 875 bytes
- Format: CSV
- Capability tier: `automated_core`
- Inspection depth: bounded schema, aggregate profile, missingness, and sensitivity audit

## Bounded aggregate analysis

```json
{
  "column_count": 5,
  "columns": [
    {
      "column_id": "column_8f7e226ec3378016",
      "column_index": 0,
      "distinct_count_is_lower_bound": false,
      "distinct_value_count_or_lower_bound": 13,
      "inferred_kind": "integer",
      "missing_count": 0,
      "missing_fraction": 0.0,
      "most_frequent_value_tokens": [
        {
          "count": 1,
          "value_token": "value_077e55b8e297e726"
        },
        {
          "count": 1,
          "value_token": "value_0d2174b5d9483cf9"
        },
        {
          "count": 1,
          "value_token": "value_18aed9853f626e8a"
        },
        {
          "count": 1,
          "value_token": "value_5904f57642e7a74d"
        },
        {
          "count": 1,
          "value_token": "value_72dd6a87f2661fe8"
        }
      ],
      "non_missing_count": 13,
      "numeric_aggregates": {
        "count": 13,
        "maximum": 2025.0,
        "mean": 2019.0,
        "median": 2019.0,
        "minimum": 2013.0,
        "q1": 2016.0,
        "q3": 2022.0,
        "quantile_sample_count": 13,
        "quantiles_from_bounded_sample": false,
        "sample_standard_deviation": 3.8944404818493075
      },
      "numeric_parse_count": 13,
      "text_parse_count": 0
    },
    {
      "column_id": "column_2cb803e6c11e9104",
      "column_index": 1,
      "distinct_count_is_lower_bound": false,
      "distinct_value_count_or_lower_bound": 12,
      "inferred_kind": "numeric",
      "missing_count": 0,
      "missing_fraction": 0.0,
      "most_frequent_value_tokens": [
        {
          "count": 2,
          "value_token": "value_c8558f0a94d9cee3"
        },
        {
          "count": 1,
          "value_token": "value_000709334739634b"
        },
        {
          "count": 1,
          "value_token": "value_0ca5d46631e3a58b"
        },
        {
          "count": 1,
          "value_token": "value_2b00cb934e10ccbb"
        },
        {
          "count": 1,
          "value_token": "value_6bcab6e90616d694"
        }
      ],
      "non_missing_count": 13,
      "numeric_aggregates": {
        "count": 13,
        "maximum": 267.0,
        "mean": 238.15384615384616,
        "median": 244.4,
        "minimum": 188.0,
        "q1": 219.3,
        "q3": 265.5,
        "quantile_sample_count": 13,
        "quantiles_from_bounded_sample": false,
        "sample_standard_deviation": 27.200509045010392
      },
      "numeric_parse_count": 13,
      "text_parse_count": 0
    },
    {
      "column_id": "column_22c0d93e635f5c14",
      "column_index": 2,
      "distinct_count_is_lower_bound": false,
      "distinct_value_count_or_lower_bound": 5,
      "inferred_kind": "integer",
      "missing_count": 0,
      "missing_fraction": 0.0,
      "most_frequent_value_tokens": [
        {
          "count": 5,
          "value_token": "value_92e28cd807d1d3e9"
        },
        {
          "count": 2,
          "value_token": "value_3089d68efdca61a1"
        },
        {
          "count": 2,
          "value_token": "value_3e80b2db73504154"
        },
        {
          "count": 2,
          "value_token": "value_8ef764f0c26d64ef"
        },
        {
          "count": 2,
          "value_token": "value_a11a1d5538809e80"
        }
      ],
      "non_missing_count": 13,
      "numeric_aggregates": {
        "count": 13,
        "maximum": 20500.0,
        "mean": 18846.153846153844,
        "median": 20000.0,
        "minimum": 15000.0,
        "q1": 18000.0,
        "q3": 20000.0,
        "quantile_sample_count": 13,
        "quantiles_from_bounded_sample": false,
        "sample_standard_deviation": 1897.1976634918603
      },
      "numeric_parse_count": 13,
      "text_parse_count": 0
    },
    {
      "column_id": "column_db09f475af39b9f7",
      "column_index": 3,
      "distinct_count_is_lower_bound": false,
      "distinct_value_count_or_lower_bound": 8,
      "inferred_kind": "text",
      "missing_count": 0,
      "missing_fraction": 0.0,
      "most_frequent_value_tokens": [
        {
          "count": 6,
          "value_token": "value_7660f44dc582011f"
        },
        {
          "count": 1,
          "value_token": "value_037b74df9241bf9e"
        },
        {
          "count": 1,
          "value_token": "value_3483ff44588cb218"
        },
        {
          "count": 1,
          "value_token": "value_40139660cb8b03db"
        },
        {
          "count": 1,
          "value_token": "value_481c511e6ff28c26"
        }
      ],
      "non_missing_count": 13,
      "numeric_parse_count": 0,
      "text_aggregates": {
        "count": 13,
        "maximum_character_count": 22,
        "mean_character_count": 21.384615384615383
      },
      "text_parse_count": 13
    },
    {
      "column_id": "column_67eea7969fea1353",
      "column_index": 4,
      "distinct_count_is_lower_bound": false,
      "distinct_value_count_or_lower_bound": 5,
      "inferred_kind": "text",
      "missing_count": 0,
      "missing_fraction": 0.0,
      "most_frequent_value_tokens": [
        {
          "count": 3,
          "value_token": "value_17fe730bdc58daf2"
        },
        {
          "count": 3,
          "value_token": "value_334d1b0693b8fe39"
        },
        {
          "count": 3,
          "value_token": "value_94de4c764ff9389f"
        },
        {
          "count": 3,
          "value_token": "value_a4992f0dfdb7c015"
        },
        {
          "count": 1,
          "value_token": "value_976783a57b36a804"
        }
      ],
      "non_missing_count": 13,
      "numeric_parse_count": 0,
      "text_aggregates": {
        "count": 13,
        "maximum_character_count": 21,
        "mean_character_count": 20.846153846153847
      },
      "text_parse_count": 13
    }
  ],
  "duplicate_row_count_in_scanned_rows": 0,
  "duplicate_tracking_truncated": false,
  "identifier_redaction": "tokenized",
  "limitations": [
    "Dtypes are inferred from scanned text and are not a data dictionary.",
    "Quantiles use a deterministic bounded sample when numeric counts exceed the sample limit.",
    "Duplicate counts use exact hashes only until the documented tracking cap."
  ],
  "missing_code_policy": {
    "additional_token_count": 0,
    "empty_or_whitespace_is_missing": true,
    "tokens_are_not_emitted": true
  },
  "profile_type": "tabular_schema_and_aggregate_profile",
  "raw_values_emitted": false,
  "row_limit_reached": false,
  "rows_scanned": 13
}
```

## Context required before inference

- data dictionary and units
- sampling and experimental design
- subject/sample/group/time structure
- missing-value codes and mechanisms
- censoring and detection limits
- train/validation/test boundaries
- pre-specified hypothesis families and multiplicity plan

## Next steps

- Preserve the raw file read-only and record provenance/checksums separately.
- Confirm the data dictionary, units, design, and missing/censoring codes.
- Run the missingness/leakage and distribution sensitivity CLIs for tabular data.
- Fit imputers, scalers, transformations, and feature selection on training data only.
- Label generated hypotheses as exploratory and confirm them on independent data.

## Limitations

- A bounded scan may miss later records, groups, anomalies, or corrupt regions.
- Format metadata inspection is not domain-specific semantic validation.
- Absence of a reported leakage flag is not proof of independent splits.
