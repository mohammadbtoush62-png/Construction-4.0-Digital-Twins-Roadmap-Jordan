#!/usr/bin/env python3
"""
Compute Cohen's kappa for dual screening decisions in prisma_and_search/screening_title_abstract.csv
Requires: Python 3, pandas, scikit-learn
Usage: python3 prisma_and_search/kappa_script.py
"""
import pandas as pd
from sklearn.metrics import cohen_kappa_score
import sys

INPUT = "prisma_and_search/screening_title_abstract.csv"
OUTPUT = "prisma_and_search/kappa_report.txt"

try:
    df = pd.read_csv(INPUT, dtype=str, keep_default_na=False)
except Exception as e:
    print(f"Could not read {INPUT}: {e}")
    sys.exit(1)

if 'Reviewer1_decision' not in df.columns or 'Reviewer2_decision' not in df.columns:
    print("Reviewer decision columns missing in screening_title_abstract.csv")
    sys.exit(1)

r1 = df['Reviewer1_decision'].fillna('').astype(str)
r2 = df['Reviewer2_decision'].fillna('').astype(str)

Map decisions to integers
labels = sorted(set(r1.unique()).union(set(r2.unique())))
mapping = {lab: i for i, lab in enumerate(labels)}
r1m = r1.map(mapping)
r2m = r2.map(mapping)

kappa = cohen_kappa_score(r1m, r2m)

with open(OUTPUT, "w") as f:
    f.write(f"Cohen's kappa: {kappa:.3f}\n")
    f.write(f"Labels mapping: {mapping}\n")

print(f"Cohen's kappa: {kappa:.3f} (written to {OUTPUT})")

Short steps to run:

Ensure screening_title_abstract.csv is populated with Reviewer1_decision and Reviewer2_decision columns.
Install dependencies if needed: pip install pandas scikit-learn
Run: python3 prisma_and_search/kappa_script.py
View result in prisma_and_search/kappa_report.txt.
