# nested function
# 嵌套函数实在另一个函数中定义的函数
# 示例


def square():
    '''return square of value'''
    def add():
        """add two local variable"""
        x = 2
        y = 3
        z = x+y
        return z
    return add()**2


print(square())
