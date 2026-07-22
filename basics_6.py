"""
Pandas Foundations: Aggregations & GroupBy Operations
------------------------------------------------------
Demonstrating whole-DataFrame summary statistics (mean, sum, min, max, count),
single-column aggregation, and grouped aggregations using groupby().
"""

import pandas as pd


def main() -> None:
    # ---------------------------------------------------------
    # 1. Load Data
    # ---------------------------------------------------------
    df = pd.read_csv("pokemon_data.csv")

    # ---------------------------------------------------------
    # 2. DataFrame-Wide Aggregations
    # ---------------------------------------------------------
    print("--- Column Means (Numeric Only) ---")
    print(df.mean(numeric_only=True))

    print("\n--- Column Sums (Numeric Only) ---")
    print(df.sum(numeric_only=True))

    print("\n--- Minimum Values ---")
    print(df.min(numeric_only=True))

    print("\n--- Maximum Values ---")
    print(df.max(numeric_only=True))

    print("\n--- Non-Null Counts Per Column ---")
    print(df.count())

    # ---------------------------------------------------------
    # 3. Single Column Aggregation
    # ---------------------------------------------------------
    mean_attack = df["attack"].mean()
    print(f"\n--- Average Attack (Overall): {mean_attack:.2f} ---")

    # ---------------------------------------------------------
    # 4. GroupBy Aggregations
    # ---------------------------------------------------------
    grouped_by_type = df.groupby("type_1")

    print("\n--- Average Attack by Primary Type (type_1) ---")
    print(grouped_by_type["attack"].mean())


if __name__ == "__main__":
    main()
