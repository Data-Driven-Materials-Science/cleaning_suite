from helper_functions.data_file_reading import ReadFileHelper as RFH
from testing import testing_data_sets as tds
from pandas.testing import assert_frame_equal


def test_csv1():
    """

    Test the ability to read a one dimensional csv file

    """

    resulting_df = RFH.read_file("datasets/CSVDataFile_1Dimensional.csv")
    assert_frame_equal(resulting_df, tds.data_df_1d)

    return True


def test_csv2():
    """

    Test the ability to read a three dimensional csv file

    """

    resulting_df = RFH.read_file("datasets/CSVDataFile_3Dimensional.csv")
    assert_frame_equal(resulting_df, tds.data_df_3d)

    return True


def test_csv3():
    """

    Test the ability to read a time series csv file

    """

    resulting_df = RFH.read_file("datasets/CSVDataFile_TimeSeries.csv")
    assert_frame_equal(resulting_df, tds.data_df_time_series)

    return True


def test_excel1():
    """

    Test the ability to read a one dimensional Excel file

    """

    resulting_df = RFH.read_file("datasets/ExcelDataFile_1Dimensional.xlsx")
    assert_frame_equal(resulting_df, tds.data_df_1d)

    return True


def test_excel2():
    """

    Test the ability to read a three dimensional Excel file

    """

    resulting_df = RFH.read_file("datasets/ExcelDataFile_3Dimensional.xlsx")
    assert_frame_equal(resulting_df, tds.data_df_3d)

    return True


def test_excel3():
    """

    Test the ability to read a time series Excel file

    """

    resulting_df = RFH.read_file("datasets/ExcelDataFile_TimeSeries.xlsx")
    assert_frame_equal(resulting_df, tds.data_df_time_series)

    return True
