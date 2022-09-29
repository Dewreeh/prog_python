def fibonachi(n):
    i = 1
    f1 = 1
    f2 = 1
    f_sum = 0
    while(i <= n-2):
        f_sum = f1+f2
        f1 = f2
        f2 = f_sum
        print(f_sum)
        i+=1
print(fibonachi(15))
