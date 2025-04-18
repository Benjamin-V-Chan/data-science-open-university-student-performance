# - import pandas, os
# - define engineer_features(master_csv, vle_csv, student_vle_csv, student_assess_csv):
#     • load master, vle, studentVle, studentAssessment
#     • agg studentVle by id_student: total_clicks, avg_clicks
#     • join activity_type from vle; pivot sum_click by activity_type per student
#     • agg studentAssessment by id_student: avg_score, num_assess
#     • merge all engineered features into master
#     • save to outputs/features.csv
# - in main():
#     • parse paths + --output_dir
#     • call engineer_features
