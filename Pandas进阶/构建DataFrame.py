# 构建DataFrame可以从csv构建,也可以从dict中创建
# 1使用zip()函数 2添加新列 3广播(Broadcasting):创建新列并为整个列赋值

import pandas as pd

data = pd.read_csv("../Pokemon.csv")

pd.set_option('display.max_columns', None)  # 给最大列设置为10列
pd.set_option('display.max_rows', None)  # 设置最大可见100行
pd.set_option('display.width', 1000)

# 从字典中构建DataFrame
country = ["Spain", "France", "China"]
population = ['11', '23', '160']
list_label = ['country', 'population']
list_col = [country, population]
# zip函数将可迭代对象中的元素一一对应成元组
zipped = list(zip(list_label, list_col))
data_dict = dict(zipped)
df = pd.DataFrame(data_dict)
print(df)

# 添加新列
df['capital'] = ["madrid", "paris", "beijing"]
print(df)

# 广播Broadcasting
df['income'] = None  # Broadcasting整列
print(df)
df['income'] = 0
print(df)

