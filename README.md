# data-science-open-university-student-performance

## Project Overview

This project uses the Open University Learning Analytics Dataset (OULAD) to build a complete end-to-end pipeline for understanding and predicting student success and dropout. It includes data loading & merging, preprocessing, exploratory analysis, feature engineering, predictive modeling, evaluation, feature importance analysis, and simulation of dropout scenarios.

## Folder Structure

```
project-root/
├── data/                          # Raw data files
│   ├── studentInfo.csv
│   ├── studentRegistration.csv
│   ├── vle.csv
│   ├── assessments.csv
│   ├── courses.csv
│   ├── studentAssessment.csv
│   └── studentVle.csv
├── scripts/                       # Analysis and modeling scripts
│   ├── 01_load_and_merge.py
│   ├── 02_preprocessing.py
│   ├── 03_exploratory_analysis.py
│   ├── 04_feature_engineering.py
│   ├── 05_modeling.py
│   ├── 06_evaluation.py
│   ├── 07_feature_importance.py
│   └── 08_simulation_dropout.py
├── outputs/                       # Results: merged files, models, plots, etc.
├── requirements.txt              # Project dependencies
└── README.md                     # This documentation file
```
