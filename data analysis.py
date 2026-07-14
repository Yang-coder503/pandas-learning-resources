import pandas as pd

df = pd.read_csv(r'/Users/mac/Desktop/机器学习/机器学习第一次作业/wine_data.csv')

# ------ 1. 计算数值列的均值
print(df.mean(numeric_only=True))

""" 
2.使用sum计算每列的总和
3.使用min和max计算每列的最小值和最大值
4.使用count计算每列的数据数量，不包括缺失值
"""

# 也可以针对某个或某几个列使用函数

print(df['Alcohol'].mean(numeric_only=True))

# ------ 2. 分组聚类函数
# 按class label进行分组
group = df.groupby('Class label')
print(group['Alcohol'].mean())

