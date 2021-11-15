from helper_functions.data_file_reading import ReadFileHelper as RFH


def run_pipeline(user_id, temp_dir_path="Temp/", target_var_name="testing", data_file_name="test.csv"):
    """

    :param user_id: The user id for the current user being processed
    :param temp_dir_path: The path to the Temp directory
    :param target_var_name: Whether or not the data file is a csv file
    :param data_file_name: The name of the original data file

    :return: Nothing

    Reads in the data file and removes the target variable column if it exists. Throws an error if it does
    not exist. Return true if successful.

    """

    dir_path = temp_dir_path + "/" + str(user_id) + "/"

    file_path = dir_path + data_file_name

    data_df = RFH.read_file(file_path)

    if target_var_name not in data_df.columns:
        raise Exception("Column not in file")

    new_df = data_df.drop(target_var_name, axis=1)

    success = len(new_df.columns) != len(data_df.columns)

    new_df.to_csv(dir_path + "data.csv", index=False)

    return success
