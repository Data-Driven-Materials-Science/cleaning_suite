import pandas as pd

from helper_functions.null_handlers.interpolation_helper import *

"""
The purpose of this class is to correct nulls from data in a grid (2D) format
"""

# TODO Research if there is a situation where a grid can have rows or columns removed


def correct_nulls_grid_interpolation(data_df, x_df, y_df):
    """

    :param data_df: A DataFrame of data
    :param x_df: A DataFrame of x values
    :param y_df: A DataFrame of y values

    :return: The corrected data as a DataFrame

    Corrects the nulls in the data DataFrame

    """

    num_x_vals = len(np.unique(x_df["Data"]))
    num_y_vals = len(np.unique(y_df["Data"]))

    assert num_x_vals > 0 and num_y_vals > 0

    # Store values in an array
    data_1d = data_df["Data"].values

    # Complete the first interpolation step
    interpolation_result_one = complete_interpolation(data_1d, x_df, y_df, "cubic")

    interpolation_result_two = complete_interpolation(interpolation_result_one, x_df, y_df, "nearest")

    ret_df = pd.DataFrame(interpolation_result_two, columns=["Data"])

    return ret_df


def correct_nulls_grid_average(data_df, x_df, y_df):
    """

    :param data_df: A DataFrame of data
    :param x_df: A DataFrame of x values
    :param y_df: A DataFrame of y values

    :return: The corrected data as a DataFrame

    Corrects the nulls in the data DataFrame

    """

    # TODO

    return None

