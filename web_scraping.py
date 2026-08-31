import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = "https://quotes.toscrape.com/page/{}/"

quotes_data = []

for page in range(1, 11):

    url = base_url.format(page)

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    quotes = soup.find_all("div", class_="quote")

    print(f"Scraping page {page}...")

    for quote in quotes:

        text = quote.find("span", class_="text").text.strip()

        author = quote.find("small", class_="author").text.strip()

        tags = []

        for tag in quote.find_all("a", class_="tag"):
            tags.append(tag.text.strip())

        tags = ", ".join(tags)

        quotes_data.append({
            "Quote": text,
            "Author": author,
            "Tags": tags
        })


df = pd.DataFrame(quotes_data)

df.to_csv("scraped_data.csv", index=False)

print("\nData scraped successfully!")
print("Total records:", len(df))



print("\n--- Dataset Information ---")

print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("\nColumn Names:")
print(df.columns.tolist())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

df = df.drop_duplicates()

df["Quote"] = df["Quote"].str.strip()
df["Author"] = df["Author"].str.strip()
df["Tags"] = df["Tags"].str.strip()

df.to_csv("cleaned_scraped_data.csv", index=False)

print("\nCleaning completed successfully!")
print("Final records:", len(df))




print("\n--- BASIC DATA ANALYSIS ---")

total_quotes = len(df)

unique_authors = df["Author"].nunique()

print("Total Quotes:", total_quotes)
print("Unique Authors:", unique_authors)

author_counts = df["Author"].value_counts()

print("\n--- TOP AUTHORS ---")
print(author_counts.head(10))

author_counts_df = author_counts.reset_index()
author_counts_df.columns = ["Author", "Quote_Count"]

author_counts_df.to_csv("author_quote_counts.csv", index=False)

print("\nAuthor analysis saved successfully!")

print("\n--- TOP TAGS ---")

all_tags = []

for tags in df["Tags"]:
    for tag in tags.split(","):
        all_tags.append(tag.strip())

tag_counts = pd.Series(all_tags).value_counts()

print(tag_counts.head(10))

tag_counts_df = tag_counts.reset_index()
tag_counts_df.columns = ["Tag", "Count"]

tag_counts_df.to_csv("tag_counts.csv", index=False)

print("\nTag analysis saved successfully!")





import matplotlib


matplotlib.use("Agg")

import matplotlib.pyplot as plt



top_authors = author_counts.head(10)

plt.figure(figsize=(10, 6))

top_authors.sort_values().plot(kind="barh")

plt.title("Top 10 Authors by Number of Quotes")
plt.xlabel("Number of Quotes")
plt.ylabel("Author")

plt.tight_layout()

plt.savefig("top_10_authors.png", dpi=300)

plt.close()



top_tags = tag_counts.head(10)

plt.figure(figsize=(10, 6))

top_tags.sort_values().plot(kind="barh")

plt.title("Top 10 Tags by Frequency")
plt.xlabel("Frequency")
plt.ylabel("Tag")

plt.tight_layout()

plt.savefig("top_10_tags.png", dpi=300)

plt.close()


print("\nCharts created successfully!")
