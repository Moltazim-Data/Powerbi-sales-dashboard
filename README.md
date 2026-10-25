# Sales Performance Dashboard — Power BI

This repository contains a sample sales dataset and a dashboard screenshot for a Power BI portfolio exercise.

## Included assets

- `data/sales.csv` — sample sales rows with date, country, product, category, sales amount, and quantity.
- `dashboard/dashboard_overview.png` — static screenshot/preview.

## Intended analysis

- Sales amount by month
- Sales amount by country
- Product/category comparison
- Filters for category and other relevant dimensions

## Metric notes

Treat the `Sales` field as the supplied sales amount. Do not multiply it by quantity unless the source data dictionary establishes that `Sales` is a unit price. Document the dataset source, currency, time coverage, and whether amounts represent gross sales, net sales, or another measure before interpreting the dashboard.

## Power BI status

A screenshot is not an interactive report file. This repository does not currently document a native `.pbix` artifact or a published Power BI service report. To complete the project, open `data/sales.csv` in Power BI Desktop, build the visuals and slicers, reconcile totals to simple source-data calculations, save the `.pbix` locally, and add a genuine screenshot/export if you want to share it.

## Suggested validation checklist

- [ ] Confirm date and numeric data types.
- [ ] Check blank values and duplicate rows.
- [ ] Reconcile total sales and quantity against the source.
- [ ] Confirm chart totals agree with the selected filters.
- [ ] Add the source and licensing details for the dataset.

This is a practice portfolio project. Do not claim an interactive or deployed dashboard until that artifact exists and has been tested.
