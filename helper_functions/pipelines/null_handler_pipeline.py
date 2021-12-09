import os

from helper_functions.null_handlers import correct_nulls as CN
from helper_functions.data_file_reading import ReadFileHelper as RFH


def run_pipeline(user_id, temp_dir_path="Temp/", method="remove"):
    """

    :param user_id: The user id for the current user being processed
    :param temp_dir_path: The path to the Temp directory
    :param method: The method we are handling the nulls with. Can be any option in the array ["remove", "leave_in",
    "correct"]

    :return: Nothing

    Handles the nulls in the data set in some way specified by method and saves the resulting file.

    """

    dir_path = temp_dir_path + "/" + str(user_id) + "/"
    image_save_dir = dir_path + "images/"
    items_at_dir = os.listdir(dir_path)
    file_name = ""
    for item in items_at_dir:
        if "data" in item:
            file_name = item
            break

    if file_name == "":
        raise Exception("The data file was not found")

    file_path = dir_path + file_name

    data_df = RFH.read_file(file_path)

    if method == "correct":
        nulls_corrected_data_df = CN.mice_null_imputer(data=data_df)
        nulls_corrected_data_df.to_csv(dir_path + "final_data_csv", index=False)
    elif method == "leave_in":
        data_df.to_csv(dir_path + "final_data_csv", index=False)
    elif method == "remove":
        nulls_removed_df = data_df.dropna()
        nulls_removed_df.to_csv(dir_path + "final_data_csv", index=False)
    else:
        raise Exception("Wrong method provided")

    return
