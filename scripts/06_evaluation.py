import pandas as pd
import argparse
import os
import json
import joblib
import matplotlib.pyplot as plt
from sklearn.metrics import (accuracy_score, precision_score, recall_score,
                             f1_score, roc_auc_score, confusion_matrix, roc_curve)

def evaluate_model(model_pkl, features_csv, output_dir):
    df = pd.read_csv(features_csv)
    X = df.drop(columns=['dropout'])
    y = df['dropout']
    model = joblib.load(model_pkl)
    y_pred = model.predict(X)
    y_prob = model.predict_proba(X)[:,1]
    metrics = {
        'accuracy': accuracy_score(y,y_pred),
        'precision': precision_score(y,y_pred),
        'recall': recall_score(y,y_pred),
        'f1': f1_score(y,y_pred),
        'roc_auc': roc_auc_score(y,y_prob)
    }
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir,'metrics.json'),'w') as f:
        json.dump(metrics, f)
    fpr, tpr, _ = roc_curve(y, y_prob)
    plt.figure(); plt.plot(fpr, tpr); plt.title('ROC Curve')
    plt.savefig(os.path.join(output_dir,'roc_curve.png'))
    cm = confusion_matrix(y, y_pred)
    plt.figure(); plt.imshow(cm); plt.title('Confusion Matrix')
    plt.colorbar()
    plt.savefig(os.path.join(output_dir,'confusion_matrix.png'))

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--model',      required=True)
    p.add_argument('--features',   required=True)
    p.add_argument('--output_dir', required=True)
    args = p.parse_args()
    evaluate_model(args.model, args.features, args.output_dir)

if __name__=='__main__':
    main()
