def football_students():
    students = {}
    i = 0
    print("Введите кол-во записей:")
    n = int(input())
    while(i < n):
        print("Введите фамилию")
        surname = input()
        print("Введите группу")
        group = input()
        students[surname] = group
        i+=1
    print(dict(sorted(students.items(), key=lambda item: item[1])))
    sorted(students.keys())

football_students()