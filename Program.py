"""
Напишите программу, которая будет преобразовывать
десятичное число в двоичное.

Пример:

- 45 -> 101101
- 3 -> 11
- 2 -> 10
"""

def to_binary(x):
    list = []
    while x > 0:
        list.append(x%2)
        x//=2
    result = ""
    for i in range(len(list)):
        result+=str(list[-i-1])
    return int(result)

def functional_testing():
    input_1 = 45
    result_1 = 101101
    if to_binary(input_1) == result_1:
        print("Test#1 - OK")
    else:
        print("Test#1 - Fail")
    input_2 = 3
    result_2 = 11
    if to_binary(input_2) == result_2:
        print("Test#2 - OK")
    else:
        print("Test#2 - Fail")
    input_3 = 2
    result_3 = 10
    if to_binary(input_3) == result_3:
        print("Test#3 - OK")
    else:
        print("Test#3 - Fail")

functional_testing()

n = int(input())
print(to_binary(n))