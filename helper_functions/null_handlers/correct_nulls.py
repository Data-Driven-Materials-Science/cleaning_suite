import pandas as pd

from helper_functions.null_handlers.interpolation_helper import *

"""
The purpose of this class is to correct nulls from data in a grid (2D) format
"""


# TODO Research if there is a situation where a grid can have rows or columns removed


def correct_nulls_all(data_df, method, x_df=None, y_df=None, drop_columns=False, threshold=0.3):
    """

    :param data_df: A DataFrame of data
    :param method: A string representation of the method we are using to correct the nulls
    :param x_df: A DataFrame of x values if it is a grid format
    :param y_df: A DataFrame of y values if it is a grid format
    :param drop_columns: A boolean of whether or not to drop column which have a certain amount of nulls in them
    :param threshold: A threshold for what percentage of data values are null as to whether or not the column gets
        dropped

    :return: The corrected data as a DataFrame

    Corrects the nulls in the data DataFrame in every column.

    """

    # TODO For every column inside of the data DataFrame ...

    for col in []:
        # TODO insert switch case if statement structure here to correct for every column

        # TODO Call one of the methods below in order to

        # TODO If the drop_columns is true then check percentage of nulls vs the threshold

        break

    return None


def correct_nulls_grid_interpolation(data_df, x_df, y_df, col_name):
    """

    :param data_df: A DataFrame of data
    :param x_df: A DataFrame of x values
    :param y_df: A DataFrame of y values
    :param col_name: The name of the column we are interpolating or changing at the moment

    :return: The corrected data as a DataFrame

    Corrects the nulls in the data DataFrame in the col_name column using interpolation. This data must conform
    to a grid format.

    """

    return None


def correct_nulls_average(data_df, col_name):
    """

    :param data_df: A DataFrame of data
    :param col_name: The name of the column we are interpolating or changing at the moment

    :return: The corrected data as a DataFrame

    Corrects the nulls in the data DataFrame in the col_name column using the average of all of the values.

    """

    # TODO

    return None


def correct_nulls_linear_remove(data_df):
    """

    :param data_df: A DataFrame of data

    :return: The corrected data as a DataFrame

    Corrects the nulls in the data DataFrame by removing any and all tuples which have nulls.

    """

    # TODO

    return None

# TODO research other methods for handling nulls


