import numpy as np
import pandas as pd

import pandas as pd
import os
# 获取当前文件所在的目录路径
# notebook_path = os.path.abspath('data_preprocessing.py')
# current_directory = os.path.dirname(notebook_path)

# # 构建数据文件的路径
# file1_path = os.path.join(current_directory, "../data/accepted_2007_to_2018q4.csv", "accepted_2007_to_2018q4.csv")

print("1")
# 读取file1.csv
#file1_path = 'D:/bristol/study/subjects/individual project/data_lendingclub/2/archive/accepted_2007_to_2018q4.csv/accepted_2007_to_2018q4.csv'
data1 = pd.read_csv("../data/accepted_2007_to_2018q4.csv/accepted_2007_to_2018Q4.csv")
print("2")
# 添加新列，并填充为1
data1['New_Column_statement'] = 1
print("3")
# 保存修改后的data1
data1.to_csv('processing_data1.csv', index=False)

print("4")
# 构建数据文件的路径
# file2_path = os.path.join(current_directory, "../data/rejected_2007_to_2018q4.csv", "rejected_2007_to_2018q4.csv")

# 读取file2.csv
#file2_path = 'D:/bristol/study/subjects/individual project/data_lendingclub/2/archive/rejected_2007_to_2018q4.csv/rejected_2007_to_2018q4.csv'
data2 = pd.read_csv("../data/rejected_2007_to_2018q4.csv/rejected_2007_to_2018Q4.csv")
print("5")
# 添加新列，并填充为0
data2['New_Column_statement'] = 0
print("6")
# 保存修改后的data2
data2.to_csv('processing_data2.csv', index=False)

# 读取修改后的两个CSV文件
data1_modified = pd.read_csv('processing_data1.csv')
data2_modified = pd.read_csv('processing_data2.csv')
print("7")
# 将两个数据集连接起来
combined_data = pd.concat([data1_modified, data2_modified], ignore_index=True)
print("8")
# 保存连接后的数据为第三个CSV文件
combined_data.to_csv('processing_data.csv', index=False)

# 读取CSV文件
data = pd.read_csv('processing_data.csv')

# 显示前几行，默认显示前5行
num_rows_to_display = 5
print(data.head(num_rows_to_display))


