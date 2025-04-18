# - import pandas, os
# - define load_and_merge(data_dir):
#     • read studentInfo.csv, studentRegistration.csv, courses.csv
#     • merge registration ← studentInfo on id_student
#     • merge result ← courses on [code_module, code_presentation]
#     • return merged DataFrame
# - in main():
#     • parse --data_dir, --output_dir
#     • call load_and_merge, save to outputs/master.csv
