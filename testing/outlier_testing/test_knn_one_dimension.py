from testing import testing_data_sets

from helper_functions.outlier_handlers import identify_outliers
import matplotlib.pyplot as plt

# Import our data sets
data_df_1d = testing_data_sets.data_df_1d.copy()

intervals = testing_data_sets.one_dimensional_x_intervals.copy()


def test_method1(show=False):
    """

    :param show: Boolean of whether or not to plot the results of the process and the original data

    Runs k-NN detection with the configuration of
    {"method_name": "knn", "is_univariate": False, "cut_off": 0.15}
    """

    data_df = data_df_1d.copy()

    if show:
        plt.hist(data_df[data_df.columns[0]].values, bins=intervals, color="blue")
        plt.title("Original Data Set - k-NN 1D")
        plt.xlabel("Data Point Value")
        plt.ylabel("Data Point Frequency")
        plt.show()

    method_details = {"method_name": "knn", "is_univariate": False, "cut_off": 0.15, "time_series": False}

    non_outliers, outliers = identify_outliers.return_outliers(data_df=data_df, method_details=method_details)

    if show:
        plt.hist(non_outliers[non_outliers.columns[0]].values, bins=intervals, color="green")
        plt.hist(outliers[outliers.columns[0]].values, bins=intervals, color="red")
        plt.title("Outliers Detected From Original Set - k-NN 1D")
        plt.xlabel("Data Point Value")
        plt.ylabel("Data Point Frequency")
        plt.show()

    assert len(non_outliers[non_outliers.columns[0]].values) == 99
    assert len(outliers[outliers.columns[0]].values) == 5

    return True


def test_method2(show=False):
    """

    :param show: Boolean of whether or not to plot the results of the process and the original data

    Runs k-NN detection with the configuration of
    {"method_name": "knn", "is_univariate": False, "cut_off": 0.25}
    """

    data_df = data_df_1d.copy()

    if show:
        plt.hist(data_df[data_df.columns[0]].values, bins=intervals, color="blue")
        plt.title("Original Data Set - k-NN 1D")
        plt.xlabel("Data Point Value")
        plt.ylabel("Data Point Frequency")
        plt.show()

    method_details = {"method_name": "knn", "is_univariate": False, "cut_off": 0.25, "time_series": False}

    non_outliers, outliers = identify_outliers.return_outliers(data_df=data_df, method_details=method_details)

    if show:
        plt.hist(non_outliers[non_outliers.columns[0]].values, bins=intervals, color="green")
        plt.hist(outliers[outliers.columns[0]].values, bins=intervals, color="red")
        plt.title("Outliers Detected From Original Set - k-NN 1D")
        plt.xlabel("Data Point Value")
        plt.ylabel("Data Point Frequency")
        plt.show()

    assert len(non_outliers[non_outliers.columns[0]].values) == 100
    assert len(outliers[outliers.columns[0]].values) == 4

    return True


def test_method3(show=False):
    """

    :param show: Boolean of whether or not to plot the results of the process and the original data

    Runs k-NN detection with the configuration of
    {"method_name": "knn", "is_univariate": False, "cut_off": 0.35}
    """

    data_df = data_df_1d.copy()

    if show:
        plt.hist(data_df[data_df.columns[0]].values, bins=intervals, color="blue")
        plt.title("Original Data Set - k-NN 1D")
        plt.xlabel("Data Point Value")
        plt.ylabel("Data Point Frequency")
        plt.show()

    method_details = {"method_name": "knn", "is_univariate": False, "cut_off": 0.35, "time_series": False}

    non_outliers, outliers = identify_outliers.return_outliers(data_df=data_df, method_details=method_details)

    if show:
        plt.hist(non_outliers[non_outliers.columns[0]].values, bins=intervals, color="green")
        plt.hist(outliers[outliers.columns[0]].values, bins=intervals, color="red")
        plt.title("Outliers Detected From Original Set - k-NN 1D")
        plt.xlabel("Data Point Value")
        plt.ylabel("Data Point Frequency")
        plt.show()

    assert len(non_outliers[non_outliers.columns[0]].values) == 100
    assert len(outliers[outliers.columns[0]].values) == 4

    return True


def test_method4(show=False):
    """

    :param show: Boolean of whether or not to plot the results of the process and the original data

    Runs k-NN detection with the configuration of
    {"method_name": "knn", "is_univariate": False, "cut_off": 0.45}
    """

    data_df = data_df_1d.copy()

    if show:
        plt.hist(data_df[data_df.columns[0]].values, bins=intervals, color="blue")
        plt.title("Original Data Set - k-NN 1D")
        plt.xlabel("Data Point Value")
        plt.ylabel("Data Point Frequency")
        plt.show()

    method_details = {"method_name": "knn", "is_univariate": False, "cut_off": 0.45, "time_series": False}

    non_outliers, outliers = identify_outliers.return_outliers(data_df=data_df, method_details=method_details)

    if show:
        plt.hist(non_outliers[non_outliers.columns[0]].values, bins=intervals, color="green")
        plt.hist(outliers[outliers.columns[0]].values, bins=intervals, color="red")
        plt.title("Outliers Detected From Original Set - k-NN 1D")
        plt.xlabel("Data Point Value")
        plt.ylabel("Data Point Frequency")
        plt.show()

    assert len(non_outliers[non_outliers.columns[0]].values) == 102
    assert len(outliers[outliers.columns[0]].values) == 2

    return True
