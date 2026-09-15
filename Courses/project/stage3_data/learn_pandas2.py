import pandas as pd
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

df = pd.read_csv("simad_qa.csv")

# ── LESSON 1: Check for missing values ───────────────────────
print("=== MISSING VALUES ===")
print(df.isnull().sum())  # count nulls in each column

# ── LESSON 2: Add a row with missing data (simulate real world)
new_row = {"id": 11, "category": "general", 
           "question_somali": "Imisa arday ayaa SIMAD leh?",
           "answer_somali": None,   # ← missing answer
           "language": "somali", "source": "manual"}
df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

print("\n=== AFTER ADDING ROW WITH MISSING ANSWER ===")
print(df.isnull().sum())

# ── LESSON 3: Drop rows with missing values ───────────────────
df_clean = df.dropna()
print("\n=== AFTER DROPPING MISSING ROWS ===")
print(f"Before: {len(df)} rows | After: {len(df_clean)} rows")

# ── LESSON 4: Fill missing values instead of dropping ─────────
df_filled = df.copy()
df_filled["answer_somali"] = df_filled["answer_somali"].fillna("Jawaabtaan waa la shaqeynayaa")
print("\n=== FILLED MISSING ANSWER ===")
print(df_filled[df_filled["id"] == 11][["question_somali", "answer_somali"]])

# ── LESSON 5: Text operations (critical for NLP) ──────────────
print("\n=== TEXT OPERATIONS ===")

# Uppercase
df["question_upper"] = df["question_somali"].str.upper()
print(df["question_upper"].head(3))

# Check if text contains a word
df["about_simad"] = df["question_somali"].str.contains("SIMAD", case=True)
print("\nQuestions that mention SIMAD:")
print(df[df["about_simad"] == True]["question_somali"])

# Word count per answer
df["word_count"] = df["answer_somali"].str.split().str.len()
print("\nWord count per answer:")
print(df[["question_somali", "word_count"]].dropna())

# ── LESSON 6: Remove duplicate rows ──────────────────────────
print(f"\n=== DUPLICATES ===")
print(f"Duplicate rows: {df.duplicated().sum()}")
df_no_dupes = df.drop_duplicates()

# ── LESSON 7: Rename a column ─────────────────────────────────
df_renamed = df_clean.rename(columns={
    "question_somali": "question",
    "answer_somali": "answer"
})
print("\n=== RENAMED COLUMNS ===")
print(df_renamed.columns.tolist())

# ── LESSON 8: Save the clean version ─────────────────────────
df_clean.to_csv("simad_qa_clean.csv", index=False)
print("\n✅ Saved simad_qa_clean.csv")