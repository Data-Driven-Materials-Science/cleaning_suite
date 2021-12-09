from helper_functions.pipelines import outlier_handler_pipeline as OHP

user_id = "279"
temp_dir_path = "../../Temp"
method = "remove"
OHP.run_pipeline(user_id=user_id, temp_dir_path=temp_dir_path, method=method)

exit(0)
