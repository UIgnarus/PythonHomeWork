"""
Задайте натуральное число N.
Напишите программу, которая составит список простых множителей числа N.
"""

def simple_multiplies(n):
    list = []
    divider = 2
    while n > 1:
        if n % divider == 0:
            list.append(divider)
            n//=divider
        else:
            divider +=1
    return list

def functional_testing():
    input_1 = 1945
    result_1 = [5, 389]
    if simple_multiplies(input_1) == result_1:
        print("Test#1 - OK")
    else:
        print("Test#1 - Fail")
functional_testing()

n = int(input())
print(*simple_multiplies(n))



