from testing import testing_data_sets

from helper_functions.outlier_handlers import identify_outliers
from helper_functions.report_generators import outlier_report_generator

# Import our data sets
data_df_1d = testing_data_sets.data_df_1d.copy()
data_df_2d = testing_data_sets.data_df_1d.copy()
data_df_3d = testing_data_sets.data_df_1d.copy()


def test_z_score_1d(print_results=False):
    """

    :param print_results: A boolean of whether or not to print the results of the process

    Test the z-score outlier detection method using one dimensional data

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
        if print_results:
            print(det1)
            print(det2)

    return True


def test_boxplot_1d(print_results=False):
    """

    :param print_results: A boolean of whether or not to print the results of the process

    Test the boxplot outlier detection method using one dimensional data

    """

    method_details = [{"method_name": "boxplot", "outlier_type": "mild", "is_univariate": True},
                      {"method_name": "boxplot", "outlier_type": "extreme", "is_univariate": True},
                      ]
    for method_detail_individual in method_details:
        non_outliers, outliers = identify_outliers.return_outliers(data_df=data_df_1d.copy(),
                                                                   method_details=method_detail_individual)
        det1, det2 = outlier_report_generator.generate_report(data_df=non_outliers, outlier_df=outliers)
        if print_results:
            print(det1)
            print(det2)

    return True


def test_DBSCAN_1d(print_results=False):
    """

    :param print_results: A boolean of whether or not to print the results of the process

    Test the DBSCAN outlier detection method using one dimensional data

    """

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
        if print_results:
            print(det1)
            print(det2)

    return True


def test_DBSCAN_2d(print_results=False):
    """

    :param print_results: A boolean of whether or not to print the results of the process

    Test the DBSCAN outlier detection method using two dimensional data

    """

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
        if print_results:
            print(det1)
            print(det2)

    return True


def test_DBSCAN_3d(print_results=False):
    """

    :param print_results: A boolean of whether or not to print the results of the process

    Test the DBSCAN outlier detection method using three dimensional data

    """

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
        if print_results:
            print(det1)
            print(det2)

    return True


def test_KNN_1d(print_results=False):
    """

    :param print_results: A boolean of whether or not to print the results of the process

    Test the k-NN outlier detection method using one dimensional data

    """

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
        if print_results:
            print(det1)
            print(det2)

    return True


def test_KNN_2d(print_results=False):
    """

    :param print_results: A boolean of whether or not to print the results of the process

    Test the k-NN outlier detection method using two dimensional data

    """

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
        if print_results:
            print(det1)
            print(det2)

    return True


def test_KNN_3d(print_results=False):
    """

    :param print_results: A boolean of whether or not to print the results of the process

    Test the k-NN outlier detection method using three dimensional data

    """

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
        if print_results:
            print(det1)
            print(det2)

    return True
