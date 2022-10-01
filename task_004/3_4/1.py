from random import uniform

def create_list(size):
    size = size if size > 0 else -size
    numbers = [round(uniform(1, 10), 2) for i in range(size)]
    return numbers

def find_difference_max_min(list):
    temp = []
    for i in range(len(list)):
        temp.append(round((list[i] - int(list[i])), 2))

    e_max = temp[0]
    e_min = temp[0]

    for i in range(len(temp)):
        if temp[i] > e_max: e_max = temp[i]
        elif temp[i] < e_min: e_min = temp[i]
    
    difference = round((e_max - e_min), 2)

    print("Min: {0}, Max: {1}. Difference: {2}".format(e_min, e_max, difference))


numbers = create_list(int(input("Размер списка: ")))
print(numbers)
find_difference_max_min(numbers)