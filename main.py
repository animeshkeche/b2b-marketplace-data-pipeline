from crawler import crawl
from cleaner import clean_data
from analysis import run_analysis
import os

# create folders if not present
os.makedirs("data", exist_ok=True)
os.makedirs("charts", exist_ok=True)

print("Collecting data...")
raw_data = crawl()

print("Cleaning data...")
df = clean_data(raw_data)

print("Saving dataset...")
df.to_csv("data/products.csv", index=False)
df.to_json("data/products.json", orient="records", indent=2)

print("Running analysis...")
run_analysis(df)

print("\nPipeline completed successfully!")