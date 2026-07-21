"""
Pandas Foundations: Boolean Indexing & Conditional Filtering
------------------------------------------------------------
Demonstrating row filtering using single conditions, OR logical operators (|),
and AND logical operators (&) on DataFrames.
"""

import pandas as pd


def main() -> None:
    # ---------------------------------------------------------
    # 1. Load Data
    # ---------------------------------------------------------
    df = pd.read_csv("pokemon_data.csv")

    # ---------------------------------------------------------
    # 2. Single Condition Filtering
    # ---------------------------------------------------------
    strong_pokemon = df[df["attack"] >= 100]

    print("--- Strong Pokemon (Attack >= 100) ---")
    print(strong_pokemon[["name", "type_1", "attack"]])

    # ---------------------------------------------------------
    # 3. Logical OR Filtering (|)
    # ---------------------------------------------------------
    grass_pokemon = df[(df["type_1"] == "Grass") | (df["type_2"] == "Grass")]

    print("\n--- Grass-Type Pokemon (Primary or Secondary) ---")
    print(grass_pokemon[["name", "type_1", "type_2"]])

    # ---------------------------------------------------------
    # 4. Logical AND Filtering (&)
    # ---------------------------------------------------------
    grass_poison_pokemon = df[(df["type_1"] == "Grass")
                              & (df["type_2"] == "Poison")]

    print("\n--- Grass & Poison Dual-Type Pokemon ---")
    print(grass_poison_pokemon[["name", "type_1", "type_2"]])


if __name__ == "__main__":
    main()
