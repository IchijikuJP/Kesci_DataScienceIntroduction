# 也叫匿名函数, 允许快速定义单行函数
# lambda函数没有名称, 会返回一个函数对象
# lambda函数后面只能有一个表达式

# 单个参数的lambda函数
square = lambda x: x ** 2  # where x is name fo argument
print(square(4))

# 多个参数的lambda函数
tot = lambda x, y, z: x + y + z  # where x,y,z are names of arguments
print(tot(1, 2, 3))

# 下一个例子
number_list = [1, 2, 3]
# map(func,seq): 对列表中的所有项应用函数
y = map(lambda x: x ** 2, number_list)
print(list(y))
