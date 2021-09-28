# Import the Necessary Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN

np.random.seed(10)

mu_cluster1_x, sigma_cluster1_x = 0.2, 0.1  # mean and standard deviation
mu_cluster1_y, sigma_cluster1_y = 0.2, 0.1  # mean and standard deviation
mu_cluster2_x, sigma_cluster2_x = 0.5, 0.05  # mean and standard deviation
mu_cluster2_y, sigma_cluster2_y = 0.8, 0.05  # mean and standard deviation
mu_cluster3_x, sigma_cluster3_x = 0.9, 0.05  # mean and standard deviation
mu_cluster3_y, sigma_cluster3_y = 0.1, 0.15  # mean and standard deviation
mu_outliers, sigma_outliers = 0.5, 0.25  # mean and standard deviation
outliers_x = np.random.normal(mu_outliers, sigma_outliers, 40)
outliers_y = np.random.normal(mu_outliers, sigma_outliers, 40)

data_x = np.append([], np.random.normal(mu_cluster1_x, sigma_cluster1_x, 100))
data_y = np.append([], np.random.normal(mu_cluster1_y, sigma_cluster1_y, 100))

data_x = np.append(data_x, np.random.normal(mu_cluster2_x, sigma_cluster2_x, 100))
data_y = np.append(data_y, np.random.normal(mu_cluster2_y, sigma_cluster2_y, 100))

data_x = np.append(data_x, np.random.normal(mu_cluster3_x, sigma_cluster3_x, 100))
data_y = np.append(data_y, np.random.normal(mu_cluster3_y, sigma_cluster3_y, 100))

data_x = np.append(data_x, outliers_x)
data_y = np.append(data_y, outliers_y)

data_df_2d = pd.DataFrame()

data_df_2d["Data X"] = data_x
data_df_2d["Data Y"] = data_y

# Raw Data Being Plotted
plt.scatter(data_df_2d["Data X"], data_df_2d["Data Y"], color="b")
plt.title("Raw Data Values")
plt.xlabel("Data Point X Values")
plt.ylabel("Data Point Y Values")
plt.savefig("./paper_images/3_cluster_DBSCAN_data_raw.png", dpi=500)
plt.show()

dbscan = DBSCAN(min_samples=20, eps=0.1).fit(data_df_2d.values.reshape(-1, 2))
dbscan_results = dbscan.labels_

combined_df = data_df_2d.copy()
combined_df["DBSCAN_Results"] = dbscan_results

unique_clusters = np.unique(dbscan_results)
print(unique_clusters)

colors = ["grey", "r", "g", "b"]
for cluster_value in unique_clusters:
    points_to_plot = combined_df[combined_df["DBSCAN_Results"] == cluster_value]
    if cluster_value == -1:
        label = "Outliers"
    else:
        label = "Cluster " + str(cluster_value)
    plt.scatter(points_to_plot["Data X"], points_to_plot["Data Y"], color=colors[cluster_value + 1], label=label)

plt.title("DBSCAN Example on 3 Cluster Dataset")
plt.xlabel("Data X Value")
plt.ylabel("Data Y Value")
plt.legend()
plt.savefig("./paper_images/3_cluster_DBSCAN_data_clustered.png", dpi=500)
plt.show()

exit(0)
