# 默认参数
# 必选参数在前，默认参数在后，否则python解释器会报错
# 默认参数一定要指向不变对象


def f(a, b=1, c=2):
    y = a + b + c
    return y


print(f(5))
# 当我们想改变默认参数时
print(f(5, 4, 3))


# 可变参数 f(*args)


def f(*args):
    for i in args:
        print(i)


f(1)
print('')
f(1, 2, 3, 4)


# 关键字参数 **kwargs


def f(**kwargs):
    """print key and value of dictionary"""
    for key, value in kwargs.items():
        print(key, ":", value)


f(country='spain', capital='madrid', population=123455)
