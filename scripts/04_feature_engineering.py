import pandas as pd
import os
import argparse

def engineer_features(master, vle, student_vle, student_assess, output_dir):
    df = pd.read_csv(master)
    vle_df = pd.read_csv(vle)
    sv = pd.read_csv(student_vle)
    sa = pd.read_csv(student_assess)
    agg1 = sv.groupby('id_student')['sum_click'].agg(['sum','mean']).reset_index().rename(columns={'sum':'total_clicks','mean':'avg_clicks'})
    df = df.merge(agg1, on='id_student', how='left')
    act = sv.merge(vle_df[['id_site','activity_type']], on='id_site')
    pivot = act.groupby(['id_student','activity_type'])['sum_click'].sum().unstack(fill_value=0).reset_index()
    df = df.merge(pivot, on='id_student', how='left')
    agg2 = sa.groupby('id_student')['score'].agg(['mean','count']).reset_index().rename(columns={'mean':'avg_score','count':'num_assess'})
    df = df.merge(agg2, on='id_student', how='left')
    os.makedirs(output_dir, exist_ok=True)
    df.to_csv(os.path.join(output_dir, 'features.csv'), index=False)

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--master',        required=True)
    p.add_argument('--vle',           required=True)
    p.add_argument('--student_vle',   required=True)
    p.add_argument('--student_assess',required=True)
    p.add_argument('--output_dir',    required=True)
    args = p.parse_args()
    engineer_features(args.master, args.vle, args.student_vle, args.student_assess, args.output_dir)

if __name__=='__main__':
    main()
