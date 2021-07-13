import matplotlib.pyplot as plt
import numpy as np


def visualize_nulls_grid(data_df, x_df, y_df):
    """

    :param data_df: A DataFrame of data we are visualizing
    :param x_df: A DataFrame containing all x values
    :param y_df: A DataFrame containing all y values

    :return: Nothing

    Visualize the nulls in a grid format

    """

    # TODO Comment, clean, and optimize

    x_values = np.unique(x_df["Data"].values)
    y_values = np.unique(y_df["Data"].values)
    grid_size_x = len(x_values)
    grid_size_y = len(y_values)

    grid = np.array(data_df["Data"].values)
    # grid = np.rot90(grid.reshape(grid_size_x, grid_size_y))

    # grid_vals = np.zeros(len(data_list))

    grid_vals = np.where((grid == grid), 1, 0)
    grid_vals = np.rot90(grid_vals.reshape(grid_size_x, grid_size_y))

    z_values = grid_vals

    fig, ax = plt.subplots(figsize=(6, 6))

    ax.set_aspect('equal')
    # Plots contour plot
    cf = ax.contourf(x_values, y_values, z_values, cmap="RdGy")
    # Plots color bar
    cb = fig.colorbar(cf, ax=ax)
    # Labels being set
    cb.set_label("1.0 is not null, 0.0 is null")
    plt.title("Is Null VS Coordinate")
    plt.xlabel("X Values (um)")
    plt.ylabel("Y Values (um)")

    plt.show()
