"""
Задайте последовательность чисел.
Напишите программу, которая выведет
список неповторяющихся элементов исходной последовательности.
"""

def elimination_of_repetitions(list):
    new_list = []
    [new_list.append(i) for i in list if i not in new_list]
    return new_list

def functional_testing():
    input_1 = [34, 34, 56, 56, 67]
    result_1 = [34, 56, 67]
    if elimination_of_repetitions(input_1) == result_1:
        print("Test#1 - OK")
    else:
        print("Test#1 - Fail")

functional_testing()

list = list(map(int, input().split()))
print(*elimination_of_repetitions(list))