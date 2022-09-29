def calc1():
    while(True):
        print('Введите два числа и операцию')
        a = input()
        if a == "q": return 0
        b = input()
        if b == "q": return 0
        operation = input()
        if operation == "q": return 0
        a = int(a)
        b = int(b)
        if operation == '+':
            print(a + b)
        elif operation == '-':
            print(a - b)
        elif operation == '*':
            print(a * b)
        elif operation == '/':
            print(a / b)
print('Чтобы выйти из программы, введите q\n')
calc1()