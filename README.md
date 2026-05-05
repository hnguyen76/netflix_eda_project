# Netflix Content Catalog Analysis

## Project Overview
This project analyzes a Netflix content dataset to understand content distribution, missing values, release trends, country representation, and catalog growth over time.

## Business Questions
- What types of content are most common?
- Which years had the most titles added?
- Which countries contribute the most content?
- Which columns contain missing or inconsistent values?
- What patterns exist in rating, release year, and duration?

## Tools Used
- Python
- Pandas
- NumPy
- Matplotlib
- VS Code

## Data Cleaning Steps
- Standardized column names
- Replaced invalid text values with NaN
- Dropped rows with missing title
- Filled missing director and country values with "Unknown"
- Converted date_added to datetime format
- Created year_added and month_added columns

## Key Insights
- Movies and TV Shows should be analyzed separately.
- Director data contains many missing values.
- Country data is useful but contains some missing values.
- Date conversion is necessary for time-based analysis.
- Content growth can be analyzed by year_added.

## Recommendations
- Improve data completeness for director and country.
- Track catalog growth by year.
- Analyze Movies and TV Shows separately.
- Use country-level insights for regional content strategy.
- Interpret director analysis carefully due to missing values.
