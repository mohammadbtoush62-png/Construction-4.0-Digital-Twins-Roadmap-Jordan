Data availability

The materials supporting this manuscript are publicly available in the project repository and archived on Zenodo.

Repository (live mirror)

GitHub: https://github.com//construction4.0-jordan-roadmap
Zenodo (archived release)

Zenodo DOI: https://doi.org/10.5281/zenodo.[YOUR_DOI] [replace with DOI after Zenodo publish]
Included files

/prisma_and_search: database export CSVs, seed_references_56.bib, merged_raw.csv, deduped_master.csv, screening_title_abstract.csv, screening_fulltext.csv, dedup_script.py, kappa_script.py, kappa_report.txt, prisma_flow.svg.
/manuscript_assets: figures, KPI_register.xlsx, feasibility_template.xlsx.
/code: analysis notebooks and scripts used for figures and KPI calculations.
Licenses

Data & documentation: CC BY 4.0
Code/scripts: MIT License
How to reproduce

Clone the GitHub repository.
Run prisma_and_search/dedup_script.py to recreate merged_raw.csv and deduped_master.csv (Python 3, pandas).
Populate screening spreadsheets and run prisma_and_search/kappa_script.py to compute Cohen’s kappa.
See /code/analysis_notebooks.ipynb for analysis steps and KPI calculation examples.
Contact
For access requests, questions or corrections contact: muhammad.albtoosh@iu.edu.jo
