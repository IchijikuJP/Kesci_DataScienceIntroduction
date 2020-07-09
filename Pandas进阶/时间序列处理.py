# datetime=object
# parse_dates(boolean): 将日期转换为ISO8601 (yyyy-mm-dd hh:mm:ss ) 格式

import pandas as pd

data = pd.read_csv("../Pokemon.csv")
pd.set_option('display.max_columns', None)  # 给最大列设置为10列
pd.set_option('display.max_rows', None)  # 设置最大可见100行
pd.set_option('display.width', 1000)

time_list = ["1995-09-26", "1995-11-30"]
print(type(time_list[1]))  # 此时日期是str类型
# 把其变成datetime类型
datetime_object = pd.to_datetime(time_list)
print(type(datetime_object))

# 调用filterwarnings()关闭警告消息
import warnings

warnings.filterwarnings("ignore")
# 取Pokemon数据集前5行进行练习
data2 = data.head(5)
date_list = ["1992-01-10", "1992-02-10", "1992-03-10", "1993-03-15", "1993-03-16"]
# 转换为datetime类型
datetime_object = pd.to_datetime(date_list)
data2["date"] = datetime_object
# 设置日期作为索引
data2 = data2.set_index("date")
print(data2)

# 现在可以根据日期索引筛选数据
print(data2.loc["1993-03-16"])
print(data2.loc["1992-03-10":"1993-03-16"])

