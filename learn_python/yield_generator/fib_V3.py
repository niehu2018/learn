#!/usr/bin/python2
# -*- coding: UTF-8 -*-
class Fab(object):

    def __init__(self, max):
        self.max = max
        self.n, self.a, self.b = 0, 0 ,1

    def __iter__(self):
        return self

    def next(self):
        if self.n < self.max:
            r = self.b
            self.a, self.b = self.b, self.a + self.b
            self.n = self.n + 1
            return r
        raise StopIteration()

for n in Fab(10):
    print(n)

# 以上代码只能用python2运行
# Python3环境下应该如何写，还有待探索
# Fab类通过next()不断返回数列的下一个数，内存占用始终为常数

# 然而，使用class改写的版本，代码远远没有第一版的fab函数简洁
# 如果我们想要保持第一版fab函数的简洁性，同时又要获得iterable的效果，yield就派上用场了
