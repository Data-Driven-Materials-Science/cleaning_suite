import matplotlib.pyplot as plt
from helper_functions.outlier_handlers import identify_outliers
from testing import testing_data_sets
import pandas as pd
import numpy as np
import math
import random

df_time_series_four_component = testing_data_sets.data_df_time_series.copy()


def helper_for_testing(data_set_df, method_details, non_outlier_len, outliers_len):
    data_df = data_set_df
    non_outliers_df, outliers_df = identify_outliers.return_outliers(data_df=data_df, method_details=method_details)

    # print(len(non_outliers_df.index))
    # print(len(outliers_df.index))

    assert len(non_outliers_df.index) == non_outlier_len
    assert len(outliers_df.index) == outliers_len


def test_method1():
    data_df = df_time_series_four_component.copy()
    method_details = {"method_name": "isolation_forest", "is_univariate": False, "time_series": True}
    helper_for_testing(data_set_df=data_df, method_details=method_details, non_outlier_len=334, outliers_len=166)


def test_method2():
    data_df = df_time_series_four_component.copy().drop(["Component One"], axis=1)
    method_details = {"method_name": "isolation_forest", "is_univariate": False, "time_series": True}
    helper_for_testing(data_set_df=data_df, method_details=method_details, non_outlier_len=316, outliers_len=184)


def test_method3():
    data_df = df_time_series_four_component.copy().drop(["Component Two"], axis=1)
    method_details = {"method_name": "isolation_forest", "is_univariate": False, "time_series": True}
    helper_for_testing(data_set_df=data_df, method_details=method_details, non_outlier_len=347, outliers_len=153)


def test_method4():
    data_df = df_time_series_four_component.copy().drop(["Component Three"], axis=1)
    method_details = {"method_name": "isolation_forest", "is_univariate": False, "time_series": True}
    helper_for_testing(data_set_df=data_df, method_details=method_details, non_outlier_len=362, outliers_len=138)


def test_method5():
    data_df = df_time_series_four_component.copy().drop(["Component Four"], axis=1)
    method_details = {"method_name": "isolation_forest", "is_univariate": False, "time_series": True}
    helper_for_testing(data_set_df=data_df, method_details=method_details, non_outlier_len=199, outliers_len=301)


def test_method6():
    data_df = df_time_series_four_component.copy().drop(["Component Four", "Component Two", "Component Three"], axis=1)
    method_details = {"method_name": "isolation_forest", "is_univariate": False, "time_series": True}
    helper_for_testing(data_set_df=data_df, method_details=method_details, non_outlier_len=181, outliers_len=319)


def test_method7():
    data_df = df_time_series_four_component.copy().drop(["Component One", "Component Four", "Component Three"], axis=1)
    method_details = {"method_name": "isolation_forest", "is_univariate": False, "time_series": True}
    helper_for_testing(data_set_df=data_df, method_details=method_details, non_outlier_len=236, outliers_len=264)


def test_method8():
    data_df = df_time_series_four_component.copy().drop(["Component One", "Component Two", "Component Four"], axis=1)
    method_details = {"method_name": "isolation_forest", "is_univariate": False, "time_series": True}
    helper_for_testing(data_set_df=data_df, method_details=method_details, non_outlier_len=295, outliers_len=205)


def test_method9():
    data_df = df_time_series_four_component.copy().drop(["Component One", "Component Two", "Component Three"], axis=1)
    method_details = {"method_name": "isolation_forest", "is_univariate": False, "time_series": True}
    helper_for_testing(data_set_df=data_df, method_details=method_details, non_outlier_len=395, outliers_len=105)

