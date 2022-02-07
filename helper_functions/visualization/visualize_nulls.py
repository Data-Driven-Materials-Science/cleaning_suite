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


def visualize_nulls_general(data, image_directory="Images/"):
    fig = generate_nulls_bar_graph(data, image_directory)
    
    fig = generate_nulls_matrix(data)
    plt.title("Locations of Null Values in Each Record", fontsize=30)
    plt.xlabel("Column", fontsize=20)
    plt.ylabel("Record", fontsize=20)
    plt.savefig(image_directory + "Matrix_nulls")
    plt.close()
    
    fig = generate_nulls_correlation_matrix(data)
    plt.title("Null Value Correlation Between Pairs of Columns", fontsize=30)
    plt.xlabel("Column 1", fontsize=20)
    plt.ylabel("Column 2", fontsize=20)
    plt.savefig(image_directory + "Correlation_matrix_nulls")
    plt.close()
    
    fig = generate_nulls_dendrogram(data)
    plt.title("Null Value Correlations Between All Columns", fontsize=30)
    plt.xlabel("Column", fontsize=20)
    plt.ylabel("Null Column Similarity", fontsize=20)
    plt.savefig(image_directory + "Dendrogram_nulls")
    plt.close()


def generate_nulls_bar_graph(data, image_directory):
    # n and p are only applicable when filter!=None

    '''
    We don't use the missingno library here because this method
    doesn't allow us to add labels to the visuals.
    '''
    # if sort == None:
    # return missingno.bar(data, color=color, filter=filter, n=n, p=p)
    null_values = data.isna().sum().values
    columns = data.columns

    if len(columns) <= 50:
        plt.figure(figsize=(25, 10))
        plt.bar(columns, null_values, color='dimgray')
    else:
        plt.figure(figsize=(25, (25 + len(columns) - 50) * 0.5))
        plt.barh(columns, null_values, color='dimgray')
        
    xlocs, _ = plt.xticks(fontsize=15, rotation=45)
    for i, v in enumerate(null_values):
        plt.text(xlocs[i], v, str(v), fontsize=15, verticalalignment='bottom', horizontalalignment='center')
        
    plt.title("Total Number of Nulls in Each Column", fontsize=30)
    plt.xlabel("Column", fontsize=20)
    plt.ylabel("Number of Null Values", fontsize=20)
    
    if(image_directory != None):
        plt.savefig(image_directory + "Bar_graph_nulls")
    plt.close()


def generate_nulls_matrix(data, filter=None, n=0, p=0, sort=None, figsize=(25, 10), fontsize=16,
                          color=(0.25, 0.25, 0.25)):
    # if sort == None:
    # return missingno.matrix(data, filter=filter, p=p, n=n, color=color, figsize=figsize, fontsize=fontsize)
    return missingno.matrix(data, filter=filter, p=p, n=n, color=color, sort=sort, figsize=figsize, fontsize=fontsize, labels=True)


def generate_nulls_correlation_matrix(data, filter=None, n=0, p=0, sort=None, figsize=(20, 12), fontsize=16,
                                      cmap='RdBu'):
    return missingno.heatmap(data, filter=filter, n=n, p=p, sort=sort, cmap=cmap, figsize=figsize, fontsize=fontsize, labels=True)


def generate_nulls_dendrogram(data, method='average', filter=None, n=0, p=0):
    return missingno.dendrogram(data, method=method, filter=filter, n=n, p=p)
