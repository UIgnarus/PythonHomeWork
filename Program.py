"""
Задайте список из N элементов,
 заполненных числами из промежутка [-N, N].
  Найдите произведение элементов на указанных позициях. 
Позиции хранятся в файле file.txt 
в одной строке одно число.
"""
import random
n = int(input("n = "))

a = [random.randrange(-n,n) for i in range(n)]

print(a)

for i in range(n//2):
    print(a[i]*a[(n-1)-i])
