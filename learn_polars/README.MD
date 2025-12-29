# Complete Pandas Cheatsheet with Explanations

---

## PART 1: LOADING DATA

```python
import pandas as pd
import numpy as np

# Load CSV file with default settings (comma separator, first row = header, UTF-8)
df = pd.read_csv("file.csv")

# Use semicolon as separator (common in European files)
df = pd.read_csv("file.csv", sep=";")

# File has NO header row — first row is actual data, columns become 0, 1, 2...
df = pd.read_csv("file.csv", header=None)

# Give your own column names
df = pd.read_csv("file.csv", names=["a", "b"])

# Use "id" column as row index instead of default 0, 1, 2...
df = pd.read_csv("file.csv", index_col="id")

# Load ONLY these columns, ignore the rest
df = pd.read_csv("file.csv", usecols=["a", "b"])

# Load only first 100 rows (good for testing big files)
df = pd.read_csv("file.csv", nrows=100)

# Skip first 5 rows before reading
df = pd.read_csv("file.csv", skiprows=5)

# Treat "?" and "-" as missing values (NaN)
df = pd.read_csv("file.csv", na_values=["?", "-"])

# Force a column to be string type (even if it looks like numbers)
df = pd.read_csv("file.csv", dtype={"col": str})

# Automatically convert column to datetime
df = pd.read_csv("file.csv", parse_dates=["date_col"])

# Specify UTF-8 encoding (default)
df = pd.read_csv("file.csv", encoding="utf-8")

# Use Latin-1 encoding (fixes "can't decode byte" errors for European files)
df = pd.read_csv("file.csv", encoding="latin-1")

# Load Excel file
df = pd.read_excel("file.xlsx")

# Load specific sheet from Excel
df = pd.read_excel("file.xlsx", sheet_name="Sheet2")

# Load JSON file
df = pd.read_json("file.json")

# Load CSV directly from a URL
df = pd.read_csv("https://example.com/data.csv")

# Save DataFrame to CSV (index=False removes row numbers)
df.to_csv("output.csv", index=False)

# Save to Excel file
df.to_excel("output.xlsx", index=False)

# Save to JSON file
df.to_json("output.json")
```

---

## PART 2: EXPLORING DATA

```python
# Show first 5 rows
df.head()

# Show first 10 rows
df.head(10)

# Show last 5 rows
df.tail()

# Show 5 random rows (different each time)
df.sample(5)

# Get (number of rows, number of columns)
df.shape

# Get number of rows
len(df)

# Get column names
df.columns

# Get column names as a Python list
df.columns.tolist()

# Get data type of each column
df.dtypes

# Get full summary: columns, types, non-null counts, memory usage
df.info()

# Get statistics for numeric columns (count, mean, std, min, 25%, 50%, 75%, max)
df.describe()

# Get statistics for text/object columns (count, unique, top, freq)
df.describe(include="object")

# Get statistics for ALL columns
df.describe(include="all")

# Count how many times each value appears (sorted most to least)
df["col"].value_counts()

# Same but as percentages (0.0 to 1.0)
df["col"].value_counts(normalize=True)

# Include NaN values in the count
df["col"].value_counts(dropna=False)

# Count how many unique values exist
df["col"].nunique()

# Get array of all unique values
df["col"].unique()

# Calculate average (mean)
df["col"].mean()

# Calculate middle value (median)
df["col"].median()

# Get smallest value
df["col"].min()

# Get largest value
df["col"].max()

# Calculate standard deviation
df["col"].std()

# Calculate variance
df["col"].var()

# Calculate sum of all values
df["col"].sum()

# Get 25th percentile value
df["col"].quantile(0.25)

# Get multiple percentiles at once
df["col"].quantile([0.25, 0.5, 0.75])

# Count missing values per column
df.isnull().sum()

# Count non-missing values per column
df.notnull().sum()

# Count TOTAL missing values in entire DataFrame
df.isnull().sum().sum()

# Get percentage of missing values per column
df.isnull().sum() / len(df) * 100

# Get True/False for each row: is this value missing?
df["col"].isna()

# Get rows WHERE the column is missing
df[df["col"].isna()]
```

---

## PART 3: SELECTING DATA

```python
# Get one column as a Series
df["col"]

# Get one column as a DataFrame (note double brackets)
df[["col"]]

# Get multiple columns as a DataFrame
df[["col1", "col2"]]

# Get column using dot notation (only works for simple column names)
df.col

# Get first row by position
df.iloc[0]

# Get last row by position
df.iloc[-1]

# Get rows 0 through 4 (5 rows total)
df.iloc[0:5]

# Get specific rows by position
df.iloc[[0, 2, 4]]

# Get value at row 0, column 2 (by position)
df.iloc[0, 2]

# Get rows 0-4 and columns 0-2 (by position)
df.iloc[0:5, 0:3]

# Get all rows, first column only
df.iloc[:, 0]

# Get all rows, last column only
df.iloc[:, -1]

# Get rows 0-4, all columns
df.iloc[0:5, :]

# Get row with index label 0
df.loc[0]

# Get row with index label "row_name"
df.loc["row_name"]

# Get rows with index labels 0 through 5
df.loc[0:5]

# Get value at row 0, column "col" (by label)
df.loc[0, "col"]

# Get rows 0-5, columns from "col1" to "col3"
df.loc[0:5, "col1":"col3"]

# Get all rows, one column
df.loc[:, "col"]

# Get row 0, multiple columns
df.loc[0, ["col1", "col2"]]

# Get all rows, multiple columns
df.loc[:, ["col1", "col2"]]

# Filter: rows where age > 30
df[df["age"] > 30]

# Filter: rows where name equals "John"
df[df["name"] == "John"]

# Filter: rows where city is NOT "NYC"
df[df["city"] != "NYC"]

# Filter: rows where column is missing (NaN)
df[df["col"].isna()]

# Filter: rows where column is NOT missing
df[df["col"].notna()]

# Filter with AND: both conditions must be true
df[(df["age"] > 30) & (df["city"] == "NYC")]

# Filter with OR: either condition can be true
df[(df["age"] > 30) | (df["city"] == "NYC")]

# Filter with NOT: opposite of condition
df[~(df["age"] > 30)]

# Filter: rows where city is in this list
df[df["city"].isin(["NYC", "LA", "Chicago"])]

# Filter: rows where city is NOT in this list
df[~df["city"].isin(["NYC", "LA"])]

# Filter: rows where age is between 20 and 30 (inclusive)
df[df["age"].between(20, 30)]

# Filter: rows where name contains "John" anywhere
df[df["name"].str.contains("John", na=False)]

# Filter: rows where name starts with "J"
df[df["name"].str.startswith("J", na=False)]

# Filter: rows where name ends with "son"
df[df["name"].str.endswith("son", na=False)]

# Filter: rows where name is longer than 5 characters
df[df["name"].str.len() > 5]

# Filter: case-insensitive contains
df[df["name"].str.contains("john", case=False, na=False)]

# Query method: cleaner syntax for filtering
df.query("age > 30")

# Query with multiple conditions
df.query("age > 30 and city == 'NYC'")

# Query with list
df.query("city in ['NYC', 'LA']")

# Query using a Python variable
df.query("age == @variable")
```

---

## PART 4: MODIFYING DATA

```python
# Create new column with constant value
df["new_col"] = 0

# Create new column from calculation
df["new_col"] = df["col1"] + df["col2"]

# Create new column: multiply existing column by 2
df["new_col"] = df["col1"] * 2

# Create new column: divide two columns
df["new_col"] = df["col1"] / df["col2"]

# Create new column using a function on each value
df["new_col"] = df["col"].apply(lambda x: x * 2)

# Create column with if/else logic (if age > 30: "old", else: "young")
df["category"] = np.where(df["age"] > 30, "old", "young")

# Create column with multiple conditions
conditions = [df["age"] < 20, df["age"] < 40, df["age"] >= 40]
choices = ["young", "middle", "old"]
df["category"] = np.select(conditions, choices, default="unknown")

# Modify existing column: multiply by 2
df["col"] = df["col"] * 2

# Convert text to UPPERCASE
df["col"] = df["col"].str.upper()

# Convert text to lowercase
df["col"] = df["col"].str.lower()

# Remove leading/trailing whitespace
df["col"] = df["col"].str.strip()

# Replace one value with another
df["col"] = df["col"].replace("old", "new")

# Replace multiple values at once
df["col"] = df["col"].replace({"old1": "new1", "old2": "new2"})

# Fill missing values with 0
df["col"] = df["col"].fillna(0)

# Modify specific rows based on condition
df.loc[df["age"] > 30, "category"] = "old"

# Modify specific cell
df.loc[0, "col"] = "new_value"

# Modify multiple columns for rows matching condition
df.loc[df["city"] == "NYC", ["col1", "col2"]] = 0

# Rename one column
df.rename(columns={"old_name": "new_name"}, inplace=True)

# Rename multiple columns
df.rename(columns={"a": "A", "b": "B"}, inplace=True)

# Replace ALL column names at once
df.columns = ["col1", "col2", "col3"]

# Convert all column names to lowercase
df.columns = df.columns.str.lower()

# Convert all column names to UPPERCASE
df.columns = df.columns.str.upper()

# Replace spaces with underscores in column names
df.columns = df.columns.str.replace(" ", "_")

# Remove whitespace from column names
df.columns = df.columns.str.strip()

# Delete one column
df.drop("col", axis=1, inplace=True)

# Delete multiple columns
df.drop(["col1", "col2"], axis=1, inplace=True)

# Delete columns (alternative syntax)
df = df.drop(columns=["col1", "col2"])

# Delete column using del keyword
del df["col"]

# Delete one row by index
df.drop(0, axis=0, inplace=True)

# Delete multiple rows by index
df.drop([0, 1, 2], axis=0, inplace=True)

# Delete rows matching a condition
df.drop(df[df["age"] < 18].index, inplace=True)

# Delete rows (alternative syntax)
df = df.drop(index=[0, 1, 2])

# Convert column to integer
df["col"] = df["col"].astype(int)

# Convert column to float
df["col"] = df["col"].astype(float)

# Convert column to string
df["col"] = df["col"].astype(str)

# Convert column to category (saves memory for repeated values)
df["col"] = df["col"].astype("category")

# Convert to numeric, turn errors into NaN
df["col"] = pd.to_numeric(df["col"], errors="coerce")

# Convert to datetime
df["col"] = pd.to_datetime(df["col"])

# Convert to datetime, turn errors into NaT (Not a Time)
df["col"] = pd.to_datetime(df["col"], errors="coerce")

# Insert column at specific position (position 0 = first column)
df.insert(0, "new_col", values)

# Limit values to a range (values below 0 become 0, above 100 become 100)
df["col"] = df["col"].clip(lower=0, upper=100)

# Convert to absolute value (remove negatives)
df["col"] = df["col"].abs()

# Round to 2 decimal places
df["col"] = df["col"].round(2)
```

---

## PART 5: HANDLING MISSING DATA

```python
# Get True/False for each cell: is it missing?
df.isnull()

# Count missing values per column
df.isnull().sum()

# Get percentage of missing values per column
df.isnull().sum() / len(df) * 100

# Check if ANY value in each column is missing
df.isnull().any()

# Check if ALL values in each column are missing
df.isnull().all()

# Drop rows that have ANY missing values
df.dropna()

# Drop rows where ALL values are missing
df.dropna(how="all")

# Drop rows where ANY value is missing (same as default)
df.dropna(how="any")

# Drop rows only if these specific columns have missing values
df.dropna(subset=["col1", "col2"])

# Keep rows that have at least 3 non-missing values
df.dropna(thresh=3)

# Drop COLUMNS that have missing values
df.dropna(axis=1)

# Replace ALL missing values with 0
df.fillna(0)

# Replace missing values with different values per column
df.fillna({"col1": 0, "col2": "unknown"})

# Fill missing in one column with 0
df["col"].fillna(0, inplace=True)

# Fill missing with column mean
df["col"].fillna(df["col"].mean())

# Fill missing with column median
df["col"].fillna(df["col"].median())

# Fill missing with most common value (mode)
df["col"].fillna(df["col"].mode()[0])

# Fill missing with group mean (smart fill based on category)
df["col"].fillna(df.groupby("category")["col"].transform("mean"))

# Forward fill: use previous row's value
df.fillna(method="ffill")

# Backward fill: use next row's value
df.fillna(method="bfill")

# Forward fill (newer syntax)
df.ffill()

# Backward fill (newer syntax)
df.bfill()

# Interpolate: estimate missing values between known values
df["col"].interpolate()

# Linear interpolation (connect the dots)
df["col"].interpolate(method="linear")

# Replace NaN with 0
df.replace(np.nan, 0)

# Replace infinity values with NaN
df.replace([np.inf, -np.inf], np.nan)
```

---

## PART 6: SORTING DATA

```python
# Sort by one column (ascending = smallest to largest)
df.sort_values("col")

# Sort descending (largest to smallest)
df.sort_values("col", ascending=False)

# Sort by multiple columns
df.sort_values(["col1", "col2"])

# Sort: first column ascending, second column descending
df.sort_values(["col1", "col2"], ascending=[True, False])

# Put NaN values first when sorting
df.sort_values("col", na_position="first")

# Put NaN values last when sorting (default)
df.sort_values("col", na_position="last")

# Sort and modify original DataFrame
df.sort_values("col", inplace=True)

# Sort by index (row labels)
df.sort_index()

# Sort index descending
df.sort_index(ascending=False)

# Get 10 smallest values
df.nsmallest(10, "col")

# Get 10 largest values
df.nlargest(10, "col")

# Get 10 smallest by multiple columns
df.nsmallest(10, ["col1", "col2"])
```

---

## PART 7: GROUPING DATA (groupby)

```python
# Group by column, calculate mean of all numeric columns
df.groupby("col").mean()

# Group by column, calculate sum
df.groupby("col").sum()

# Group by column, count rows per group
df.groupby("col").count()

# Group by column, get size (includes NaN)
df.groupby("col").size()

# Group by column, get minimum
df.groupby("col").min()

# Group by column, get maximum
df.groupby("col").max()

# Group by column, get first row of each group
df.groupby("col").first()

# Group by column, get last row of each group
df.groupby("col").last()

# Group by column, calculate standard deviation
df.groupby("col").std()

# Group by column, calculate variance
df.groupby("col").var()

# Group by column, calculate median
df.groupby("col").median()

# Group by column, count unique values
df.groupby("col").nunique()

# Group by city, calculate mean salary only
df.groupby("city")["salary"].mean()

# Group by city, calculate mean of multiple columns
df.groupby("city")[["salary", "age"]].mean()

# Group by multiple columns
df.groupby(["city", "department"]).mean()

# Group by multiple columns, get mean of one column
df.groupby(["city", "department"])["salary"].mean()

# Group with different functions for different columns
df.groupby("city").agg({"salary": "mean", "age": "max", "name": "count"})

# Multiple functions per column
df.groupby("city").agg({"salary": ["mean", "min", "max"], "age": ["mean", "std"]})

# Named aggregations (cleaner output)
df.groupby("city").agg(avg_salary=("salary", "mean"), max_age=("age", "max"), count=("name", "count"))

# Custom function: range (max - min)
df.groupby("city").agg(lambda x: x.max() - x.min())

# Transform: add group mean as new column (keeps original row count)
df["group_mean"] = df.groupby("city")["salary"].transform("mean")

# Transform: add group sum as new column
df["group_sum"] = df.groupby("city")["salary"].transform("sum")

# Transform: add group count as new column
df["group_count"] = df.groupby("city")["salary"].transform("count")

# Transform: add rank within each group
df["group_rank"] = df.groupby("city")["salary"].transform("rank")

# Calculate percentage of group total
df["pct_of_group"] = df["salary"] / df.groupby("city")["salary"].transform("sum")

# Calculate deviation from group mean
df["deviation"] = df["salary"] - df.groupby("city")["salary"].transform("mean")

# Filter: keep only groups where mean salary > 50000
df.groupby("city").filter(lambda x: x["salary"].mean() > 50000)

# Filter: keep only groups with more than 10 members
df.groupby("city").filter(lambda x: len(x) > 10)

# Apply: get top 3 salaries per city
df.groupby("city").apply(lambda x: x.nlargest(3, "salary"))

# Loop through groups
for name, group in df.groupby("city"):
    print(name, group)

# Keep group column as regular column (not index)
df.groupby("city", as_index=False).mean()

# Include NaN as a group
df.groupby("city", dropna=False).mean()
```

---

## PART 8: MERGING AND JOINING

```python
# Stack DataFrames vertically (add rows)
pd.concat([df1, df2])

# Stack vertically with fresh index (0, 1, 2, 3...)
pd.concat([df1, df2], ignore_index=True)

# Stack DataFrames horizontally (add columns)
pd.concat([df1, df2], axis=1)

# Stack with labels to identify source
pd.concat([df1, df2], keys=["first", "second"])

# Stack keeping only columns that exist in BOTH
pd.concat([df1, df2], join="inner")

# Merge on common column (like SQL JOIN)
pd.merge(df1, df2, on="key")

# Merge on multiple columns
pd.merge(df1, df2, on=["key1", "key2"])

# Merge when column names are different
pd.merge(df1, df2, left_on="id", right_on="user_id")

# Inner join: only keep rows that match in BOTH tables
pd.merge(df1, df2, on="key", how="inner")

# Left join: keep ALL rows from left table
pd.merge(df1, df2, on="key", how="left")

# Right join: keep ALL rows from right table
pd.merge(df1, df2, on="key", how="right")

# Outer join: keep ALL rows from BOTH tables
pd.merge(df1, df2, on="key", how="outer")

# Cross join: every row paired with every row (cartesian product)
pd.merge(df1, df2, on="key", how="cross")

# Merge on index instead of column
pd.merge(df1, df2, left_index=True, right_index=True)

# Merge: left on column, right on index
pd.merge(df1, df2, left_on="key", right_index=True)

# Add suffix to duplicate column names
pd.merge(df1, df2, on="key", suffixes=("_left", "_right"))

# Add indicator column showing where each row came from
pd.merge(df1, df2, on="key", indicator=True)

# Validate merge type (throws error if not one-to-many)
pd.merge(df1, df2, on="key", validate="one_to_many")

# Join on index (simpler than merge for index-based joins)
df1.join(df2)

# Join with outer join
df1.join(df2, how="outer")

# Join with custom suffixes
df1.join(df2, lsuffix="_left", rsuffix="_right")

# Append rows (older method, use concat instead)
df.append(df2, ignore_index=True)
```

---

## PART 9: RESHAPING DATA

```python
# Pivot table: rows=department, columns=city, values=mean salary
df.pivot_table(values="salary", index="department", columns="city", aggfunc="mean")

# Pivot with sum instead of mean
df.pivot_table(values="salary", index="department", columns="city", aggfunc="sum")

# Pivot with count
df.pivot_table(values="salary", index="department", columns="city", aggfunc="count")

# Pivot with multiple aggregations
df.pivot_table(values="salary", index="department", columns="city", aggfunc=["mean", "count"])

# Pivot with 0 instead of NaN for missing combinations
df.pivot_table(values="salary", index="department", columns="city", aggfunc="mean", fill_value=0)

# Pivot with row/column totals
df.pivot_table(values="salary", index="department", columns="city", aggfunc="mean", margins=True)

# Pivot multiple values
df.pivot_table(values=["salary", "age"], index="department", columns="city", aggfunc="mean")

# Pivot with multiple index levels
df.pivot_table(index=["dept", "city"], columns="year", values="sales", aggfunc="sum")

# Melt: convert wide format to long format (unpivot)
pd.melt(df, id_vars=["name"], value_vars=["Jan", "Feb", "Mar"], var_name="month", value_name="sales")

# Melt with just id_vars (melt all other columns)
pd.melt(df, id_vars=["name"])

# Pivot: convert long format to wide format
df.pivot(index="name", columns="month", values="sales")

# Stack: pivot columns into rows (creates MultiIndex)
df.stack()

# Unstack: pivot rows into columns
df.unstack()

# Unstack specific level
df.unstack(level=0)

# Unstack with fill value for missing
df.unstack(fill_value=0)

# Transpose: swap rows and columns
df.T
```

---

## PART 10: STRING OPERATIONS

```python
# Convert to lowercase
df["col"].str.lower()

# Convert to UPPERCASE
df["col"].str.upper()

# Convert to Title Case
df["col"].str.title()

# Capitalize first letter only
df["col"].str.capitalize()

# Swap case (upper→lower, lower→upper)
df["col"].str.swapcase()

# Remove leading and trailing whitespace
df["col"].str.strip()

# Remove leading whitespace only
df["col"].str.lstrip()

# Remove trailing whitespace only
df["col"].str.rstrip()

# Remove specific character from both ends
df["col"].str.strip("x")

# Replace text
df["col"].str.replace("old", "new")

# Replace text (literal, no regex)
df["col"].str.replace("old", "new", regex=False)

# Remove all digits using regex
df["col"].str.replace(r"\d+", "", regex=True)

# Remove all punctuation using regex
df["col"].str.replace(r"[^\w\s]", "", regex=True)

# Check if string contains pattern (returns True/False)
df["col"].str.contains("pattern")

# Case-insensitive contains
df["col"].str.contains("pattern", case=False)

# Contains with NaN handling (False for NaN)
df["col"].str.contains("pattern", na=False)

# Contains with regex pattern
df["col"].str.contains(r"\d+", regex=True)

# Check if string starts with
df["col"].str.startswith("A")

# Check if string ends with
df["col"].str.endswith("Z")

# Check if string matches regex pattern
df["col"].str.match(r"^\d+")

# Get length of each string
df["col"].str.len()

# Count occurrences of character
df["col"].str.count("a")

# Split string into list
df["col"].str.split(",")

# Split string into separate columns
df["col"].str.split(",", expand=True)

# Split with max splits
df["col"].str.split(",", n=2)

# Split from right side
df["col"].str.rsplit(",", n=1)

# Join list elements with separator
df["col"].str.join("-")

# Concatenate two columns with separator
df["col"].str.cat(df["col2"], sep="-")

# Get first character
df["col"].str[0]

# Get first 5 characters
df["col"].str[0:5]

# Get last 3 characters
df["col"].str[-3:]

# Slice characters (same as [0:5])
df["col"].str.slice(0, 5)

# Get character at position
df["col"].str.get(0)

# Extract first match of regex group
df["col"].str.extract(r"(\d+)")

# Extract multiple regex groups into columns
df["col"].str.extract(r"(\d+)-(\d+)")

# Extract all matches
df["col"].str.extractall(r"(\d+)")

# Find all matches as list
df["col"].str.findall(r"\d+")

# Find position of substring (-1 if not found)
df["col"].str.find("x")

# Find position from right
df["col"].str.rfind("x")

# Pad string to length with character
df["col"].str.pad(10, side="left", fillchar="0")

# Pad with zeros on left
df["col"].str.zfill(10)

# Center string with padding
df["col"].str.center(20)

# Left justify with padding
df["col"].str.ljust(20)

# Right justify with padding
df["col"].str.rjust(20)

# Wrap text at specified width
df["col"].str.wrap(50)

# Replace slice of string
df["col"].str.slice_replace(0, 3, "NEW")

# Repeat string N times
df["col"].str.repeat(2)

# Normalize unicode characters
df["col"].str.normalize("NFKD")

# Check if all characters are letters
df["col"].str.isalpha()

# Check if all characters are digits
df["col"].str.isdigit()

# Check if all characters are alphanumeric
df["col"].str.isalnum()

# Check if all characters are whitespace
df["col"].str.isspace()

# Check if all characters are lowercase
df["col"].str.islower()

# Check if all characters are uppercase
df["col"].str.isupper()

# Check if string is numeric
df["col"].str.isnumeric()

# Check if string is decimal
df["col"].str.isdecimal()
```

---

## PART 11: DATE OPERATIONS

```python
# Convert string to datetime
df["date"] = pd.to_datetime(df["date"])

# Convert with specific format (YYYY-MM-DD)
df["date"] = pd.to_datetime(df["date"], format="%Y-%m-%d")

# Convert European format (DD/MM/YYYY)
df["date"] = pd.to_datetime(df["date"], format="%d/%m/%Y")

# Convert with time (MM-DD-YYYY HH:MM:SS)
df["date"] = pd.to_datetime(df["date"], format="%m-%d-%Y %H:%M:%S")

# Convert with errors → NaT for bad dates
df["date"] = pd.to_datetime(df["date"], errors="coerce")

# Let pandas guess the format
df["date"] = pd.to_datetime(df["date"], infer_datetime_format=True)

# Create datetime from separate year, month, day columns
df["date"] = pd.to_datetime(df[["year", "month", "day"]])

# Extract year
df["year"] = df["date"].dt.year

# Extract month (1-12)
df["month"] = df["date"].dt.month

# Extract day of month (1-31)
df["day"] = df["date"].dt.day

# Extract hour (0-23)
df["hour"] = df["date"].dt.hour

# Extract minute (0-59)
df["minute"] = df["date"].dt.minute

# Extract second (0-59)
df["second"] = df["date"].dt.second

# Extract day of week (0=Monday, 6=Sunday)
df["weekday"] = df["date"].dt.dayofweek

# Extract day name ("Monday", "Tuesday", etc.)
df["weekday_name"] = df["date"].dt.day_name()

# Extract month name ("January", "February", etc.)
df["month_name"] = df["date"].dt.month_name()

# Extract quarter (1-4)
df["quarter"] = df["date"].dt.quarter

# Extract week number (1-52)
df["week"] = df["date"].dt.isocalendar().week

# Extract day of year (1-366)
df["dayofyear"] = df["date"].dt.dayofyear

# Check if date is first day of month
df["is_month_start"] = df["date"].dt.is_month_start

# Check if date is last day of month
df["is_month_end"] = df["date"].dt.is_month_end

# Check if date is first day of quarter
df["is_quarter_start"] = df["date"].dt.is_quarter_start

# Check if date is last day of quarter
df["is_quarter_end"] = df["date"].dt.is_quarter_end

# Check if date is first day of year
df["is_year_start"] = df["date"].dt.is_year_start

# Check if date is last day of year
df["is_year_end"] = df["date"].dt.is_year_end

# Check if year is leap year
df["is_leap_year"] = df["date"].dt.is_leap_year

# Get number of days in the month
df["days_in_month"] = df["date"].dt.days_in_month

# Extract date only (remove time)
df["date_only"] = df["date"].dt.date

# Extract time only (remove date)
df["time_only"] = df["date"].dt.time

# Format date as string (YYYY-MM-DD)
df["date_str"] = df["date"].dt.strftime("%Y-%m-%d")

# Format date as string (Month DD, YYYY)
df["date_str"] = df["date"].dt.strftime("%B %d, %Y")

# Calculate days ago from today
df["days_ago"] = (pd.Timestamp.now() - df["date"]).dt.days

# Add 7 days to date
df["next_week"] = df["date"] + pd.Timedelta(days=7)

# Add 1 month to date
df["next_month"] = df["date"] + pd.DateOffset(months=1)

# Calculate difference between consecutive dates
df["diff"] = df["date"].diff()

# Calculate difference in days
df["diff_days"] = df["date"].diff().dt.days

# Filter: dates after 2023-01-01
df[df["date"] > "2023-01-01"]

# Filter: dates in range
df[df["date"].between("2023-01-01", "2023-12-31")]

# Filter: dates in 2023
df[df["date"].dt.year == 2023]

# Filter: dates in December
df[df["date"].dt.month == 12]

# Set date column as index
df.set_index("date", inplace=True)

# Resample: monthly average
df.resample("M").mean()

# Resample: weekly sum
df.resample("W").sum()

# Resample: quarterly count
df.resample("Q").count()

# Resample: yearly first value
df.resample("Y").first()

# Create date range
pd.date_range(start="2023-01-01", end="2023-12-31", freq="D")

# Create date range with specific number of periods
pd.date_range(start="2023-01-01", periods=10, freq="M")

# Create business days only (no weekends)
pd.bdate_range(start="2023-01-01", periods=10)
```

---

## PART 12: BINNING AND CATEGORIZING

```python
# Cut continuous variable into categories with custom bins
df["age_group"] = pd.cut(df["age"], bins=[0, 18, 35, 50, 100], labels=["child", "young", "middle", "old"])

# Cut into 5 equal-width bins (pandas decides boundaries)
df["age_group"] = pd.cut(df["age"], bins=5)

# Include lowest value in first bin
df["age_group"] = pd.cut(df["age"], bins=[0, 18, 35, 50, 100], labels=["child", "young", "middle", "old"], include_lowest=True)

# Right=False: bins are [0,18), [18,35), etc. instead of (0,18], (18,35]
df["age_group"] = pd.cut(df["age"], bins=[0, 18, 35, 50, 100], labels=["child", "young", "middle", "old"], right=False)

# Qcut: cut into equal-SIZE groups (same number of items per group)
df["income_quartile"] = pd.qcut(df["income"], q=4, labels=["Q1", "Q2", "Q3", "Q4"])

# Qcut without labels (shows actual ranges)
df["income_quartile"] = pd.qcut(df["income"], q=4)

# Qcut with custom percentile boundaries
df["income_quartile"] = pd.qcut(df["income"], q=[0, 0.25, 0.5, 0.75, 1], labels=["Q1", "Q2", "Q3", "Q4"])

# Qcut into 10 groups (deciles), return numbers 0-9
df["income_decile"] = pd.qcut(df["income"], q=10, labels=False)
```

---

## PART 13: DUPLICATES

```python
# Check which rows are duplicates (True/False)
df.duplicated()

# Count total duplicate rows
df.duplicated().sum()

# Get duplicate rows
df[df.duplicated()]

# Get ALL rows that have duplicates (including first occurrence)
df[df.duplicated(keep=False)]

# Check duplicates based on specific columns only
df[df.duplicated(subset=["col1", "col2"])]

# Mark duplicates keeping first occurrence as non-duplicate
df[df.duplicated(subset=["col1"], keep="first")]

# Mark duplicates keeping last occurrence as non-duplicate
df[df.duplicated(subset=["col1"], keep="last")]

# Remove duplicate rows
df.drop_duplicates()

# Remove duplicates based on one column
df.drop_duplicates(subset=["col1"])

# Remove duplicates based on multiple columns
df.drop_duplicates(subset=["col1", "col2"])

# Keep first occurrence, remove rest
df.drop_duplicates(keep="first")

# Keep last occurrence, remove rest
df.drop_duplicates(keep="last")

# Remove ALL duplicates (keep none)
df.drop_duplicates(keep=False)

# Remove duplicates in place
df.drop_duplicates(inplace=True)
```

---

## PART 14: APPLY AND MAP

```python
# Apply function to each value in column
df["col"].apply(lambda x: x * 2)

# Apply string method to each value
df["col"].apply(lambda x: x.upper())

# Apply built-in function
df["col"].apply(len)

# Apply method directly
df["col"].apply(str.upper)

# Apply with conditional logic
df["col"].apply(lambda x: x if x > 0 else 0)

# Apply function to each ROW (axis=1)
df.apply(lambda row: row["a"] + row["b"], axis=1)

# Get max of each row
df.apply(lambda row: row.max(), axis=1)

# Apply function to each COLUMN (axis=0, default)
df.apply(lambda col: col.max() - col.min())

# Get mean of each column
df.apply(lambda col: col.mean(), axis=0)

# Apply pandas function to all columns
df.apply(pd.to_numeric, errors="coerce")

# Map: replace values using dictionary
df["col"].map({"old1": "new1", "old2": "new2"})

# Map: apply function to each value
df["col"].map(lambda x: x * 2)

# Map: apply method
df["col"].map(str.upper)

# Applymap: apply function to EVERY cell in DataFrame
df.applymap(lambda x: f"${x:.2f}")

# Applymap: convert all cells to uppercase
df.applymap(str.upper)

# Applymap: get length of each cell
df.applymap(lambda x: len(str(x)))

# Pipe: chain operations on DataFrame
df.pipe(lambda df: df[df["col"] > 0])

# Pipe: chain multiple operations
df.pipe(lambda df: df.dropna()).pipe(lambda df: df.sort_values("col"))
```

---

## PART 15: WINDOW FUNCTIONS

```python
# Rolling mean: average of last 7 values
df["rolling_mean"] = df["col"].rolling(window=7).mean()

# Rolling sum: sum of last 7 values
df["rolling_sum"] = df["col"].rolling(window=7).sum()

# Rolling minimum
df["rolling_min"] = df["col"].rolling(window=7).min()

# Rolling maximum
df["rolling_max"] = df["col"].rolling(window=7).max()

# Rolling standard deviation
df["rolling_std"] = df["col"].rolling(window=7).std()

# Rolling variance
df["rolling_var"] = df["col"].rolling(window=7).var()

# Rolling median
df["rolling_median"] = df["col"].rolling(window=7).median()

# Rolling count of non-null values
df["rolling_count"] = df["col"].rolling(window=7).count()

# Rolling with minimum 1 period (don't require full window)
df["rolling_mean"] = df["col"].rolling(window=7, min_periods=1).mean()

# Rolling centered (window centered on current row)
df["rolling_mean"] = df["col"].rolling(window=7, center=True).mean()

# Exponential weighted mean (recent values weighted more)
df["ewm_mean"] = df["col"].ewm(span=7).mean()

# EWM with alpha parameter
df["ewm_mean"] = df["col"].ewm(alpha=0.5).mean()

# Cumulative sum (running total)
df["cumsum"] = df["col"].cumsum()

# Cumulative maximum (running max)
df["cummax"] = df["col"].cummax()

# Cumulative minimum (running min)
df["cummin"] = df["col"].cummin()

# Cumulative product
df["cumprod"] = df["col"].cumprod()

# Expanding mean: mean of all values up to current row
df["expanding_mean"] = df["col"].expanding().mean()

# Expanding sum
df["expanding_sum"] = df["col"].expanding().sum()

# Expanding max
df["expanding_max"] = df["col"].expanding().max()

# Expanding min
df["expanding_min"] = df["col"].expanding().min()

# Shift: get previous row's value
df["previous"] = df["col"].shift(1)

# Shift by 2 rows
df["previous_2"] = df["col"].shift(2)

# Shift negative: get next row's value
df["next"] = df["col"].shift(-1)

# Calculate change from previous row
df["change"] = df["col"] - df["col"].shift(1)

# Percentage change from previous row
df["pct_change"] = df["col"].pct_change()

# Percentage change from 3 rows ago
df["pct_change_3"] = df["col"].pct_change(periods=3)

# Difference from previous row
df["diff"] = df["col"].diff()

# Difference from 2 rows ago
df["diff_2"] = df["col"].diff(periods=2)

# Rank values (1 = smallest)
df["rank"] = df["col"].rank()

# Rank descending (1 = largest)
df["rank"] = df["col"].rank(ascending=False)

# Rank with ties: min (all ties get lowest rank)
df["rank"] = df["col"].rank(method="min")

# Rank with ties: max (all ties get highest rank)
df["rank"] = df["col"].rank(method="max")

# Rank with ties: first (first occurrence gets lower rank)
df["rank"] = df["col"].rank(method="first")

# Rank with ties: dense (like min but no gaps)
df["rank"] = df["col"].rank(method="dense")

# Rank as percentile (0 to 1)
df["rank"] = df["col"].rank(pct=True)

# Rank within each group
df["group_rank"] = df.groupby("category")["col"].rank()

# Cumulative sum within each group
df["group_cumsum"] = df.groupby("category")["col"].cumsum()

# Percentage change within each group
df["group_pct_change"] = df.groupby("category")["col"].pct_change()

# Shift within each group
df["group_shift"] = df.groupby("category")["col"].shift(1)

# Rolling mean within each group
df["group_rolling"] = df.groupby("category")["col"].rolling(3).mean().reset_index(level=0, drop=True)
```

---

## PART 16: INDEX OPERATIONS

```python
# Set a column as the index
df.set_index("col", inplace=True)

# Set multiple columns as MultiIndex
df.set_index(["col1", "col2"], inplace=True)

# Reset index back to 0, 1, 2... (old index becomes column)
df.reset_index(inplace=True)

# Reset index and drop old index
df.reset_index(drop=True, inplace=True)

# Reindex with specific values
df.reindex([0, 1, 2, 3, 4])

# Reindex columns
df.reindex(columns=["col1", "col2", "col3"])

# Reindex to match another DataFrame
df.reindex_like(other_df)

# Get the index
df.index

# Name the index
df.index.name = "my_index"

# Get index as list
df.index.tolist()

# Get index values as array
df.index.values

# Rename the index axis
df.rename_axis("my_index")

# Rename the columns axis
df.rename_axis("my_columns", axis=1)
```

---

## PART 17: CORRELATION AND COVARIANCE

```python
# Correlation matrix of all numeric columns
df.corr()

# Pearson correlation (default, linear relationship)
df.corr(method="pearson")

# Spearman correlation (rank-based, monotonic relationship)
df.corr(method="spearman")

# Kendall correlation (rank-based, good for small samples)
df.corr(method="kendall")

# Correlation between two specific columns
df["col1"].corr(df["col2"])

# Correlation with target, sorted by strength
df.corr()["target"].sort_values(ascending=False)

# Correlation of all columns with one column
df.corrwith(df["target"])

# Covariance matrix
df.cov()

# Covariance between two columns
df["col1"].cov(df["col2"])
```

---

## PART 18: CROSSTAB AND VALUE COUNTS

```python
# Cross tabulation: count combinations of two columns
pd.crosstab(df["col1"], df["col2"])

# Crosstab as percentages (of total)
pd.crosstab(df["col1"], df["col2"], normalize=True)

# Crosstab as percentages (of each row)
pd.crosstab(df["col1"], df["col2"], normalize="index")

# Crosstab as percentages (of each column)
pd.crosstab(df["col1"], df["col2"], normalize="columns")

# Crosstab with row/column totals
pd.crosstab(df["col1"], df["col2"], margins=True)

# Crosstab with aggregation function
pd.crosstab(df["col1"], df["col2"], values=df["col3"], aggfunc="mean")

# Crosstab with multiple row variables
pd.crosstab([df["col1"], df["col2"]], df["col3"])
```

---

## PART 19: ADVANCED OPERATIONS

```python
# Explode: convert list column into separate rows
df.explode("col")

# Explode with fresh index
df.explode("col", ignore_index=True)

# Assign: create new columns in chain
df.assign(new_col=lambda x: x["col1"] + x["col2"])

# Assign multiple columns
df.assign(new_col1=lambda x: x["a"] * 2, new_col2=lambda x: x["b"] * 3)

# Eval: create column using string expression
df.eval("new_col = col1 + col2")

# Eval in place
df.eval("new_col = col1 + col2", inplace=True)

# Where: keep values where condition is True, else replace
df.where(df > 0, 0)

# Where with custom replacement
df.where(df > 0, other=-1)

# Mask: opposite of where (replace where condition is True)
df.mask(df < 0, 0)

# Clip: limit values to range
df["col"].clip(lower=0, upper=100)

# Select only numeric columns
df.select_dtypes(include=["number"])

# Select only text columns
df.select_dtypes(include=["object"])

# Select only datetime columns
df.select_dtypes(include=["datetime"])

# Exclude text columns
df.select_dtypes(exclude=["object"])

# Random sample: 10 rows
df.sample(n=10)

# Random sample: 10% of rows
df.sample(frac=0.1)

# Random sample with seed (reproducible)
df.sample(n=10, random_state=42)

# Random sample with replacement
df.sample(n=10, replace=True)

# Random sample with weights (probability)
df.sample(n=10, weights="col")

# Get 10 largest values
df.nlargest(10, "col")

# Get 10 smallest values
df.nsmallest(10, "col")

# Get index of maximum value in each column
df.idxmax()

# Get index of minimum value in each column
df.idxmin()

# Get index of maximum value in one column
df["col"].idxmax()

# Get index of minimum value in one column
df["col"].idxmin()

# Filter by time range (requires datetime index)
df.between_time("09:00", "17:00")

# Filter by specific time
df.at_time("12:00")

# Get first 3 days (requires datetime index)
df.first("3D")

# Get last 3 days
df.last("3D")

# Truncate by date range
df.truncate(before="2023-01-01", after="2023-12-31")
```

---

## PART 20: MEMORY AND PERFORMANCE

```python
# Get memory usage per column
df.memory_usage()

# Get accurate memory usage (including string content)
df.memory_usage(deep=True)

# Get total memory in MB
df.memory_usage(deep=True).sum() / 1024**2

# Convert to category (saves memory for columns with repeated values)
df["col"] = df["col"].astype("category")

# Use smaller integer type
df["col"] = df["col"].astype("int32")

# Use smaller float type
df["col"] = df["col"].astype("float32")

# Use smallest integer type
df["col"] = df["col"].astype("int8")

# Automatically downcast to smallest integer type
df["col"] = pd.to_numeric(df["col"], downcast="integer")

# Automatically downcast to smallest float type
df["col"] = pd.to_numeric(df["col"], downcast="float")

# Make a copy of DataFrame
df.copy()

# Deep copy (copy everything including data)
df.copy(deep=True)

# Shallow copy (copy structure, share data)
df.copy(deep=False)
```

---

## PART 21: MULTIINDEX (HIERARCHICAL INDEX)

```python
# Create MultiIndex from columns
df.set_index(["col1", "col2"], inplace=True)

# Get names of index levels
df.index.names

# Get unique values at each level
df.index.levels

# Get values at first level
df.index.get_level_values(0)

# Get values at second level
df.index.get_level_values(1)

# Select by first level value
df.loc["value1"]

# Select by both level values
df.loc[("value1", "value2")]

# Select range of first level values
df.loc["value1":"value3"]

# Cross-section: select by one level, keep other levels
df.xs("value1", level="col1")

# Cross-section at second level
df.xs("value2", level="col2")

# Cross-section with multiple values
df.xs(("value1", "value2"))

# Reset one level of index
df.reset_index(level="col1")

# Reset first level of index
df.reset_index(level=0)

# Swap index levels
df.swaplevel()

# Swap specific levels
df.swaplevel(0, 1)

# Sort by first index level
df.sort_index(level=0)

# Sort by multiple index levels
df.sort_index(level=[0, 1])

# Group by first index level
df.groupby(level=0).mean()

# Group by multiple index levels
df.groupby(level=[0, 1]).sum()

# Unstack first level (rows → columns)
df.unstack(level=0)

# Unstack second level
df.unstack(level=1)

# Stack (columns → rows)
df.stack(level=0)

# Create MultiIndex from tuples
pd.MultiIndex.from_tuples([("a", 1), ("a", 2), ("b", 1)])

# Create MultiIndex from cartesian product
pd.MultiIndex.from_product([["a", "b"], [1, 2, 3]])

# Create MultiIndex from arrays
pd.MultiIndex.from_arrays([["a", "a", "b"], [1, 2, 1]])
```