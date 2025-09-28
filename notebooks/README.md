# CORD-19 Data Explorer

## Overview

This project explores the CORD-19 dataset of COVID-19 research papers. It includes basic data analysis, visualizations, and a Streamlit app for interactive exploration.

## Structure

- `data/metadata.csv` - CORD-19 metadata file (download from Kaggle)
- `notebooks/analysis.ipynb` - Data exploration and visualization
- `app.py` - Streamlit application
- `requirements.txt` - Required Python packages

## Analysis

- Publications by year
- Top journals publishing COVID-19 research
- Word cloud of paper titles
- Abstract word counts

## How to Run

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Reflection

This assignment helped me practice:

- Loading and cleaning real-world datasets
- Handling missing data and datetime conversion
- Creating meaningful visualizations
- Building a simple interactive web app with Streamlit
- Challenges included dealing with missing values and large dataset size, which I handled by filtering and using caching in Streamlit.
