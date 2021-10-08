from testing import testing_data_sets

from helper_functions.outlier_handlers import identify_outliers
import matplotlib.pyplot as plt

# Import our data sets
data_df_2d = testing_data_sets.data_df_2d.copy()


def helper_test_method(method_details, outlier_num, non_outlier_num, show=False):
    """

    :param method_details: The details of the method configuration we are running
    :param outlier_num: The number of expected outliers
    :param non_outlier_num: The number of expected non outliers
    :param show: Boolean of whether or not to plot the results of the process and the original data

    Runs k-NN detection with the configuration of method_details
    """

    data_df = data_df_2d.copy()

    if show:
        plt.scatter(data_df[data_df.columns[0]].values, data_df[data_df.columns[1]], color="blue")
        plt.title("Original Data Set - k-NN 2D")
        plt.xlabel("Data Point X Value")
        plt.ylabel("Data Point Y Value")
        plt.show()

    non_outliers, outliers = identify_outliers.return_outliers(data_df=data_df, method_details=method_details)

    if show:
        plt.scatter(non_outliers[non_outliers.columns[0]].values, non_outliers[non_outliers.columns[1]], color="green")
        plt.scatter(outliers[outliers.columns[0]].values, outliers[outliers.columns[1]], color="red")
        plt.title("Outliers Detected From Original Set - k-NN 2D")
        plt.xlabel("Data Point X Value")
        plt.ylabel("Data Point Y Value")
        plt.show()

    assert len(non_outliers[non_outliers.columns[0]].values) == non_outlier_num
    assert len(outliers[outliers.columns[0]].values) == outlier_num

    return True


def test_method1(show=False):
    """

    :param show: Boolean of whether or not to plot the results of the process and the original data

    Runs k-NN detection with the configuration of
    {"method_name": "knn", "is_univariate": False, "cut_off": 0.15}
    """

    return helper_test_method(method_details={"method_name": "knn", "is_univariate": False, "cut_off": 0.15}, show=show,
                              outlier_num=52, non_outlier_num=52)


def test_method2(show=False):
    """

    :param show: Boolean of whether or not to plot the results of the process and the original data

    Runs k-NN detection with the configuration of
    {"method_name": "knn", "is_univariate": False, "cut_off": 0.25}
    """

    return helper_test_method(method_details={"method_name": "knn", "is_univariate": False, "cut_off": 0.25}, show=show,
                              outlier_num=24, non_outlier_num=80)


def test_method3(show=False):
    """

    :param show: Boolean of whether or not to plot the results of the process and the original data

    Runs k-NN detection with the configuration of
    {"method_name": "knn", "is_univariate": False, "cut_off": 0.35}
    """

    return helper_test_method(method_details={"method_name": "knn", "is_univariate": False, "cut_off": 0.35}, show=show,
                              outlier_num=20, non_outlier_num=84)


def test_method4(show=False):
    """

    :param show: Boolean of whether or not to plot the results of the process and the original data

    Runs k-NN detection with the configuration of
    {"method_name": "knn", "is_univariate": False, "cut_off": 0.45}
    """

    return helper_test_method(method_details={"method_name": "knn", "is_univariate": False, "cut_off": 0.45}, show=show,
                              outlier_num=11, non_outlier_num=93)


def test_method5(show=False):
    """

    :param show: Boolean of whether or not to plot the results of the process and the original data

    Runs k-NN detection with the configuration of
    {"method_name": "knn", "is_univariate": False, "cut_off": 0.55}
    """

    return helper_test_method(method_details={"method_name": "knn", "is_univariate": False, "cut_off": 0.55}, show=show,
                              outlier_num=7, non_outlier_num=97)


def test_method6(show=False):
    """

    :param show: Boolean of whether or not to plot the results of the process and the original data

    Runs k-NN detection with the configuration of
    {"method_name": "knn", "is_univariate": False, "cut_off": 0.65}
    """

    return helper_test_method(method_details={"method_name": "knn", "is_univariate": False, "cut_off": 0.65}, show=show,
                              outlier_num=6, non_outlier_num=98)
