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
    method_details = {"method_name": "isolation_forest", "is_univariate": False, "time_series": True, "random_state": 0}
    helper_for_testing(data_set_df=data_df, method_details=method_details, non_outlier_len=312, outliers_len=188)


def test_method2():
    data_df = df_time_series_four_component.copy().drop(["Component One"], axis=1)
    method_details = {"method_name": "isolation_forest", "is_univariate": False, "time_series": True, "random_state": 0}
    helper_for_testing(data_set_df=data_df, method_details=method_details, non_outlier_len=337, outliers_len=163)


def test_method3():
    data_df = df_time_series_four_component.copy().drop(["Component Two"], axis=1)
    method_details = {"method_name": "isolation_forest", "is_univariate": False, "time_series": True, "random_state": 0}
    helper_for_testing(data_set_df=data_df, method_details=method_details, non_outlier_len=349, outliers_len=151)


def test_method4():
    data_df = df_time_series_four_component.copy().drop(["Component Three"], axis=1)
    method_details = {"method_name": "isolation_forest", "is_univariate": False, "time_series": True, "random_state": 0}
    helper_for_testing(data_set_df=data_df, method_details=method_details, non_outlier_len=360, outliers_len=140)


def test_method5():
    data_df = df_time_series_four_component.copy().drop(["Component Four"], axis=1)
    method_details = {"method_name": "isolation_forest", "is_univariate": False, "time_series": True, "random_state": 0}
    helper_for_testing(data_set_df=data_df, method_details=method_details, non_outlier_len=195, outliers_len=305)


def test_method6():
    data_df = df_time_series_four_component.copy().drop(["Component Four", "Component Two", "Component Three"], axis=1)
    method_details = {"method_name": "isolation_forest", "is_univariate": False, "time_series": True, "random_state": 0}
    helper_for_testing(data_set_df=data_df, method_details=method_details, non_outlier_len=231, outliers_len=269)


def test_method7():
    data_df = df_time_series_four_component.copy().drop(["Component One", "Component Four", "Component Three"], axis=1)
    method_details = {"method_name": "isolation_forest", "is_univariate": False, "time_series": True, "random_state": 0}
    helper_for_testing(data_set_df=data_df, method_details=method_details, non_outlier_len=266, outliers_len=234)


def test_method8():
    data_df = df_time_series_four_component.copy().drop(["Component One", "Component Two", "Component Four"], axis=1)
    method_details = {"method_name": "isolation_forest", "is_univariate": False, "time_series": True, "random_state": 0}
    helper_for_testing(data_set_df=data_df, method_details=method_details, non_outlier_len=270, outliers_len=230)


def test_method9():
    data_df = df_time_series_four_component.copy().drop(["Component One", "Component Two", "Component Three"], axis=1)
    method_details = {"method_name": "isolation_forest", "is_univariate": False, "time_series": True, "random_state": 0}
    helper_for_testing(data_set_df=data_df, method_details=method_details, non_outlier_len=402, outliers_len=98)
