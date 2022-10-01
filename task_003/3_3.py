# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования: встроенной функции преобразования, строк.

# in 13 out 1101
# in 88 out 1011000

def get_binary(num):
    binary_num = []

    i = 0
    while True:
        if abs(num / 2) < 1:
            binary_num.append(1)
            return binary_num
        else:
            binary_num.append(num % 2)
            num = int(num / 2)
        i += 1

binary_num = get_binary(int(input("Введите десятичное число: ")))
binary_num.reverse()

for i in binary_num:
    print(i, end='')
print()

