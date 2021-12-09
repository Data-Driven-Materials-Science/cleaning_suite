from helper_functions.pipelines import outlier_handler_pipeline as OHP

user_id = "278"
temp_dir_path = "../../Temp"
method = "correct"
OHP.run_pipeline(user_id=user_id, temp_dir_path=temp_dir_path, method=method)

exit(0)
