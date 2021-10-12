from testing import testing_data_sets

from helper_functions.outlier_handlers import identify_outliers
from helper_functions.visualization import visualize_outliers

# Import our data sets
data_df_1d = testing_data_sets.data_df_1d.copy()
data_df_2d = testing_data_sets.data_df_2d.copy()
data_df_3d = testing_data_sets.data_df_3d.copy()


def test_z_score_1d(show=False):
    """

    :param show: Boolean of whether or not to plot the results of the process

    Test visualize outliers and original data using the z-score outlier detection method on one dimensional data

    """

    method_details = [{"method_name": "z-score", "z_value": 0.1, "is_univariate": True, "time_series": False},
                      {"method_name": "z-score", "z_value": 1, "is_univariate": True, "time_series": False},
                      {"method_name": "z-score", "z_value": 2, "is_univariate": True, "time_series": False},
                      {"method_name": "z-score", "z_value": 3, "is_univariate": True, "time_series": False},
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
    """

    :param show: Boolean of whether or not to plot the results of the process

    Test visualize outliers and original data using the boxplot outlier detection method on one dimensional data

    """

    method_details = [{"method_name": "boxplot", "outlier_type": "mild", "is_univariate": True, "time_series": False},
                      {"method_name": "boxplot", "outlier_type": "extreme", "is_univariate": True,
                       "time_series": False},
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
    """

    :param show: Boolean of whether or not to plot the results of the process

    Test visualize outliers and original data using the DBSCAN outlier detection method on one dimensional data

    """

    method_details = [
        {"method_name": "dbscan", "is_univariate": False, "algorithm": "auto", "eps": 0.5, "min_samples": 5,
         "time_series": False},
        {"method_name": "dbscan", "is_univariate": False, "algorithm": "auto", "eps": 1, "min_samples": 5,
         "time_series": False},
        {"method_name": "dbscan", "is_univariate": False, "algorithm": "auto", "eps": 0.5, "min_samples": 10,
         "time_series": False},
        {"method_name": "dbscan", "is_univariate": False, "algorithm": "ball_tree", "eps": 0.5, "min_samples": 1,
         "time_series": False},
        {"method_name": "dbscan", "is_univariate": False, "algorithm": "ball_tree", "eps": 0.5, "min_samples": 5,
         "time_series": False},
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
    """

    :param show: Boolean of whether or not to plot the results of the process

    Test visualize outliers and original data using the DBSCAN outlier detection method on two dimensional data

    """

    method_details = [
        {"method_name": "dbscan", "is_univariate": False, "algorithm": "auto", "eps": 0.5, "min_samples": 5,
         "time_series": False},
        {"method_name": "dbscan", "is_univariate": False, "algorithm": "auto", "eps": 1, "min_samples": 5,
         "time_series": False},
        {"method_name": "dbscan", "is_univariate": False, "algorithm": "auto", "eps": 0.5, "min_samples": 10,
         "time_series": False},
        {"method_name": "dbscan", "is_univariate": False, "algorithm": "ball_tree", "eps": 0.5, "min_samples": 1,
         "time_series": False},
        {"method_name": "dbscan", "is_univariate": False, "algorithm": "ball_tree", "eps": 0.5, "min_samples": 5,
         "time_series": False},
    ]

    for method_detail_individual in method_details:
        non_outliers, outliers = identify_outliers.return_outliers(data_df=data_df_2d.copy(),
                                                                   method_details=method_detail_individual)
        for diff_colors in [True, False]:
            visualize_outliers.visualize_outliers(non_outliers, outliers, bars=False, diff_colors=diff_colors,
                                                  show=show, title="DBSCAN 2D Test")

    return True


def test_DBSCAN_3d(show=False):
    """

    :param show: Boolean of whether or not to plot the results of the process

    Test visualize outliers and original data using the DBSCAN outlier detection method on three dimensional data

    """

    method_details = [
        {"method_name": "dbscan", "is_univariate": False, "algorithm": "auto", "eps": 0.5, "min_samples": 5,
         "time_series": False},
        {"method_name": "dbscan", "is_univariate": False, "algorithm": "auto", "eps": 1, "min_samples": 5,
         "time_series": False},
        {"method_name": "dbscan", "is_univariate": False, "algorithm": "auto", "eps": 0.5, "min_samples": 10,
         "time_series": False},
        {"method_name": "dbscan", "is_univariate": False, "algorithm": "ball_tree", "eps": 0.5, "min_samples": 1,
         "time_series": False},
        {"method_name": "dbscan", "is_univariate": False, "algorithm": "ball_tree", "eps": 0.5, "min_samples": 5,
         "time_series": False},
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
    """

    :param show: Boolean of whether or not to plot the results of the process

    Test visualize outliers and original data using the k-NN outlier detection method on one dimensional data

    """

    method_details = [
        {"method_name": "knn", "is_univariate": False, "cut_off": 0.15, "time_series": False},
        {"method_name": "knn", "is_univariate": False, "cut_off": 0.25, "time_series": False},
        {"method_name": "knn", "is_univariate": False, "cut_off": 0.35, "time_series": False},
        {"method_name": "knn", "is_univariate": False, "cut_off": 0.45, "time_series": False},
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
    """

    :param show: Boolean of whether or not to plot the results of the process

    Test visualize outliers and original data using the k-NN outlier detection method on two dimensional data

    """

    method_details = [
        {"method_name": "knn", "is_univariate": False, "cut_off": 0.15, "time_series": False},
        {"method_name": "knn", "is_univariate": False, "cut_off": 0.25, "time_series": False},
        {"method_name": "knn", "is_univariate": False, "cut_off": 0.35, "time_series": False},
        {"method_name": "knn", "is_univariate": False, "cut_off": 0.45, "time_series": False},
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
    """

    :param show: Boolean of whether or not to plot the results of the process

    Test visualize outliers and original data using the k-NN outlier detection method on three dimensional data

    """

    method_details = [
        {"method_name": "knn", "is_univariate": False, "cut_off": 0.15, "time_series": False},
        {"method_name": "knn", "is_univariate": False, "cut_off": 0.25, "time_series": False},
        {"method_name": "knn", "is_univariate": False, "cut_off": 0.35, "time_series": False},
        {"method_name": "knn", "is_univariate": False, "cut_off": 0.45, "time_series": False},
    ]

    for method_detail_individual in method_details:
        non_outliers, outliers = identify_outliers.return_outliers(data_df=data_df_3d.copy(),
                                                                   method_details=method_detail_individual)
        for bars in [True, False]:
            for diff_colors in [True, False]:
                visualize_outliers.visualize_outliers(non_outliers, outliers, bars=bars, diff_colors=diff_colors,
                                                      show=show, title="k-NN 1D Test")

    return True
