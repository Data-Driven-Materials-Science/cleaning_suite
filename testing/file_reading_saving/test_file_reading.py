from helper_functions.data_file_reading import ReadFileHelper as RFH
from testing import testing_data_sets as tds
from pandas.testing import assert_frame_equal


def test_csv1(file_path="datasets/CSVDataFile_1Dimensional.csv"):
    """

    :param file_path: The path for the file to test
    Test the ability to read a one dimensional csv file

    """

    resulting_df = RFH.read_file(file_path)
    assert_frame_equal(resulting_df, tds.data_df_1d)

    return True


def test_csv2(file_path="datasets/CSVDataFile_3Dimensional.csv"):
    """

    :param file_path: The path for the file to test
    Test the ability to read a three dimensional csv file

    """

    resulting_df = RFH.read_file(file_path)
    assert_frame_equal(resulting_df, tds.data_df_3d)

    return True


def test_csv3(file_path="datasets/CSVDataFile_TimeSeries.csv"):
    """

    :param file_path: The path for the file to test
    Test the ability to read a time series csv file

    """

    resulting_df = RFH.read_file(file_path)
    assert_frame_equal(resulting_df, tds.data_df_time_series)

    return True


def test_csv4(file_path="datasets/CSVDataFile_1Dimensional_Clean.csv"):
    """

    :param file_path: The path for the file to test
    Test the ability to read a one dimensional csv file, clean config

    """

    resulting_df = RFH.read_file(file_path)
    assert_frame_equal(resulting_df, tds.data_df_1d)

    return True


def test_csv5(file_path="datasets/CSVDataFile_1Dimensional_Messy.csv"):
    """

    :param file_path: The path for the file to test
    Test the ability to read a one dimensional csv file, messy config

    """

    resulting_df = RFH.read_file(file_path)
    assert_frame_equal(resulting_df, tds.data_df_1d)

    return True


def test_csv6(file_path="datasets/CSVDataFile_3Dimensional_Clean.csv"):
    """

    :param file_path: The path for the file to test
    Test the ability to read a three dimensional csv file, clean config

    """

    resulting_df = RFH.read_file(file_path)
    assert_frame_equal(resulting_df, tds.data_df_3d)

    return True


def test_csv7(file_path="datasets/CSVDataFile_3Dimensional_Messy.csv"):
    """

    :param file_path: The path for the file to test
    Test the ability to read a three dimensional csv file, messy config

    """

    resulting_df = RFH.read_file(file_path)
    assert_frame_equal(resulting_df, tds.data_df_3d)

    return True


def test_excel1(file_path="datasets/ExcelDataFile_1Dimensional.xlsx"):
    """

    :param file_path: The path for the file to test
    Test the ability to read a one dimensional Excel file

    """

    resulting_df = RFH.read_file(file_path)
    assert_frame_equal(resulting_df, tds.data_df_1d)

    return True


def test_excel2(file_path="datasets/ExcelDataFile_3Dimensional.xlsx"):
    """

    :param file_path: The path for the file to test
    Test the ability to read a three dimensional Excel file

    """

    resulting_df = RFH.read_file(file_path)
    assert_frame_equal(resulting_df, tds.data_df_3d)

    return True


def test_excel3(file_path="datasets/ExcelDataFile_TimeSeries.xlsx"):
    """

    :param file_path: The path for the file to test
    Test the ability to read a time series Excel file

    """

    resulting_df = RFH.read_file(file_path)
    assert_frame_equal(resulting_df, tds.data_df_time_series)

    return True


def test_excel4(file_path="datasets/ExcelDataFile_1Dimensional_Clean.xlsx"):
    """

    :param file_path: The path for the file to test
    Test the ability to read a one dimensional Excel file, clean config

    """

    resulting_df = RFH.read_file(file_path)
    assert_frame_equal(resulting_df, tds.data_df_1d)

    return True


def test_excel5(file_path="datasets/ExcelDataFile_1Dimensional_Messy.xlsx"):
    """

    :param file_path: The path for the file to test
    Test the ability to read a one dimensional Excel file, messy config

    """

    resulting_df = RFH.read_file(file_path)
    assert_frame_equal(resulting_df, tds.data_df_1d)

    return True


def test_excel6(file_path="datasets/ExcelDataFile_3Dimensional_Clean.xlsx"):
    """

    :param file_path: The path for the file to test
    Test the ability to read a three dimensional Excel file, clean config

    """

    resulting_df = RFH.read_file(file_path)
    assert_frame_equal(resulting_df, tds.data_df_3d)

    return True


def test_excel7(file_path="datasets/ExcelDataFile_3Dimensional_Messy.xlsx"):
    """

    :param file_path: The path for the file to test
    Test the ability to read a three dimensional Excel file, messy config

    """

    resulting_df = RFH.read_file(file_path)
    assert_frame_equal(resulting_df, tds.data_df_3d)

    return True
