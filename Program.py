string = list(input())
coded_string = ''
k = 1
for i in range(len(string) - 1):
    if string[i] == string[i + 1]:
        k += 1
        continue
    else:
        coded_string += str(k) + string[i]
        k = 1
coded_string += str(k) + string[-1]
print(coded_string)