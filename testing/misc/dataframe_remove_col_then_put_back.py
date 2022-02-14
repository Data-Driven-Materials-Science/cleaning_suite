import pandas as pd
from helper_functions.data_file_reading import ReadFileHelper as RFH

file_path = "../../datasets/CSVDataFile_TimeSeries.csv"
target_var = "Component Four"
data_df = RFH.read_file(file_path)

print("----------------------------Checkpoint 1----------------------------")

print(data_df)

print("----------------------------Checkpoint 2----------------------------")

target_col = data_df[[target_var]]
data_df = data_df.drop([target_var], axis=1)

print(data_df)
print(data_df)

print("----------------------------Checkpoint 3----------------------------")

normal_data_df = data_df.head(10)
print(normal_data_df)

print("----------------------------Checkpoint 4----------------------------")

normal_data_df[target_var] = target_col[target_col.index.isin(normal_data_df.index)]
print(normal_data_df)

exit(0)
