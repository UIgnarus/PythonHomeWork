n = round(float(input()), 4)

def numbers_sum(x):
    sum = 0
    for i in str(x):
        if i.isdigit():
            sum+=int(i)
    return sum

print(int(numbers_sum(n)))


