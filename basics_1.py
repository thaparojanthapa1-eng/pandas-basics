"""
Pandas Foundations: Working with Series
----------------------------------------
A quick walkthrough of Pandas Series created while working through 
Stanford CS229 Problem Set 1.
"""

import pandas as pd


def main() -> None:
    # ---------------------------------------------------------
    # 1. Creating a Series with Custom Labels
    # ---------------------------------------------------------
    data = [100, 101, 105, 108, 111]
    labels = ["a", "b", "c", "d", "e"]

    series = pd.Series(data, index=labels)

    print("--- Initial Series ---")
    print(series)
    print("\nAccess element by label 'a':", series.loc["a"])

    # ---------------------------------------------------------
    # 2. Modifying Values & Indexing Methods
    # ---------------------------------------------------------
    series.loc["b"] = 200

    print("\n--- Updated Series ---")
    print(series)
    print("\nAccess element by label 'b':", series.loc["b"])
    print("Access element by positional index 1:", series.iloc[1])

    # ---------------------------------------------------------
    # 3. Filtering / Boolean Indexing
    # ---------------------------------------------------------
    print("\n--- Filtering: Elements >= 105 ---")
    print(series[series >= 105])

    # ---------------------------------------------------------
    # 4. Creating a Series from a Dictionary
    # ---------------------------------------------------------
    daily_steps = {
        "day1": 1000,
        "day2": 2000,
        "day3": 1100,
        "day4": 1050,
    }

    steps_series = pd.Series(daily_steps)

    print("\n--- Series from Dictionary ---")
    print(steps_series)


if __name__ == "__main__":
    main()
