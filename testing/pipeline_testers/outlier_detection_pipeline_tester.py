from helper_functions.pipelines import outlier_detection_pipeline as ODP

user_id = "001"
temp_dir_path = "../../Temp"
time_series = True
print("1")
ODP.run_pipeline(user_id=user_id, temp_dir_path=temp_dir_path, time_series=time_series)

exit(0)
