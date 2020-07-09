import pandas as pd
from 时间序列处理 import data2

data = pd.read_csv("../Pokemon.csv")
pd.set_option('display.max_columns', None)  # 给最大列设置为10列
pd.set_option('display.max_rows', None)  # 设置最大可见100行
pd.set_option('display.width', 1000)

# 回顾一下data2的样子
print(data2.head(100))
# 按年进行重采样
print(data2.resample("Y").mean())
# 按月进行重采样
print(data2.resample("M").mean())
# 可以看到有很多NaN值，因为data2中不包括所有月份

# 在真实数据场景中 我们可以使用interpolate()"篡改"
# 从初值开始插值
print(data2.resample("M").first().interpolate("linear"))
# 我们也可以使用mean()进行插值
print(data2.resample("M").mean().interpolate("linear"))
# describe()函数总结数据集分布的中心趋势
# 常用的算数指标: count出现次数 mean平均值 std标准差 25%第一四分位数
# 50%中位数 75%第三四分位数
