"""
Pandas Foundations: Working with I/O and Advanced Indexing
---------------------------------------------------------
Demonstrating CSV data loading, full string conversions, multi-column 
selection, index setting, slicing with .loc and .iloc, and input handling.
"""

import pandas as pd


def main() -> None:
    # ---------------------------------------------------------
    # 1. Reading CSV Files & String Printing
    # ---------------------------------------------------------
    df = pd.read_csv("pokemon_data.csv")

    print("--- Truncated DataFrame Output ---")
    print(df)

    print("\n--- Complete DataFrame Output ---")
    print(df.to_string())

    # ---------------------------------------------------------
    # 2. Selecting Single & Multiple Columns
    # ---------------------------------------------------------
    print("\n--- Single Column Selection ('name') ---")
    print(df["name"])

    print("\n--- Multiple Column Selection ('name', 'hp', 'is_legendary') ---")
    print(df[["name", "hp", "is_legendary"]])

    # ---------------------------------------------------------
    # 3. Reading CSV with Index Column & Label Slicing (.loc)
    # ---------------------------------------------------------
    df_indexed = pd.read_csv("pokemon_data.csv", index_col="name")

    print("\n--- Specific Row and Columns for 'Bulbasaur' ---")
    print(df_indexed.loc["Bulbasaur", ["type_1", "type_2"]])

    print("\n--- Label Slicing ('Bulbasaur' to 'Mewtwo') ---")
    print(df_indexed.loc["Bulbasaur":"Mewtwo", ["type_1", "type_2"]])

    # ---------------------------------------------------------
    # 4. Positional Indexing & Slicing (.iloc)
    # ---------------------------------------------------------
    print("\n--- First Row (.iloc[0]) ---")
    print(df_indexed.iloc[0])

    print("\n--- First Three Rows (.iloc[0:3]) ---")
    print(df_indexed.iloc[0:3])

    print("\n--- First Three Rows & First Six Columns (.iloc[0:3, 0:6]) ---")
    print(df_indexed.iloc[0:3, 0:6])

    # ---------------------------------------------------------
    # 5. Dynamic User Input & Error Handling
    # ---------------------------------------------------------
    pokemon = input("\nEnter a Pokemon name: ").strip().capitalize()

    try:
        print(f"\n--- Data for '{pokemon}' ---")
        print(df_indexed.loc[pokemon])
    except KeyError:
        print(f"Error: '{pokemon}' was not found in the dataset.")


if __name__ == "__main__":
    main()
