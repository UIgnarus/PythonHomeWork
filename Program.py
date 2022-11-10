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
        result+=str(list(-i-1))
    return result
