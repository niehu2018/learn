#!/usr/bin/python3

def divide(x, y):
    try:
        result = x/y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print( "result is " + str(result) )
    finally:
        print("executing finally clause")

divide(2,1)
print()
divide(2,0)
