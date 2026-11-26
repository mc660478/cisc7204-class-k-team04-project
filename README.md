# CISC7204 Class K - Team 04 Final Project

Housing prices and employment income in Macao, 2013-2025.

Maintained by Zhu Lingjing (MC660478) for Team 04. This repository holds the team's analysis artefacts for the CISC7204 Project Data and Jupyter Notebooks submission.

## Contents

- `cisc7204-Class_K-Team_04_FinalAnalysis.ipynb` - main Jupyter notebook with executed outputs
- `build_visuals.py`, `rerun_notebook.py` - code used to export visualisations and reproduce the notebook
- `annual_inputs.csv`, `annual_analysis.csv`, `resident_earnings_annual.csv`, `rppi_annual.csv`, `period_comparisons.csv`, `all_base_year_sensitivity.csv` - input and derived datasets
- `data_dictionary.csv`, `derived_tables_dictionary.csv` - data dictionaries
- `figures/` - exported PNG figures
- `source_register.csv`, `source_notes.txt`, `provenance_support/`, `source_extracts/` - official source register and raw excerpts
- `environment/REPRODUCE.txt`, `pyproject.toml` - reproduction instructions and dependencies
- `design_references.txt`, `visual_qa.json`, `summary_metrics.json`, `quality_check.json` - design/QA notes

## Design principles (Alberto Cairo's five questions)

O1 Truthful: data and figures derive from official DSEC sources recorded in `source_register.csv`.
O2 Substantial: the analysis covers the full 2013-2025 period with base-year sensitivity checks.
O3 Functional: tables and figures are annotated and readable in the notebook and exported PNGs.
O4 Beautiful: consistent typography and colour encoding documented in `design_references.txt`.
O5 Insightful: period comparisons and relative price pressure reveal patterns beyond the raw series.

## Reproduce

See `environment/REPRODUCE.txt`. The notebook can be run with Jupyter; `build_visuals.py` regenerates the figures.
