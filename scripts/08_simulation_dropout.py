import pandas as pd
import numpy as np
import argparse
import os
import joblib
import matplotlib.pyplot as plt

def simulate_dropout(model_pkl, features_csv, n_sim, output_dir):
    model = joblib.load(model_pkl)
    df = pd.read_csv(features_csv)
    X = df.drop(columns=['dropout'])
    probs = model.predict_proba(X)[:,1]
    sims = np.random.binomial(1, probs.reshape(-1,1), size=(len(probs), n_sim))
    counts = sims.sum(axis=0)
    os.makedirs(output_dir, exist_ok=True)
    pd.Series(counts).to_csv(os.path.join(output_dir,'simulation_results.csv'), index=False)
    plt.figure(); plt.hist(counts, bins=30); plt.title('Simulated Dropout Distribution')
    plt.savefig(os.path.join(output_dir,'dropout_simulation_hist.png'))

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--model',      required=True)
    p.add_argument('--features',   required=True)
    p.add_argument('--n_sim',      type=int, default=1000)
    p.add_argument('--output_dir', required=True)
    args = p.parse_args()
    simulate_dropout(args.model, args.features, args.n_sim, args.output_dir)

if __name__=='__main__':
    main()
