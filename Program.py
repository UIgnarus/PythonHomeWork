"""
1 Напишите программу, которая принимает
 на вход вещественное число и показывает сумму его цифр.
Пример:
- 6782 -> 23
- 0,56 -> 11
"""
n = (input("n = "))

def numbers_sum(x):
    sum = 0
    for i in x:
        if i.isdigit():
            sum+=int(i)
    return sum

print(numbers_sum(n))


