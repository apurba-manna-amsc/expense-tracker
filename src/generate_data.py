import pandas as pd
import random
from datetime import datetime, timedelta
import os

# Ensure path always points to ../data/
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "transactions.csv")

descriptions = [
    "Amazon Purchase", "Flipkart Order", "Uber Ride", "Ola Ride",
    "Swiggy Order", "Zomato Order", "Restaurant Bill",
    "Electricity Bill", "Internet Bill", "Mobile Recharge",
    "Pharmacy Purchase", "Hospital Visit", "Gym Membership",
    "Movie Tickets", "Bus Ticket", "Train Ticket",
    "Salary Credit", "Bonus Credit"
]

data = []
start_date = datetime(2026, 1, 1)

for i in range(60):
    date = start_date + timedelta(days=i)

    desc = random.choice(descriptions)

    if "Credit" in desc:
        amount = random.randint(20000, 50000)
        tx_type = "credit"
    else:
        amount = -random.randint(100, 6000)
        tx_type = "debit"

    data.append([date.strftime("%Y-%m-%d"), desc, amount, tx_type])

df = pd.DataFrame(data, columns=["date", "description", "amount", "type"])

# Create data folder if missing
os.makedirs(os.path.dirname(DATA_PATH), exist_ok=True)

df.to_csv(DATA_PATH, index=False)

print(f"Synthetic CSV generated at: {DATA_PATH}")
