from helper_functions.pipelines import null_handler_pipeline as NHP

user_id = "066"
temp_dir_path = "../../Temp"
method = "remove"
NHP.run_pipeline(user_id=user_id, temp_dir_path=temp_dir_path, method=method)

exit(0)
