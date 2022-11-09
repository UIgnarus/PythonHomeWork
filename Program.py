n = round(float(input()), 4)
sum = 0
for i in str(n):
    if i.isdigit():
        sum+=int(i)
print(int(sum))