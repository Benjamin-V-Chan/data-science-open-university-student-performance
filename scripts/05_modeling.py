# - import pandas, sklearn, joblib, argparse, os, json
# - define train_model(features_csv):
#     • load features.csv
#     • split X/y (y = dropout)
#     • train_test_split
#     • build Pipeline(StandardScaler, RandomForestClassifier)
#     • GridSearchCV over n_estimators, max_depth
#     • fit on training set
#     • save best_estimator_ → model.pkl
#     • save best_params_ → best_params.json
# - in main():
#     • parse --features, --output_dir
#     • call train_model
