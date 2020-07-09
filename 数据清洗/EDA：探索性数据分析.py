# value_counts(): pandas的函数, 可以对序列里的每个值进行计数并且排序
# 离群值(outliers): 也称逸出值
# describe()函数总结数据集分布的中心趋势
# 常用的算数指标: count出现次数 mean平均值 std标准差 25%第一四分位数
# 50%中位数 75%第三四分位数

import pandas as pd

data = pd.read_csv("../Pokemon.csv")
pd.set_option('display.max_columns', None)  # 给最大列设置为10列
pd.set_option('display.max_rows', None)  # 设置最大可见100行
pd.set_option('display.width', 1000)

# 看看不同属性口袋妖怪出现的频率
print(data['Type 1'].value_counts(dropna=False))  # 此处为降序排列, 升序排列为True
# 水系小精灵有112个

print(data.describe())  # 其中NaN值被忽略掉

