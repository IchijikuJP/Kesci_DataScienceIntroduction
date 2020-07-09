import pandas as pd

data = pd.read_csv("../Pokemon.csv")

pd.set_option('display.max_columns', None)  # 给最大列设置为10列
pd.set_option('display.max_rows', None)  # 设置最大可见100行
pd.set_option('display.width', 1000)

# 将两个DataFrame连在一起
# 首先生成两个新的DataFrame
data1 = data.head(3)
data2 = data.tail(3)
# 使用comcat函数将两个表拼接在一起
conc_data_row = pd.concat([data1, data2], axis=0, ignore_index=True)
# axis = 0 : 行拼接，即纵向拼接
print(conc_data_row)

data3 = data['Attack'].head(3)
data4 = data['Defense'].head(3)
conc_data_col = pd.concat([data3, data4], axis=1)
# axis = 1 : 列拼接, 即横向拼接
print(conc_data_col)
