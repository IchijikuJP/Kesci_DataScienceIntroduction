import pandas as pd
import numpy as np

data = pd.read_csv('../Pokemon.csv')
# 条件为真则保持循环
# 直到条件为假, 跳出循环, 执行下一行语句
i = 0
while i != 5:
    print("i是:", i)
    i += 1
print(i, '是5')

list1 = [1, 2, 3, 4, 5, 6]
for i in list1:
    print('i是:', i)
print('')

# 遍历列表中的索引(index)和值(value)
# index:value = 0:1, 1:2, 2:3, 3:4, 4:5, 5:6
# enumerate为内置函数, 对于遍历的对象组成索引序列
for index, value in enumerate(list1):
    print(index, ':', value)
print('')

# 对于字典, 可以使用for循环遍历字典中的所有键值对
dictionary = {'spain': 'madrid', 'france': 'paris'}
for key, value in dictionary.items():
    print(key, ':', value)
print('')

# 在pandas里我们可以使用for循环显示索引和值
# pandas对dataframe遍历的方法: iterrows
for index, value in data[['Attack']][0:2].iterrows():
    print(index, ':', value)
