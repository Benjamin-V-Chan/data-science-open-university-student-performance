import pandas as pd
import numpy as np
import os
import argparse
from sklearn.preprocessing import OneHotEncoder, StandardScaler

def preprocess(input_csv):
    df = pd.read_csv(input_csv)
    df['final_result'] = df['final_result'].fillna('Unknown')
    df['dropout'] = df['final_result'].apply(lambda x: 1 if x=='Withdrawn' else 0)
    df = df.drop(columns=['final_result'])
    df = df.fillna({'imd_band':'Unknown','disability':False})
    cat = df.select_dtypes(include=['object']).columns.tolist()
    num = df.select_dtypes(include=[np.number]).columns.tolist()
    ohe = OneHotEncoder(sparse=False, handle_unknown='ignore')
    cat_df = pd.DataFrame(ohe.fit_transform(df[cat]), columns=ohe.get_feature_names_out(cat))
    scaler = StandardScaler()
    num_df = pd.DataFrame(scaler.fit_transform(df[num]), columns=num)
    out = pd.concat([num_df, cat_df], axis=1)
    out['dropout'] = df['dropout'].values
    return out

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--input_path', required=True)
    p.add_argument('--output_dir', required=True)
    args = p.parse_args()
    os.makedirs(args.output_dir, exist_ok=True)
    processed = preprocess(args.input_path)
    processed.to_csv(os.path.join(args.output_dir, 'processed_master.csv'), index=False)

if __name__=='__main__':
    main()
