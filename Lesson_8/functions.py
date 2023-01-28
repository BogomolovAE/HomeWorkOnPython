def addstudent(studentlist, journal):
    studentlist.append(input('Введите имя '))
    journal.append([])
    for j in range(len(journal[0])):
      journal[-1].append()


def addsubject(subjectlist, journal):
    subjectlist.append(input('Введите  предмет '))
    for student in journal:
        student.append([])


def addgrade(studentlist, subjectlist, journal):
    student = studentlist.index(str(input('Введите имя ')))
    subject = subjectlist.index(str(input('Введите предмет ')))
    grade = input('Введите оценку ')
    [journal[student][subject].append(int(i)) for i in list(grade)]


def printstudents(list):
    for student in list:
        print(student)


def printgrades(studentlist, subjectlist, journal):
    student = studentlist.index(str(input('Введите имя ')))
    for i in range(len(subjectlist)):
        print(subjectlist[i], '  ', journal[student][i])


def help():
    print("1 addstudent - добавление студента")
    print("2 addsubject - добавление предмета")
    print("3 addgrade - добавление оценки")
    print("4 printstudents - список учеников")
    print("5 printgrades - список оценок ученика")