# Import the Necessary Libraries
import pandas as pd
import matplotlib.pyplot as plt
from paper_examples import figure_colors_key as ck

data_df = pd.read_csv("../datasets/Results_FourDimensional_OutliersRemovedData.csv")

# Raw Data Being Plotted
for col in data_df.columns:
    intervals = []
    interval_increment = (max(data_df[col].values) - min(data_df[col].values)) / 50.0

    accumulator = min(data_df[col].values) - interval_increment
    max_limit = max(data_df[col].values) + 2 * interval_increment

    while accumulator < max_limit:
        intervals.append(accumulator)
        accumulator = accumulator + interval_increment

    plt.plot(data_df[col], color=ck.resulting_data_colors[0])
    plt.title("Raw Data Values - " + str(col))
    plt.xlabel("Point Index")
    plt.ylabel(str(col))
    plt.savefig("./paper_images/results_4d_time_series_after_" + str(col) + ".png", dpi=500)
    plt.show()
