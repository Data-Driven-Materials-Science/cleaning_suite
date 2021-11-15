from helper_functions.pipelines import remove_target_var_pipeline as RTVP

user_id = "002"
temp_dir_path = "../../Temp"
time_series = True
print("1")
RTVP.run_pipeline(user_id=user_id, temp_dir_path=temp_dir_path, target_var_name="Target Variable",
                  data_file_name="../../datasets/ExcelDataFile_3Dimensional_Clean_WithTargetVar.csv")

exit(0)
