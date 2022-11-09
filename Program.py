array = [int(i) for i in input().split()]
if array[0] % 2:
    array[i], array[i+1] = array[i+1], array[i]
for i in range(1, len(array)-1):
    if not array[i] % 2:
        array[i], array[i-1] = array[i-1], array[i]
    else:
        for j in range(i, len(array) -1):
            array[j], array[j+1] = array[j+1], array[j]
        break
if not array[len(array)-1] % 2:
    array[i], array[i-1] = array[i-1], array[i]
print(*array)
