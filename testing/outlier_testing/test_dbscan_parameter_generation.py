from helper_functions.outlier_handlers import dbscan_parameter_generation as DPG
from helper_functions.outlier_handlers import identify_outliers
from helper_functions.visualization import visualize_outliers
from testing import testing_data_sets as TDS


def test_set_one(show=False):
    """

    :param show: Boolean of whether or not to plot the results of the process

    :return: True if successful

    Assures that we generate parameters for the DBSCAN method based on a 1d data set

    """

    data_df = TDS.data_df_1d
    eps, min_neighbors = DPG.get_parameters(data_df)

    method_details = {"method_name": "dbscan", "is_univariate": False, "algorithm": "auto", "eps": eps,
                      "min_samples": min_neighbors, "time_series": False}

    non_outliers, outliers = identify_outliers.return_outliers(data_df=data_df.copy(),
                                                               method_details=method_details)
    visualize_outliers.visualize_outliers(non_outliers, outliers, bars=False, diff_colors=True,
                                          show=show, title="DBSCAN Auto Parameter Test - 1D", multiple_hists=True)

    return True


def test_set_two(show=False):
    """

    :param show: Boolean of whether or not to plot the results of the process

    :return: True if successful

    Assures that we generate parameters for the DBSCAN method based on a 3d data set

    """

    data_df = TDS.data_df_3d
    eps, min_neighbors = DPG.get_parameters(data_df)

    method_details = {"method_name": "dbscan", "is_univariate": False, "algorithm": "auto", "eps": eps,
                      "min_samples": min_neighbors, "time_series": False}

    non_outliers, outliers = identify_outliers.return_outliers(data_df=data_df.copy(),
                                                               method_details=method_details)
    visualize_outliers.visualize_outliers(non_outliers, outliers, bars=False, diff_colors=True,
                                          show=show, title="DBSCAN Auto Parameter Test - 3D", multiple_hists=True)

    return True
