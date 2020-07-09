# 使用melt()函数来转换数据的行列
# pandas.melt(frame, id_vars=None, value_vars=None, var_name=None, value_name='value', col_level=None)
import pandas as pd

data = pd.read_csv("../Pokemon.csv")

pd.set_option('display.max_columns', None)  # 给最大列设置为10列
pd.set_option('display.max_rows', None)  # 设置最大可见100行
pd.set_option('display.width', 1000)

# 从Pokemon数据中创建一组新的数据
data_new = data[10:15]
print(data_new)
# 使用melt()函数
# frame:要处理的数据集
# id_vars: 不需要被转换的列名
# value_vars ：需要转换的列名
melted = pd.melt(frame=data_new, id_vars='Name', value_vars=['Attack', 'Defense'])
print(melted)
print(melted.pivot(index='Name', columns='variable', values='value'))
