"""
Pandas Foundations: Working with DataFrames
-------------------------------------------
Practicing DataFrame creation, row/column indexing, feature engineering,
and concatenation using pd.concat().
"""

import pandas as pd


def main() -> None:
    # ---------------------------------------------------------
    # 1. Create Initial DataFrame with Custom Index
    # ---------------------------------------------------------
    data = {
        "Name": ["Ash", "Pikachu", "Brock", "Misty"],
        "Age": [10, 5, 20, 12],
    }
    indices = ["Character_1", "Character_2", "Character_3", "Character_4"]

    df = pd.DataFrame(data, index=indices)

    print("--- Initial DataFrame ---")
    print(df)

    # ---------------------------------------------------------
    # 2. Row Selection with .loc vs .iloc
    # ---------------------------------------------------------
    print("\n--- Row Selection ---")
    print("Label-based selection (.loc['Character_2']):")
    print(df.loc["Character_2"])

    print("\nPosition-based selection (.iloc[2]):")
    print(df.iloc[2])

    # ---------------------------------------------------------
    # 3. Adding a New Column
    # ---------------------------------------------------------
    df["Job"] = ["Trainer", "Pokemon", "Gym Leader", "Gym Leader"]

    print("\n--- After Adding 'Job' Column ---")
    print(df)

    # ---------------------------------------------------------
    # 4. Appending New Rows using pd.concat()
    # ---------------------------------------------------------
    new_characters = pd.DataFrame(
        [
            {
                "Name": "Gary",
                "Age": 11,
                "Job": "Trainer"
            },
            {
                "Name": "Sandy",
                "Age": 11,
                "Job": "Trainer"
            },
        ],
        index=["Character_5", "Character_6"],
    )

    df = pd.concat([df, new_characters])

    print("\n--- Final DataFrame (Post Concatenation) ---")
    print(df)


if __name__ == "__main__":
    main()
