import pandas as pd

REFERENCE_DATE = pd.Timestamp("2024-06-01")
CHURN_THRESHOLD_DAYS = 90


def load_cleaned_data():
    df = pd.read_csv("outputs/cleaned_customers.csv")
    df["signup_date"] = pd.to_datetime(df["signup_date"])
    df["last_purchase_date"] = pd.to_datetime(df["last_purchase_date"])
    return df


def add_derived_metrics(df):

    # how long they've been a customer
    df["tenure_days"] = (REFERENCE_DATE - df["signup_date"]).dt.days

    # how long since they last bought something
    df["days_since_last_purchase"] = (REFERENCE_DATE - df["last_purchase_date"]).dt.days

    # average order value
    df["avg_order_value"] = (df["total_spent"] / df["total_orders"]).round(2)

    # churn flag: no purchase in last 90 days = churned
    df["status"] = df["days_since_last_purchase"].apply(
        lambda x: "Churned" if x > CHURN_THRESHOLD_DAYS else "Active"
    )

    return df


def add_value_segment(df):

    def segment(spent):
        if spent >= 20000:
            return "High Value"
        elif spent >= 8000:
            return "Medium Value"
        else:
            return "Low Value"

    df["value_segment"] = df["total_spent"].apply(segment)
    return df


def compute_kpis(df):
    total_customers = len(df)
    churned = (df["status"] == "Churned").sum()

    return {
        "total_customers": total_customers,
        "active_customers": total_customers - churned,
        "churned_customers": churned,
        "churn_rate_percent": round((churned / total_customers) * 100, 2),
        "avg_customer_spend": round(df["total_spent"].mean(), 2),
        "avg_tenure_days": round(df["tenure_days"].mean(), 2),
    }


def churn_by_region(df):
    return (
        df.groupby("region")["status"]
        .apply(lambda x: (x == "Churned").mean() * 100)
        .round(2)
        .sort_values(ascending=False)
    )


def churn_by_segment(df):
    return (
        df.groupby("value_segment")["status"]
        .apply(lambda x: (x == "Churned").mean() * 100)
        .round(2)
        .sort_values(ascending=False)
    )


def spend_by_region(df):
    return df.groupby("region")["total_spent"].sum().sort_values(ascending=False)


def segment_distribution(df):
    return df["value_segment"].value_counts()


def save_reports(kpis, churn_region, churn_segment, region_spend, segment_dist, df):

    with open("outputs/kpi_summary.csv", "w") as f:
        f.write("KPI,Value\n")
        for k, v in kpis.items():
            f.write(f"{k},{v}\n")

    churn_region.to_csv("outputs/churn_by_region.csv")
    churn_segment.to_csv("outputs/churn_by_segment.csv")
    region_spend.to_csv("outputs/spend_by_region.csv")
    segment_dist.to_csv("outputs/segment_distribution.csv")
    df.to_csv("outputs/customers_with_metrics.csv", index=False)
