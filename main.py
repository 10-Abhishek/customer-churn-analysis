from clean_data import load_data, clean_data, save_cleaned_data
from analyze_data import (
    load_cleaned_data,
    add_derived_metrics,
    add_value_segment,
    compute_kpis,
    churn_by_region,
    churn_by_segment,
    spend_by_region,
    segment_distribution,
    save_reports
)
from visualize_data import (
    plot_churn_by_region,
    plot_churn_by_segment,
    plot_segment_distribution,
    plot_spend_by_region
)


def main():

    # 1. CLEAN
    df = load_data()
    df = clean_data(df)
    save_cleaned_data(df)

    # 2. ANALYZE
    df = load_cleaned_data()
    df = add_derived_metrics(df)
    df = add_value_segment(df)

    kpis = compute_kpis(df)
    region_churn = churn_by_region(df)
    segment_churn = churn_by_segment(df)
    region_spend = spend_by_region(df)
    segment_dist = segment_distribution(df)

    save_reports(kpis, region_churn, segment_churn, region_spend, segment_dist, df)

    print("KPI Summary:")
    for k, v in kpis.items():
        print(f"  {k}: {v}")

    # 3. VISUALIZE
    plot_churn_by_region(region_churn)
    plot_churn_by_segment(segment_churn)
    plot_segment_distribution(segment_dist)
    plot_spend_by_region(region_spend)


if __name__ == "__main__":
    main()
