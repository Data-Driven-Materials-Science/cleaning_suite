import os

from helper_functions.visualization import visualize_nulls as VN
from helper_functions.data_file_reading import ReadFileHelper as RFH


def run_pipeline(user_id, temp_dir_path="Temp/"):
    """

    :param user_id: The user id for the current user being processed
    :param temp_dir_path: The path to the Temp directory

    :return: Nothing

    Visualizes the nulls for the user and saves these plots

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

    VN.visualize_nulls_general(data=data_df, image_directory=image_save_dir)

    return

