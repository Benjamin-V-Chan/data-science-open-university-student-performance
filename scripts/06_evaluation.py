# - import pandas, sklearn.metrics, matplotlib, joblib, argparse, os, json
# - define evaluate_model(model_pkl, features_csv):
#     • load features.csv
#     • separate X/y
#     • load model
#     • y_pred, y_prob = model.predict, predict_proba
#     • compute accuracy, precision, recall, f1, roc_auc
#     • save metrics.json
#     • plot ROC curve → roc_curve.png
#     • plot confusion matrix heatmap → confusion_matrix.png
# - in main():
#     • parse --model, --features, --output_dir
#     • call evaluate_model
