# ==============================
# CRIME DATA VISUALIZATION SCRIPT
# ==============================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- Step 1: Load cleaned data ---
df = pd.read_csv("cleaned_crime_data.csv")

# --- Step 2: Setup plot aesthetics ---
sns.set(style="whitegrid", palette="deep")
plt.rcParams["figure.figsize"] = (10, 6)

# --- Step 3: Top 10 crime categories ---
if "category" in df.columns:
    top_crimes = df["category"].value_counts().nlargest(10)
    sns.barplot(x=top_crimes.values, y=top_crimes.index, palette="coolwarm")
    plt.title("Top 10 Crime Categories")
    plt.xlabel("Number of Crimes")
    plt.ylabel("Crime Type")
    plt.tight_layout()
    plt.show()

# --- Step 4: Crimes by Year ---
if "year" in df.columns:
    sns.countplot(x="year", data=df, palette="viridis")
    plt.title("Yearly Crime Count")
    plt.xlabel("Year")
    plt.ylabel("Number of Crimes")
    plt.tight_layout()
    plt.show()

# --- Step 5: Crimes by Day of Week ---
if "weekday" in df.columns:
    order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    sns.countplot(x="weekday", data=df, order=order, palette="pastel")
    plt.title("Crimes by Day of Week")
    plt.xlabel("Day")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()

# --- Step 6: Crimes by Hour ---
if "hour" in df.columns:
    sns.histplot(df["hour"].dropna(), bins=24, kde=True, color="purple")
    plt.title("Crimes by Hour of Day")
    plt.xlabel("Hour")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()

print("✅ Visualization complete!")
