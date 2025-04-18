import pandas as pd
import argparse
import os
import json
import joblib
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

def train_model(features_csv, output_dir):
    df = pd.read_csv(features_csv)
    X = df.drop(columns=['dropout'])
    y = df['dropout']
    X_train,X_test,y_train,y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    pipe = Pipeline([('scale', StandardScaler()), ('clf', RandomForestClassifier(random_state=42))])
    param_grid = {'clf__n_estimators':[100,200], 'clf__max_depth':[None,10,20]}
    gs = GridSearchCV(pipe, param_grid, cv=5, n_jobs=-1)
    gs.fit(X_train, y_train)
    os.makedirs(output_dir, exist_ok=True)
    joblib.dump(gs.best_estimator_, os.path.join(output_dir, 'model.pkl'))
    with open(os.path.join(output_dir, 'best_params.json'), 'w') as f:
        json.dump(gs.best_params_, f)

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--features',   required=True)
    p.add_argument('--output_dir', required=True)
    args = p.parse_args()
    train_model(args.features, args.output_dir)

if __name__=='__main__':
    main()
