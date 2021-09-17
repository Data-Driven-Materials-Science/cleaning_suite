# import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import NearestNeighbors

# Taken from https://towardsdatascience.com/k-nearest-neighbors-knn-for-anomaly-detection-fdf8ee160d13

# import data
data = pd.read_csv("https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv")
# input data
df = data[["sepal_length", "sepal_width"]]

# scatterplot of inputs data
plt.scatter(df["sepal_length"], df["sepal_width"])
plt.show()

# create arrays
X = df.values

print(X)

# instantiate model
nbrs = NearestNeighbors(n_neighbors = 3)
# fit model
nbrs.fit(X)

# distances and indexes of k-neaighbors from model outputs
distances, indexes = nbrs.kneighbors(X)
# plot mean of k-distances of each observation
plt.plot(distances.mean(axis =1))
plt.title("k-NN Distance Values")
plt.ylabel("Distance Values")
plt.xlabel("Point Index")
plt.show()

# visually determine cutoff values > 0.15
outlier_index = np.where(distances.mean(axis = 1) > 0.15)
print(outlier_index)

# filter outlier values
outlier_values = df.iloc[outlier_index]
print(outlier_values)

# plot data
plt.scatter(df["sepal_length"], df["sepal_width"], color = "b", s = 65)
# plot outlier values
plt.scatter(outlier_values["sepal_length"], outlier_values["sepal_width"], color = "r")
plt.show()

exit(0)

