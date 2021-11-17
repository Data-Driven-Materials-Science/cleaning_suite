from kneebow.rotor import Rotor
from sklearn.neighbors import NearestNeighbors
import numpy as np
import pandas as pd

"""
Resources:
https://towardsdatascience.com/machine-learning-clustering-dbscan-determine-the-optimal-value-for-epsilon-eps-python-example-3100091cfbc
https://medium.com/@tarammullin/dbscan-parameter-estimation-ff8330e3a3bd

"""


def get_parameters(data_df):
    neighbors = NearestNeighbors()
    neighbors_fit = neighbors.fit(data_df)
    distances, indices = neighbors_fit.kneighbors(data_df)

    index_values = data_df.index

    distances = np.sort(distances, axis=0)
    distances = distances[:, 1]

    distances_df = pd.DataFrame()
    distances_df["Index"] = index_values
    distances_df["Distances"] = distances

    data_with_indices = distances_df.values

    rotor = Rotor()
    rotor.fit_rotate(data_with_indices)

    elbow_idx = rotor.get_elbow_index()

    eps = distances[elbow_idx]
    min_neighbors = len(data_df.columns) * 2

    return eps, min_neighbors
