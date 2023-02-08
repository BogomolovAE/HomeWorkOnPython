students = []
disciplines = []
journal = []
from random import randint
import view
def Init():
    global students,journal,disciplines
    students=view.ReadStudentsFromFile()
    disciplines=view.ReadDisciplinesFromFile()
    if len(students)==0 and len(disciplines)==0:
        view.PrintMessage("No students and disciplines records were found")
        return
    journal=view.ReadJournalFromFile()
    JournalChecking()


# Adding student function
def AddStudent(newStudent):
    global students,journal
    students.append(newStudent)                     #adding student to RAM
    view.WriteStudentToFile(newStudent)             #adding student to FILE
    view.AddStudentToJournal(journal)               #adding student to journal in RAM
    view.WriteJournalToFile(journal)


# Adding discipline function
def AddDiscipline(newDiscipline):
    global disciplines,journal
    disciplines.append(newDiscipline)               #adding dscipline to RAM
    view.WriteDisciplineToFile(newDiscipline)       #adding discipline to FILE   
    view.AddDisciplineToJournal(journal)           #adding discipline to journal in RAM
    view.WriteJournalToFile(journal)


# Adding grade function
def AddGrade():
    global students, disciplines, journal
    view.printList(students)
    student=view.GettingNumberFromList('student',students)
    view.printList(disciplines)
    view.PrintMessage(f"You have chosen student: {students[student]}")
    discipline=view.GettingNumberFromList('discipline',disciplines)
    grade = view.readInput(f'grade for student: \"{students[student]}\" in discipline: \"{disciplines[discipline]}\": ')
    journal[student][discipline]+=grade
    view.WriteJournalToFile(journal)


# Printing grades function
def PrintGrades():
    global students, disciplines, journal
    view.printList(students)
    student=view.GettingNumberFromList('student',students)
   
    view.PrintMessage(f"Grades of student \'{students[student]}\'")
    view.PrintMessage(*tuple(map(lambda x:": ".join(x),list(zip(disciplines,journal[student])))))


# Printing students function
def PrintStudents():
    global students
    view.printList(students)


# Journal size cheking function
def JournalChecking():
    global students, disciplines, journal
    if len(journal)==len(students):
         for i in range(len(journal)):
              if not(len(journal[i])==len(disciplines)):
                JournalRebuilding(journal,students,disciplines)
    else:
         JournalRebuilding(journal,students,disciplines)

                  
# Journal rebuild function                 
def JournalRebuilding(journal,students,disciplines):
    command=1
    while not(command==0):
        view.PrintMessage("WARNING! THE JOURNAL WAS CRASHED!","It must be rebuild to continue!","Do it now?:")
        view.printList(['yes','no'])
        command=view.GettingNumberFromList("command",['yes','no'])
    ListErase(journal)
    for student in students:
        journal.append([])
        for discipline in disciplines:
            journal[-1].append(' ')
    view.PrintMessage(f"Journal was rebuild for {len(journal)} student\'s and {len(journal[0])} discipline\'s")
    view.WriteJournalToFile(journal)

# Adding random student, random disciplines and random grades (to journal)
def RandomGenerator():
    global students, disciplines, journal
    studentsQuantity=int(view.readInput("students quantity"))
    disciplinesQuantity=int(view.readInput("disciplines quantity"))
    gradesQuantity=int(view.readInput("grades quantity"))
    view.PrintMessage("Your current information of students, disciplines and grades will be removed, continue?")
    view.printList(['yes','no'])
    command=view.GettingNumberFromList("command",['yes','no'])
    if command==0:
        ListErase(journal)
        view.DeleteStudentsFromFile()
        ListErase(students)
        view.DeleteDisciplinesFromFile()
        ListErase(disciplines)
        namesList=view.ReadNamesListFromFile()
        surnamesList=view.ReadSurnamesListFromFile()
        disciplinesList=view.ReadDisciplinesListFromFile()
        if disciplinesQuantity>len(disciplinesList):
            disciplinesQuantity=len(disciplinesList)
            view.PrintMessage(f"Your quantity of disciplines was too high and reduced to maximum value ({disciplinesQuantity})")
        for i in range(studentsQuantity):
            AddRandomStudent(namesList,surnamesList)
        for j in range(disciplinesQuantity):
            AddRandomDiscipline(disciplinesList)  
        AddRandomGrades(gradesQuantity)         
    else:
        return

# Journal erasing function
def ListErase(listToErase):            
    while not(len(listToErase)==0):
        listToErase.pop()

# Getting random full name and calling AddStudent() function
def AddRandomStudent(namesList,surnamesList):
    global students
    while True:
            try:
                name=namesList[randint(0,len(namesList)-1)]
                surname=surnamesList[randint(0,len(surnamesList)-1)]
                fullName=name+" "+surname
                students.index[fullName]
            except Exception:
                break
    AddStudent(fullName)

# Getting random discipline and calling AddDiscipline() function
def AddRandomDiscipline(disciplinesList):
    global disciplines
    discipline=disciplinesList.pop(randint(0,len(disciplinesList)-1))
    AddDiscipline(discipline)

#Adding random grades to journal
def AddRandomGrades(gradesQuantity):
    global journal
    for i in range(len(journal)):
        for j in range(len(journal[0])):
            for z in range(gradesQuantity):
                journal[i][j]+=str(randint(1,5))
    view.WriteJournalToFile(journal)
    

def AverageInDiscipline():
    global students, disciplines, journal
    view.printList(students)
    student=view.GettingNumberFromList('student',students)
    view.printList(disciplines)
    discipline=view.GettingNumberFromList('discipline',disciplines)
    view.PrintMessage(f"Average grade for student : \"{students[student]}\" in discipline \"{disciplines[discipline]}\""+\
                      f"is: {round((sum(list(map(int ,journal[student][discipline]))))/len(journal[student][discipline]),2)}")


def AverageInDisciplineAll():
    global disciplines, journal
    view.printList(disciplines)
    discipline=view.GettingNumberFromList('discipline',disciplines)
    listOfAllGradesInDiscipline=list(map(int,''.join([i[discipline] for i in journal])))
    view.PrintMessage(f"in discipline \"{disciplines[discipline]}\" at school"+\
                      f"is: {round(sum(listOfAllGradesInDiscipline)/len(listOfAllGradesInDiscipline),2)}")
    
def QuantityOfMedalists():
    global journal
    medalistsQuantity=0
    for student in journal:
        studentsGrades=''.join(student)
        if not(("3" in studentsGrades) or ('2' in studentsGrades) or ('1' in studentsGrades)):
            medalistsQuantity+=1
    if medalistsQuantity==0:
        view.PrintMessage("There are NO medalist\'s at school")
    elif medalistsQuantity==1:
        view.PrintMessage("There is only one medalist at school")     
    else:
        view.PrintMessage(f"There are {medalistsQuantity} medalist\'s at school")         


