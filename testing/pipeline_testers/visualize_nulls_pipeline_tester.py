from helper_functions.pipelines import visualize_nulls_pipeline as VNP

user_id = "003"
temp_dir_path = "../../Temp"
VNP.run_pipeline(user_id=user_id, temp_dir_path=temp_dir_path)

exit(0)
