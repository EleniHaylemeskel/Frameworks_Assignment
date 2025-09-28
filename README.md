# Frameworks_Assignment

Python Frameworks Assignment

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

- This assignment helped me practice:

1. Loading and cleaning real-world datasets

2. Handling missing data and datetime conversion

3. Creating meaningful visualizations

4. Building a simple interactive web app with Streamlit

5. Challenges included dealing with missing values and large dataset size, which I handled by removing the metadata.csv file from my workbench.

6. I had a challeng on the git platform due to file size limit so I have to remove the metadata.csv file and also updaing my repo was a challeng due to some directories and I had cloned the repo but it did not workout, also I commit a change on an exsiting repo by mistake so I have to track back my actions.


## Dataset

Due to GitHub file size limits, the `metadata.csv` file is not included in this repository.  
Please download it from Kaggle with the given link below and place it inside the `data/` folder before running the analysis:
https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge
