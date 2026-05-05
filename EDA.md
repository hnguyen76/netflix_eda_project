
#### EDA — Exploratory Data Analysis

## Step 1: Import Libraries

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```

---

## Step 2: Load Dataset

```python
df = pd.read_csv("netflix_titles.csv")
```

Check first few rows:

```python
df.head()
```

Check dataset shape:

```python
df.shape
```

This shows how many rows and columns are in the dataset.

---

## Step 3: Standardize Column Names

Convert all column names to lowercase and replace spaces with underscores.

```python
df.columns = df.columns.str.lower().str.replace(" ", "_")
```

Check column names:

```python
df.columns
```

This makes the dataset easier to work with.

Example:

```text
Date Added → date_added
Release Year → release_year
Adj Close → adj_close
```

---

## Step 4: Check Data Types

```python
df.dtypes
```

Or:

```python
df.info()
```

This helps identify whether columns are stored correctly.

For example:

```text
date_added should be datetime
release_year should be numeric
title should be object/string
```

---

## Step 5: Check Missing Values

```python
df.isna().sum()
```

To see missing value percentage:

```python
missing_percent = df.isna().mean() * 100
missing_percent.sort_values(ascending=False)
```

Based on your earlier result:

```text
title       1
director    2588
country     287
```

Interpretation:

```text
title has only 1 missing value, so dropping that row is reasonable.
director has many missing values, so replacing with "Unknown" is better than dropping.
country has some missing values, so it can be replaced with "Unknown" or handled separately.
```

---

## Step 6: Replace Bad Values with NaN

Some missing values may appear as text such as `"unknown"`, `"n/a"`, `"missing"`, or `"-"`.

```python
bad_values = [
    "not given", "unknown", "n/a", "na", "none",
    "null", "missing", "-", "--", "?"
]

for col in df.select_dtypes(include=["object", "string"]).columns:
    temp = df[col].astype(str).str.strip()
    mask = temp.str.lower().isin(bad_values)
    df.loc[mask, col] = np.nan
```

Then check again:

```python
df.isna().sum().sort_values(ascending=False)
```

---

## Step 7: Handle Missing Values

```python
df = df.dropna(subset=["title"])

df["director"] = df["director"].fillna("Unknown")
df["country"] = df["country"].fillna("Unknown")
```

Explanation:

```text
title is critical, so missing title rows should be removed.
director has many missing values, so replacing with "Unknown" avoids losing too much data.
country can also be filled with "Unknown" to preserve rows.
```

---

## Step 8: Convert Date Column

```python
df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")
```

This converts `date_added` from text into real datetime format.

Then create new date features:

```python
df["year_added"] = df["date_added"].dt.year
df["month_added"] = df["date_added"].dt.month
df["month_name_added"] = df["date_added"].dt.month_name()
```

These new columns help analyze content added by year and month.

---

# 3. Key EDA Questions

## Question 1: How many Movies vs TV Shows?

```python
content_type_counts = df["type"].value_counts()
print(content_type_counts)
```

Visualization:

```python
content_type_counts.plot(kind="bar")
plt.title("Count of Movies vs TV Shows")
plt.xlabel("Content Type")
plt.ylabel("Number of Titles")
plt.show()
```

Business insight example:

```text
If Movies make up the majority of the catalog, Netflix may have historically focused more on movie acquisition. If TV Shows are increasing over time, this may suggest a strategic shift toward serialized content.
```

---

## Question 2: Which years had the most titles added?

```python
titles_by_year = df.groupby("year_added").size().sort_values(ascending=False)
print(titles_by_year)
```

For chronological order:

```python
titles_by_year_sorted = df.groupby("year_added").size().sort_index()
print(titles_by_year_sorted)
```

Visualization:

```python
titles_by_year_sorted.plot(kind="line")
plt.title("Number of Titles Added by Year")
plt.xlabel("Year Added")
plt.ylabel("Number of Titles")
plt.show()
```

Business insight example:

```text
A strong increase in titles added over time may indicate platform expansion. A decline in recent years may suggest content strategy changes, licensing reductions, or incomplete recent-year data.
```

---

## Question 3: Which countries have the most content?

```python
top_countries = df["country"].value_counts().head(10)
print(top_countries)
```

Visualization:

```python
top_countries.plot(kind="bar")
plt.title("Top 10 Countries by Number of Titles")
plt.xlabel("Country")
plt.ylabel("Number of Titles")
plt.show()
```

Business insight example:

```text
The United States is likely one of the largest content contributors. Other countries with high content counts may reflect Netflix's international expansion and regional content strategy.
```

---

## Question 4: Which directors have the most titles?

```python
top_directors = df[df["director"] != "Unknown"]["director"].value_counts().head(10)
print(top_directors)
```

Visualization:

```python
top_directors.plot(kind="bar")
plt.title("Top 10 Directors by Number of Titles")
plt.xlabel("Director")
plt.ylabel("Number of Titles")
plt.show()
```

Important note:

```text
Because many director values are missing, director-based analysis should be interpreted carefully.
```

---

## Question 5: What ratings are most common?

```python
rating_counts = df["rating"].value_counts()
print(rating_counts)
```

Visualization:

```python
rating_counts.plot(kind="bar")
plt.title("Content Count by Rating")
plt.xlabel("Rating")
plt.ylabel("Number of Titles")
plt.show()
```

Business insight example:

```text
Rating distribution helps understand the target audience. A high number of TV-MA or PG-13 titles may suggest a focus on mature or general audience content.
```

---

# 4. Sample Findings

Based on the cleaning and EDA approach, possible findings may include:

```text
1. The dataset contains both Movies and TV Shows, with Movies likely representing the larger share.
2. The director column has a high number of missing values, so director analysis should be treated carefully.
3. Country data has some missing values but is still useful for geographic content analysis.
4. The date_added column needs to be converted into datetime format before time-based analysis.
5. Content added by year can reveal Netflix catalog growth trends.
6. Top countries and ratings can help identify content focus and audience targeting.
```

---

# 5. Business Recommendations

## Recommendation 1: Improve Data Quality

Netflix or the data provider should improve completeness for fields like:

```text
director
country
date_added
rating
duration
```

Missing values reduce the reliability of analysis.

## Recommendation 2: Track Content Growth by Year

The company should monitor how many titles are added each year to understand whether catalog growth is increasing, slowing, or shifting by content type.

## Recommendation 3: Separate Movie and TV Show Analysis

Movies and TV Shows should be analyzed separately because their duration, production patterns, and audience behavior are different.

Example:

```python
movies = df[df["type"] == "Movie"]
tv_shows = df[df["type"] == "TV Show"]
```

## Recommendation 4: Use Country Analysis for Regional Strategy

Country-level content analysis can help identify which regions are underrepresented and where Netflix may need more local content.

## Recommendation 5: Be Careful with Director Analysis

Because `director` has many missing values, any conclusion about top directors should mention this limitation.

---

# 6. Final Project Summary

This project used Python and Pandas to perform exploratory data analysis on a Netflix content dataset. The analysis included data cleaning, missing value handling, date conversion, grouping, aggregation, and visualization.

The dataset showed important patterns in content type, year added, country distribution, ratings, and director availability. Several data quality issues were identified, especially in the `director` and `country` columns. These issues were handled by converting invalid values to missing values and replacing selected missing values with `"Unknown"` where appropriate.

Overall, this EDA provides a foundation for understanding Netflix catalog composition and can support further analysis related to content strategy, regional expansion, and audience targeting.

This analysis demonstrates the importance of data cleaning before generating insights. Missing values, inconsistent formats, and date conversion issues can significantly affect the accuracy of business conclusions. After cleaning the dataset, the analysis provides a clearer view of Netflix's content catalog, growth trends, and content distribution across countries, ratings, and content types.
---



