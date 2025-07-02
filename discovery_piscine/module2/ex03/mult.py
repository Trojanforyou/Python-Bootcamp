#!/usr/bin/env python3
first_num = int(input("Enter the first number :\n"))
second_num = int(input("Enter the second number :\n"))
if (first_num * second_num > 0):
    print(f"{first_num} X {second_num} = {first_num * second_num}\nThe result is positive")
elif(first_num * second_num == 0):
    print(f"{first_num} X {second_num} = {first_num * second_num}\nThe result is zero")
else:
    print(f"{first_num} X {second_num} = {first_num * second_num}\nThe result is negative")