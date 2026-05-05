# 1. SOW — Statement of Work

## Project Overview

This project analyzes a Netflix content dataset to understand content distribution, missing data quality, release trends, country representation, and catalog growth over time. The goal is to perform exploratory data analysis using Python, Pandas, and visualization tools to identify meaningful insights that could support content strategy and business decision-making.

## Business Objective

The main objective is to answer the following questions:

1. What types of content are most common: Movies or TV Shows?
2. Which years had the highest number of titles added to the platform?
3. Which countries contribute the most content?
4. Are there missing or inconsistent values in key columns such as `director`, `country`, and `date_added`?
5. What patterns can be found in content release year, date added, rating, and duration?

## Scope of Work

The project includes:

```text
1. Data loading and initial inspection
2. Data cleaning and standardization
3. Missing value analysis
4. Date conversion and feature engineering
5. Descriptive statistics
6. Grouping and aggregation
7. Data visualization
8. Insight generation
9. Final summary and business recommendations
```

## Dataset Columns

Expected columns may include:

```text
show_id
type
title
director
cast
country
date_added
release_year
rating
duration
listed_in
description
```

## Tools Used

```text
Python
Pandas
NumPy
Matplotlib
VS Code
Jupyter Notebook optional
```

## Deliverables

Final deliverables include:

```text
1. Cleaned dataset
2. Python EDA notebook or script
3. Summary of missing values
4. Visual charts
5. Key findings
6. Business recommendations
7. GitHub-ready project README
```

## Assumptions

Some fields such as `director`, `country`, and `date_added` may contain missing or inconsistent values. These values will be cleaned and handled based on their importance to the analysis.

## Out of Scope

This project does not include machine learning prediction, recommendation systems, or advanced statistical modeling. The focus is on exploratory data analysis and business insight generation.

---