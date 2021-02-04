#!/usr/bin/python3

mylist = [1,2,3,4] # 创建列表
it = iter(mylist)  # 创建迭代器

# 使用for循环遍历迭代器对象
for x in it:
    print(x, end = " ")
print("\n")
