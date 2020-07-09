# 列表推导式list comprehension 非常重要
# 列表推导式或列表解析式是一种简洁的创建列表的方式
# 比for循环更高效(执行时调用底层C代码,而for循环用python代码)
# 语法：[i+1 for i in range(10) if i%2==0]
import pandas as pd
import numpy as np
# 列表推导式示例
num1 = [1, 2, 3]
num2 = [i + 1 for i in num1]
print(num2)
# 使用if语句进行过滤
num1 = [6, 10, 15]
num2 = [i ** 2 if i == 10 else i - 5 if i < 7 else i + 6 for i in num1]
print(num2)

# 使用口袋妖怪数据集, 进一步联系列表推导式
# 将Pokemon按速度分为两类, 大于平均速度的值归为high speed, 否则归为low speed
data = pd.read_csv('../Pokemon.csv')
average_speed = sum(data.Speed) / len(data.Speed)
data["speed_level"] = ["high" if i > average_speed else "low" for i in data.Speed]
print(data.loc[:8, ["speed_level", "Speed"]])
