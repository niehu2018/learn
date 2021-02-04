#!/usr/bin/python3
from inspect import isgeneratorfunction
from collections.abc import Iterable
import types
def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield(b) # 使用yield
        #print(b)
        a, b = b, a + b
        n = n + 1

# fab是生成器函数，而fab(10)是调用fab函数返回的一个生成器
# 好比类的定义和类的实例的区别

# fab()
if isgeneratorfunction(fab):
    print("fab is a generator function")

if isinstance(fab, Iterable) == False:
    print('fab is not iterable')
print("")

# fab(10)
if isinstance( fab(10), types.GeneratorType):
    print("fab(10) is a instance")


if isinstance(fab(10), Iterable) == True:
    print('fab(10) is iterable')
