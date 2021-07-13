from scipy import interpolate
import numpy as np


def complete_interpolation(data_list, x_df, y_df, method):
    """

    :param data_list: A list of data we are interpolating
    :param x_df: A DataFrame containing all x values
    :param y_df: A DataFrame containing all y values
    :param method: The method we are using to interpolate. This is based on the interpolate.griddata method so refer
        to their documentation. We typically use 'cubic' and then 'nearest'.

    :return: A 1D array of interpolated results

    This method will attempt to interpolate any and all null values in a list of data. It will then
    return the product of the interpolation process. This is not guaranteed to fill in all null values.

    """

    num_x_vals = len(np.unique(x_df["Data"]))
    num_y_vals = len(np.unique(y_df["Data"]))

    # Reshape the data so it is in the format of a grid
    data_2d = data_list.reshape(num_x_vals, num_y_vals)

    # All possible points in the format of a grid.
    # all_x_values[0][0] and all_y_values[0][0] represents one point.
    all_x_values = np.reshape(x_df["Data"].values, (num_x_vals, num_y_vals))
    all_y_values = np.reshape(y_df["Data"].values, (num_x_vals, num_y_vals))

    # For every invalid value that exists, mark it as being invalid
    # This will make another 2d array that shows where everything is null
    masked_data_2d = np.ma.masked_invalid(data_2d)

    # This value will be false in every cell that needs to be replaced
    data_2d_mask = ~masked_data_2d.mask

    # Get only the valid values
    null_x_values = all_x_values[data_2d_mask]
    null_y_values = all_y_values[data_2d_mask]

    # Get all of the valid values
    unmasked_data_2d = masked_data_2d[data_2d_mask]

    # Complete the interpolation and get a grid result back
    interpolated_grid = interpolate.griddata((null_x_values, null_y_values), unmasked_data_2d,
                                             (all_x_values, all_y_values), method=method)

    # Return the grid reshaped into a 1D array
    return interpolated_grid.reshape(-1, 1)


# TODO Try to find another interpolation method
