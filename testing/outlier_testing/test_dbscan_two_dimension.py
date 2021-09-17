import numpy as np
from helper_functions.outlier_handlers import identify_outliers
import matplotlib.pyplot as plt
import pandas as pd


def test_method1():
    # Tests the z score outlier removal
    np.random.seed(10)

    mu, sigma = 0, 1  # mean and standard deviation
    mu_outliers, sigma_outliers = 20, 1  # mean and standard deviation
    s_x = np.random.normal(mu, sigma, 100)
    s_y = np.random.normal(mu, sigma, 100)
    outliers_x = np.random.normal(mu_outliers, sigma_outliers, 4)
    outliers_y = np.random.normal(mu_outliers, sigma_outliers, 4)
    s_x = np.append(s_x, outliers_x)
    s_y = np.append(s_y, outliers_y)

    # print(s_x)
    # print(s_y)

    combined_list = np.append(s_x, s_y)
    combined_list = combined_list.reshape(-1, 2)

    # print(combined_list)

    data_df = pd.DataFrame(combined_list, columns=["Data X", "Data Y"])

    # plt.scatter(data_df["Data X"].values, data_df["Data Y"], color="blue")
    # plt.title("Original Data Set")
    # plt.xlabel("Data Point X Value")
    # plt.ylabel("Data Point Y Value")
    # plt.show()

    method_details = {"method_name": "dbscan", "is_univariate": False, "algorithm": "auto", "eps": 0.5,
                      "min_samples": 5}

    # print(identify_outliers.return_outliers(data_df=data_df, method_details=method_details))
    non_outliers, outliers = identify_outliers.return_outliers(data_df=data_df, method_details=method_details)

    # plt.scatter(non_outliers["Data X"].values, non_outliers["Data Y"], color="green")
    # plt.scatter(outliers["Data X"].values, outliers["Data Y"], color="red")
    # plt.title("Outliers Detected From Original Set")
    # plt.xlabel("Data Point X Value")
    # plt.ylabel("Data Point Y Value")
    # plt.show()

    assert len(non_outliers["Data X"].values) == 80
    assert len(outliers["Data X"].values) == 24

    # exit(0)
