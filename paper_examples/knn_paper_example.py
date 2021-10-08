# Import the Necessary Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import NearestNeighbors

# Based on example from https://towardsdatascience.com/k-nearest-neighbors-knn-for-anomaly-detection-fdf8ee160d13

np.random.seed(10)

mu, sigma = 0, 1  # mean and standard deviation
mu_outliers, sigma_outliers = 20, 1  # mean and standard deviation

s_x = np.random.normal(mu, sigma, 100)
s_y = np.random.normal(mu, sigma, 100)
outliers_x = np.random.normal(mu_outliers, sigma_outliers, 4)
outliers_y = np.random.normal(mu_outliers, sigma_outliers, 4)
s_x = np.append(s_x, outliers_x)
s_y = np.append(s_y, outliers_y)

data_df_2d = pd.DataFrame()

data_df_2d["Data X"] = s_x
data_df_2d["Data Y"] = s_y

# Raw Data Being Plotted
plt.scatter(data_df_2d["Data X"], data_df_2d["Data Y"], color="b")
plt.title("Raw Data Values")
plt.xlabel("Data Point X Values")
plt.ylabel("Data Point Y Values")
plt.savefig("./paper_images/2d_knn_data_raw.png", dpi=500)
plt.show()

# Create Arrays
data_array = data_df_2d.values

# Create the class instance for the model
knn_model = NearestNeighbors(n_neighbors=4)
# Generate a model
knn_model.fit(data_array)

# Get the distances and indexes of every point that was fit using the model
distances, indexes = knn_model.kneighbors(data_array)

# Plot the distance threshold needed for each point to be marked as not an outlier
plt.plot(data_df_2d.index, distances.mean(axis=1), color="g")
plt.title("k-NN Distance Values")
plt.ylabel("Distance Values (d)")
plt.xlabel("Point Index")
plt.savefig("./paper_images/2d_knn_distance_values.png", dpi=500)
plt.show()

# Establish a cutoff where all points with a distance value above it are outliers
cutoff = 0.8
outlier_index = np.where(distances.mean(axis=1) > cutoff)

# filter outlier values
outlier_values = data_df_2d.iloc[outlier_index]

# plot data
plt.scatter(data_df_2d["Data X"], data_df_2d["Data Y"], color="b", label="Non Outliers")
# plot outlier values
plt.scatter(outlier_values["Data X"], outlier_values["Data Y"], color="r", label="Outliers")
plt.title("Non Outliers vs Outliers")
plt.xlabel("Data Point X Values")
plt.ylabel("Data Point Y Values")
plt.legend()
plt.savefig("./paper_images/2d_knn_outliers_result.png", dpi=500)
plt.show()

exit(0)
