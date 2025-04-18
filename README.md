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

## Usage

1. Setup the Project:
   - Clone the repository.
   - Ensure you have Python installed.
   - Install required dependencies using the requirements.txt file.
     ```bash
     pip install -r requirements.txt
     ```

2. Load and merge data:
   ```bash
   python scripts/01_load_and_merge.py --data_dir data --output_dir outputs
   ```

3. Preprocess data:
   ```bash
   python scripts/02_preprocessing.py --input_path outputs/master.csv --output_dir outputs
   ```

4. Exploratory analysis:
   ```bash
   python scripts/03_exploratory_analysis.py --input_path outputs/processed_master.csv --output_dir outputs/eda
   ```

5. Feature engineering:
   ```bash
   python scripts/04_feature_engineering.py \
     --master outputs/master.csv \
     --vle data/vle.csv \
     --student_vle data/studentVle.csv \
     --student_assess data/studentAssessment.csv \
     --output_dir outputs
   ```

6. Train predictive model:
   ```bash
   python scripts/05_modeling.py --features outputs/features.csv --output_dir outputs
   ```

7. Evaluate model performance:
   ```bash
   python scripts/06_evaluation.py --model outputs/model.pkl --features outputs/features.csv --output_dir outputs
   ```

8. Analyze feature importance:
   ```bash
   python scripts/07_feature_importance.py --model outputs/model.pkl --features outputs/features.csv --output_dir outputs
   ```

9. Simulate dropout scenarios:
   ```bash
   python scripts/08_simulation_dropout.py --model outputs/model.pkl --features outputs/features.csv --n_sim 1000 --output_dir outputs
   ```

## Requirements

- Python 3.8 or higher
- pandas
- numpy
- scikit-learn
- matplotlib
- joblib

## Acknowledgments

dataset name: Student Performance at Open University  
dataset author: M Ehsani  
dataset source: https://www.kaggle.com/datasets/mohammadehsani/student-performance-at-open-university