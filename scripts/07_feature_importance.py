# - import pandas, joblib, matplotlib, argparse, os
# - define feature_importance(model_pkl, features_csv):
#     • load model
#     • load features.csv
#     • get feature_names = all cols except 'dropout'
#     • importances = model.named_steps['clf'].feature_importances_
#     • build DataFrame(feature, importance), sort desc
#     • save to feature_importances.csv
#     • plot top 20 importances → top20_importances.png
# - in main():
#     • parse --model, --features, --output_dir
#     • call feature_importance
