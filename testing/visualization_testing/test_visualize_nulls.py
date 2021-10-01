import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from helper_functions.visualization import visualize_nulls

np.random.seed(10)

def create_null_values(data, prob=0.3):
    for column in data.columns:
        for entry in data[column]:
            random_indicator = np.random.randint(0, 10)
            if random_indicator < prob*10:
                data[entry][column] = np.nan
    return data

test_data_set = pd.read_csv('datasets/mammals.csv')


def test_bar_graph_null_values(show=False):
    """
    :param show: indicates whether the visual should be shown
    :return: True or False depending on if the visualization task passed without error

    Test 1 bar graph visual of null values

    """
    sort = ['None', 'ascending', 'descending']
    color = ['dimgray', 'red', 'blue', 'black']
    filters = ['None', 'top', 'bottom']
    n = [0, 5, 5]
    p = [0, 0.5, 0.95]

    for s in sort:
        for col in color:
            for f, n_val, p_val in zip(filters, n, p):
                fig = visualize_nulls.generate_nulls_bar_graph(test_data_set, color=col, filter=f, n=n_val, p=p_val, sort=s)
                if show:
                    plt.show()
                    plt.close()
    return True


def test_matrix_null_values(show=False):
    """
    :param show: indicates whether the visual should be shown
    :return: True or False depending on if the visualization task passed without error

    Test 1 matrix visual of null values

    """
    sort = ['None', 'ascending', 'descending']
    color = [(0,0,0.9), (0,0,0), (0.9,0,0), (0,0.9,0), (0.5,0.5,0.5)]
    filters = ['None', 'top', 'bottom']
    n = [0, 5, 5]
    p = [0, 0.5, 0.95]

    for s in sort:
        for col in color:
            for f, n_val, p_val in zip(filters, n, p):
                fig = visualize_nulls.generate_nulls_matrix(test_data_set, sort=s, color=col, filter=f, n=n_val, p=p_val)
                if show:
                    plt.show()
                    plt.close()
    return True


def test_correlation_matrix_null_values(show=False):
    """
    :param show: indicates whether the visual should be shown
    :return: True or False depending on if the visualization task passed without error

    Test 1 correlation matrix visual of null values

    """
    sort = ['None', 'ascending', 'descending']
    color = ['PiYG', 'PRGn', 'BrBG', 'PuOr', 'RdGy', 'RdBu',
            'RdYlBu', 'RdYlGn', 'Spectral', 'coolwarm', 'bwr', 'seismic']
    filters = ['None', 'top', 'bottom']
    n = [0, 5, 5]
    p = [0, 0.5, 0.95]

    for s in sort:
        for col in color:
            for f, n_val, p_val in zip(filters, n, p):
                fig = visualize_nulls.generate_nulls_correlation_matrix(test_data_set, filter=f, n=n_val, p=p_val, sort=s, cmap=col)
                if show:
                    plt.show()
                    plt.close()
    return True


def test_dendrogram_null_values(show=False):
    """
    :param show: indicates whether the visual should be shown
    :return: True or False depending on if the visualization task passed without error

    Test 1 dendrogram visual of null values

    """
    method = ['average', 'single', 'complete', 'weighted', 'centroid', 'median', 'ward']
    filters = ['None', 'top', 'bottom']
    n = [0, 5, 5]
    p = [0, 0.5, 0.95]

    for m in method:
        for f, n_val, p_val in zip(filters, n, p):
            fig = visualize_nulls.generate_nulls_dendrogram(test_data_set, method=m, filter=f, n=n_val, p=p_val)
            if show:
                plt.show()
                plt.close()
    return True


test_bar_graph_null_values(show=True)
test_matrix_null_values(show=True)
test_correlation_matrix_null_values(show=True)
test_dendrogram_null_values(show=True)

exit(0)
