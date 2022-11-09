n = int(input())
list = [round((1+1/i)**i, 2) for i in range(1, n + 1)]
sum = float(0)
for i in range(len(list)):
    sum+= list[i]
sum = round(float(sum), 2)
print(sum)
