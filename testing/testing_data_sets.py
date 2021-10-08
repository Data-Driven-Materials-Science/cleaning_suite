import numpy as np
import pandas as pd
import math
import random

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

# Data sets that have varying dimensionality with most points centered around origin and 4 points 20 units away in each
# direction
data_df_1d = pd.DataFrame()
data_df_2d = pd.DataFrame()
data_df_3d = pd.DataFrame()

data_df_1d["Data X"] = s_x
data_df_2d["Data X"] = s_x
data_df_3d["Data X"] = s_x

data_df_2d["Data Y"] = s_y
data_df_3d["Data Y"] = s_y

data_df_3d["Data Z"] = s_z

# Intervals for hardcoded histograms in tests which just test outlier detection are calculated here
one_dimensional_x_intervals = []
interval_increment = 0.25

accumulator = min(s_x) - interval_increment
max_limit = max(s_x) + 2 * interval_increment

while accumulator < max_limit:
    one_dimensional_x_intervals.append(accumulator)
    accumulator = accumulator + interval_increment

""" Time Series Data set """

random.seed(0)

num_points = 500

x_values = np.linspace(0.0, math.pi * 4, num_points)
data_one_component = np.sin(x_values) + np.random.normal(0, 0.1, num_points)
data_two_component = np.cos(x_values) + np.random.normal(0, 0.1, num_points)
data_three_component = np.linspace(0, 20, num_points) + np.random.normal(0, 0.1, num_points)
data_four_component = np.random.normal(0, 0.1, num_points) + np.random.normal(0, 0.1, num_points)

outlier_probability = 0.03

data_df_time_series = pd.DataFrame()
# data_df["X Values"] = x_values
data_df_time_series["Component One"] = data_one_component
data_df_time_series["Component Two"] = data_two_component
data_df_time_series["Component Three"] = data_three_component
data_df_time_series["Component Four"] = data_four_component
