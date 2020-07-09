# 文档字符串Docstrings: 给代码加注释
def f():
    print('hello world')


"""这个函数的功能是打印hello world"""

f()


# 元组tuple
# 与列表类似 但元组不能修改
# 元组使用小括号, 列表使用方括号
def tuple_ex():
    """return defined t tuple"""
    t = (1, 2, 3)
    return t


# 将tuple分解为a b c三个变量
a, b, c = tuple_ex()
print(a, b, c)
# 打印一下注释内容
print(tuple_ex.__doc__)
# 用help来调用注释内容
help(tuple_ex)
