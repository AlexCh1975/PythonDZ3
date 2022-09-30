# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in
# 4

# out
# [2, 5, 8, 10]
# [20, 40]

# in
# 5

# out
# [2, 2, 4, 8, 8]
# [16, 16, 4]

from random import randint

def create_list(size):
    size = size if size > 0 else -size
    numbers = [randint(1, 10) for i in range(size)]
    return numbers

numbers = create_list(int(input("Введите размер списка: ")))
print(numbers)

def find_sum_pairs(list):
    new_numbers = []
    i = 0
    while True:
        if i == int(len(list)/2):
            if len(list) % 2 != 0:
                new_numbers.append(list[int(len(list)/2)])
            print(new_numbers)
            break
        else:
           new_numbers.append((list[i]) * (list[(len(list)-1) - i]))
        i += 1    

find_sum_pairs(numbers)