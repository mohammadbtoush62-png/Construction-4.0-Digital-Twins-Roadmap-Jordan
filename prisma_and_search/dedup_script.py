#!/usr/bin/env python3
"""
Deduplicate and merge database export CSVs placed in prisma_and_search/
Usage: python3 prisma_and_search/dedup_script.py
Requires: Python 3, pandas
Outputs:

prisma_and_search/merged_raw.csv (all records concatenated)
prisma_and_search/deduped_master.csv (duplicates removed by normalized title+authors) """ import pandas as pd import glob, os, sys
Change pattern if your export filenames differ
pattern = "prisma_and_search/*.csv"
files = sorted([f for f in glob.glob(pattern) if not f.endswith(("merged_raw.csv","deduped_master.csv","screening_title_abstract.csv","screening_fulltext.csv","interviews.csv","kappa_report.txt"))])

if not files:
    print("No CSV export files found in prisma_and_search/. Place your exports there and re-run.")
    sys.exit(1)

dfs = []
for f in files:
    try:
        df = pd.read_csv(f, dtype=str, keep_default_na=False)
        df['__source_file'] = os.path.basename(f)
        dfs.append(df)
    except Exception as e:
        print(f"Warning: could not read {f}: {e}")

if not dfs:
    print("No readable CSVs found.")
    sys.exit(1)

master = pd.concat(dfs, ignore_index=True, sort=False)

Attempt to standardize title and author fields (common variants)
title_cols = [c for c in master.columns if c.lower() in ('title','article title','document title')]
author_cols = [c for c in master.columns if 'author' in c.lower() or 'authors' in c.lower()]

Create normalized title and authors for deduplication
if title_cols:
    master['__title_raw'] = master[title_cols[0]].fillna('').astype(str)
else:
    master['__title_raw'] = master.get('Title','').astype(str)

if author_cols:
    master['__authors_raw'] = master[author_cols[0]].fillna('').astype(str)
else:
    master['__authors_raw'] = master.get('Authors','').astype(str)

master['__title_norm'] = master['__title_raw'].str.strip().str.lower().str.replace(r'\s+',' ', regex=True)
master['__authors_norm'] = master['__authors_raw'].str.strip().str.lower().str.replace(r'\s+',' ', regex=True)

before = len(master)
deduped = master.drop_duplicates(subset=['__title_norm','__authors_norm'], keep='first').copy()
after = len(deduped)

Save outputs
merged_path = "prisma_and_search/merged_raw.csv"
dedup_path = "prisma_and_search/deduped_master.csv"
master.to_csv(merged_path, index=False)
deduped.to_csv(dedup_path, index=False)

print(f"Processed files: {len(files)}")
print(f"Records before deduplication: {before}")
print(f"Records after deduplication: {after}")
print(f"Saved: {merged_path} and {dedup_path}")
