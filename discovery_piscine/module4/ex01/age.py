#! /usr/bin/env python3
i = 0
j = 1
age = int(input("Please tell me your age: "))
print(f"Your currently {age} years old")
while (i < 3):
    print(f"In {j * 10} years, you'll be {age} years old")
    i += 1
    j += 1
    age += 10