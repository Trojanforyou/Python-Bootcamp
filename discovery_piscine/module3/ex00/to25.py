#! /usr/bin/env python3
value = 26
user = int(input("Enter a number less than 25: "))
if (user > 25):
    print("ERROR")
elif (user < 25):
    while(user < value):
        print(f"Inside the loop, my variable is {user}")
        user += 1