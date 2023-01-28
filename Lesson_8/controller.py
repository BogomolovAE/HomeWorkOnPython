from functions import *

help()
students = []
subjects = []
journal = []
command = input('Введите команду ')
while command != 'exit':
    try:
        if (command == 'addstudent') or (command == '1'):
            addstudent(students, journal)
            print(students)
            print(journal)
        elif (command == 'addsubject') or (command == '2'):
            addsubject(subjects, journal)
            print(subjects)
            print(journal)
        elif (command == 'addgrade') or (command == '3'):
            addgrade(students, subjects, journal)
        elif (command == 'printstudents') or (command == '4'):
            printstudents(students)
        elif (command == 'printgrades') or (command == '5'):
            printgrades(students, subjects, journal)
        elif command == 'help':
            help()   
        command = input('Введите команду ')
    except Exception:
        command = input('Будьте внимательнее! Введите команду повторно ')
