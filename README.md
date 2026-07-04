## Customer Churn & Behavior Analysis

A Python pipeline analysing customer purchase behavior to identify churn patterns, value segments, and regional trends. Built as a multi-stage pipeline — clean, analyze, visualize — using a 50-row synthetic customer dataset.

---

## Project Structure

| File | Purpose |
|---|---|
| `clean_data.py` | Loads raw data, removes duplicates and nulls, fixes date types, standardises text fields |
| `analyze_data.py` | Calculates derived metrics, assigns churn status and value segments, runs aggregations |
| `visualize_data.py` | Generates and saves charts for churn and spend patterns |
| `main.py` | Runs the full pipeline end to end |

---

## What the Pipeline Does

**Cleaning** — Removes duplicate and missing records, converts date columns, standardises region and name casing, filters out invalid spend or order values.

**Derived Metrics** — Calculates customer tenure, days since last purchase, and average order value for every customer.

**Churn Classification** — Flags a customer as Churned if they haven't purchased in the last 90 days, otherwise Active.

**Value Segmentation** — Buckets customers into High, Medium, and Low value based on total spend.

**Aggregation** — Churn rate by region, churn rate by value segment, total spend by region, and segment distribution.

**Visualization** — Four charts: churn rate by region, churn rate by segment, value segment distribution, and spend by region.

---

## Key Findings

- Overall churn rate is 24% — 12 out of 50 customers haven't purchased in over 90 days
- East region has the highest churn rate at 30.8%, North has the lowest at 9.1%
- Low Value customers churn at 41.7%, more than 5x the rate of Medium Value customers
- High Value customers make up half the customer base but still show a 24% churn rate — retention efforts shouldn't only target low spenders
- Average customer tenure is around 585 days

---

## How to Run

```
python main.py
```

Runs the full pipeline and saves all outputs to the `outputs/` folder.

## Requirements

```
pandas
matplotlib
```
