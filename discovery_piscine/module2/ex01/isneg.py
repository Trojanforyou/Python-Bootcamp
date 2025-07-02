#! /usr/bin/env python3
user = int(input(""))
if (user < 0):
    print("This number is negative")
elif (user > 0):
    print("This number is positive")
else:
    print("This number is both positive and negative")