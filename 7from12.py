def factorial(n):
    if n == 0:
        return 1
    return n*factorial(n-1)

def ver():
    p = factorial(100)/factorial((100-3))
    return 1/p

print(ver())