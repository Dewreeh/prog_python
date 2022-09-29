import random
def fun(n):
    array1 = [int(c) for c in "0"*n]
    for i in range(0, n):
        array1[i] = random.randint(-100, 100)
    print(array1)
    array2 = []
    for j in array1:
        if j >= 0:
            array2.append(j)
    print(array2, "max elem:", max(array2))
fun(100)