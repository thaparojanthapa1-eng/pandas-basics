"""
Pandas Foundations: Data Cleaning & Preprocessing
-------------------------------------------------
Demonstrating dropping missing values, filling NaNs, value replacement, 
string operations, type casting, and duplicate removal.
"""

import pandas as pd


def main() -> None:
    # ---------------------------------------------------------
    # 1. Load Data
    # ---------------------------------------------------------
    df = pd.read_csv("pokemon_data.csv")

    print("--- Original DataFrame ---")
    print(df.head())

    # ---------------------------------------------------------
    # 2. Handling Missing Data (NaNs)
    # ---------------------------------------------------------
    # Drop rows where 'type_2' is missing
    df = df.dropna(subset=["type_2"])

    # Fill remaining missing values in 'type_2' (if any) with 'none'
    df = df.fillna({"type_2": "none"})

    # ---------------------------------------------------------
    # 3. Value Replacement & String Manipulations
    # ---------------------------------------------------------
    # Replace categorical values in a column
    df["type_1"] = df["type_1"].replace({"Grass": "Leaf"})

    # Convert strings to lowercase using vectorised .str accessor
    df["name"] = df["name"].str.lower()

    # ---------------------------------------------------------
    # 4. Type Casting & Removing Duplicates
    # ---------------------------------------------------------
    # Explicitly cast column to boolean type
    df["is_legendary"] = df["is_legendary"].astype(bool)

    # Remove duplicate rows across the DataFrame
    df = df.drop_duplicates()

    # ---------------------------------------------------------
    # 5. Processed Result
    # ---------------------------------------------------------
    print("\n--- Cleaned & Processed DataFrame ---")
    print(df)


if __name__ == "__main__":
    main()
