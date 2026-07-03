import pandas as pd


def load_data():
    df = pd.read_csv("data/customers.csv")
    return df


def clean_data(df):

    # remove duplicates
    df = df.drop_duplicates()

    # remove missing values
    df = df.dropna()

    # fix dates
    df["signup_date"] = pd.to_datetime(df["signup_date"])
    df["last_purchase_date"] = pd.to_datetime(df["last_purchase_date"])

    # standardize text
    df["region"] = df["region"].str.title()
    df["customer_name"] = df["customer_name"].str.title()

    # remove invalid spend or orders
    df = df[df["total_spent"] > 0]
    df = df[df["total_orders"] > 0]

    return df


def save_cleaned_data(df):
    df.to_csv("outputs/cleaned_customers.csv", index=False)
