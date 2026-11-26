CISC7204 CLASS K TEAM 04 — FINAL ANALYSIS
Housing Prices and Employment Earnings in Macao
Release: 4 November 2026

READ
Open cisc7204-Class_K-Team_04_FinalAnalysis.html for the complete offline analysis.
The .ipynb is the executed, editable Jupyter notebook. All code and outputs are saved.
The report and presentation use the same annual values and calculations.

INPUTS AND PROVENANCE
rppi_annual.csv and resident_earnings_annual.csv: separate annual source tables.
annual_inputs.csv: their checked, one-to-one join for 2013–2025.
annual_analysis.csv: input values and derived measures.
data_dictionary.csv: definitions, units and formulas for the main annual table.
derived_tables_dictionary.csv: definitions for period and sensitivity tables.
observation_provenance.csv: exact publication location for all 26 observations.
source_register.csv: 18 official source records, URLs, dates and SHA256 hashes.
raw_sources/: original DSEC publications and current database response.
source_extracts/: convenience extracts; the originals remain authoritative.
provenance_support/: saved database query and indicator metadata.
vintage_crosscheck.csv: all 26 archived/current value comparisons and update dates.

RESULTS
2013–2025: RPPI +3.9894%; employed-resident earnings +36.6667%.
The relative-pressure index in 2025 is 76.0898 with 2013=100.
2013–2020: RPPI +42.0213%; earnings +33.3333%.
2020–2025: RPPI -26.7790%; earnings +2.5%.
2018–2025: RPPI -26.3653%; earnings +2.5%.
All 12 earlier observed bases (2013–2024) give a 2025 pressure index below 100.
The range is 59.3317 with base 2014 to 90.5931 with base 2024.
The direction is consistent across the observed bases; magnitudes depend on period.
This is a nominal descriptive comparison, not a household affordability measure.
See summary_metrics.json, period_comparisons.csv and all_base_year_sensitivity.csv.

FIGURES
figures/ contains four PNG charts and matching vector PDF files:
01_common_base_trends; 02_annual_growth; 03_relative_price_pressure;
04_all_base_year_sensitivity.

CHECKS
All 13 common annual years are present. There are no duplicate years, missing levels
or nonpositive levels. Annual growth uses consecutive years only. No observation
was removed or interpolated. No quarterly median was averaged to form an annual one.
All 26 archived annual values exactly match DSEC's current database on 4 November 2026.
The 2017 RPPI uses the revised 244.8, confirmed by later history and the database.
Source hashes and a full top-to-bottom execution were checked. See quality_check.json.
source_notes.txt explains source vintages, the 2017 method change and interpretation.
Supporting_Evidence/ contains complete ordered captures of executable cells and outputs.

REPEAT
Use the established project Python to run rerun_notebook.py, or select that environment
when opening the .ipynb in Jupyter/VS Code. The helper uses relative paths and creates
a temporary kernel definition. It refreshes the notebook, HTML, tables, metrics and
figures without changing raw sources. The saved database snapshot makes execution
offline once dependencies are installed. It does not silently fetch a later vintage.
Exact project pyproject.toml and uv.lock copies are in environment/; see its instructions.

TEAM
All six members share the agreed Python, visualization and interpretation work.
This release does not infer who typed a cell or invent individual reviews or meetings.

VISUAL REDESIGN
This separate release preserves all numerical tables and results from the completed
final package. Four Plotly charts now use IBM Plex, direct labels and annual markers.
figures/ also contains report_ PNG/PDF/SVG layouts, font-embedded SVG, editable
.plotly.json specifications and self-contained interactive .html pages with tables.
Open any chart HTML directly in a browser; no server or internet is required.
The notebook regenerates the redesigned charts on a full rerun. build_visuals.py
provides a chart-only rerender. See design_references.txt for software and design
sources, licences, axis choices and accessibility decisions.
