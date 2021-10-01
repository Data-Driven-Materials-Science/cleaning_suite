import matplotlib.pyplot as plt
import numpy as np
import missingno
from pandas._libs import missing
import matplotlib.pyplot as plt


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


def visualize_nulls_general(data):
    fig = generate_nulls_bar_graph(data)
    plt.savefig("Images/Bar_graph_nulls")
    plt.close()
    fig = generate_nulls_matrix(data)
    plt.savefig("Images/Matrix_nulls")
    plt.close()
    fig = generate_nulls_correlation_matrix(data)
    plt.savefig("Images/Correlation_matrix_nulls")
    plt.close()
    fig = generate_nulls_dendrogram(data)
    plt.savefig("Images/Dendrogram_nulls")
    plt.close()

def generate_nulls_bar_graph(data, color='dimgray', filter=None, n=0, p=0, sort=None):
    # n and p are only applicable when filter!=None
    
    '''
    Use of params:
    - color: YES
    - sort: YES
    - orientation: eh, maybe
    - log: probably not useful
    - filter: only useful if there are a TON of columns
    - Actually, filter could be used to grab the 10 most null columns if we wanted to
    - n,p: only useful if filter is used
    '''

    return missingno.bar(data, sort=sort, color=color, filter=filter, n=n, p=p)

def generate_nulls_matrix(data, filter=None, n=0, p=0, sort=None, figsize=(25, 10), fontsize=16, color=(0.25, 0.25, 0.25)):
    return missingno.matrix(data, filter=filter, p=p, n=n, color=color, sort=sort, figsize=figsize, fontsize=fontsize)

def generate_nulls_correlation_matrix(data, filter=None, n=0, p=0, sort=None, figsize=(20,12), fontsize=16, cmap='RdBu'):
    return missingno.heatmap(data, filter=filter, n=n, p=p, sort=sort, cmap=cmap, figsize=figsize, fontsize=fontsize)

def generate_nulls_dendrogram(data, method='average', filter=None, n=0, p=0):
    return missingno.dendrogram(data, method=method, filter=filter, n=n, p=p)
