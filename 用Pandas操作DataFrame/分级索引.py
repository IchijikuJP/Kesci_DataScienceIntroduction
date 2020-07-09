import pandas as pd

data = pd.read_csv("../Pokemon.csv")  # 写入数据
pd.set_option('display.max_columns', None)  # 给最大列设置为10列
pd.set_option('display.max_rows', None)  # 设置最大可见100行
pd.set_option('display.width', 1000)

print(data.head())
# 可以看到这里有索引 但我们希望将一个或多个列设置为索引

# 设置索引: Type1是外部索引 Type2是内部索引
data1 = data.set_index(["Type 1", "Type 2"])
print(data1.head(20))
# print(data1.loc["Fire", "Flying"])  # 如何使用索引
