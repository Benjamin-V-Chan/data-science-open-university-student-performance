# - import pandas, numpy, joblib, matplotlib, argparse, os
# - define simulate_dropout(model_pkl, features_csv, n_sim):
#     • load model
#     • load features.csv
#     • X = df.drop('dropout')
#     • probs = model.predict_proba(X)[:,1]
#     • for each sim: draw binomial(1, probs) → simulate dropout events
#     • sum over students for each sim → dropout_counts
#     • save dropout_counts → simulation_results.csv
#     • plot histogram → dropout_simulation_hist.png
# - in main():
#     • parse --model, --features, --output_dir, --n_sim
#     • call simulate_dropout
