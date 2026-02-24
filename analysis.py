import matplotlib.pyplot as plt

def run_analysis(df):
    """Perform EDA and generate charts safely"""

    print("\n===== SUMMARY =====")
    print("Total products:", len(df))
    print("Unique suppliers:", df["supplier"].nunique())
    print("Average price:", df["price"].mean())

    # Category chart
    if df["category"].notna().sum() > 0:
        df["category"].value_counts().plot(kind="bar")
        plt.title("Products per Category")
        plt.tight_layout()
        plt.savefig("charts/category_distribution.png")
        plt.clf()

    # Price histogram (only if prices exist)
    if df["price"].notna().sum() > 0:
        df["price"].dropna().plot(kind="hist", bins=20)
        plt.title("Price Distribution")
        plt.tight_layout()
        plt.savefig("charts/price_distribution.png")
        plt.clf()

    # Location chart (only if data exists)
    if df["location"].notna().sum() > 0:
        df["location"].value_counts().head(10).plot(kind="bar")
        plt.title("Top Supplier Locations")
        plt.tight_layout()
        plt.savefig("charts/location_distribution.png")
        plt.clf()

    generate_report(df)


def generate_report(df):
    """Generate insights report"""
    with open("report.txt", "w", encoding="utf-8") as f:
        f.write("B2B Marketplace Insights\n")
        f.write("========================\n\n")
        f.write("\n\nObservations:\n")
        f.write("- Supplier and price data may be missing due to marketplace protections.\n")
        f.write("- Product listings still reveal market demand patterns.\n")

        f.write(f"Total products collected: {len(df)}\n")
        f.write(f"Unique suppliers: {df['supplier'].nunique()}\n\n")

        f.write("Top Categories:\n")
        f.write(str(df["category"].value_counts().head()))
        f.write("\n\nTop Supplier Locations:\n")
        f.write(str(df["location"].value_counts().head()))

        f.write("\n\nMissing Prices:\n")
        f.write(str(df["price"].isna().sum()))

        f.write("\n\nData Observations:\n")
        f.write("- Some listings do not include prices (negotiation-based).\n")
        f.write("- Supplier clusters indicate regional manufacturing hubs.\n")