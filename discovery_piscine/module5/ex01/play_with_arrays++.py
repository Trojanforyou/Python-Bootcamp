#! /usr/bin/env python3
original = [2, 4, 6, 8]
new_list = []
for i in range(len(original)):
    temp = original[i] + 2
    new_list.append(temp)
print(original, new_list)
