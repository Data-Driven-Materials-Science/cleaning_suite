import numpy as np
from helper_functions.outlier_handlers import identify_outliers
import matplotlib.pyplot as plt
import pandas as pd


def test_method1():
    # Tests the z score outlier removal
    np.random.seed(10)

    mu, sigma = 0, 1  # mean and standard deviation
    mu_outliers, sigma_outliers = 20, 1  # mean and standard deviation
    s = np.random.normal(mu, sigma, 100)
    outliers = np.random.normal(mu_outliers, sigma_outliers, 4)
    s = np.append(s, outliers)

    intervals = []
    interval_increment = 0.25

    accumulator = min(s) - interval_increment
    max_limit = max(s) + 2 * interval_increment

    while accumulator < max_limit:
        intervals.append(accumulator)
        accumulator = accumulator + interval_increment

    data_df = pd.DataFrame(s, columns=["Data"])
    #
    # plt.hist(data_df["Data"].values, bins=intervals, color="blue")
    # plt.title("Original Data Set")
    # plt.xlabel("Data Point Value")
    # plt.ylabel("Data Point Frequency")
    # plt.show()

    method_details = {"method_name": "boxplot", "outlier_type": "mild", "is_univariate": True}

    print(identify_outliers.return_outliers(data_df=data_df, method_details=method_details))
    non_outliers, outliers = identify_outliers.return_outliers(data_df=data_df, method_details=method_details)

    # plt.hist(non_outliers["Data"].values, bins=intervals, color="green")
    # plt.hist(outliers["Data"].values, bins=intervals, color="red")
    # plt.title("Outliers Detected From Original Set")
    # plt.xlabel("Data Point Value")
    # plt.ylabel("Data Point Frequency")
    # plt.show()

    assert len(non_outliers["Data"].values) == 100
    assert len(outliers["Data"].values) == 4

    method_details = {"method_name": "boxplot", "outlier_type": "extreme", "is_univariate": True}

    non_outliers, outliers = identify_outliers.return_outliers(data_df=data_df, method_details=method_details)

    # plt.hist(non_outliers["Data"].values, bins=intervals, color="green")
    # plt.hist(outliers["Data"].values, bins=intervals, color="red")
    # plt.title("Outliers Detected From Original Set")
    # plt.xlabel("Data Point Value")
    # plt.ylabel("Data Point Frequency")
    # plt.show()

    assert len(non_outliers["Data"].values) == 100
    assert len(outliers["Data"].values) == 4

    # exit(0)
