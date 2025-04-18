# - import pandas, numpy, sklearn encoders/scalers
# - define preprocess(input_csv):
#     • load master.csv
#     • fill missing categorical/numeric
#     • create binary target “dropout” from final_result
#     • drop original final_result
#     • one‑hot encode categorical columns
#     • scale numeric columns
#     • return processed DataFrame
# - in main():
#     • parse --input_path, --output_dir
#     • call preprocess, save to outputs/processed_master.csv
