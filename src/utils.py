import pandas as pd

CATEGORY_KEYWORDS = {
    "Food": ["swiggy", "zomato", "restaurant"],
    "Transport": ["uber", "ola", "bus", "train"],
    "Shopping": ["amazon", "flipkart"],
    "Utilities": ["electricity", "internet", "recharge"],
    "Health": ["pharmacy", "hospital"],
    "Fitness": ["gym"],
    "Entertainment": ["movie"],
    "Income": ["salary", "bonus"]
}


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df["date"] = pd.to_datetime(df["date"])
    df["description"] = df["description"].str.lower().str.strip()
    df["amount"] = df["amount"].astype(float)
    return df


def categorize_transaction(description: str) -> str:
    for category, keywords in CATEGORY_KEYWORDS.items():
        if any(k in description for k in keywords):
            return category
    return "Other"


def add_categories(df: pd.DataFrame) -> pd.DataFrame:
    df["category"] = df["description"].apply(categorize_transaction)
    return df
