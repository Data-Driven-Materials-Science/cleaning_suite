from testing import testing_data_sets as TDS
from helper_functions.pickle_saving_reading import PickleFileManager as PKM
from pandas.testing import assert_frame_equal


def test_set_one(dir_path="datasets/001_data_files_test"):
    """

    Test pickle file saving and reading for the 1d Data Set

    :param dir_path: The directory's relative path we are using
    :return: True if passes

    """

    data_df = TDS.data_df_1d
    portion_one = data_df[:50]
    portion_two = data_df[50:]

    PKM.save_outliers_and_normal_data(directory_path=dir_path, data_df=portion_one, outlier_df=portion_two)
    portion_one_read, portion_two_saved = PKM.read_outliers_and_normal_data(directory_path=dir_path)

    assert_frame_equal(portion_one, portion_one_read)
    assert_frame_equal(portion_two, portion_two_saved)

    return True


def test_set_two(dir_path="datasets/002_data_files_test"):
    """

    Test pickle file saving and reading for the 3d Data Set

    :param dir_path: The directory's relative path we are using
    :return: True if passes

    """

    data_df = TDS.data_df_3d
    portion_one = data_df[:50]
    portion_two = data_df[50:]

    PKM.save_outliers_and_normal_data(directory_path=dir_path, data_df=portion_one, outlier_df=portion_two)
    portion_one_read, portion_two_saved = PKM.read_outliers_and_normal_data(directory_path=dir_path)

    assert_frame_equal(portion_one, portion_one_read)
    assert_frame_equal(portion_two, portion_two_saved)

    return True


def test_set_three(dir_path="datasets/003_data_files_test"):
    """

    Test pickle file saving and reading for the data series Data Set

    :param dir_path: The directory's relative path we are using
    :return: True if passes

    """

    data_df = TDS.data_df_time_series
    portion_one = data_df[:50]
    portion_two = data_df[50:]

    PKM.save_outliers_and_normal_data(directory_path=dir_path, data_df=portion_one, outlier_df=portion_two)
    portion_one_read, portion_two_saved = PKM.read_outliers_and_normal_data(directory_path=dir_path)

    assert_frame_equal(portion_one, portion_one_read)
    assert_frame_equal(portion_two, portion_two_saved)

    return True

