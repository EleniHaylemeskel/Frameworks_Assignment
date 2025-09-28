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

### Analysis

- Publications by year
- Top journals publishing COVID-19 research
- Word cloud of paper titles
- Abstract word counts

## How to Run

1. Create a virtual environment (Windows CMD):

   ```bash
   py -m venv myenv
   myenv\Scripts\activate.bat
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app
   ```bash
   streamlit run app.py
   ```

## Reflection

### Skills Practiced

      1. Loading and cleaning real-world datasets

      2. Handling missing data and datetime conversions

      3. Creating meaningful visualizations

      4. Building an interactive web app with Streamlit

### Technical Challenges

      - PowerShell execution policy blocked activate.ps1; resolved by using activate.bat

      - Pushing large files to GitHub failed; resolved by removing metadata.csv from history using git filter-repo

      - Configuring Git upstream branches and consolidating multiple folders

### Lessons Learned

      1. Avoid pushing large files to GitHub; use .gitignore or external storage.

      2. Git LFS does not remove files from commit history; use git filter-repo.

      3. Rewrite Git history only on a fresh clone.

      4. Manage virtual environments carefully in PowerShell.

      5. Track the correct upstream branch to avoid sync errors.

### This experience strengthened problem-solving skills and deepened understanding of Python environments, version control, and working with large datasets.

## Dataset

Due to GitHub file size limits, the `metadata.csv` file is not included in this repository.  
Please download it from Kaggle with the given link below and place it inside the `data/` folder before running the analysis:
https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge
`bash
   mkdir data   # if the folder does not exist move metadata.csv into data/
    `
