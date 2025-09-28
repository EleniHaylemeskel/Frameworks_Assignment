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

## Challenges

- Challenges included dealing with missing values and large dataset size, which I handled by removing the metadata.csv file from my workbench.

- Throughout this assignment, I encountered several technical challenges that deepened my understanding of Python environments, Git, and repository management.

   First, I ran into issues running my Streamlit app due to missing packages and PowerShell execution policy restrictions. I resolved these by activating my virtual environment, installing the required libraries, and using activate.bat to bypass PowerShell’s policy.

   Later, pushing my project to GitHub failed because of a large dataset (metadata.csv). Even after trying Git LFS, the push was unsuccessful due to the file being present in the commit history. I eventually used git filter-repo on a fresh clone to completely remove the file from history, then force-pushed the cleaned repository.

   I also had to address Git configuration issues, like setting the correct upstream branch to enable smooth pushing and pulling. Managing multiple folders—one with a corrupted history and one clean—created confusion, so I consolidated all my work into the clean repository.

- Lesson Learned:

   1. Avoid pushing large files to GitHub; use .gitignore or external storage.

   2. Git LFS doesn't remove files from history—use git filter-repo.

   3. Always rewrite history on a fresh clone.

   4. Manage virtual environments carefully in PowerShell.

   5. Track the correct upstream branch to avoid sync errors.

These experiences strengthened my problem-solving skills and gave me a deeper appreciation for good version control practices.


## Dataset

Due to GitHub file size limits, the `metadata.csv` file is not included in this repository.  
Please download it from Kaggle with the given link below and place it inside the `data/` folder before running the analysis:
https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge
