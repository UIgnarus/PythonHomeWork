n = int(input())
list = [(1+1/i)**i for i in range(1, n + 1)]
sum = float(0)
for i in range(len(list)):
    sum+= list[i]
sum = float(sum)
print(sum)
