from helper_functions.outlier_handlers import identify_outliers
from testing import testing_data_sets
import matplotlib.pyplot as plt

# Import our data sets
data_df_1d = testing_data_sets.data_df_1d.copy()

intervals = testing_data_sets.one_dimensional_x_intervals.copy()


def test_method1(show=False):
    """

    :param show: Boolean of whether or not to plot the results of the process and the original data

    Runs boxplot outlier detection using the mild outlier type case.
    """

    data_df = data_df_1d.copy()

    if show:
        plt.hist(data_df[data_df_1d.columns[0]].values, bins=intervals, color="blue")
        plt.title("Original Data Set - Boxplot Outlier Detection")
        plt.xlabel("Data Point Value")
        plt.ylabel("Data Point Frequency")
        plt.show()

    method_details = {"method_name": "boxplot", "outlier_type": "mild", "is_univariate": True}

    non_outliers, outliers = identify_outliers.return_outliers(data_df=data_df, method_details=method_details)

    if show:
        plt.hist(non_outliers[non_outliers.columns[0]].values, bins=intervals, color="green")
        plt.hist(outliers[outliers.columns[0]].values, bins=intervals, color="red")
        plt.title("Outliers Detected From Original Set - Boxplot Outlier Detection")
        plt.xlabel("Data Point Value")
        plt.ylabel("Data Point Frequency")
        plt.show()

    assert len(non_outliers[outliers.columns[0]].values) == 100
    assert len(outliers[outliers.columns[0]].values) == 4

    return True


def test_method2(show=False):
    """

    :param show: Boolean of whether or not to plot the results of the process and the original data

    Runs boxplot outlier detection using the extreme outlier type case.
    """

    data_df = data_df_1d.copy()

    if show:
        plt.hist(data_df[data_df_1d.columns[0]].values, bins=intervals, color="blue")
        plt.title("Original Data Set - Boxplot Outlier Detection")
        plt.xlabel("Data Point Value")
        plt.ylabel("Data Point Frequency")
        plt.show()

    method_details = {"method_name": "boxplot", "outlier_type": "extreme", "is_univariate": True}

    non_outliers, outliers = identify_outliers.return_outliers(data_df=data_df, method_details=method_details)

    if show:
        plt.hist(non_outliers[outliers.columns[0]].values, bins=intervals, color="green")
        plt.hist(outliers[outliers.columns[0]].values, bins=intervals, color="red")
        plt.title("Outliers Detected From Original Set - Boxplot Outlier Detection")
        plt.xlabel("Data Point Value")
        plt.ylabel("Data Point Frequency")
        plt.show()

    assert len(non_outliers[outliers.columns[0]].values) == 100
    assert len(outliers[outliers.columns[0]].values) == 4

    return True
