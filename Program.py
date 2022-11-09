array = [int(i) for i in input().split()]
for i in range(len(array)- 1):
    array[i], array[i+1] = array[i+1], array[i]
    print(int(array[i]), end = " ")
print(int(array[-1]))