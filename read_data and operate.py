import pandas as pd

# ------ 1. 用read_csv函数读入一个csv表格并自动转化为dataframe
df = pd.read_csv(r'/Users/mac/Desktop/机器学习/机器学习第一次作业/wine_data.csv')

# 可以使用to_string()函数打印表格的全部内容
print(df.head())

#还可以传入json文件（即javasript的对象表示法）

# ------ 2. 按列选择数据
# 输出一列，直接传入列名
print(df['Alcohol'])

#输出多列，传入一个列表保存的列名
print(df[['Alcohol', 'Ash']])

# ------ 3. 按行选择数据
print(df.loc[0])
"""可以在read_csv传入index_col参数来设置每行的名称"""

# ------ 4. 对dataframe进行切片 传入起始行、结束行的后一行和步长 起始列、结束列的后一列和步长
print(df.iloc[0:10:2,0:3:2])

# 通过条件判断筛选酒精浓度在14以上的葡萄酒
print(df[df['Alcohol'] > 14])

# 通过条件运算符筛选Malic Acid在1.6到2之间的数据
print(df[(df['Malic acid'] >= 1.6) | (df['Malic acid'] <= 2.0)])