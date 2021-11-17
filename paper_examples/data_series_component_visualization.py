import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
import numpy as np
import math
import random
from paper_examples import figure_colors_key as ck

random.seed(10)

# Derived from example at https://neptune.ai/blog/anomaly-detection-in-time-series

num_values = 400
periods = 16
x_values = np.linspace(0.0, math.pi * 2 * periods, num_values)
seasonality_values = np.sin(x_values)
trend_values = np.linspace(0, 5, num_values)
noise_component = np.random.normal(0, 0.3, num_values)
outliers = []
frequency = int(num_values / (periods / 2))

# Making outliers:
outlier_freq = 0.03
for i in range(num_values):
    if random.uniform(0, 1) < outlier_freq:
        noise_component[i] = noise_component[i] + random.uniform(0, 5)
        outliers.append(i)

resulting_data_set = seasonality_values + noise_component + trend_values

# plt.rc('figure', figsize=(12, 8))
# plt.rc('font', size=15)
result = seasonal_decompose(resulting_data_set, model='additive', period=frequency)
fig, ax = plt.subplots(nrows=4, figsize=(15, 9))
ax[0].plot(result.observed, color=ck.raw_data_color)
ax[1].plot(result.seasonal, color=ck.resulting_data_colors[0])
ax[2].plot(result.trend, color=ck.resulting_data_colors[1])
ax[3].plot(result.resid, color=ck.resulting_data_colors[2], label="Residuals")
ax[0].set_title("Seasonal Decomposition of a Data Series")
ax[0].set_ylabel("Observed Values")
ax[1].set_ylabel("Seasonality Values")
ax[2].set_ylabel("Trend Values")
ax[3].set_ylabel("Residual Values")
ax[0].set_xlabel("Index")
ax[1].set_xlabel("Index")
ax[2].set_xlabel("Index")
ax[3].set_xlabel("Index")
legendNotDont = True

plt.savefig("./paper_images/DataSeriesExampleAllVals", dpi=500)

for outlier in outliers:
    ax[3].axvline(x_values[outlier], color=ck.outlier_color, label="Outliers")
    if legendNotDont:
        # Needed to only make one line appear
        ax[3].legend()
        legendNotDont = False

plt.savefig("./paper_images/DataSeriesExampleAllValsOutliersMarked", dpi=500)

plt.show()

# fig = result.plot()
# plt.show()

plt.plot(result.observed, color=ck.raw_data_color)
plt.title("Observed Values of a Data-Series - Actual")
plt.ylabel("Observed Values")
plt.xlabel("Index")
plt.savefig("./paper_images/DataSeriesExampleObservedVals", dpi=500)
plt.show()

plt.plot(seasonality_values, color=ck.resulting_data_colors[0])
plt.title("Seasonality Values of a Data-Series - Actual")
plt.ylabel("Seasonality Values")
plt.xlabel("Index")
plt.savefig("./paper_images/DataSeriesExampleSeasonalityActualVals", dpi=500)
plt.show()

plt.plot(result.seasonal, color=ck.resulting_data_colors[0])
plt.title("Seasonality Values of a Data-Series - Calculated")
plt.ylabel("Seasonality Values")
plt.xlabel("Index")
plt.savefig("./paper_images/DataSeriesExampleSeasonalityCalculatedVals", dpi=500)
plt.show()

plt.plot(trend_values, color=ck.resulting_data_colors[1])
plt.title("Trend-Cycle Values of a Data-Series - Actual")
plt.ylabel("Trend-Cycle Values")
plt.xlabel("Index")
plt.savefig("./paper_images/DataSeriesExampleTrendCycleActualVals", dpi=500)
plt.show()

plt.plot(trend_values, color=ck.resulting_data_colors[1])
plt.title("Trend-Cycle Values of a Data-Series - Calculated")
plt.ylabel("Trend-Cycle Values")
plt.xlabel("Index")
plt.savefig("./paper_images/DataSeriesExampleTrendCycleCalculatedVals", dpi=500)
plt.show()

plt.plot(noise_component, color=ck.resulting_data_colors[2])
plt.title("Residual Values of a Data-Series - Actual")
plt.ylabel("Residual Values")
plt.xlabel("Index")
plt.savefig("./paper_images/DataSeriesExampleResidualActualVals", dpi=500)
plt.show()

plt.plot(result.resid, color=ck.resulting_data_colors[2])
plt.title("Residual Values of a Data-Series - Calculated")
plt.ylabel("Residual Values")
plt.xlabel("Index")
plt.savefig("./paper_images/DataSeriesExampleResidualCalculatedVals", dpi=500)
plt.show()

exit(0)
