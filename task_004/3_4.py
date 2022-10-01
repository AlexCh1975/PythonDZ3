# Задайте список из произвольных вещественных чисел, количество задает пользователь.
# Напишите программу, которая найдет разницу между максимальным и минимальным значением 
# дробной части элементов.

# in 3 out [2.84, 9.42, 1.87] --> "Min: 0.42, Max: 0.87. Difference: 0.45"
# in 4 out [4.83, 9.91, 7.74, 9.39] --> "Min: 0.39, Max: 0.91. Difference: 0.52"

from random import uniform

def create_list(size):
    size = size if size > 0 else -size
    numbers = [round(uniform(1, 10), 2) for i in range(size)]
    return numbers

def find_difference_max_min(list):
    temp = []
    for i in range(len(list)):
        temp.append(round((list[i] - int(list[i])), 2))

    e_max = max(temp)
    e_min = min(temp)
    difference = round((e_max - e_min), 2)

    print("Min: {0}, Max: {1}. Difference: {2}".format(e_min, e_max, difference))


numbers = create_list(int(input("Размер списка: ")))
print(numbers)
find_difference_max_min(numbers)