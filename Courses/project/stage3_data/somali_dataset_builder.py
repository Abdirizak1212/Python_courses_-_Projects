import pandas as pd
import numpy as np
from datetime import date

# Load the dataset
df = pd.read_csv("simad_ogaal_dataset.csv")

print("=" * 50)
print("SIMAD OGAAL CHATBOT DATASET — QUALITY REPORT")
print("=" * 50)

# Basic info
print(f"\nTotal rows: {len(df)}")
print(f"Columns: {df.columns.tolist()}")

# Category breakdown
print("\n--- ROWS PER CATEGORY ---")
print(df["category"].value_counts())

# Difficulty breakdown
print("\n--- DIFFICULTY BREAKDOWN ---")
print(df["difficulty"].value_counts())

# Verified status
print("\n--- VERIFIED STATUS ---")
print(df["verified"].value_counts())

# Missing values check
print("\n--- MISSING VALUES ---")
print(df.isnull().sum())

# Answer length analysis
df["answer_length_somali"] = df["answer_somali"].str.split().str.len()
df["answer_length_english"] = df["answer_english"].str.split().str.len()

print("\n--- ANSWER WORD COUNT STATS ---")
print(f"Somali answers — avg words: {df['answer_length_somali'].mean():.1f}")
print(f"English answers — avg words: {df['answer_length_english'].mean():.1f}")

# Save clean version
df.to_csv("simad_ogaal_clean.csv", index=False)
print("\n✅ Saved simad_ogaal_clean.csv")
print(f"Dataset ready: {len(df)} Q&A pairs across {df['category'].nunique()} categories")
# Generate HTML report
html = f"""
<html>
<head>
    <title>SIMAD Ogaal Dataset Report</title>
    <style>
        body {{ font-family: Arial; padding: 30px; background: #f5f5f5; }}
        h1 {{ color: #1a1a2e; }}
        h2 {{ color: #16213e; margin-top: 30px; }}
        table {{ border-collapse: collapse; width: 100%; background: white; margin-top: 10px; }}
        th {{ background: #1a1a2e; color: white; padding: 10px; text-align: left; }}
        td {{ padding: 8px 10px; border-bottom: 1px solid #ddd; }}
        tr:hover {{ background: #f0f0f0; }}
        .stat {{ display: inline-block; background: white; padding: 15px 25px;
                 margin: 10px; border-radius: 8px; text-align: center;
                 box-shadow: 0 2px 4px rgba(0,0,0,0.1); }}
        .stat-number {{ font-size: 32px; font-weight: bold; color: #e94560; }}
        .badge-easy {{ background: #d4edda; color: #155724; padding: 2px 8px; border-radius: 10px; }}
        .badge-medium {{ background: #fff3cd; color: #856404; padding: 2px 8px; border-radius: 10px; }}
        .badge-hard {{ background: #f8d7da; color: #721c24; padding: 2px 8px; border-radius: 10px; }}
        .badge-yes {{ background: #d4edda; color: #155724; padding: 2px 8px; border-radius: 10px; }}
        .badge-no {{ background: #f8d7da; color: #721c24; padding: 2px 8px; border-radius: 10px; }}
    </style>
</head>
<body>
    <h1>SIMAD Ogaal Chatbot Dataset Report</h1>
    <p>Generated: {date.today()} &nbsp;|&nbsp; Source: manual &nbsp;|&nbsp; Language: Somali + English</p>

    <h2>Summary</h2>
    <div class="stat"><div class="stat-number">{len(df)}</div>Total Q&A Pairs</div>
    <div class="stat"><div class="stat-number">{df['category'].nunique()}</div>Categories</div>
    <div class="stat"><div class="stat-number">{df[df['verified']=='yes'].shape[0]}</div>Verified</div>
    <div class="stat"><div class="stat-number">{df['answer_length_somali'].mean():.1f}</div>Avg Words (Somali)</div>

    <h2>Full Dataset</h2>
    <table>
        <tr>
            <th>ID</th>
            <th>Category</th>
            <th>Question (Somali)</th>
            <th>Question (English)</th>
            <th>Answer (Somali)</th>
            <th>Difficulty</th>
            <th>Verified</th>
        </tr>
"""

for _, row in df.iterrows():
    html += f"""
        <tr>
            <td>{row['id']}</td>
            <td>{row['category']}</td>
            <td>{row['question_somali']}</td>
            <td>{row['question_english']}</td>
            <td>{row['answer_somali']}</td>
            <td><span class="badge-{row['difficulty']}">{row['difficulty']}</span></td>
            <td><span class="badge-{row['verified']}">{row['verified']}</span></td>
        </tr>"""

html += """
    </table>
</body>
</html>"""

with open("dataset_report.html", "w", encoding="utf-8") as f:
    f.write(html)

print("✅ Report saved — open dataset_report.html in your browser")