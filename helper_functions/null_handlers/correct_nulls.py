import pandas as pd

import sys
import sklearn.neighbors._base

sys.modules['sklearn.neighbors.base'] = sklearn.neighbors._base

from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from missingpy import MissForest

from helper_functions.null_handlers.interpolation_helper import *

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

    This method is the MAIN driver of null correction. The recommendations will be called from here, and
    the proper technique will also be called from this method.

    """

    # TODO For every column inside of the data DataFrame ...

    for col in []:
        # TODO insert switch case if statement structure here to correct for every column

        # TODO Call one of the methods below in order to

        # TODO For the remove method, we need some way of specifying how many tuples should be null to be removed
        # TODO also it isn't column by column. This may have to be done with a configuration dictionary

        # TODO Maybe have a for each column method and a for every column at once method
        # TODO Interpolation is a for each column, remove is a for every column at once

        # TODO If the drop_columns is true then check percentage of nulls vs the threshold

        break

    return None


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


def correct_nulls_linear_remove(data_df):
    """

    :param data_df: A DataFrame of data

    :return: The corrected data as a DataFrame

    Corrects the nulls in the data DataFrame by removing any and all tuples which have nulls.

    """

    # TODO

    return None

def remove_monotone_columns(data):
    # Keeps track of the columns that contain more than 1 unique value
    columns_to_keep = []
    for col in data.columns:
        unique_values = data[col].unique()

        # If the column only contains one value, add it for removal
        if len(unique_values) != 1:
            columns_to_keep.append(col)

    return data[columns_to_keep]

def mice_null_imputer(data):
    data = remove_monotone_columns(data)
    mice_imputer = IterativeImputer(sample_posterior=True)
    imputed_data = mice_imputer.fit(data).transform(data)
    return pd.DataFrame(imputed_data, columns=data.columns)


def miss_forest_null_imputer(data):
    miss_forest_imputer = MissForest()
    imputed_data = miss_forest_imputer.fit(data).transform(data)
    return imputed_data
