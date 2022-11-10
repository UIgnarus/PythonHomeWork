"""
Напишите программу, которая найдёт
произведение пар чисел списка.
Парой считаем первый и последний элемент,
второй и предпоследний и т.д.

Пример:

- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]
"""

n = [int(item) for item in input().split()]


def pairwise_sum(list):
    result_list = []
    for i in range((len(list)//2) if (not len(list) % 2)
                   else (len(list)//2 + 1)):
        result_list.append(list[i]*list[-i-1])
    return result_list

print(pairwise_sum(n))
