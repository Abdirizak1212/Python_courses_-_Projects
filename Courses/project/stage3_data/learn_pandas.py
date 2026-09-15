import pandas as pd
import numpy as np

# ── LESSON 1: Load your dataset ──────────────────────────────
df = pd.read_csv("simad_qa.csv")

print("=== DATASET LOADED ===")
print(df.head())           # first 5 rows
print("\nShape:", df.shape) # rows, columns

# ── LESSON 2: Explore the data ───────────────────────────────
print("\n=== COLUMN NAMES ===")
print(df.columns.tolist())

print("\n=== DATA TYPES ===")
print(df.dtypes)

print("\n=== BASIC INFO ===")
print(df.info())

# ── LESSON 3: Filter rows ────────────────────────────────────
print("\n=== ONLY 'courses' CATEGORY ===")
courses = df[df["category"] == "courses"]
print(courses[["question_somali", "answer_somali"]])

# ── LESSON 4: Count by category ──────────────────────────────
print("\n=== HOW MANY ROWS PER CATEGORY ===")
print(df["category"].value_counts())

# ── LESSON 5: Add a new column ───────────────────────────────
df["answer_length"] = df["answer_somali"].str.len()
print("\n=== WITH ANSWER LENGTH COLUMN ===")
print(df[["question_somali", "answer_length"]])

# ── LESSON 6: Sort by answer length ──────────────────────────
print("\n=== SORTED BY ANSWER LENGTH ===")
print(df.sort_values("answer_length", ascending=False)[["question_somali", "answer_length"]])

# ── LESSON 7: NumPy on a column ──────────────────────────────
lengths = np.array(df["answer_length"])
print("\n=== ANSWER LENGTH STATS ===")
print("Average:", lengths.mean())
print("Longest:", lengths.max())
print("Shortest:", lengths.min())

# ── LESSON 8: Save a filtered result ─────────────────────────
general = df[df["category"] == "general"]
general.to_csv("simad_general_only.csv", index=False)
print("\n✅ Saved simad_general_only.csv")