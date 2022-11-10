"""
Задайте список из вещественных чисел.
Напишите программу, которая найдёт разницу
между максимальным и минимальным значением
дробной части элементов.

Пример:

- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
"""

def discarding(list):
    """
    Функция отбрасывает целую часть у числа
    и записывает в новый список
    """
    result_list = []
    for i in range(len(list)):
        if int(list[i]) != list[i]:
            rounding = len(str(list[i])) - (len(str(int(list[i])))+1)
            result_list.append(round(list[i]%1, rounding))
    return result_list

def find_min_and_max(list):
    min = list[0]
    max = list[0]
    for i in range(1, len(list)):
        if list[i] > max:
            max = list[i]
        if list[i] < min:
            min = list[i]
    return [min, max]

def fractional_difference(list):
    values = find_min_and_max(discarding(list))
    return (values[1] - values[0])
    

def functional_testing():
    list1 = [1.1, 1.2, 3.1, 5, 10.01]
    result1 = 0.19
    if fractional_difference(list1) == result1:
        print("Test#1 - OK")
    else:
        print("Test#1 - Fail")

functional_testing()

n = [float(item) for item in input().split()]
print(fractional_difference(n))