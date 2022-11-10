"""
Задайте список из нескольких чисел.
Напишите программу, которая найдёт сумму элементов списка, 
стоящих на нечётной позиции.

Пример:

- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9,
 ответ: 12
"""

def sum_on_odd(list):
    sum = 0
    for i in range(1, len(list), 2):
        sum+=list[i]
    return sum

def functional_testing():
    list1 = [2, 3, 5, 9, 3]
    result1 = 12
    if sum_on_odd(list1) == result1:
        print("Test#1 - OK")
    else:
        print("Test#1 - Fail")

functional_testing()

n = [int(item) for item in input().split()]
print(sum_on_odd(n))