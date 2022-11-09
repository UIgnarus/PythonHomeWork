n = float(input())
sum = 0
for i in str(n):
    if i != ".":
        sum+=int(i)
print(int(sum))