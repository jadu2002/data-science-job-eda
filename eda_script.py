import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Load the dataset
file_path = "Glassdoor_Salary_Cleaned_Version.csv"  # Change if necessary
df = pd.read_csv(file_path)

# Display basic info
print("Dataset Overview:")
print(df.info())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Display first few rows
print("\nSample Data:")
print(df.head())

# Salary Distribution
plt.figure(figsize=(8, 5))
sns.histplot(df["Salary"], bins=30, kde=True)
plt.title("Salary Distribution of Data Science Jobs")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.show()

# Top Job Titles
plt.figure(figsize=(10, 5))
df["Job Title"].value_counts().head(10).plot(kind="bar", color="skyblue")
plt.title("Top 10 Most Common Job Titles")
plt.xlabel("Job Title")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()

# Top Locations
plt.figure(figsize=(10, 5))
df["Location"].value_counts().head(10).plot(kind="bar", color="lightcoral")
plt.title("Top 10 Locations for Data Science Jobs")
plt.xlabel("Location")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()

# Generate WordCloud for job descriptions or skills
text = " ".join(str(desc) for desc in df["Job Description"].dropna())
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("Most Common Words in Job Descriptions")
plt.show()

print("\nEDA Completed Successfully!")
