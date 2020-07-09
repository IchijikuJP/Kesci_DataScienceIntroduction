# 容器:是一系列元素的集合, str list set dict file sockets对象都可以是容器
# 容器都可以被迭代(for while等语句中), 因此被称为可迭代对象
# iterable可迭代对象: 实现了iter方法, 该方法返回一个迭代器对象
# iterator迭代器: next()和iter()方法
# 迭代器持有一个内部状态的字段, 用于记录下次迭代返回值
# 迭代器不会一次性把所有元素加载到内存, 而是需要的时候在生成返回结果

# 迭代器示例
name = "ronaldo"
it = iter(name)
print(next(it))  # 打印容器中的下一个值
print(next(it))  # 打印容器中的下一个值
print(next(it))  # 打印容器中的下一个值
print(next(it))  # 打印容器中的下一个值
print(next(it))  # 打印容器中的下一个值
print(*it)   # 打印容器中的剩余值
