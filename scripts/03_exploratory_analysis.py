# - import pandas, matplotlib, os
# - define exploratory_analysis(df, output_dir):
#     • save df.describe() → summary_stats.csv
#     • for each numeric column: plot histogram → <col>_hist.png
#     • for each categorical column: plot bar chart → <col>_bar.png
# - in main():
#     • parse --input_path, --output_dir
#     • load processed_master.csv
#     • call exploratory_analysis
