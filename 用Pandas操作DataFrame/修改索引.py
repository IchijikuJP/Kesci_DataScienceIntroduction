import pandas as pd

data = pd.read_csv("../Pokemon.csv")  # 写入数据
pd.set_option('display.max_columns', None)  # 给最大列设置为10列
pd.set_option('display.max_rows', None)  # 设置最大可见100行
pd.set_option('display.width', 1000)

# index: label序列
data = data.set_index("#")
print(data.head())
print(data.index.name)  # 结果是None
# 改变一下试试
data.index.name = "编号"
print(data.head())

# 修改索引需要整体修改所有的索引
# 将数据赋值到data3, 然后更改索引
data3 = data.copy()
# 让索引从100开始
data3.index = range(100, 900, 1)
print(data3.head())
