import pandas as pd

EXPECTED_DATA_FILE_NAME = "non_outlier_data.pkl"
OUTLIER_DATA_FILE_NAME = "outlier_data.pkl"


def save_outliers_and_normal_data(directory_path, data_df, outlier_df):
    """
    :param directory_path: The path to the directory to save the files at
    :param data_df: A DataFrame which holds all of the data we will be detecting outliers in
    :param outlier_df: A DataFrame which holds all of the outliers that have been separated from the main data set

    :return:
    """

    data_df.to_pickle(directory_path + "/" + EXPECTED_DATA_FILE_NAME)
    outlier_df.to_pickle(directory_path + "/" + OUTLIER_DATA_FILE_NAME)

    return True


def read_outliers_and_normal_data(directory_path):
    """
    :param directory_path: The path to the directory to save the files at

    :return: The two DataFrames in the order of the expected data DataFrame and then the outlier DataFrame
    """

    data_df = pd.read_pickle(directory_path + "/" + EXPECTED_DATA_FILE_NAME)
    outlier_df = pd.read_pickle(directory_path + "/" + OUTLIER_DATA_FILE_NAME)

    return data_df, outlier_df
