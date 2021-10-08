from testing import testing_data_sets

from helper_functions.outlier_handlers import identify_outliers
import matplotlib.pyplot as plt

# Import our data sets
data_df_2d = testing_data_sets.data_df_2d.copy()


def test_method1(show=False):
    """

    :param show: Boolean of whether or not to plot the results of the process and the original data

    Runs DBSCAN detection with the configuration of
    {"method_name": "dbscan", "is_univariate": False, "algorithm": "auto", "eps": 0.5, "min_samples": 5}
    """

    data_df = data_df_2d.copy()

    if show:
        plt.scatter(data_df[data_df.columns[0]].values, data_df[data_df.columns[1]], color="blue")
        plt.title("Original Data Set - DBSCAN 2D")
        plt.xlabel("Data Point X Value")
        plt.ylabel("Data Point Y Value")
        plt.show()

    method_details = {"method_name": "dbscan", "is_univariate": False, "algorithm": "auto", "eps": 0.5,
                      "min_samples": 5}

    non_outliers, outliers = identify_outliers.return_outliers(data_df=data_df, method_details=method_details)

    if show:
        plt.scatter(non_outliers[non_outliers.columns[0]].values, non_outliers[non_outliers.columns[1]], color="green")
        plt.scatter(outliers[outliers.columns[0]].values, outliers[outliers.columns[1]], color="red")
        plt.title("Outliers Detected From Original Set - DBSCAN 2D")
        plt.xlabel("Data Point X Value")
        plt.ylabel("Data Point Y Value")
        plt.show()

    assert len(non_outliers[non_outliers.columns[0]].values) == 75
    assert len(outliers[outliers.columns[0]].values) == 29

    return True


def test_method2(show=False):
    """

    :param show: Boolean of whether or not to plot the results of the process and the original data

    Runs DBSCAN detection with the configuration of
    {"method_name": "dbscan", "is_univariate": False, "algorithm": "auto", "eps": 1, "min_samples": 5}
    """

    data_df = data_df_2d.copy()

    if show:
        plt.scatter(data_df[data_df.columns[0]].values, data_df[data_df.columns[1]], color="blue")
        plt.title("Original Data Set - DBSCAN 2D")
        plt.xlabel("Data Point X Value")
        plt.ylabel("Data Point Y Value")
        plt.show()

    method_details = {"method_name": "dbscan", "is_univariate": False, "algorithm": "auto", "eps": 1, "min_samples": 5}

    non_outliers, outliers = identify_outliers.return_outliers(data_df=data_df, method_details=method_details)

    if show:
        plt.scatter(non_outliers[non_outliers.columns[0]].values, non_outliers[non_outliers.columns[1]], color="green")
        plt.scatter(outliers[outliers.columns[0]].values, outliers[outliers.columns[1]], color="red")
        plt.title("Outliers Detected From Original Set - DBSCAN 2D")
        plt.xlabel("Data Point X Value")
        plt.ylabel("Data Point Y Value")
        plt.show()

    assert len(non_outliers[non_outliers.columns[0]].values) == 99
    assert len(outliers[outliers.columns[0]].values) == 5

    return True


def test_method3(show=False):
    """

    :param show: Boolean of whether or not to plot the results of the process and the original data

    Runs DBSCAN detection with the configuration of
    {"method_name": "dbscan", "is_univariate": False, "algorithm": "auto", "eps": 0.5, "min_samples": 10}
    """

    data_df = data_df_2d.copy()

    if show:
        plt.scatter(data_df[data_df.columns[0]].values, data_df[data_df.columns[1]], color="blue")
        plt.title("Original Data Set - DBSCAN 2D")
        plt.xlabel("Data Point X Value")
        plt.ylabel("Data Point Y Value")
        plt.show()

    method_details = {"method_name": "dbscan", "is_univariate": False, "algorithm": "auto", "eps": 0.5,
                      "min_samples": 10}

    non_outliers, outliers = identify_outliers.return_outliers(data_df=data_df, method_details=method_details)

    if show:
        plt.scatter(non_outliers[non_outliers.columns[0]].values, non_outliers[non_outliers.columns[1]], color="green")
        plt.scatter(outliers[outliers.columns[0]].values, outliers[outliers.columns[1]], color="red")
        plt.title("Outliers Detected From Original Set - DBSCAN 2D")
        plt.xlabel("Data Point X Value")
        plt.ylabel("Data Point Y Value")
        plt.show()

    assert len(non_outliers[non_outliers.columns[0]].values) == 63
    assert len(outliers[outliers.columns[0]].values) == 41

    return True


def test_method4(show=False):
    """

    :param show: Boolean of whether or not to plot the results of the process and the original data

    Runs DBSCAN detection with the configuration of
    {"method_name": "dbscan", "is_univariate": False, "algorithm": "ball_tree", "eps": 0.5, "min_samples": 1}
    """

    data_df = data_df_2d.copy()

    if show:
        plt.scatter(data_df[data_df.columns[0]].values, data_df[data_df.columns[1]], color="blue")
        plt.title("Original Data Set - DBSCAN 2D")
        plt.xlabel("Data Point X Value")
        plt.ylabel("Data Point Y Value")
        plt.show()

    method_details = {"method_name": "dbscan", "is_univariate": False, "algorithm": "ball_tree", "eps": 0.5,
                      "min_samples": 1}

    non_outliers, outliers = identify_outliers.return_outliers(data_df=data_df, method_details=method_details)

    if show:
        plt.scatter(non_outliers[non_outliers.columns[0]].values, non_outliers[non_outliers.columns[1]], color="green")
        plt.scatter(outliers[outliers.columns[0]].values, outliers[outliers.columns[1]], color="red")
        plt.title("Outliers Detected From Original Set - DBSCAN 2D")
        plt.xlabel("Data Point X Value")
        plt.ylabel("Data Point Y Value")
        plt.show()

    assert len(non_outliers[non_outliers.columns[0]].values) == 104
    assert len(outliers[outliers.columns[0]].values) == 0

    return True


def test_method5(show=False):
    """

    :param show: Boolean of whether or not to plot the results of the process and the original data

    Runs DBSCAN detection with the configuration of
    {"method_name": "dbscan", "is_univariate": False, "algorithm": "auto", "eps": 0.5, "min_samples": 5}
    """

    data_df = data_df_2d.copy()

    if show:
        plt.scatter(data_df[data_df.columns[0]].values, data_df[data_df.columns[1]], color="blue")
        plt.title("Original Data Set - DBSCAN 2D")
        plt.xlabel("Data Point X Value")
        plt.ylabel("Data Point Y Value")
        plt.show()

    method_details = {"method_name": "dbscan", "is_univariate": False, "algorithm": "ball_tree", "eps": 0.5,
                      "min_samples": 5}

    non_outliers, outliers = identify_outliers.return_outliers(data_df=data_df, method_details=method_details)

    if show:
        plt.scatter(non_outliers[non_outliers.columns[0]].values, non_outliers[non_outliers.columns[1]], color="green")
        plt.scatter(outliers[outliers.columns[0]].values, outliers[outliers.columns[1]], color="red")
        plt.title("Outliers Detected From Original Set - DBSCAN 2D")
        plt.xlabel("Data Point X Value")
        plt.ylabel("Data Point Y Value")
        plt.show()

    assert len(non_outliers[non_outliers.columns[0]].values) == 75
    assert len(outliers[outliers.columns[0]].values) == 29

    return True
