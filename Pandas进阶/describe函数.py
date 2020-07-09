# describe()函数总结数据集分布的中心趋势
# 常用的算数指标: count出现次数 mean平均值 std标准差 25%第一四分位数
# 50%中位数 75%第三四分位数

import pandas as pd

data = pd.read_csv("../Pokemon.csv")
pd.set_option('display.max_columns', None)  # 给最大列设置为10列
pd.set_option('display.max_rows', None)  # 设置最大可见100行
pd.set_option('display.width', 1000)

print(data.describe())