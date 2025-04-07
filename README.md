# Olympic Medal Count.
Medal Counts by Country.

This repository contains a Python script that calculates and displays Olympic medal counts by country. The script also saves the results to a CSV file.

## Dataset

The dataset includes the following columns:

- **Country**: The name of the country.
- **Gold**: The number of gold medals won.
- **Silver**: The number of silver medals won.
- **Bronze**: The number of bronze medals won.
- **Total**: The total number of medals (calculated).

### Example Data:

| Country | Gold | Silver | Bronze | Total |
|--------|------|-------|--------|-------|
| USA    | 39   | 41    | 33     | 113   |
| China  | 38   | 32    | 18     | 88    |
| Japan  | 27   | 14    | 17     | 58    |
| Germany| 10   | 11    | 16     | 37    |
| Russia | 20   | 28    | 23     | 71    |

## Python Script

The script `olympic_medal_count.py` performs the following tasks:

1. Loads a sample dataset of Olympic medal counts.
2. Calculates the total number of medals for each country.
3. Displays the sorted medal count in descending order.
4. Saves the final data to a CSV file named `olympic_medal_count.csv`.

## Requirements

- Python 3.x
- pandas library

To install the pandas library, use:
```bash
pip install pandas
