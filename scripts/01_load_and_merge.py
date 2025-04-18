import pandas as pd
import os
import argparse

def load_and_merge(data_dir):
    info = pd.read_csv(os.path.join(data_dir, 'studentInfo.csv'))
    reg  = pd.read_csv(os.path.join(data_dir, 'studentRegistration.csv'))
    crs  = pd.read_csv(os.path.join(data_dir, 'courses.csv'))
    df = reg.merge(info, on='id_student', how='left')
    df = df.merge(crs, on=['code_module','code_presentation'], how='left')
    return df

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--data_dir', required=True)
    p.add_argument('--output_dir', required=True)
    args = p.parse_args()
    os.makedirs(args.output_dir, exist_ok=True)
    master = load_and_merge(args.data_dir)
    master.to_csv(os.path.join(args.output_dir, 'master.csv'), index=False)

if __name__=='__main__':
    main()
