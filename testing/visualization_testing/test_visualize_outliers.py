import pandas as pd
import numpy as np

from helper_functions.outlier_handlers import identify_outliers
from helper_functions.visualization import visualize_outliers

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


def test_z_score_1d(show=False):
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
        for bars in [True, False]:
            for diff_colors in [True, False]:
                visualize_outliers.visualize_outliers(non_outliers, outliers, bars=bars, diff_colors=diff_colors,
                                                      show=show, title="Z Score Test")

    return True


def test_boxplot_1d(show=False):
    method_details = [{"method_name": "boxplot", "outlier_type": "mild", "is_univariate": True},
                      {"method_name": "boxplot", "outlier_type": "extreme", "is_univariate": True},
                      ]
    for method_detail_individual in method_details:
        non_outliers, outliers = identify_outliers.return_outliers(data_df=data_df_1d.copy(),
                                                                   method_details=method_detail_individual)
        for bars in [True, False]:
            for diff_colors in [True, False]:
                visualize_outliers.visualize_outliers(non_outliers, outliers, bars=bars, diff_colors=diff_colors,
                                                      show=show, title="Boxplot Test")

    return True


def test_DBSCAN_1d(show=False):
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
        for bars in [True, False]:
            for diff_colors in [True, False]:
                visualize_outliers.visualize_outliers(non_outliers, outliers, bars=bars, diff_colors=diff_colors,
                                                      show=show, title="DBSCAN 1D Test")

    return True


def test_DBSCAN_2d(show=False):
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
        for diff_colors in [True, False]:
            visualize_outliers.visualize_outliers(non_outliers, outliers, bars=False, diff_colors=diff_colors,
                                                  show=show, title="DBSCAN 2D Test")

    return True


def test_DBSCAN_3d(show=False):
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
        for bars in [True, False]:
            for diff_colors in [True, False]:
                visualize_outliers.visualize_outliers(non_outliers, outliers, bars=bars, diff_colors=diff_colors,
                                                      show=show, title="DBSCAN 3D Test")

    return True


def test_KNN_1d(show=False):
    method_details = [
        {"method_name": "knn", "is_univariate": False, "cut_off": 0.15},
        {"method_name": "knn", "is_univariate": False, "cut_off": 0.25},
        {"method_name": "knn", "is_univariate": False, "cut_off": 0.35},
        {"method_name": "knn", "is_univariate": False, "cut_off": 0.45},
        ]

    for method_detail_individual in method_details:
        non_outliers, outliers = identify_outliers.return_outliers(data_df=data_df_1d.copy(),
                                                                   method_details=method_detail_individual)
        for bars in [True, False]:
            for diff_colors in [True, False]:
                visualize_outliers.visualize_outliers(non_outliers, outliers, bars=bars, diff_colors=diff_colors,
                                                      show=show, title="k-NN 1D Test")

    return True


def test_KNN_2d(show=False):
    method_details = [
        {"method_name": "knn", "is_univariate": False, "cut_off": 0.15},
        {"method_name": "knn", "is_univariate": False, "cut_off": 0.25},
        {"method_name": "knn", "is_univariate": False, "cut_off": 0.35},
        {"method_name": "knn", "is_univariate": False, "cut_off": 0.45},
        ]

    for method_detail_individual in method_details:
        non_outliers, outliers = identify_outliers.return_outliers(data_df=data_df_2d.copy(),
                                                                   method_details=method_detail_individual)
        for bars in [True, False]:
            for diff_colors in [True, False]:
                visualize_outliers.visualize_outliers(non_outliers, outliers, bars=bars, diff_colors=diff_colors,
                                                      show=show, title="k-NN 2D Test")

    return True


def test_KNN_3d(show=False):
    method_details = [
        {"method_name": "knn", "is_univariate": False, "cut_off": 0.15},
        {"method_name": "knn", "is_univariate": False, "cut_off": 0.25},
        {"method_name": "knn", "is_univariate": False, "cut_off": 0.35},
        {"method_name": "knn", "is_univariate": False, "cut_off": 0.45},
        ]

    for method_detail_individual in method_details:
        non_outliers, outliers = identify_outliers.return_outliers(data_df=data_df_3d.copy(),
                                                                   method_details=method_detail_individual)
        for bars in [True, False]:
            for diff_colors in [True, False]:
                visualize_outliers.visualize_outliers(non_outliers, outliers, bars=bars, diff_colors=diff_colors,
                                                      show=show, title="k-NN 1D Test")

    return True


# test_z_score_1d(show=True)
# test_boxplot_1d(show=True)
# test_DBSCAN_1d(show=True)
# test_DBSCAN_2d(show=True)
# test_DBSCAN_3d(show=True)
# test_KNN_1d(show=True)
# test_KNN_2d(show=True)
# test_KNN_3d(show=True)

# exit(0)
