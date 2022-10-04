def neg_fib(num):
    list_nums = [0]
    a, b = 1, 1

    for i in range(num):
        list_nums.append(a)
        list_nums.insert(0, a * (-1) ** i)
        a, b = b, b + a

    return list_nums

print(*neg_fib(int(input("Число: "))))