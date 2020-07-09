# pandas两个主要数据结构: series和DataFrame
# series: 一维数组对象, 带索引
# DataFrame: 表格形数据结构
import pandas as pd
import numpy as np

data = pd.read_csv('../Pokemon.csv')
series = data['Defense']
print(type(series))
data_frame = data[['Defense']]
print(type(data_frame))

# 用比较运算 逻辑运算 来过滤数据
print(3 > 2)
print(3 == 2)
print(True)
print(True and False)

pd.set_option('display.max_columns', None)  # 给最大列设置为10列
pd.set_option('display.max_rows', None)  # 设置最大可见100行
pd.set_option('display.width', 1000)
# 1 过滤数据: 防御值大于200的怪物3只
x = data['Defense'] > 200
print(data[x])
# 2 使用逻辑运算符and过滤数据
# 防御值大于200且攻击值大于100的口袋妖怪只有2只
print(data[np.logical_and(data['Defense'] > 200, data['Attack'] > 100)])
# 3 使用&达到相同的效果
print(data[(data['Defense'] > 200) & (data['Attack'] > 100)])
