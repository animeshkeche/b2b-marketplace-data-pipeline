import pandas as pd

def clean_data(data):
    """Clean and normalize scraped data"""

    df = pd.DataFrame(data)

    # remove duplicate rows
    df.drop_duplicates(inplace=True)

    # clean price column
    df["price"] = (
        df["price"]
        .astype(str)
        .str.replace(r"[^\d.]", "", regex=True)
        .replace("", None)
    )

    df["price"] = pd.to_numeric(df["price"], errors="coerce")

    # normalize location
    df["location"] = df["location"].str.replace("India", "", regex=False)
    df["location"] = df["location"].str.strip()

    return df