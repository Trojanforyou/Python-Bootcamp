#! /usr/bin/env python3

arr = [2, 8, 9, 48, 8, 22, -12, 2]
new_arr = set() #set() создает множество Множество это неупорядоченная коллекция уникальных элементов
for i in range(len(arr)):
    if (arr[i] > 5):
        new_arr.add(arr[i] + 2) #.add()  это метод множества, который добавляет элемент в set
print(new_arr)