"""
1 Напишите программу,
 которая принимает на вход число N 
 и выдает набор произведений чисел от 1 до N.
Пример:
- пусть N = 4,
 тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
"""

n = int(input("n = "))

def factorial_sequence(x):
    a = [1]
    for i in range(2,x+1):
        a.append(i*a[i-2])
    return(a)

print(factorial_sequence(n))
