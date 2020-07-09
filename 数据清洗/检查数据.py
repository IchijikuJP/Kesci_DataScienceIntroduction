# unclean data:
# 列名不一致, 数据缺失, 语言不同
# 经常使用head tail columns shape 和info等函数来检查数据
import pandas as pd
data = pd.read_csv("../Pokemon.csv")

pd.set_option('display.max_columns', None)  # 给最大列设置为10列
pd.set_option('display.max_rows', None)  # 设置最大可见100行
pd.set_option('display.width', 1000)

# DataFrame开头的5行数据
print(data.head(5))
print(data.tail(3))
print(data.columns)  # 查看列名
print(data.shape)  # 查看行数,列数
print(data.info())  # 展示index datatype memory相关信息
