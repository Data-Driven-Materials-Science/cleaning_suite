import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import IsolationForest
import pandas as pd
import numpy as np
import math

x_values = np.linspace(0.0, math.pi * 4, 100)
base_values = np.sin(x_values)
noise_component = np.random.normal(0, 0.1, 100)

# Making outliers:
noise_component[10] = noise_component[10] + 1
noise_component[17] = noise_component[17] - 0.5
noise_component[39] = noise_component[39] - 2.8
noise_component[55] = noise_component[55] + 2.8
noise_component[69] = noise_component[69] - 0.9

resulting_data_set = base_values + noise_component

# data_df = pd.DataFrame()
# data_df["X Values"] = x_values
# data_df["Series"] = resulting_data_set

plt.rc('figure', figsize=(12, 8))
plt.rc('font', size=15)
result = seasonal_decompose(resulting_data_set, model='additive', period=2)
fig = result.plot()

plt.show()

plt.rc('figure', figsize=(12, 6))
plt.rc('font', size=15)
fig, ax = plt.subplots()
x = x_values
y = result.resid
ax.plot(x, y, color='black', linestyle='--', marker="o")
# ax.annotate('Anomaly', (mdates.date2num(x[35]), y[35]), xytext=(30, 20),
#             textcoords='offset points', color='red', arrowprops=dict(facecolor='red', arrowstyle='fancy'))
plt.axvline(x_values[10])
plt.axvline(x_values[17])
plt.axvline(x_values[39])
plt.axvline(x_values[69])

plt.show()

data_df = pd.DataFrame()
data_df["X Values"] = x_values
data_df["Series"] = resulting_data_set
data_df["Total"] = [False for i in range(100)]

# outliers_fraction = float(.5)
scaler = StandardScaler()
np_scaled = scaler.fit_transform(resulting_data_set.reshape(-1, 1))
data = pd.DataFrame(np_scaled)
# train isolation forest
model = IsolationForest()
model.fit(data)

data_df['anomaly'] = model.predict(data)
# anomaly_values = model.predict(resulting_data_set)
# visualization
fig, ax = plt.subplots(figsize=(10, 6))
a = data_df.loc[data_df['anomaly'] == -1, ['Total']]  # anomaly
ax.plot(data_df.index, data_df['Series'], color='black', label='Normal')
ax.scatter(a.index, data_df['Series'][a.index], color='red', label='Anomaly')
plt.legend()
plt.show()


exit(0)
