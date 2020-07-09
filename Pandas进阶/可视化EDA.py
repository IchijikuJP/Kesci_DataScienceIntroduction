# 探索性数据分析（Exploratory Data Analysis，简称EDA）
# 对于已有数据在尽量少的先验假定下进行探索, 通过作图 制表 方程拟合 计算特征量等手段探索数据的结构和规律的一种数据分析方法

# 1绘图 2绘制子图 3 直方图(柱状图)
# 直方图参数: bins(条形个数) range(tuple)上下界,最大值最小值
# density(boolean)是否将直方图的频数转换成频率
# cumulative(Boolean)是否需要计算累计频数或频率

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("../Pokemon.csv")

pd.set_option('display.max_columns', None)  # 给最大列设置为10列
pd.set_option('display.max_rows', None)  # 设置最大可见100行
pd.set_option('display.width', 1000)

# 绘制所有数据
data1 = data.loc[:, ["Attack", "Defense", "Speed"]]
# data1.plot()
# plt.show()
# 三个曲线混在一张图里看起来很乱

# 分别绘制子图
# data1.plot(subplots=True)
# plt.show()

# 绘制散点图
# data1.plot(kind="scatter", x="Attack", y="Defense")
# plt.show()

# 直方图
# data1.plot(kind="hist", y="Defense", bins=50, range=(0, 250), density=False)

# 将直方图的频数转换成频率
# data1.plot(kind="hist", y="Defense", bins=50, range=(0, 250), density=True)
# plt.show()

# 统计直方图
fig, axes = plt.subplots(nrows=2, ncols=1)
data1.plot(kind="hist", y="Defense", bins=50, range=(0, 250), density=True, ax=axes[0])
# 累计直方图
data1.plot(kind="hist", y="Defense", bins=50, range=(0, 250), density=True, ax=axes[1], cumulative=True)
plt.savefig('graph.png')
plt.show()
