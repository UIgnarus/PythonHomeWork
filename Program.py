"""
Задайте число.
Составьте список чисел Фибоначчи, в
том числе для отрицательных индексов.

Пример:

- для k = 8 список будет выглядеть так:
[-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

"""


def fibonacci(n):
    n = abs(n)
    right_list = [0, 1]
    left_list = [1]
    if n == 0:
        return None
    if n > 1:
        for i in range(1, n):
            right_list.append(right_list[i]+right_list[i-1])
        for i in range(2,n+1):
            left_list.insert(0, right_list[i]*-1**(i+1))
    result = left_list + right_list
    return result


