# ==============================
# CRIME DATA CLEANING SCRIPT
# ==============================

import pandas as pd
import numpy as np

# --- Step 1: Load the dataset ---
df = pd.read_csv("crime_data.csv")

# --- Step 2: Clean column names ---
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# --- Step 3: Handle missing and duplicate values ---
df.drop_duplicates(inplace=True)

# Fill missing categories or types
if "category" in df.columns:
    df["category"] = np.where(df["category"].isna(), "Unknown", df["category"])

# Fill missing descriptions
if "description" in df.columns:
    df["description"] = np.where(df["description"].isna(), "No Description", df["description"])

# --- Step 4: Convert date/time fields and extract new columns ---
# Find the column that contains date/time info
date_cols = [col for col in df.columns if "date" in col or "time" in col]
if date_cols:
    df["date"] = pd.to_datetime(df[date_cols[0]], errors="coerce")
    df["year"] = df["date"].dt.year
    df["month"] = df["date"].dt.month
    df["weekday"] = df["date"].dt.day_name()
    df["hour"] = df["date"].dt.hour

# --- Step 5: Handle invalid or missing location data ---
if "latitude" in df.columns and "longitude" in df.columns:
    df = df[(df["latitude"].between(-90, 90)) & (df["longitude"].between(-180, 180))]

# --- Step 6: Save cleaned data ---
df.to_csv("cleaned_crime_data.csv", index=False)

print("✅ Crime data cleaned successfully!")
print("📁 Saved as: cleaned_crime_data.csv")
print(f"Total Records after cleaning: {len(df)}")
print(f"Columns: {list(df.columns)}")
