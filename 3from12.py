def nok(a, b):
    max = 0
    for i in range(1, int((min(a, b))) + 1):
        if a%i == 0 and b%i == 0:
            if i > max:
                max = i
    return max
a = int(input())
b = int(input())
print((a*b)/nok(a, b))
