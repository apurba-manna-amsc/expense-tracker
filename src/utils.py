import pandas as pd

CATEGORY_KEYWORDS = {
    "Food": ["swiggy", "zomato", "restaurant", "pizza", "hotel"],
    "Transport": ["uber", "ola", "fuel", "metro", "bus"],
    "Shopping": ["amazon", "flipkart", "shopping", "mall"],
    "Utilities": ["electricity", "water", "gas", "recharge", "wifi"],
    "Health": ["doctor", "hospital", "medicine", "pharmacy"],
    "Income": ["salary", "credit"],
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
