# Import the Necessary Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from paper_examples import figure_colors_key as ck
import random
import math

np.random.seed(10)
num_points = 500
null_rate = 0.05
outlier_rate = 0.1
outlier_multiplier = 5

angle_range_x, noise_low_x, noise_high_x = 5*math.pi, 0.2, 3.0  # mean and standard deviation
angle_range_y, noise_low_y, noise_high_y = 35*math.pi, 0.0, 0.1  # mean and standard deviation
angle_range_z, noise_low_z, noise_high_z = 2*math.pi, 1.1, 1.3  # mean and standard deviation
angle_range_a, noise_low_a, noise_high_a = 90*math.pi, 4.2, 8.2  # mean and standard deviation

data_x = np.sin(np.linspace(0, angle_range_x, num_points)) + np.random.uniform(noise_low_x, noise_high_x)
data_y = np.sin(np.linspace(0, angle_range_y, num_points)) + np.random.uniform(noise_low_y, noise_high_y)
data_z = np.cos(np.linspace(0, angle_range_z, num_points)) + np.random.uniform(noise_low_z, noise_high_z)
data_a = np.cos(np.linspace(0, angle_range_a, num_points)) + np.random.uniform(noise_low_a, noise_high_a)

for data_array in [data_x, data_y, data_z, data_a]:
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

data_df.to_csv("../datasets/Results_FourDimensional_Datafile.csv", index=False)

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
    plt.savefig("./paper_images/results_4d_" + str(col) + ".png", dpi=500)
    plt.show()
