"""
Pandas Foundations: Working with JSON Data
-----------------------------------------
Demonstrating JSON data loading and complete string representation output.
"""

import pandas as pd


def main() -> None:
    # ---------------------------------------------------------
    # 1. Loading Data from a JSON File
    # ---------------------------------------------------------
    df = pd.read_json("pokemon_data.json")

    # ---------------------------------------------------------
    # 2. Displaying Truncated vs. Complete DataFrame Output
    # ---------------------------------------------------------
    print("--- Truncated DataFrame Output ---")
    print(df)

    print("\n--- Complete DataFrame Output ---")
    print(df.to_string())


if __name__ == "__main__":
    main()
