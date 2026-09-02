# AFDP Python Training

Materials for the Python workshop delivered at the Actuarial Faculty Development Program (AFDP). Each year's session lives in its own folder with a slide deck, Jupyter notebooks, the dataset, and participant instructions.

| Folder | Session | Contents |
|---|---|---|
| [`2025 AFDP Python Training`](./2025%20AFDP%20Python%20Training) | AFDP 2025 | Four notebooks (Python basics, data analysis, intermediate Python, pandas/seaborn), "Introduction to Python" deck, Colab/Anaconda instructions |
| [`2026 AFDP Python Training`](./2026%20AFDP%20Python%20Training) | AFDP 2026 | Three notebooks (Python basics, data analysis, a first AI agent with Agno + Gemini), updated deck with speaker notes, Colab instructions |

All notebooks are designed to run in [Google Colab](https://colab.research.google.com) with nothing installed locally; they also run under Anaconda / Jupyter. See the README inside each folder for setup, timing, and the pre-session checklist.

## Dataset

`us_health_insurance_dataset_afdp.csv` (1,338 rows) is used in both years and comes from Kaggle: [US Health Insurance Dataset](https://www.kaggle.com/datasets/teertha/ushealthinsurancedataset).

## Contributing / editing the notebooks

Notebooks are committed **with** their cell outputs so the tables and charts render directly on GitHub. A git clean filter (`.gitattributes` + `scripts/normalise_notebook_metadata.py`) resets machine-specific metadata (local kernel name, Python version, execution timestamps) at commit time so diffs contain only real changes. It is repo-local configuration, so run this once after cloning:

```bash
git config filter.nbnorm.clean "python3 scripts/normalise_notebook_metadata.py"
git config filter.nbnorm.smudge cat
git config filter.nbnorm.required true
```
