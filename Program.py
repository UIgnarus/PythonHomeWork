"""
Продолжение
Вычислить число c заданной точностью d

Пример:

- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
"""

from math import pi

def rounding_pi(d):
    """
    10^{-1} ≤ d ≤10^{-10}
    """
    rounding = len(str(d)) - 2
    result = int(pi * 10**rounding)/10**rounding
    return result

def functional_testing():
    input_1 = 0.001
    result_1 = 3.141
    if rounding_pi(input_1) == result_1:
        print("Test#1 - OK")
    else:
        print("Test#1 - Fail")
    input_2 = "0.00001"
    result_2 = 3.14159
    if rounding_pi(input_2) == result_2:
        print("Test#2 - OK")
    else:
        print("Test#2 - Fail")

functional_testing()

d = input()
print(rounding_pi(d))

        
