import pandas as pd

# ------ 用pandas将列表、字典转化为series序列 ------
data = [100, 101, 102, 103, 104, 105, 106]

calories = {'Day1': 1700, 'Day2': 2000, 'Day3':2050}

series1 = pd.Series(data)

calories_series = pd.Series(calories)

# 使用.head方法只显示序列的前五行
print(series1.head())

"""输出结果中的dtype表示原始数据的类型，包括整数、浮点数、对象布尔值等"""

# ------ Series还可以传入标签列，如果不传入，默认为从0开始的整数序列 ------

series2 = pd.Series(data,['a', 'b', 'c', 'd', 'e', 'f', 'g'])

"""index参数可以为列表，数组，ndarray或者另一个series"""

print(series2.head())

# ------ 使用.loc或者.iloc方法索引series中的数据
print(series1.loc[0])
print(series2.loc['a'])

#注意iloc方法之能通过整数进行索引,虽然series2的标签已经变成字符，但仍然能通过iloc索引
print(series1.iloc[0])
print(series2.iloc[0])

# ------ 通过.loc和.iloc方法还可以更新数据元素
series2['a'] = 109
print(series2.loc['a'])

# ------ series本身还可以通过条件索引 ------
print(series2[ series2 >= 105 ])
print(calories_series[calories_series < 2000])
"""结果返回索引和对应的数据"""

# ------ pandas还可以将二维字典或矩阵转化为dataframe格式存储数据 ------

person_info = {'Name' : ['Alan', 'Bob', 'David'] ,
               'Age' : [30, 35, 40]
               }

df = pd.DataFrame(person_info)
print(df)

# 同样可以给dataframe传入行标签
df = pd.DataFrame(person_info, index = ['employee1', 'employee2', 'employee3'])
print(df)

# 往dataframe中加入新的列名
df['Job'] = ['Cook', 'Cashier', 'N/A']

# 往dataframe中加入新的行
new_row = pd.DataFrame({'Name' : 'Nick', 'Age' : 45, 'Job' : 'Engineer'} , index = ['employee4'])
df = pd.concat([df, new_row])

print(df)

