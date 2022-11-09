array = [int(i) for i in input().split()]
for i in range(len(array)):
    if array[i] % 2:
        if i < len(array) - 1:
            array[i], array[i+1] = array[i+1], array[i]
    else:
        if i != 0:
            array[i], array[i-1] = array[i-1], array[i]
print(*array)
