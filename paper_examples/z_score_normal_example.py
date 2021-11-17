import numpy as np
import pandas as pd
from helper_functions.outlier_handlers import identify_outliers
import matplotlib.pyplot as plt
from paper_examples import figure_colors_key as ck

np.random.seed(10)

mu, sigma = 0, 1  # mean and standard deviation
mu_outliers, sigma_outliers = 20, 1  # mean and standard deviation

s_x = np.random.normal(mu, sigma, 100)

outliers_x = np.random.normal(mu_outliers, sigma_outliers, 4)

s_x = np.append(s_x, outliers_x)

data_df_1d = pd.DataFrame()

data_df_1d["Data X"] = s_x

one_dimensional_x_intervals = []
interval_increment = 0.25

accumulator = min(s_x) - interval_increment
max_limit = max(s_x) + 2 * interval_increment

while accumulator < max_limit:
    one_dimensional_x_intervals.append(accumulator)
    accumulator = accumulator + interval_increment

plt.hist(data_df_1d[data_df_1d.columns[0]].values, bins=one_dimensional_x_intervals, color=ck.raw_data_color)
plt.title("Original Data Set - Z-Score Outlier Detection")
plt.xlabel("Data Point Value")
plt.ylabel("Data Point Frequency")
plt.savefig("./paper_images/z_score_normal_raw_data.png", dpi=500)
plt.show()

method_details = {"method_name": "z-score", "z_value": 3, "is_univariate": True}

non_outliers, outliers = identify_outliers.return_outliers(data_df=data_df_1d, method_details=method_details)

plt.hist(non_outliers[non_outliers.columns[0]].values, bins=one_dimensional_x_intervals,
         color=ck.resulting_data_colors[0], label="Not Outliers")
plt.hist(outliers[outliers.columns[0]].values, bins=one_dimensional_x_intervals, color=ck.outlier_color,
         label="Outliers")
plt.title("Outliers Detected From Original Set - Z-Score Outlier Detection")
plt.xlabel("Data Point Value")
plt.ylabel("Data Point Frequency")
plt.legend()
plt.savefig("./paper_images/z_score_normal_outliers.png", dpi=500)
plt.show()

exit(0)
