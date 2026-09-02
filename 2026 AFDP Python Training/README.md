# AFDP 2026 - Python Workshop

Materials for the two-hour Python session at the 2026 Actuarial Faculty Development Program. Everything runs in Google Colab with nothing installed.

## What is in this folder

| File | What it is | Used when |
|---|---|---|
| `Introduction to Python - AFDP 2026.pptx` | Slide deck (16 slides, ACTEX theme) with speaker notes and timings on every slide | Throughout |
| `Notebook1_Python_Basics.ipynb` | Variables, arithmetic, `if`, lists, loops, functions. Ends with a mortality-table loop and an EPV function | Minutes 15-40 |
| `Notebook2_Data_Analysis.ipynb` | pandas, NumPy, matplotlib, seaborn on the insurance dataset. Claim frequency by age band, severity distribution, missing data, heatmap, export to Excel | Minutes 40-85 |
| `Notebook3_Agentic_AI_Agno.ipynb` | A first AI agent with Agno + Gemini: two pandas tools, a before/after demo with and without tools | Minutes 90-110 |
| `us_health_insurance_dataset_afdp.csv` | The dataset (1,338 rows). Source: [Kaggle - US Health Insurance Dataset](https://www.kaggle.com/datasets/teertha/ushealthinsurancedataset) | Notebooks 2 and 3 |
| `Instructions for running python file.pdf` | Participant pre-read: how to open a notebook in Colab, or install Anaconda as a fallback | Send out before the session |

## Running the notebooks in Google Colab

1. Go to [colab.research.google.com](https://colab.research.google.com) and sign in with a Google account.
2. *File -> Upload notebook* and choose the `.ipynb` file.
3. Run each grey cell with **Shift + Enter**.

Notebooks 2 and 3 need the CSV. The loading cell opens a file-chooser in Colab the first time it runs - pick `us_health_insurance_dataset_afdp.csv` from your computer. Uploaded files are deleted when a Colab session ends, so participants may need to upload again on a second day.

The loading cell in Notebooks 2 and 3 is pre-set with `DATA_URL` pointing at the CSV in this GitHub repository, so participants normally do not need to upload anything. If the repository is renamed or the file moves, update that link; setting `DATA_URL = ""` falls back to the Colab file-chooser.

Notebook 3 additionally needs a free Gemini API key: create one at [aistudio.google.com/apikey](https://aistudio.google.com/apikey), then in Colab add it under *Secrets* (key icon in the left sidebar) with the name `GOOGLE_API_KEY` and *Notebook access* switched on. The notebook explains this step to participants; it is worth doing it live on the projector. The default model is `gemini-3.5-flash-lite`, which is on Google's free tier at the time of writing; the model id is a single variable at the top of section 4 if it needs changing.

The notebooks also run locally under Anaconda / Jupyter with the CSV in the same folder. Notebook 3 needs `pip install agno google-genai` and the key in the `GOOGLE_API_KEY` environment variable.

The notebooks are committed with their cell outputs cleared so participants run everything live. Notebook 2 writes `claim_frequency_by_age_band.xlsx` and `charges_by_region_smoker.csv` next to itself when run; both are regenerated each time and are excluded from the repository via `.gitignore`.

## Suggested timing (2 hours)

| Minutes | Segment |
|---|---|
| 0-15 | Why Python, how we run it today (slides 1-7) |
| 15-40 | Notebook 1 - Python basics |
| 40-85 | Notebook 2 - Data analysis with pandas |
| 85-90 | Break |
| 90-110 | Notebook 3 - Your first agent |
| 110-120 | Wrap-up and questions |

## What changed from the 2025 materials

- Four notebooks became three, sized for the two-hour slot. The 2025 File3 (file handling, exceptions, `input()`) was dropped; its function example lives on in Notebook 1.
- The notebooks now contain the actuarial examples the slides promise: a mortality-table loop and EPV function (Notebook 1), claim frequency by age band and a severity distribution (Notebook 2).
- All notebooks run standalone in Colab: Colab-first setup text, a CSV loader that works in Colab, locally, or from a URL, no Jupyter-only instructions, no `input()` calls.
- A new agentic AI segment (slides 12-14, Notebook 3) using Agno with Gemini via Colab Secrets.
- Slide deck: agenda slide, one bridge slide per notebook, three agent slides, a wrap-up slide, speaker notes with timings on every slide, and the "Predictive Modeling Intro" title overflow fixed. Existing slides and the ACTEX theme are unchanged.
- Typos and garbled sentences in the 2025 notebooks corrected.

## Before the session - checklist

- Update the date on slide 1 and the presenters on slide 2 if needed.
- Check that the `DATA_URL` link in Notebooks 2 and 3 still resolves (the repository must be public).
- Run all three notebooks end-to-end in Colab once, with a fresh Gemini key, the day before.
- Send participants the instructions PDF and ask them to test Colab in advance.
