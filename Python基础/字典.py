# 字典dict是另一种可变容器模型
# 创建一个字典
dictionary = {'spain': 'madrid', 'usa': 'vegas'}
# 打印字典中的keys和values
print(dictionary.keys())
print(dictionary.values())

# 键必须是不可变的对象，如字符串、布尔值、浮点数、整数、元组
# 列表是可变的对象，不能作为键
# 键是唯一的，创建时如果同一个键被赋值两次，后一个值会被记住
# 值不需要唯一
dictionary['spain'] = "barcelona"  # 将‘spain’对应的值从‘madrid’替换为‘barcelona’
print(dictionary)
dictionary['france'] = "paris"  # 增加新的键/值对
print(dictionary)
del dictionary['spain']  # 删除键是‘spain’的条目
print(dictionary)
print('usa' in dictionary)  # 查看‘spain’是否在字典里
dictionary.clear()  # 清空字典所有条目
print(dictionary)

