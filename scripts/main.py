import pandas as pd

df = pd.read_csv("../data/sales_data.csv")

print("Accuracy Check")
df["date"] = pd.to_datetime(df["date"])

negative_prices = (df["price"] < 0).sum()
print(f"Negative prices: {negative_prices}")

future_dates = (df["date"] > pd.Timestamp.now()).sum()
print(f"Future dates: {future_dates}")

print("Consistency Check")
unique_products = df["product"].unique()
unique_count = df["product"].nunique()
print("Unique products:", unique_products)
print("Count of unique products:", unique_count)

print("Completeness Check")
missing_values = df.isnull().sum()
completeness_rate = df.notnull().mean().mean() * 100
print(f"Missing Values: \n{missing_values}")
print(f"Overall completeness rate: {completeness_rate:.1f}%")

assert (df["price"] >= 0).all(), "Cannot have Negative Price"


