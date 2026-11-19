# Sales Performance Dashboard — Power BI

A sales reporting practice project built around a sample dataset. The repository contains source data and a static dashboard preview to guide a Power BI report build.

## Dataset
`data/sales.csv` includes sample sales records with date, country, product, category, sales amount and quantity.

## Dashboard preview
`dashboard/dashboard_overview.png` is a static image—not an interactive report.

## Report goals
- Monthly sales trend
- Country comparison
- Product and category performance
- Filters for relevant business dimensions

## Metric notes
Use the supplied `Sales` value as the sales amount; do not multiply it by quantity unless the source definition confirms that Sales is a unit price. Before interpreting the report, document dataset source, currency, date coverage and gross/net meaning.

## Current status
This repo includes the dataset and preview image. A native Power BI `.pbix` and published report are not included yet.

## Validation checklist
- Confirm data types and missing values.
- Reconcile totals with source rows.
- Ensure filtered chart totals match the selected data.
- Document source and license.
- Save the completed report and add a genuine screenshot/export.
