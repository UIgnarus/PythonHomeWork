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
        for i in range(2, n+1):
            left_list.insert(0, right_list[i]*(-1)**(i+1))
    result = left_list + right_list
    return result

def functional_testing():
    input_1 = 8
    result_1 = [-21, 13, -8, 5, -3, 2,
                -1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
    if fibonacci(input_1) == result_1:
        print("Test#1 - OK")
    else:
        print("Test#1 - Fail")
    input_2 = 0
    result_2 = None
    if fibonacci(input_2) == result_2:
        print("Test#2 - OK")
    else:
        print("Test#2 - Fail")
    input_3 = 1
    result_3 = [1, 0, 1]
    if fibonacci(input_3) == result_3:
        print("Test#3 - OK")
    else:
        print("Test#3 - Fail")
    input_4 = -8
    result_4 = [-21, 13, -8, 5, -3, 2,
                -1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
    if fibonacci(input_4) == result_4:
        print("Test#4 - OK")
    else:
        print("Test#4 - Fail")

functional_testing()

n = int(input())
print(fibonacci(n))
