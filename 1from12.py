def eratosphen(n):
    k = 2
    a = list(range(2, n+1))
    while(k**2 <= n**0.5):
        kbefore = k
        k**2
        while(k < n):
            k += kbefore
            if a.count(k) == 1: a.remove(k)
        k = kbefore + 1
    return a
print(eratosphen(2000))




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
