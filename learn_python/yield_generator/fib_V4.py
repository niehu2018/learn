#!/usr/bin/python3

def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield(b) # 使用yield
        #print(b)
        a, b = b, a + b
        n = n + 1

# Run
for n in fab(10): # 使用for循环遍历迭代器
    print(n)

# 第四版的fab与第一版的fab相比，仅仅是把print b改为了yield b
# 就在保持简洁性的同时获得了iterable的效果
# 调用第四版的fab和第二版的fab完全一致


# 简单地讲，yield 的作用就是把一个函数变成一个 generator，带有 yield 的函数不再是一个普通函数。
# Python解释器会将其视为一个generator，调用fab(5)不会执行fab函数，而是返回一个iterable 对象！
# 在for循环执行时，每次循环都会执行fab函数内部的代码，执行到yield b时，fab函数就返回一个迭代值，下次迭代时，代码从yield b的下一条语句继续执行，而函数的本地变量看起来和上次中断执行前是完全一样的，于是函数继续执行，直到再次遇到yield。
# 也可以手动调用fab(10)的next()方法因为fab(10)是一个generator对象，该对象具有next()方法），这样我们就可以更清楚地看到 fab 的执行流程

# 当函数执行结束时，generator自动抛出StopIteration异常，表示迭代完成。在for循环里，无需处理StopIteration 异常，循环会正常结束。
