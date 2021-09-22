import pandas as pd
import numpy as np

from helper_functions.outlier_handlers import identify_outliers
from helper_functions.report_generators import outlier_report_generator

np.random.seed(10)

mu, sigma = 0, 1  # mean and standard deviation
mu_outliers, sigma_outliers = 20, 1  # mean and standard deviation

s_x = np.random.normal(mu, sigma, 100)
s_y = np.random.normal(mu, sigma, 100)
s_z = np.random.normal(mu, sigma, 100)
outliers_x = np.random.normal(mu_outliers, sigma_outliers, 4)
outliers_y = np.random.normal(mu_outliers, sigma_outliers, 4)
outliers_z = np.random.normal(mu_outliers, sigma_outliers, 4)
s_x = np.append(s_x, outliers_x)
s_y = np.append(s_y, outliers_y)
s_z = np.append(s_z, outliers_z)

data_df_1d = pd.DataFrame()
data_df_2d = pd.DataFrame()
data_df_3d = pd.DataFrame()

data_df_1d["Data X"] = s_x
data_df_2d["Data X"] = s_x
data_df_3d["Data X"] = s_x

data_df_2d["Data Y"] = s_y
data_df_3d["Data Y"] = s_y

data_df_3d["Data Z"] = s_z


# print(data_df_1d)
# print(data_df_2d)
# print(data_df_3d)


def test_z_score_1d():
    """

    :param show:
    :return:

    Test 1 dimensional and z-score

    """
    method_details = [{"method_name": "z-score", "z_value": 0.1, "is_univariate": True},
                      {"method_name": "z-score", "z_value": 1, "is_univariate": True},
                      {"method_name": "z-score", "z_value": 2, "is_univariate": True},
                      {"method_name": "z-score", "z_value": 3, "is_univariate": True},
                      ]
    for method_detail_individual in method_details:
        non_outliers, outliers = identify_outliers.return_outliers(data_df=data_df_1d.copy(),
                                                                   method_details=method_detail_individual)
        det1, det2 = outlier_report_generator.generate_report(data_df=non_outliers, outlier_df=outliers)
        print(det1)
        print(det2)

    return True


def test_boxplot_1d():
    method_details = [{"method_name": "boxplot", "outlier_type": "mild", "is_univariate": True},
                      {"method_name": "boxplot", "outlier_type": "extreme", "is_univariate": True},
                      ]
    for method_detail_individual in method_details:
        non_outliers, outliers = identify_outliers.return_outliers(data_df=data_df_1d.copy(),
                                                                   method_details=method_detail_individual)
        det1, det2 = outlier_report_generator.generate_report(data_df=non_outliers, outlier_df=outliers)
        print(det1)
        print(det2)

    return True


def test_DBSCAN_1d():
    method_details = [
        {"method_name": "dbscan", "is_univariate": False, "algorithm": "auto", "eps": 0.5, "min_samples": 5},
        {"method_name": "dbscan", "is_univariate": False, "algorithm": "auto", "eps": 1, "min_samples": 5},
        {"method_name": "dbscan", "is_univariate": False, "algorithm": "auto", "eps": 0.5, "min_samples": 10},
        {"method_name": "dbscan", "is_univariate": False, "algorithm": "ball_tree", "eps": 0.5, "min_samples": 1},
        {"method_name": "dbscan", "is_univariate": False, "algorithm": "ball_tree", "eps": 0.5, "min_samples": 5},
    ]

    for method_detail_individual in method_details:
        non_outliers, outliers = identify_outliers.return_outliers(data_df=data_df_1d.copy(),
                                                                   method_details=method_detail_individual)
        det1, det2 = outlier_report_generator.generate_report(data_df=non_outliers, outlier_df=outliers)

        print(det1)
        print(det2)

    return True


def test_DBSCAN_2d():
    method_details = [
        {"method_name": "dbscan", "is_univariate": False, "algorithm": "auto", "eps": 0.5, "min_samples": 5},
        {"method_name": "dbscan", "is_univariate": False, "algorithm": "auto", "eps": 1, "min_samples": 5},
        {"method_name": "dbscan", "is_univariate": False, "algorithm": "auto", "eps": 0.5, "min_samples": 10},
        {"method_name": "dbscan", "is_univariate": False, "algorithm": "ball_tree", "eps": 0.5, "min_samples": 1},
        {"method_name": "dbscan", "is_univariate": False, "algorithm": "ball_tree", "eps": 0.5, "min_samples": 5},
    ]

    for method_detail_individual in method_details:
        non_outliers, outliers = identify_outliers.return_outliers(data_df=data_df_2d.copy(),
                                                                   method_details=method_detail_individual)
        det1, det2 = outlier_report_generator.generate_report(data_df=non_outliers, outlier_df=outliers)
        print(det1)
        print(det2)

    return True


def test_DBSCAN_3d():
    method_details = [
        {"method_name": "dbscan", "is_univariate": False, "algorithm": "auto", "eps": 0.5, "min_samples": 5},
        {"method_name": "dbscan", "is_univariate": False, "algorithm": "auto", "eps": 1, "min_samples": 5},
        {"method_name": "dbscan", "is_univariate": False, "algorithm": "auto", "eps": 0.5, "min_samples": 10},
        {"method_name": "dbscan", "is_univariate": False, "algorithm": "ball_tree", "eps": 0.5, "min_samples": 1},
        {"method_name": "dbscan", "is_univariate": False, "algorithm": "ball_tree", "eps": 0.5, "min_samples": 5},
    ]

    for method_detail_individual in method_details:
        non_outliers, outliers = identify_outliers.return_outliers(data_df=data_df_3d.copy(),
                                                                   method_details=method_detail_individual)
        det1, det2 = outlier_report_generator.generate_report(data_df=non_outliers, outlier_df=outliers)
        print(det1)
        print(det2)

    return True


def test_KNN_1d():
    method_details = [
        {"method_name": "knn", "is_univariate": False, "cut_off": 0.15},
        {"method_name": "knn", "is_univariate": False, "cut_off": 0.25},
        {"method_name": "knn", "is_univariate": False, "cut_off": 0.35},
        {"method_name": "knn", "is_univariate": False, "cut_off": 0.45},
    ]

    for method_detail_individual in method_details:
        non_outliers, outliers = identify_outliers.return_outliers(data_df=data_df_1d.copy(),
                                                                   method_details=method_detail_individual)
        det1, det2 = outlier_report_generator.generate_report(data_df=non_outliers, outlier_df=outliers)
        print(det1)
        print(det2)

    return True


def test_KNN_2d():
    method_details = [
        {"method_name": "knn", "is_univariate": False, "cut_off": 0.15},
        {"method_name": "knn", "is_univariate": False, "cut_off": 0.25},
        {"method_name": "knn", "is_univariate": False, "cut_off": 0.35},
        {"method_name": "knn", "is_univariate": False, "cut_off": 0.45},
    ]

    for method_detail_individual in method_details:
        non_outliers, outliers = identify_outliers.return_outliers(data_df=data_df_2d.copy(),
                                                                   method_details=method_detail_individual)
        det1, det2 = outlier_report_generator.generate_report(data_df=non_outliers, outlier_df=outliers)
        print(det1)
        print(det2)

    return True


def test_KNN_3d():
    method_details = [
        {"method_name": "knn", "is_univariate": False, "cut_off": 0.15},
        {"method_name": "knn", "is_univariate": False, "cut_off": 0.25},
        {"method_name": "knn", "is_univariate": False, "cut_off": 0.35},
        {"method_name": "knn", "is_univariate": False, "cut_off": 0.45},
    ]

    for method_detail_individual in method_details:
        non_outliers, outliers = identify_outliers.return_outliers(data_df=data_df_3d.copy(),
                                                                   method_details=method_detail_individual)
        det1, det2 = outlier_report_generator.generate_report(data_df=non_outliers, outlier_df=outliers)
        print(det1)
        print(det2)

    return True


# test_z_score_1d()
# test_boxplot_1d()
# test_DBSCAN_1d()
# test_DBSCAN_2d()
# test_DBSCAN_3d()
# test_KNN_1d()
# test_KNN_2d()
# test_KNN_3d()

# exit(0)
