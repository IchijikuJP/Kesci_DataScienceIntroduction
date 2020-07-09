# 数据索引
# 1使用[]索引 2使用列属性和行标签 3使用loc访问器 4只选择某些列

import pandas as pd

data = pd.read_csv("../Pokemon.csv")  # 写入数据
pd.set_option('display.max_columns', None)  # 给最大列设置为10列
pd.set_option('display.max_rows', None)  # 设置最大可见100行
pd.set_option('display.width', 1000)

data = data.set_index("#")
print(data.head())

# 方括号索引
print(data["HP"][3])
# 使用列属性和行标签
print(data.HP[3])
# 使用loc访问器
print(data.loc[1, ["HP"]])
# 只选取某些列
# print(data[["HP", "Attack"]])

# 列选取的差异: series和data frames
print(type(data["HP"]))  # series
print(type(data[["HP"]]))  # data frames

# 用索引切片
print(data.loc[1:10, "HP":"Defense"])  # 包括第10行和"Defense"列
# 反向切片
print(data.loc[10:1:-1, "HP":"Defense"])

# 从某一列开始到最后一列
print(data.loc[1:10, "HP":])  # 从HP到最后

