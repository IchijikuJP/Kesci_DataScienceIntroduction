# Python3基础数据类型
# Number(int float bool complex)
# string list tuple set dictionary
# 不同的数据类型间可以转换，例如将字符串转换为categorical数据（分类数据），或者将整数转换为浮点数。
import pandas as pd

data = pd.read_csv("../Pokemon.csv")

pd.set_option('display.max_columns', None)  # 给最大列设置为10列
pd.set_option('display.max_rows', None)  # 设置最大可见100行
pd.set_option('display.width', 1000)

print(data.dtypes)
# 将str转换为categorical(分类数据), 将int转换为float
data['Type 1'] = data['Type 1'].astype('category')
data['Speed'] = data['Speed'].astype('float')
print(data.dtypes)