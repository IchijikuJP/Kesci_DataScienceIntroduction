# 1使用普通函数 2使用Lambda函数 3使用其他列创建新列
import pandas as pd

data = pd.read_csv("../Pokemon.csv")  # 写入数据
pd.set_option('display.max_columns', None)  # 给最大列设置为10列
pd.set_option('display.max_rows', None)  # 设置最大可见100行
pd.set_option('display.width', 1000)


# 使用普通函数
def div(n):
    return n / 2


# print(data.HP.apply(div))

# 使用Lambda函数
# print(data.HP.apply(lambda n: n / 2))

# 使用其他列创建新列
data["total_power"] = data.Attack + data.Defense
print(data.head())
