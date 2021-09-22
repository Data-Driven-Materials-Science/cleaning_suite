import pandas as pd
import numpy as np
from scipy.stats import iqr
from sklearn.cluster import DBSCAN
from sklearn.neighbors import NearestNeighbors


# import matplotlib.pyplot as plt


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

    # TODO parameters will include data properties that determine optimal outlier detection technique
    # TODO pass in a dictionary, multivariate or univariate, distribution

    # TODO if statement that changes if it is multivariate or univariate

    # TODO For every column in the DataFrame we are going to try to correct the outliers inside of it
    for col in []:
        # TODO Switch case based on methods that will be below this

        break

    return None


def z_score_method(data_df, method_details):
    assert method_details["z_value"] is not None

    z_value = method_details["z_value"]
    data_column = data_df.columns[0]
    mean, std_dev = np.mean(data_df[data_column]), np.std(data_df[data_column])

    return data_df[abs(data_df[data_column] - mean) / std_dev <= z_value], data_df[
        abs(data_df[data_column] - mean) / std_dev > z_value]


def boxplot_method(data_df, method_details):
    assert method_details["outlier_type"] is not None

    outlier_type = method_details["outlier_type"]

    z_value = None

    # The extra 0.5 is added to allow us to treat this exactly the same as the z-score method for how the values are
    # returned

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

    # print(outlier_df)
    # print(non_outliers_df)
    #
    return non_outliers_df, outlier_df


def k_nearest_neighbors_method(data_df, method_details):
    assert method_details["cut_off"] is not None

    cut_off_val = method_details["cut_off"]

    raw_values = data_df.values

    # print(raw_values)

    nearest_neighbors_model = NearestNeighbors(n_neighbors=3)

    nearest_neighbors_model.fit(raw_values)

    # distances and indexes of k-neaighbors from model outputs
    distance_values, index_values = nearest_neighbors_model.kneighbors(raw_values)
    # # plot mean of k-distances of each observation
    # plt.plot(distance_values.mean(axis=1))
    # plt.show()

    # visually determine cutoff values > 0.15
    outlier_index = np.where(distance_values.mean(axis=1) > cut_off_val)
    # print(outlier_index[0])

    # filter outlier values
    outlier_index_values = data_df.index.isin(outlier_index[0])
    non_outlier_df = data_df[~outlier_index_values]
    outlier_df = data_df[outlier_index_values]
    # print(outlier_values)

    # plot data
    # plt.scatter(df["sepal_length"], df["sepal_width"], color="b", s=65)
    # plot outlier values
    # plt.scatter(outlier_values["sepal_length"], outlier_values["sepal_width"], color="r")
    # plt.show()

    return non_outlier_df, outlier_df
