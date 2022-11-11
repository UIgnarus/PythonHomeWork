"""
Напишите программу, которая найдёт
произведение пар чисел списка.
Парой считаем первый и последний элемент,
второй и предпоследний и т.д.

Пример:

- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]
"""

def pairwise_sum(list):
    result_list = []
    for i in range((len(list)//2+len(list)%2)):
        result_list.append(list[i]*list[-i-1])
    return result_list

def functional_testing():
    list1 = [2, 3, 4, 5, 6]
    result1 = [12, 15, 16]
    if pairwise_sum(list1) == result1:
        print("Test#1 - OK")
    else:
        print("Test#1 - Fail")
    list2 = [2, 3, 5, 6]
    result2 = [12, 15]
    if pairwise_sum(list2) == result2:
        print("Test#2 - OK")
    else:
        print("Test#2 - Fail")

functional_testing()

n = [int(item) for item in input().split()]
print(pairwise_sum(n))
