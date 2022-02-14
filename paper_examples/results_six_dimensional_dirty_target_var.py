# Import the Necessary Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from paper_examples import figure_colors_key as ck
import random

np.random.seed(10)
num_points = 500
null_rate = 0.05
outlier_rate = 0.1
outlier_multiplier = 5

mu_x, sigma_x = 50, 8  # mean and standard deviation
low_y, high_y = 10.0, 100.0  # mean and standard deviation
mu_z, sigma_z = 98.6, 20.0  # mean and standard deviation
mu_a, sigma_a = 4.0, 5.0  # mean and standard deviation
mu_b, scale_b = 9, 2.0  # mean and standard deviation

data_x = np.random.normal(mu_x, sigma_x, num_points)
data_y = np.random.uniform(low_y, high_y, num_points)
data_z = np.random.normal(mu_z, sigma_z, num_points)
data_a = np.random.normal(mu_a, sigma_a, num_points)
data_b = np.random.wald(mu_b, scale_b, num_points)

for data_array in [data_x, data_y, data_z, data_a, data_b]:
    for i in range(num_points):
        if random.random() < null_rate:
            data_array[i] = None
            data_x[i] = None
        elif random.random() < outlier_rate:
            data_array[i] = (random.random() - 0.5) * outlier_multiplier * data_array[i]
            if data_z[i] is not None:
                data_z[i] = (random.random() - 0.5) * outlier_multiplier * data_z[i]

data_df = pd.DataFrame()

data_df["Data X"] = data_x
data_df["Data Y"] = data_y
data_df["Data Z"] = data_z
data_df["Data A"] = data_a
data_df["Data B"] = data_b
data_df["Data C"] = data_x + data_y + data_z + data_a + data_b

data_df.to_csv("../datasets/Results_SixDimensional_Datafile.csv", index=False)

# Raw Data Being Plotted
for col in data_df.columns:
    intervals = []
    interval_increment = (max(data_df[col].values) - min(data_df[col].values)) / 50.0

    accumulator = min(data_df[col].values) - interval_increment
    max_limit = max(data_df[col].values) + 2 * interval_increment

    while accumulator < max_limit:
        intervals.append(accumulator)
        accumulator = accumulator + interval_increment

    plt.hist(data_df[col], color=ck.raw_data_color, bins=intervals)
    plt.title("Raw Data Values - " + str(col))
    plt.xlabel(str(col) + " Value")
    plt.ylabel("Frequency")
    plt.savefig("./paper_images/results_6d_" + str(col) + ".png", dpi=500)
    plt.show()
