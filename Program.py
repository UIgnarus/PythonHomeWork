
n = int(input())

def factorial_seqance(x):
    a = [1]
    result = "1"
    for i in range(2, x + 1):
        a.append(i*a[i-2])
        result += " " + str(a[i-1]) 
    return result

print(factorial_seqance(n))
