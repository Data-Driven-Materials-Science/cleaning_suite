

def correct_outliers(data_df, x_df=None, y_df=None, outlier_identification_method="Z-Score",
                     outlier_correction_method=""):
    """

    :param data_df: A DataFrame which holds all of the data we will be detecting outliers in
    :param x_df: A DataFrame of the x coordinates of the grid
    :param y_df: A DataFrame of the y coordinates of the grid
    :param outlier_identification_method: The method to identify outliers by, must be "Z-Score" or "IQR" as of
        right now. TODO

    :param outlier_correction_method: The method to correct outliers by. Must be TODO

    # TODO Should we just specify which columns to remove outliers from? If so then add another param

    :return: A DataFrame without outliers in the marked columns

    Removes the outliers inside of the data_df DataFrame and corrects them according to the data around them in
    their grid.

    """

    # TODO For every column in the DataFrame we are going to try to correct the outliers inside of it
    for col in []:

        # TODO Switch case based on methods that will be inside of identify_outliers.py

        # TODO Identify outliers returns the outliers. We must make all of these indices null and then rejoin
        # TODO using the EXACT SAME INDEX. This is crucial or it breaks everything. Order matters heavily.

        break

    return None
