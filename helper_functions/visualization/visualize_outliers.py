import matplotlib.pyplot as plt
import numpy as np


def visualize_outliers(data_df, outlier_df, bars=True, diff_colors=True, show=True, save=False, title="",
                       multiple_hists=False):
    """

    :param data_df: A DataFrame which holds all of the data we will be detecting outliers in
    :param outlier_df: A DataFrame which holds all of the outliers that have been separated from the main data set
    :param bars: A boolean which determines whether or not we will use bars on either side of the data to
        highlight outliers

    :param diff_colors: A boolean which is whether or not we will use different colors to represent outliers

    :param show: A boolean of whether or not to show the plot (primarily used for testing)
    :param save: A boolean of whether or not to save the plot
    :param title: A String title to use for the plot
    :param multiple_hists: A boolean of whether or not to have multiple histograms for the 1 or n dimensional
        visualization

    :return: None

    Visualizes the outliers.

    """

    # TODO Implement function
    # TODO Clean comment

    num_columns_data = len(data_df.columns)
    num_columns_outliers = len(outlier_df.columns)

    # Change this into catch except
    assert num_columns_data == num_columns_outliers

    if num_columns_data == 2:
        visualize_outliers_2d(data_df=data_df, outlier_df=outlier_df, diff_colors=diff_colors,
                              show=show, save=save, title=title)
    else:
        for column in data_df.columns:
            visualize_outliers_1d(data_df=data_df, outlier_df=outlier_df, column=column, bars=bars,
                                  diff_colors=diff_colors, show=show, save=save, title=title,
                                  multiple_hists=multiple_hists)

    return None


def visualize_outliers_1d(data_df, outlier_df, column, bars=True, diff_colors=True, show=True, save=False, title="",
                          multiple_hists=False):
    """

    :param data_df: A DataFrame which holds all of the data we will be detecting outliers in
    :param outlier_df: A DataFrame which holds all of the outliers that have been separated from the main data set
    :param column: The DataFrame column we are visualizing
    :param bars: A boolean which determines whether or not we will use bars on either side of the data to
        highlight outliers

    :param diff_colors: A boolean which is whether or not we will use different colors to represent outliers

    :param show: A boolean of whether or not to show the plot (primarily used for testing)
    :param save: A boolean of whether or not to save the plot
    :param title: A String title to use for the plot
    :param multiple_hists: A boolean of whether or not to have multiple histograms for the 1 or n dimensional
        visualization

    :return: None

    Visualizes the outliers.

    """

    # TODO Implement function
    # TODO Clean comment

    data_non_outliers = data_df[column].values
    data_outliers = outlier_df[column].values

    all_values = np.append(data_non_outliers, data_outliers)

    intervals = []
    interval_increment = 0.25

    accumulator = min(all_values) - interval_increment
    max_limit = max(all_values) + 2 * interval_increment

    while accumulator < max_limit:
        intervals.append(accumulator)
        accumulator = accumulator + interval_increment

    if diff_colors:

        # Alternate method to possibly look into in the future...
        # data_combined = [data_df[column].values, outlier_df[column].values]
        # colors = ["green", "red"]
        # labels = ["Not Outliers", "Outliers"]
        # plt.hist(data_combined, bins=intervals, histtype="bar", color=colors, label=labels)

        # Another alternate version
        # data_combined = [data_df[column].values, outlier_df[column].values]
        # colors = ["green", "red"]
        # labels = ["Not Outliers", "Outliers"]
        # plt.hist(data_combined, bins=intervals, histtype="step", fill=True, color=colors, label=labels)

        if multiple_hists:
            fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(10, 10))
            ax_normal_data = axes[0]
            ax_outliers = axes[1]
            ax_combined = axes[2]
            ax_normal_data.hist(data_df[column].values, bins=intervals, histtype="bar", color="green",
                                label="Not Outliers")
            ax_outliers.hist(outlier_df[column].values, bins=intervals, histtype="bar", color="red", label="Outliers")
            ax_combined.hist(data_df[column].values, bins=intervals, histtype="bar", color="green",
                             label="Not Outliers")
            ax_combined.hist(outlier_df[column].values, bins=intervals, histtype="bar", color="red", label="Outliers")

            # Find the largest y limit so all plots have an equal scale
            largest_y = max(axes[0].get_ylim()[1], axes[1].get_ylim()[1], axes[2].get_ylim()[1])
            axes[0].set_ylim([0, largest_y])
            axes[1].set_ylim([0, largest_y])
            axes[2].set_ylim([0, largest_y])

            axes[0].set_title(str(title) + " - " + str(column) + " - Non Outliers")
            axes[1].set_title(str(title) + " - " + str(column) + " - Outliers")
            axes[2].set_title(str(title) + " - " + str(column) + " - Combined Data")

            axes[0].set_ylabel("Data Point Frequency")
            axes[1].set_ylabel("Data Point Frequency")
            axes[2].set_ylabel("Data Point Frequency")

            axes[0].set_xlabel("Data Point Value For " + str(column))
            axes[1].set_xlabel("Data Point Value For " + str(column))
            axes[2].set_xlabel("Data Point Value For " + str(column))

            pass

        else:
            plt.hist(data_df[column].values, bins=intervals, histtype="bar", color="green", label="Not Outliers")
            plt.hist(outlier_df[column].values, bins=intervals, histtype="bar", color="red", label="Outliers")
        plt.legend()
    else:
        plt.hist(data_df[column].values, bins=intervals, color="green")
        plt.hist(outlier_df[column].values, bins=intervals, color="green")

    if bars:
        if len(data_non_outliers) > 0:
            plt.axvline(max(data_non_outliers))
            plt.axvline(min(data_non_outliers))

    if not (multiple_hists and diff_colors):
        plt.title(str(title) + " - " + str(column))
        plt.xlabel("Data Point Value For " + str(column))
        plt.ylabel("Data Point Frequency")

    if show:
        plt.show()
    else:
        plt.close()

    return None


def visualize_outliers_2d(data_df, outlier_df, diff_colors=True, show=True, save=False, title=""):
    """

    :param data_df: A DataFrame which holds all of the data we will be detecting outliers in
    :param outlier_df: A DataFrame which holds all of the outliers that have been separated from the main data set

    :param diff_colors: A boolean which is whether or not we will use different colors to represent outliers

    :param show: A boolean of whether or not to show the plot (primarily used for testing)
    :param save: A boolean of whether or not to save the plot
    :param title: A String title to use for the plot

    :return: None

    Visualizes the outliers.

    """

    # TODO Implement function
    # TODO Clean comment

    num_columns_data = len(data_df.columns)
    num_columns_outliers = len(outlier_df.columns)

    # Change this into catch except
    assert num_columns_data == num_columns_outliers

    data_cols = data_df.columns

    if diff_colors:
        plt.scatter(data_df[data_cols[0]].values, data_df[data_cols[1]], color="green", label="Not Outliers")
        plt.scatter(outlier_df[data_cols[0]].values, outlier_df[data_cols[1]], color="red", label="Outliers")
    else:
        plt.scatter(data_df[data_cols[0]].values, data_df[data_cols[1]], color="green")
        plt.scatter(outlier_df[data_cols[0]].values, outlier_df[data_cols[1]], color="green")
    plt.title(title)
    plt.xlabel("Data Point Value For " + str(data_cols[0]))
    plt.ylabel("Data Point Value For " + str(data_cols[1]))

    if show:
        plt.show()
    else:
        plt.close()

    return None


def visualize_outliers_grid(data_df, outlier_df, x_df, y_df, bars=True, diff_colors=True):
    """

    :param data_df: A DataFrame which holds all of the data we will be detecting outliers in
    :param outlier_df: A DataFrame which holds all of the outliers that have been separated from the main data set
    :param bars: A boolean which determines whether or not we will use bars on either side of the data to
        highlight outliers

    :param diff_colors: A boolean which is whether or not we will use different colors to represent outliers

    :return: None

    Visualizes the outliers.

    """

    # TODO plan this out to see if it is possible

    return None
