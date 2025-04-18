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
