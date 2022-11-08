"""
Задача 2 - task2

Напишите программу для.
 проверки истинности утверждения 
 ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
 для всех значений предикат.
"""
# def inputNumbers(x):
#     xyz = ["X", "Y", "Z"]
#     a = []
#     for i in range(x):
#         a.append(input(f"Введите значение {xyz[i]}: "))
#     return a

def checkPredicate(x):
    left = not (x[0] or x[1] or x[2])
    right = not x[0] and not x[1] and not x[2]
    result = left == right
    return result


for x in range(0,2):
    for y in range(0,2):
        for z in range(0,2):
            print(checkPredicate([x, y, z]))

