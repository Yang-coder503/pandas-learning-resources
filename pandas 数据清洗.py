import pandas as pd

df = pd.read_csv(r'/Users/mac/Desktop/机器学习/机器学习第一次作业/wine_data.csv')

# ------ 1. 删去无关列
df = df.drop(columns = ['Class label'], axis=1, inplace=True)
print(df)

# ------ 2. 删去缺失值或按条件删去
df = df.dropna(subset = ['Magnesium'])

# ------ 3. 补全有缺失值的dataframe单元格
df = df.fillna({'Magnesium': None})

"""用replace函数进行替换"""
df = df.replace(to_replace = 'Magnesium', value = None, inplace = True, regex = True)

# ------ 4. 多种替换方式
df_test = pd.DataFrame({'A': [1, 2, 3, 2], 'B': ['x', 'y', 'x', 'z']})

# 把 2 替换成 200
df.replace(2, 200)

# 把 1、2 都替换成 0
df.replace([1, 2], 0)

# 1→10，2→20，3→30
df.replace([1, 2, 3], [10, 20, 30])

# 只替换 A 列：1→100，2→200
df.replace({'A': {1: 100, 2: 200}})

# 同时替换多列不同值
df.replace({
    'A': {1: 10, 2: 20},
    'B': {'x': 'XX', 'y': 'YY'}
})

# 开启 regex=True
# 把所有包含 'x' 的字符串替换成 'NEW'
df.replace(r'x', 'NEW', regex=True)

# 把所有以 x 开头的内容替换成 'START_X'
df.replace(r'^x', 'START_X', regex=True)

