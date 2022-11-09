"""
Задайте список из n чисел последовательности
 $(1+\frac 1 n)^n$ и выведите на экран их сумму.

Пример:
- Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
"""

n = int(input("n = "))

list = {i: round((1+1/i)**i, 2) for i in range(1, n+ 1)}

print(list)

sum = float(0)
for i in range(1, len(list)+1):
    sum+= list[i]
print(f"sum = {sum}")
