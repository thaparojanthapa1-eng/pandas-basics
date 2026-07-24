Markdown
# Pandas Foundations: Data Analysis & Manipulation 🐼

A code-first repository covering core **Pandas** operations, data structure manipulations, vectorization, boolean filtering, aggregations, and file I/O workflows (e.g., Stanford CS229 prerequisites).

---

## 📌 Repository Overview

This project serves as a hands-on log and reference guide for core **Pandas** workflows. It demonstrates how to create and manipulate 1D `Series` and 2D `DataFrames`, run label/position-based indexing (`.loc` vs. `.iloc`), filter data via compound boolean masks, perform grouped aggregations, clean dirty datasets, and process CSV/JSON files.

---

## 🛠️ Key Topics & Code Modules

### 1. **Working with Pandas Series**
* Creating 1D `Series` with custom string labels vs. positional indexing[cite: 1].
* Label-based element access (`.loc['label']`) and positional lookup (`.iloc[index]`)[cite: 1].
* Modifying series elements by label in-place[cite: 1].
* Boolean filtering directly on Series values (`series[series >= 105]`)[cite: 1].
* Initializing Series directly from Python dictionaries[cite: 1].

### 2. **DataFrame Fundamentals & Structural Operations**
* Constructing 2D `DataFrames` with custom index labels[cite: 2].
* Selecting full rows via label (`df.loc['label']`) and integer position (`df.iloc[i]`)[cite: 2].
* Feature engineering by assigning new DataFrame columns[cite: 2].
* Appending new records/rows using `pd.concat()`[cite: 2].

### 3. **Data I/O & Advanced Indexing**
* Reading structured files via `pd.read_csv()` and `pd.read_json()`[cite: 3, 4].
* Controlling output formatting using `df.to_string()` for full printing vs. truncated previews[cite: 3, 4].
* Single-column selection (`df["col"]`) vs. multi-column extraction (`df[["col1", "col2"]]`)[cite: 3].
* Setting custom index columns upon import (`index_col="name"`)[cite: 3].
* Label-based slicing (`df.loc["Start":"End", ["col1", "col2"]]`) and 2D positional slicing (`df.iloc[0:3, 0:6]`)[cite: 3].
* Handling runtime lookups with dynamic user inputs and `KeyError` exception blocks[cite: 3].

### 4. **Boolean Indexing & Conditional Filtering**
* Single condition row filtering (e.g., `df["attack"] >= 100`)[cite: 5].
* Logical **OR** filtering using bitwise operations (`|`)[cite: 5].
* Logical **AND** compound filtering using bitwise operations (`&`)[cite: 5].

### 5. **Aggregations & GroupBy Operations**
* Computing dataset-wide summary statistics (`mean()`, `sum()`, `min()`, `max()`, `count()`) across numeric columns[cite: 6].
* Calculating targeted metrics for individual columns[cite: 6].
* Grouping data by categorical features using `groupby("type_1")` and aggregating target columns[cite: 6].

### 6. **Data Cleaning & Preprocessing**
* Dropping missing records (`dropna(subset=[...])`) and filling missing values (`fillna(...)`)[cite: 7].
* Value mapping and replacement (`df["col"].replace(...)`)[cite: 7].
* Vectorized string manipulations using the `.str` accessor (`df["col"].str.lower()`)[cite: 7].
* Explicit data type casting using `astype()`[cite: 7].
* Removing duplicate rows across the DataFrame (`df.drop_duplicates()`)[cite: 7].

---

## 💻 Environment Setup

### Prerequisites
* **Python 3.9+**
* **pandas**

### Installation & Execution

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/pandas-foundations.git](https://github.com/YOUR_USERNAME/pandas-foundations.git)
   cd pandas-foundations
Set up a virtual environment (optional but recommended):

Bash
# macOS/Linux
python -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
Install dependencies:

Bash
pip install pandas
Run any script:

Bash
python 01_series.py
python 02_dataframes.py
📄 License
This project is open-source and available under the MIT License.