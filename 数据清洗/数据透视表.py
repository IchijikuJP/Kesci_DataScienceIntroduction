# pivot()函数根据列值重塑数据, 生成数据透视表
# DataFrame.pivot_table(index=None, columns=None, values=None)
from 重塑数据 import melted
import pandas as pd

data = pd.read_csv("../Pokemon.csv")

pd.set_option('display.max_columns', None)  # 给最大列设置为10列
pd.set_option('display.max_rows', None)  # 设置最大可见100行
pd.set_option('display.width', 1000)

# 根据上面的'melted'数据表生成一张新表
# 新表显示名字 及对应的攻击防御值

# 设置index为'name'
# 设置column为'variable'
# 设置values为'value'
print(melted.pivot(index='Name', columns='variable', values='value'))

