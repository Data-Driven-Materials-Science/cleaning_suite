import pandas as pd


def read_file(filepath):
    """

    :param filepath: The path to the file we are reading in
    :return: A DataFrame representation of the file

    Reads in a file and converts it to a DataFrame.

    """

    if ".csv" in filepath:
        df = pd.read_csv(filepath)
    elif ".xlsx" in filepath:
        df = pd.read_excel(filepath)
    else:
        raise ValueError("You provided the wrong file type! We do not support your file type at this moment.")
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    return df
