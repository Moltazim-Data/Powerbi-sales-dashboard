from pathlib import Path
import csv
from datetime import date

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "sales.csv"

def test_sales_csv_contract():
    with DATA.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    assert rows
    assert {"OrderDate", "Country", "Product", "Category", "Sales", "Quantity"} <= set(rows[0])
    for row in rows:
        date.fromisoformat(row["OrderDate"])
        assert float(row["Sales"]) >= 0
        assert int(row["Quantity"]) > 0
