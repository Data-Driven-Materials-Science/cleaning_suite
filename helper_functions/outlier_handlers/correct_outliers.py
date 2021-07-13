from helper_functions.null_handlers.correct_nulls_grid import *


def correct_outliers(data_df, x_df, y_df, method="Z-Score"):
    """

    :param data_df: A DataFrame which holds all of the data we will be detecting outliers in
    :param x_df: A DataFrame of the x coordinates of the grid
    :param y_df: A DataFrame of the y coordinates of the grid
    :param method: The method to remove outliers by, must be "Z-Score" or "IQR" as of right now

    :return: A DataFrame without outliers

    Removes the outliers inside of the data_df DataFrame and corrects them according to the data around them in
    their grid.

    """

    # Store values in an data_array_1d
    data_array_1d = data_df["Data"].values

    # TODO Separate these into separate function calls
    if method == "Z-Score":
        # Remove outliers z_score many standard deviations away from the mean
        mean_val = np.mean(data_array_1d)
        stddev_val = np.std(data_array_1d)
        z_scores = 3
        data_array_1d[abs(data_array_1d - mean_val) > stddev_val * z_scores] = np.nan

    elif method == "IQR":
        # Remove outliers
        med_val = np.median(data_array_1d)

        # First quartile (Q1)
        q1 = np.median(data_array_1d[data_array_1d < med_val])

        # Third quartile (Q3)
        q3 = np.median(data_array_1d[data_array_1d > med_val])

        # Interquartile range (IQR)
        iqr = q3 - q1

        data_array_1d[data_array_1d < (q1 - 1.5 * iqr)] = np.nan
        data_array_1d[data_array_1d > (q3 + 1.5 * iqr)] = np.nan

    return correct_nulls_grid_interpolation(data_df=pd.DataFrame(data_array_1d, columns=["Data"]), x_df=x_df, y_df=y_df)
