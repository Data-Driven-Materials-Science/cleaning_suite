import os

from helper_functions.outlier_handlers import identify_outliers, dbscan_parameter_generation as DPG
from helper_functions.data_file_reading import ReadFileHelper as RFH
from helper_functions.pickle_saving_reading import PickleFileManager as PFM
from helper_functions.visualization import visualize_outliers


def run_pipeline(user_id, temp_dir_path="Temp/", time_series=False):
    """

    :param user_id: The user id for the current user being processed
    :param temp_dir_path: The path to the Temp directory
    :param time_series: Whether or not the data file is a csv file

    :return: Nothing

    Runs the outlier detection process. Outliers are saved as a separate file than non outlier values. Plots are also
    saved in a images folder. This process assumes that a data file is present in the user id folder and that the
    necessary folder structure has already been built.

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

    is_univariate = data_df.columns == 1

    if time_series:
        method_details = {"method_name": "isolation_forest", "is_univariate": False, "time_series": True}
    elif is_univariate:
        method_details = {"method_name": "boxplot", "outlier_type": "extreme", "is_univariate": True,
                          "time_series": False}
    else:
        eps, min_neighbors = DPG.get_parameters(data_df=data_df)
        method_details = {"method_name": "dbscan", "is_univariate": False, "algorithm": "auto", "eps": eps,
                          "min_samples": min_neighbors, "time_series": False}

    normal_data_df, outliers_df = identify_outliers.return_outliers(data_df=data_df, method_details=method_details)

    PFM.save_outliers_and_normal_data(directory_path=dir_path + "additional_files/", data_df=data_df,
                                      outlier_df=outliers_df)

    visualize_outliers.visualize_outliers(data_df=data_df, outlier_df=outliers_df, bars=True, diff_colors=True,
                                          show=True, save=True, title="Testing123", multiple_hists=True,
                                          save_dir=image_save_dir)

    return
