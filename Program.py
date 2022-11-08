"""
Реализуйте алгоритм перемешивания списка.
"""
import random

def mixing(input_list):
    result_list = []
    while input_list != []:
        x = random.randrange(0,len(input_list))
        result_list.append(input_list[x])
        input_list.pop(x)
    return result_list


list = [i for i in input("list = ").split()]

print(list)
print(mixing(list))


