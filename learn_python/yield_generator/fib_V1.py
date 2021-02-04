#!/usr/bin/python3

def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1

# Run
fab(10)

# 直接在fab函数中用print打印数字会导致该函数可重复性较差, 因为fab函数返回None
# 并且其他函数无法获得该函数生成的序列
