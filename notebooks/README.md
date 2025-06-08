## 📂 `notebooks/` Folder

This directory contains Jupyter notebooks that document the exploratory data analysis (EDA)

### Suggested README Content for `notebooks/`

````markdown
# 📂 Notebooks

This folder contains Jupyter notebooks for exploring and analyzing customer experience data in fintech applications.

## Contents

- `eda.ipynb`: Exploratory Data Analysis
- `Sentiment Analysis.ipynb`: Sentiment Analysis

## Usage

1.  Install dependencies using:

```
pip install -r requirements.txt
```

2. Run the script:

```
cd Scripts
python3 scrapeDataFromPlayStore.py
```

## Preprocessing the Data

Steps:

- Clean text: Remove punctuation, special characters, convert to lowercase.
- Tokenize: Split text into words.
- Remove stop words: Eliminate common words (e.g., "the," "and").
- Lemmatize: Reduce words to base form (e.g., "running" → "run").

## Sentiment Analysis with TextBlob

Description: TextBlob provides a straightforward way to classify sentiments based on polarity scores.

### Sentiment Analysis with VADER

Description: VADER is tailored for short texts like reviews, accounting for sentiment intensity and informal language.
````
