def triangle(a, b, c):
    p = (a+b+c)/2
    high_from_a = (2*(p*(p-a)*(p-b)*(p-c))**0.5)/a
    high_from_b = (2*(p*(p-a)*(p-b)*(p-c))**0.5)/b
    high_from_c = (2*(p*(p-a)*(p-b)*(p-c))**0.5)/c
    print("Высоты:", high_from_a, high_from_b, high_from_c)
    AM = ((2*c**2 + 2*b**2 - a**2)**0.5)/2
    BM = ((2*c**2 + 2*a**2 - b**2)**0.5)/2
    CM = ((2*a**2 + 2*b**2 - c**2)**0.5)/2
    print("Медианы:", AM, BM, CM)

triangle(int(input("введите a: ")), int(input("введите b: ")), int(input("введите c: ")))