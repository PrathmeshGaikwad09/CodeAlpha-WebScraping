# CodeAlpha Data Analytics Internship - Task 3
# Data Visualization

## Project Overview

This project was developed as part of the CodeAlpha Data Analytics Internship.

Task 3 focuses on transforming the cleaned web-scraped quote dataset into meaningful visualizations. The project uses Python, Pandas, and Matplotlib to analyze quote authors, tags, quote length, word count, and tag distribution.

The visualizations help identify important patterns and trends in the dataset and make the analysis easier to understand.

---

## Objective

The main objectives of Task 3 are:

- Transform analyzed data into meaningful visualizations.
- Create clear and easy-to-understand charts.
- Visualize author-wise quote distribution.
- Visualize the most frequent tags.
- Analyze quote length and word count.
- Analyze the number of tags associated with each quote.
- Compare average quote length across authors.
- Generate data-driven insights from the visualizations.
- Save the generated charts in PNG format.

---

## Dataset

The dataset used for this task is the cleaned dataset generated during the previous tasks.

### Dataset File

`data/cleaned_scraped_data.csv`

### Dataset Details

- Total Quotes: 100
- Total Authors: 50
- Number of Columns: 3

### Columns

| Column | Description |
|---|---|
| Quote | Text of the quote |
| Author | Author of the quote |
| Tags | Tags associated with the quote |

---

## Technologies Used

- Python
- Pandas
- Matplotlib
- CSV

---

## Data Visualization Process

The visualization process follows these steps:

1. Load the cleaned dataset using Pandas.
2. Analyze authors and their quote counts.
3. Analyze the frequency of tags.
4. Calculate quote length.
5. Calculate word count for each quote.
6. Calculate the number of tags per quote.
7. Calculate average quote length by author.
8. Create charts using Matplotlib.
9. Save all visualizations in the `charts` folder.
10. Analyze the results and generate key insights.

---

# Visualizations Created

## 1. Top 10 Authors by Number of Quotes

This horizontal bar chart shows the top 10 authors based on the number of quotes available in the dataset.

Output:

`charts/01_top_10_authors.png`

### Key Finding

Albert Einstein has the highest number of quotes in the dataset with 10 quotes.

---

## 2. Top 10 Tags by Frequency

This chart shows the 10 most frequently occurring tags in the dataset.

Output:

`charts/02_top_10_tags.png`

### Key Finding

The `love` tag is the most frequently occurring tag with 14 occurrences.

Other highly frequent tags include:

- Life
- Inspirational
- Humor
- Books

---

## 3. Quote Length Distribution

This visualization shows the distribution of quote lengths in the dataset.

Output:

`charts/03_quote_length_distribution.png`

### Purpose

The chart helps understand how short or long the quotes are and shows the overall distribution of quote lengths.

---

## 4. Word Count Distribution

This visualization shows the distribution of the number of words in each quote.

Output:

`charts/04_word_count_distribution.png`

### Key Finding

The average quote contains approximately 23.63 words.

---

## 5. Tags per Quote

This chart visualizes the number of tags associated with each quote.

Output:

`charts/05_tags_per_quote.png`

### Key Finding

Each quote has an average of approximately 2.32 tags.

---

## 6. Average Quote Length by Author

This visualization compares the average number of words in quotes written by different authors.

Output:

`charts/06_average_quote_length_by_author.png`

### Purpose

This chart helps compare writing length across authors and identify authors whose quotes are relatively shorter or longer on average.

---

# Key Insights

The visualization and analysis produced the following insights:

1. Albert Einstein has the highest number of quotes in the dataset with 10 quotes.

2. `love` is the most frequently occurring tag with 14 occurrences.

3. The dataset contains 100 quotes from 50 unique authors.

4. The average quote contains approximately 23.63 words.

5. Each quote has an average of approximately 2.32 tags.

6. The dataset contains a variety of themes represented through tags such as love, life, inspirational, humor, books, reading, friendship, truth, friends, and simile.

---

# Insights Script

The `insights.py` script was created to calculate and display important findings from the dataset.

The script calculates:

- Total number of quotes
- Total number of authors
- Top 10 authors
- Top 10 tags
- Average quote length
- Shortest quote length
- Longest quote length
- Average words per quote
- Average tags per quote

### Run the Insights Script

```bash
python insights.py