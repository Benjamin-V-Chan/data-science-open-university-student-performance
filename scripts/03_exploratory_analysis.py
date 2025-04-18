import pandas as pd
import os
import argparse
import matplotlib.pyplot as plt

def exploratory_analysis(df, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    df.describe().to_csv(os.path.join(output_dir, 'summary_stats.csv'))
    nums = df.select_dtypes(include=['number']).columns
    cats = df.select_dtypes(include=['object','category']).columns
    for c in nums:
        plt.figure()
        df[c].hist(bins=50)
        plt.title(c)
        plt.savefig(os.path.join(output_dir, f'{c}_hist.png'))
    for c in cats:
        plt.figure()
        df[c].value_counts().plot(kind='bar')
        plt.title(c)
        plt.savefig(os.path.join(output_dir, f'{c}_bar.png'))

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--input_path', required=True)
    p.add_argument('--output_dir', required=True)
    args = p.parse_args()
    df = pd.read_csv(args.input_path)
    exploratory_analysis(df, args.output_dir)

if __name__=='__main__':
    main()
