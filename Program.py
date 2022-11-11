"""
Продолжение
Вычислить число c заданной точностью d

Пример:

- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
"""

from math import pi

d =  float(input())

def rounding(d):
    for i in range(len(str(d))):
        
