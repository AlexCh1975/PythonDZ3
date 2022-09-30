# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
# in
# 5

# out
# [10, 2, 3, 8, 9]
# 22

import random

def find_sum(length):
    length = length if length > 0 else -length 
    numbers = [random.randint(0, 100) for i in range(length)]
    sum = 0
    for i in range(length):
        if (i + 1) % 2 != 0: sum += numbers[i]
        # else: sum += numbers[i]
    print(numbers)
    print(sum)

find_sum(int(input("Задайте длину списка: ")))