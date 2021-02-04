#!/usr/bin/python3

while True:
    try:
        x = int( input("Please input a number: "))
        break
    except ValueError:
        print("What you input is not a number, please try again!")
