#! /usr/bin/env python3

user = float(input("Give me a number: "))
#is.integer() метод обьекта типа float в питоне возвращает true если число не имеет дроби и false если имеет. Не работает с int 
if (user.is_integer()): 
    print('Your number is integer. ')
else:
    print("Your number is a decimal. ")