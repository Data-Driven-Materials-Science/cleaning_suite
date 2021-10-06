import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import IsolationForest
import pandas as pd
import numpy as np
import math
import random

random.seed(0)
num_points = 500

x_values = np.linspace(0.0, math.pi * 4, num_points)
data_one_component = np.sin(x_values) + np.random.normal(0, 0.1, num_points)
data_two_component = np.cos(x_values) + np.random.normal(0, 0.1, num_points)
data_three_component = np.linspace(0, 20, num_points) + np.random.normal(0, 0.1, num_points)
data_four_component = np.random.normal(0, 0.1, num_points) + np.random.normal(0, 0.1, num_points)

outlier_probability = 0.03

data_df = pd.DataFrame()
data_df["X Values"] = x_values
data_df["Component One"] = data_one_component
data_df["Component Two"] = data_two_component
data_df["Component Three"] = data_three_component
data_df["Component Four"] = data_four_component
data_df["Total"] = [False for i in range(num_points)]

for column in data_df.columns:
    if column != "X Values" and column != "Total":
        for i in range(0, len(data_df[column].values)):
            if random.uniform(0, 1) < outlier_probability:
                data_df[column][i] = data_df[column][i] + random.uniform(-10, 10)

for column in data_df.columns:
    if column != "X Values" and column != "Total":
        plt.plot(data_df["X Values"], data_df[column])
        plt.xlabel("X Value")
        plt.ylabel(column)
        plt.title("X Value vs " + column)
        plt.savefig("./paper_images/IsolationForestRawData_" + column + ".png", dpi=500)
        plt.show()

# Generate a DataFrame that only has the data columns
only_components = pd.DataFrame()
only_components["C One"] = data_df["Component One"].copy()
only_components["C Two"] = data_df["Component Two"].copy()
only_components["C Three"] = data_df["Component Three"].copy()
only_components["C Four"] = data_df["Component Four"].copy()
resulting_data_set = only_components.values

# Generate the necessary class
scaler = StandardScaler()
np_scaled = scaler.fit_transform(resulting_data_set.reshape(-1, 4))
data = pd.DataFrame(np_scaled)
# Train the isolation forest model
model = IsolationForest()
model.fit(data)

data_df["anomaly"] = model.predict(data)
a = data_df.loc[data_df["anomaly"] == -1, ["Total"]]  # anomaly

# Visualization
fig, ax = plt.subplots(4, figsize=(20, 12))

columns = ["Component One", "Component Two", "Component Three", "Component Four"]
for i in range(0, 4):
    ax[i].plot(data_df.index, data_df[str(columns[i])], color="black", label="Normal")
    ax[i].scatter(a.index, data_df[str(columns[i])][a.index], color="red", label="Anomaly")
    ax[i].set_xlabel("Point Index")
    ax[i].set_ylabel(str(columns[i]))
    ax[i].legend()
    ax[i].set_title("Time Series Outlier Detection Using Isolation Forest - " + str(columns[i]))

# ax[0].plot(data_df.index, data_df['Component One'], color='black', label='Normal')
# ax[1].plot(data_df.index, data_df['Component Two'], color='black', label='Normal')
# ax[2].plot(data_df.index, data_df['Component Three'], color='black', label='Normal')
# ax[3].plot(data_df.index, data_df['Component Four'], color='black', label='Normal')
# ax[0].scatter(a.index, data_df['Component One'][a.index], color='red', label='Anomaly')
# ax[1].scatter(a.index, data_df['Component Two'][a.index], color='red', label='Anomaly')
# ax[2].scatter(a.index, data_df['Component Three'][a.index], color='red', label='Anomaly')
# ax[3].scatter(a.index, data_df['Component Four'][a.index], color='red', label='Anomaly')
# ax[0].set_xlabel("Point Index")
# ax[1].set_xlabel("Point Index")
# ax[2].set_xlabel("Point Index")
# ax[3].set_xlabel("Point Index")
# ax[0].set_ylabel("Component One")
# ax[1].set_ylabel("Component Two")
# ax[2].set_ylabel("Component Three")
# ax[3].set_ylabel("Component Four")
# ax[0].legend()
# ax[1].legend()
# ax[2].legend()
# ax[3].legend()
# ax[0].set_title("Time Series Outlier Detection Using Isolation Forest - Component One")
# ax[1].set_title("Time Series Outlier Detection Using Isolation Forest - Component Two")
# ax[2].set_title("Time Series Outlier Detection Using Isolation Forest - Component Three")
# ax[3].set_title("Time Series Outlier Detection Using Isolation Forest - Component Four")
plt.tight_layout(h_pad=3.0)
plt.savefig("./paper_images/IsolationForestOutlierDetectionResults", dpi=500)
plt.show()

exit(0)
