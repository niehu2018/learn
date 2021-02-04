#!/usr/bin/python3

def fab(max):
    n, a, b = 0, 0, 1
    L = []
    while n < max:
        L.append(b)
        a, b = b, a + b
        n = n + 1
    return L

for n in fab(10):
    print(n)

# 改写后的fab函数通过返回list能满足复用性的要求。
# 更有经验的开发者会支出，该函数在运行中占用的内存会随着参数max的增加而增大
# 如果要控制内存占用，最好不要用list来保存中间结果，而是通过iterable对象来迭代。
