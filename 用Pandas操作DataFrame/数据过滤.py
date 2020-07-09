# 1创建一个布尔序列 2多重过滤 3基于其他过滤列的过滤
import pandas as pd

data = pd.read_csv("../Pokemon.csv")  # 写入数据
pd.set_option('display.max_columns', None)  # 给最大列设置为10列
pd.set_option('display.max_rows', None)  # 设置最大可见100行
pd.set_option('display.width', 1000)

# 创建一个布尔序列
boolean = data.HP > 200
print(data[boolean])

# 多重过滤
first_filter = data.HP > 150
second_filter = data.Speed > 35
print(data[first_filter & second_filter])

# 基于其他过滤列的过滤
print(data.HP[data.Speed < 15])  # 打印出速度小于15的小精灵的编号和对应的HP
