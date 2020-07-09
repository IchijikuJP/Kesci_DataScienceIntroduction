from pivot函数 import df1
import pandas as pd
print(df1)

# 聚合取平均值
print(df1.groupby("treatment").mean())
# 还有其他方法如:sum std max min

# 选择一个特征
print(df1.groupby("treatment").age.max())
# 也可以选择多个特征
print(df1.groupby("treatment")[["age", "response"]].min())

print(df1.info())
