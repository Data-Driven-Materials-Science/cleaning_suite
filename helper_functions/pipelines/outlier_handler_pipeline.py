import pandas as pd

from helper_functions.pickle_saving_reading import PickleFileManager as PFM


def run_pipeline(user_id, temp_dir_path="Temp/", method="remove"):
    """

    :param user_id: The user id for the current user being processed
    :param temp_dir_path: The path to the Temp directory
    :param method: A string of the method we are handling the outliers with. Options are in the array:
        ["remove", "correct", "leave_in"].

    :return: Nothing

    Handles the outliers according to the method specified. It will either remove the outliers, correct them using
    the data correction methods in the library, or leave them in the data set.

    """
    dir_path = temp_dir_path + "/" + str(user_id) + "/"
    pickle_path = dir_path + "additional_files"

    data_df, outlier_df = PFM.read_outliers_and_normal_data(directory_path=pickle_path)

    if method == "remove":
        data_df.to_csv(dir_path + "final_data.csv", index=False)
    # This method is not yet implemented and still being decided on how it will function
    # elif method == "correct":
    #     return
    elif method == "leave_in":
        combined_df = pd.concat([data_df, outlier_df])
        combined_df = combined_df.sort_index()
        combined_df.to_csv(dir_path + "final_data.csv", index=False)
        return
    else:
        raise Exception("Wrong method was provided")

    return
