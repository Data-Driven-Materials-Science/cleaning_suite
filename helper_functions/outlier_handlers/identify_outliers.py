import numpy as np
from scipy.stats import iqr
from sklearn.cluster import DBSCAN
from sklearn.neighbors import NearestNeighbors


def return_outliers(data_df, method_details={"method_name": "z-score", "z_value": 3, "is_univariate": True}):
    """
    :param data_df: A DataFrame which holds all of the data we will be detecting outliers in
    :param method_details: A dictionary of the details of the outlier detection method we are using. Contains
        different parameters depending on the method we are using.


    :return: Two DataFrames. One DataFrame without outliers and one DataFrame with outliers. Same columns.

    Identifies the outliers inside of the data_df DataFrame.

    """

    try:
        if method_details["method_name"] == "dbscan":
            return dbscan_method(data_df=data_df, method_details=method_details)
        elif method_details["method_name"] == "knn":
            return k_nearest_neighbors_method(data_df=data_df, method_details=method_details)
        if method_details["is_univariate"]:
            if method_details["method_name"] == "z-score":
                return z_score_method(data_df=data_df, method_details=method_details)
            if method_details["method_name"] == "boxplot":
                return boxplot_method(data_df=data_df, method_details=method_details)
    except KeyError:
        print("You have the wrong method details!")
        return -1

    return None


def z_score_method(data_df, method_details):
    """
    
    :param data_df: The DataFrame which contains the one dimensional, univariate data
    :param method_details: The details we are using for this outlier detection method. The parameter 'z_value'
        determines which z value to use for this method.

    :return: Two DataFrames, the first with non outlier values and the second containing all outlier values
    
    This method determines which values are outliers according to the z-score outlier detection method. Once this
    is done, it will return the data points which are not outliers and the outliers in two separate DataFrames. The
    original data can then be rebuilt as the index is preserved for the non outliers and outlier data points. This
    method calculates the standard deviation and mean value, identifying any point more than z standard deviations
    away from the mean as an outlier.

    """
    assert method_details["z_value"] is not None

    z_value = method_details["z_value"]
    data_column = data_df.columns[0]
    mean, std_dev = np.mean(data_df[data_column]), np.std(data_df[data_column])

    return data_df[abs(data_df[data_column] - mean) / std_dev <= z_value], data_df[
        abs(data_df[data_column] - mean) / std_dev > z_value]


def boxplot_method(data_df, method_details):
    """

    :param data_df: The DataFrame which contains the one dimensional, univariate data
    :param method_details: The details we are using for this outlier detection method. The parameter
        'outlier_type' determines which z values to use for the equation. 'mild' uses 1.5 while 'extreme' uses 3.

    :return: Two DataFrames, the first with non outlier values and the second containing all outlier values

    This method determines which values are outliers according to the boxplot outlier detection method. Once this
    is done, it will return the data points which are not outliers and the outliers in two separate DataFrames. The
    original data can then be rebuilt as the index is preserved for the non outliers and outlier data points. This
    method uses the boxplot method. It takes the first and third quartile to determine the Interquartile Range (IQR).
    Once this is done, it takes all values outside of the interval (q1 - z*IQR, q3 + z*IQR) and marks them as
    outliers. The z values varies depending on level of outliers.

    """
    assert method_details["outlier_type"] is not None

    outlier_type = method_details["outlier_type"]

    # 0.5 is added to allow us to treat this exactly the same as the z-score method for how the values are returned

    if outlier_type == "mild":
        z_value = 1.5 + 0.5
    elif outlier_type == "extreme":
        z_value = 3 + 0.5
    else:
        print("You entered a wrong method_type!")
        return None

    data_column = data_df.columns[0]

    q1 = np.percentile(data_df[data_column].values, 25)
    q3 = np.percentile(data_df[data_column].values, 75)
    average_of_quartiles = (q1 + q3) / 2.0
    iqr_value = iqr(data_df[data_column].values)

    return data_df[abs(data_df[data_column] - average_of_quartiles) / iqr_value <= z_value], data_df[
        abs(data_df[data_column] - average_of_quartiles) / iqr_value > z_value]


def dbscan_method(data_df, method_details):
    """

    :param data_df: The DataFrame which contains the n dimensional, univariate or multivariate data
    :param method_details: The details we are using for this outlier detection method DBSCAN was taken from
        sklearn's library at https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html.
        Parameters 'eps', 'min_samples', and 'algorithm' are used.


    :return: Two DataFrames, the first with non outlier values and the second containing all outlier values.

    This method determines which values are outliers according to the DBSCAN outlier detection method. Once this
    is done, it will return the data points which are not outliers and the outliers in two separate DataFrames. The
    original data can then be rebuilt as the index is preserved for the non outliers and outlier data points. This
    method works by clustering the data using DBSCAN. All data points which do not end up in a cluster are then
    labeled as outliers.

    """

    assert method_details["algorithm"] is not None
    assert method_details["eps"] is not None
    assert method_details["min_samples"] is not None

    algorithm = method_details["algorithm"]
    eps = method_details["eps"]
    min_samples = method_details["min_samples"]

    num_data_column = len(data_df.columns)

    dbscan = DBSCAN(algorithm=algorithm, eps=eps, min_samples=min_samples).fit(
        data_df.values.reshape(-1, num_data_column))
    dbscan_results = dbscan.labels_

    combined_df = data_df.copy()
    combined_df["DBSCAN_Results"] = dbscan_results

    outlier_df = combined_df[combined_df["DBSCAN_Results"] == -1]
    non_outliers_df = combined_df[combined_df["DBSCAN_Results"] != -1]

    outlier_df = outlier_df.drop(columns=["DBSCAN_Results"])
    non_outliers_df = non_outliers_df.drop(columns=["DBSCAN_Results"])

    return non_outliers_df, outlier_df


def k_nearest_neighbors_method(data_df, method_details):
    """

    :param data_df: The DataFrame which contains the n dimensional, univariate or multivariate data
    :param method_details: The details we are using for this outlier detection method

    :return: Two DataFrames, the first with non outlier values and the second containing all outlier values. The
        parameter 'cutoff' is used to determine what cutoff to use for a distance value needed for a point to not be
        considered an outlier.

    This method determines which values are outliers according to the k-NN outlier detection method. Once this
    is done, it will return the data points which are not outliers and the outliers in two separate DataFrames. The
    original data can then be rebuilt as the index is preserved for the non outliers and outlier data points.
    This method is taken from sklean's neighbors module at https://scikit-learn.org/stable/modules/neighbors.html.

    """
    assert method_details["cut_off"] is not None

    cut_off_val = method_details["cut_off"]

    raw_values = data_df.values

    nearest_neighbors_model = NearestNeighbors(n_neighbors=3)

    nearest_neighbors_model.fit(raw_values)

    # A list of the distance values along with the indexes
    distance_values, index_values = nearest_neighbors_model.kneighbors(raw_values)

    # All values with a distance value above the cutoff are deemed outliers
    outlier_index = np.where(distance_values.mean(axis=1) > cut_off_val)

    # Mark the outlier values and the non outlier values
    outlier_index_values = data_df.index.isin(outlier_index[0])
    non_outlier_df = data_df[~outlier_index_values]
    outlier_df = data_df[outlier_index_values]

    return non_outlier_df, outlier_df
