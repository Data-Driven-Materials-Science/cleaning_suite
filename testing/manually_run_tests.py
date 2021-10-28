from testing.outlier_testing import test_boxplot, test_dbscan_one_dimension, test_dbscan_two_dimension, \
    test_knn_one_dimension, test_knn_two_dimension, test_z_score
from testing.visualization_testing import test_visualize_outliers
from testing.report_testing import test_report_outliers
from testing.file_reading_saving import test_file_reading, test_pickle_file_reading_saving

# Runs the outlier detection testing for the boxplot outlier detection type
assert test_boxplot.test_method1(show=True)
assert test_boxplot.test_method2(show=True)

# Runs the outlier detection testing for the z-score outlier detection type
assert test_z_score.test_method1(show=True)
assert test_z_score.test_method2(show=True)
assert test_z_score.test_method3(show=True)
assert test_z_score.test_method4(show=True)

# Runs the outlier detection testing for the DBSCAN outlier detection type on one dimensional data
assert test_dbscan_one_dimension.test_method1(show=True)
assert test_dbscan_one_dimension.test_method2(show=True)
assert test_dbscan_one_dimension.test_method3(show=True)
assert test_dbscan_one_dimension.test_method4(show=True)
assert test_dbscan_one_dimension.test_method5(show=True)

# Runs the outlier detection testing for the DBSCAN outlier detection type on two dimensional data
assert test_dbscan_two_dimension.test_method1(show=True)
assert test_dbscan_two_dimension.test_method2(show=True)
assert test_dbscan_two_dimension.test_method3(show=True)
assert test_dbscan_two_dimension.test_method4(show=True)
assert test_dbscan_two_dimension.test_method5(show=True)

# Runs the outlier detection testing for the k-NN outlier detection type on one dimensional data
assert test_knn_one_dimension.test_method1(show=True)
assert test_knn_one_dimension.test_method2(show=True)
assert test_knn_one_dimension.test_method3(show=True)
assert test_knn_one_dimension.test_method4(show=True)

# Runs the outlier detection testing for the k-NN outlier detection type on two dimensional data
assert test_knn_two_dimension.test_method1(show=True)
assert test_knn_two_dimension.test_method2(show=True)
assert test_knn_two_dimension.test_method3(show=True)
assert test_knn_two_dimension.test_method4(show=True)
assert test_knn_two_dimension.test_method5(show=True)
assert test_knn_two_dimension.test_method6(show=True)

# Runs the visualize outlier tests after outliers have been identified
assert test_visualize_outliers.test_z_score_1d(show=True)
assert test_visualize_outliers.test_boxplot_1d(show=True)
assert test_visualize_outliers.test_DBSCAN_1d(show=True)
assert test_visualize_outliers.test_DBSCAN_2d(show=True)
assert test_visualize_outliers.test_DBSCAN_3d(show=True)
assert test_visualize_outliers.test_KNN_1d(show=True)
assert test_visualize_outliers.test_KNN_2d(show=True)
assert test_visualize_outliers.test_KNN_3d(show=True)

# Runs the report generator tests after outliers have been identified
assert test_report_outliers.test_z_score_1d()
assert test_report_outliers.test_boxplot_1d()
assert test_report_outliers.test_DBSCAN_1d()
assert test_report_outliers.test_DBSCAN_2d()
assert test_report_outliers.test_DBSCAN_3d()
assert test_report_outliers.test_KNN_1d()
assert test_report_outliers.test_KNN_2d()
assert test_report_outliers.test_KNN_3d()

# Runs the pickle file reading and writing tests
assert test_pickle_file_reading_saving.test_set_one(dir_path="../datasets/001_data_files_test")
assert test_pickle_file_reading_saving.test_set_two(dir_path="../datasets/002_data_files_test")
assert test_pickle_file_reading_saving.test_set_three(dir_path="../datasets/003_data_files_test")

# Runs the tests for the file reading manually
assert test_file_reading.test_csv1(file_path="../datasets/CSVDataFile_1Dimensional.csv")
assert test_file_reading.test_csv2(file_path="../datasets/CSVDataFile_3Dimensional.csv")
assert test_file_reading.test_csv3(file_path="../datasets/CSVDataFile_TimeSeries.csv")
assert test_file_reading.test_csv4(file_path="../datasets/CSVDataFile_1Dimensional_Clean.csv")
assert test_file_reading.test_csv5(file_path="../datasets/CSVDataFile_1Dimensional_Messy.csv")
assert test_file_reading.test_csv6(file_path="../datasets/CSVDataFile_3Dimensional_Clean.csv")
assert test_file_reading.test_csv7(file_path="../datasets/CSVDataFile_3Dimensional_Messy.csv")
assert test_file_reading.test_excel1(file_path="../datasets/ExcelDataFile_1Dimensional.xlsx")
assert test_file_reading.test_excel2(file_path="../datasets/ExcelDataFile_3Dimensional.xlsx")
assert test_file_reading.test_excel3(file_path="../datasets/ExcelDataFile_TimeSeries.xlsx")
assert test_file_reading.test_excel4(file_path="../datasets/ExcelDataFile_1Dimensional_Clean.xlsx")
assert test_file_reading.test_excel5(file_path="../datasets/ExcelDataFile_1Dimensional_Messy.xlsx")
assert test_file_reading.test_excel6(file_path="../datasets/ExcelDataFile_3Dimensional_Clean.xlsx")
assert test_file_reading.test_excel7(file_path="../datasets/ExcelDataFile_3Dimensional_Messy.xlsx")

exit(0)
