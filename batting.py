import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv('./all_season_batting_card.csv')

# Inspect the dataset
print("First 5 rows:")
print(df.head())

print("\nColumns:")
print(df.columns)

print("\nDataset information:")
df.info()

print("\nSecond row:")
print(df.iloc[1])

print("\nRow with index 1:")
print(df.loc[1])

# Check missing values
print("\nMissing values before cleaning:")
print(df.isnull().sum())

# Drop unnecessary columns
df = df.drop(
    columns=['link', 'commentary', 'runningOver', 'minutes'],
    errors='ignore'
)

# Check missing values again
print("\nMissing values after dropping columns:")
print(df.isnull().sum())

# Convert Boolean columns safely
df["captain"] = df["captain"].map({
    True: True, False: False,
    1: True, 0: False,
    "True": True, "False": False
})

df["isNotOut"] = df["isNotOut"].map({
    True: True, False: False,
    1: True, 0: False,
    "True": True, "False": False
})

# Remove duplicate rows
df = df.drop_duplicates()

# Handle missing values in selected columns
cols = ['runs', 'ballsFaced', 'strikeRate', 'fours', 'sixes']

# Display missing-value counts before filling
print("\nMissing values in selected columns:")
print(df[cols].isnull().sum())

# Replace missing values with 0 (if appropriate for your data)
df[cols] = df[cols].fillna(0)

# Verify cleaning
print("\nMissing values after cleaning:")
print(df.isnull().sum())

print("\nCleaned dataset:")
print(df.head())

# Save cleaned dataset
df.to_csv("clean_data.csv", index=False)

print("\nCleaned data saved to clean_data.csv")