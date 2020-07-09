# zip()函数用于将可迭代对象作为参数, 将对象中对应的元素打包成一个个元组
# 然后返回由这些元组组成的对象, 这样可以节约内存
# 如果各个迭代器的元素个数不一致, 则返回列表长度与最短的对象相同

# zip()示例:
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
z = zip(list1, list2)
print(z)
z_list = list(z)
print(z_list)

# 与zip相反, zip(*)可理解为解压, 返回二维矩阵式
un_zip = zip(*z_list)
un_list1, un_list2 = list(un_zip)
print(un_list1)
print(un_list2)
print(type(un_list2))
