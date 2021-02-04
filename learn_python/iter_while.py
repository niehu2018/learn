#!/usr/bin/python3
import sys

mylist = [1,2,3,4] # 创建列表
it = iter(mylist)  # 创建迭代器

while True:
    try:
        print( next(it) )
    except StopIteration:
        sys.exit()
