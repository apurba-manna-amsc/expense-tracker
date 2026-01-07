import pandas as pd
import matplotlib.pyplot as plt
from utils import clean_data, add_categories
import os

def load_data():
    # Ensure path always points to ../data/
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATA_PATH = os.path.join(BASE_DIR, "data", "transactions.csv")
    return pd.read_csv(DATA_PATH)


def summarize_monthly(df):
    summary = df.groupby("category")["amount"].sum().sort_values()
    print("\n==== Expense Summary by Category ====\n")
    print(summary)
    return summary


def plot_expenses(summary):
    plt.figure()
    summary.plot(kind="bar")
    plt.title("Expenses by Category")
    plt.ylabel("Total Amount")
    plt.xlabel("Category")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def main():
    df = load_data()
    
    df = clean_data(df)
    
    df = add_categories(df)

    df_expenses = df[df["amount"] < 0]

    summary = summarize_monthly(df_expenses)

    plot_expenses(summary)


if __name__ == "__main__":
    main()
