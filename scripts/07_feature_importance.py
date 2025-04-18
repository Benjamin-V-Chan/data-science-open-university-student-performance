import pandas as pd
import argparse
import os
import joblib
import matplotlib.pyplot as plt

def feature_importance(model_pkl, features_csv, output_dir):
    model = joblib.load(model_pkl)
    df = pd.read_csv(features_csv)
    names = [c for c in df.columns if c!='dropout']
    imps = model.named_steps['clf'].feature_importances_
    fi = pd.DataFrame({'feature':names,'importance':imps}).sort_values('importance', ascending=False)
    os.makedirs(output_dir, exist_ok=True)
    fi.to_csv(os.path.join(output_dir,'feature_importances.csv'), index=False)
    plt.figure(figsize=(10,6))
    plt.bar(fi['feature'][:20], fi['importance'][:20])
    plt.xticks(rotation=90); plt.tight_layout()
    plt.savefig(os.path.join(output_dir,'top20_importances.png'))

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--model',      required=True)
    p.add_argument('--features',   required=True)
    p.add_argument('--output_dir', required=True)
    args = p.parse_args()
    feature_importance(args.model, args.features, args.output_dir)

if __name__=='__main__':
    main()
