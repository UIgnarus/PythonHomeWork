"""
Продолжение
Вычислить число c заданной точностью d

Пример:

- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
"""

from math import pi


def rounding_pi(d):
    rounding = len(str(d)) - (len(str(int(d)))+1)
    return round(pi, rounding)




        
