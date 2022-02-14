# Import the Necessary Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from paper_examples import figure_colors_key as ck
import random

np.random.seed(10)
num_points = 500
null_rate = 0.06
outlier_rate = 0.06
outlier_multiplier = 5

mu_x, sigma_x = 50, 8  # mean and standard deviation
data_x = np.random.normal(mu_x, sigma_x, num_points)

for i in range(num_points):
    if random.random() < null_rate:
        data_x[i] = None
    elif random.random() < outlier_rate:
        data_x[i] = (random.random() - 0.5) * outlier_multiplier * data_x[i]

data_df = pd.DataFrame()

data_df["Data X"] = data_x

data_df.to_csv("../datasets/Results_OneDimensional_Datafile.csv", index=False)

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
    plt.savefig("./paper_images/results_1d_" + str(col) + ".png", dpi=500)
    plt.show()
