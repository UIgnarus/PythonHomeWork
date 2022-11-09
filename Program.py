
n = int(input())
position = [int(i) for i in input().split()]
array = [int(i) for i in range(-n, n+1)]
result = int(1)
for i in range(len(position)):
    result*= array[position[i]]
print(int(result))
