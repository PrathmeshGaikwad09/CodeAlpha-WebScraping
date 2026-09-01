import pandas as pd
import matplotlib.pyplot as plt
import os

# Load quote dataset
df = pd.read_csv("data/quotes_data.csv")

# Create charts folder
os.makedirs("charts", exist_ok=True)

# Clean data
df["Quote"] = df["Quote"].fillna("")
df["Author"] = df["Author"].fillna("Unknown")
df["Tags"] = df["Tags"].fillna("")

# --------------------------------------------------
# 1. Top 10 Authors
# --------------------------------------------------

author_counts = df["Author"].value_counts().head(10)

plt.figure(figsize=(10, 6))
author_counts.sort_values().plot(kind="barh")

plt.title("Top 10 Authors by Number of Quotes")
plt.xlabel("Number of Quotes")
plt.ylabel("Author")
plt.tight_layout()

plt.savefig("charts/01_top_10_authors.png")
plt.close()


# --------------------------------------------------
# 2. Top 10 Tags
# --------------------------------------------------

tags = (
    df["Tags"]
    .str.split(",")
    .explode()
    .str.strip()
)

tag_counts = tags.value_counts().head(10)

plt.figure(figsize=(10, 6))
tag_counts.sort_values().plot(kind="barh")

plt.title("Top 10 Tags")
plt.xlabel("Number of Quotes")
plt.ylabel("Tag")
plt.tight_layout()

plt.savefig("charts/02_top_10_tags.png")
plt.close()


# --------------------------------------------------
# 3. Quote Length Distribution
# --------------------------------------------------

df["Quote_Length"] = df["Quote"].str.len()

plt.figure(figsize=(10, 6))
plt.hist(df["Quote_Length"], bins=20, edgecolor="black")

plt.title("Quote Length Distribution")
plt.xlabel("Quote Length (Characters)")
plt.ylabel("Number of Quotes")
plt.tight_layout()

plt.savefig("charts/03_quote_length_distribution.png")
plt.close()


# --------------------------------------------------
# 4. Word Count Distribution
# --------------------------------------------------

df["Word_Count"] = df["Quote"].str.split().str.len()

plt.figure(figsize=(10, 6))
plt.hist(df["Word_Count"], bins=15, edgecolor="black")

plt.title("Word Count Distribution")
plt.xlabel("Number of Words")
plt.ylabel("Number of Quotes")
plt.tight_layout()

plt.savefig("charts/04_word_count_distribution.png")
plt.close()


# --------------------------------------------------
# 5. Tags Per Quote
# --------------------------------------------------

df["Tags_Per_Quote"] = (
    df["Tags"]
    .apply(lambda x: len([tag for tag in x.split(",") if tag.strip()]))
)

plt.figure(figsize=(10, 6))
df["Tags_Per_Quote"].value_counts().sort_index().plot(kind="bar")

plt.title("Number of Tags per Quote")
plt.xlabel("Number of Tags")
plt.ylabel("Number of Quotes")
plt.tight_layout()

plt.savefig("charts/05_tags_per_quote.png")
plt.close()


# --------------------------------------------------
# 6. Average Quote Length by Author
# --------------------------------------------------

avg_quote_length = (
    df.groupby("Author")["Quote_Length"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10, 6))
avg_quote_length.sort_values().plot(kind="barh")

plt.title("Average Quote Length by Author")
plt.xlabel("Average Quote Length (Characters)")
plt.ylabel("Author")
plt.tight_layout()

plt.savefig("charts/06_average_quote_length_by_author.png")
plt.close()


print("TASK 3 COMPLETED SUCCESSFULLY!")
print("6 visualizations created:")
print("1. Top 10 Authors")
print("2. Top 10 Tags")
print("3. Quote Length Distribution")
print("4. Word Count Distribution")
print("5. Tags per Quote")
print("6. Average Quote Length by Author")
print("Charts saved inside the 'charts' folder.")
