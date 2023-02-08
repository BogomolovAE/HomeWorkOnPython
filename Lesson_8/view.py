SEPARATOR='|'


# List output function
def printList(itemList):
    msgText=tuple([str(i[0])+" "+str(i[1]) for i in list(enumerate(itemList,1))])
    PrintMessage(*msgText)


# Reading from CONSOLE function
def readInput(text):
    return input("Input "+text+": ")


# Reading students from FILE function
def ReadStudentsFromFile():
    students=[]
    studentsList=open("Lesson_8\students.txt",'r')
    for line in studentsList:
        students.append(line.rstrip("\n"))
    studentsList.close()
    if len(students)==0:
            return students
    else:
        PrintMessage(f"{len(students)} student\'s were load from FILE")
        return students


# Reading disciplines from FILE function
def ReadDisciplinesFromFile():
    disciplines=[]
    disciplineList=open("Lesson_8\disciplines.txt",'r')
    for line in disciplineList:
        disciplines.append(line.rstrip("\n"))
    disciplineList.close()
    if len(disciplines)==0:    
        return disciplines  
    else:
        PrintMessage(f"{len(disciplines)} discipline\'s were load from FILE")
        return disciplines


# Reading journal from FILE function
def ReadJournalFromFile():
    journal=[]
    journalFile=open("Lesson_8\journal.txt",'r')    
    for record in journalFile:
        journal.append(record.rstrip("\n").split(SEPARATOR))
    try:
        PrintMessage(f"Journal was loaded from file for {len(journal)} student\'s and {len(journal[0])} discipline\'s")
    except Exception:
        pass
    journalFile.close()
    return journal


# Writing student to FILE function
def WriteStudentToFile(newStudent):
    file=open("Lesson_8\students.txt",'a')
    file.write(newStudent+"\n")
    file.close()


# Writing discipline to FILE function
def WriteDisciplineToFile(newDiscipline):
    file=open("Lesson_8\disciplines.txt",'a')
    file.write(newDiscipline+"\n")
    file.close()


# Adding student (line) to journal in RAM function
def AddStudentToJournal(journal):
    journal.append([])
    for j in range(len(journal[0])):
      journal[-1].append('')
    
        
# Adding discipline (column) to journal in RAM function
def AddDisciplineToJournal(journal):
    for student in journal:
        student.append('')


# Getting number of element from list function
def GettingNumberFromList(text,itemList):
    while True:    
        try:
            item = readInput('name of '+text+' or it\'s number in list: ')
            if item.isdigit() and 0<=int(item)<=len(itemList):
                return int(item)-1
            else:
                return itemList.index(item)
        except Exception:
            PrintMessage("Error! Try again")


# Printing help from File
def help():
    commandList=open('Lesson_8\help.txt','r')
    helplist=[]
    for line in commandList:
        helplist.append(line.rstrip())
    commandList.close()
    PrintMessage(*tuple(helplist))

# Writing journal to FILE
def WriteJournalToFile(journal):
    journalFile=open("Lesson_8\journal.txt",'w')
    for student in range(len(journal)):
        journalFile.write(SEPARATOR.join(journal[student])+"\n")
    journalFile.truncate()
    journalFile.close()


def DeleteStudentsFromFile():    
    students=open("Lesson_8\students.txt",'w')
    students.truncate()
    students.close()

def DeleteDisciplinesFromFile():    
    disciplines=open("Lesson_8\disciplines.txt",'w')
    disciplines.truncate()
    disciplines.close()


# Reading names from FILE function
def ReadNamesListFromFile():
    namesList=[]
    names=open("Lesson_8\\name_base.txt",'r')
    for line in names:
        namesList.append(line.rstrip("\n"))
    names.close()
    if len(namesList)==0:
            PrintMessage(f"File with names is empty!")
    else:
        PrintMessage(f"{len(namesList)} names were load from FILE")
        return namesList    

# Reading surnames from FILE function
def ReadSurnamesListFromFile():
    surnamesList=[]
    surnames=open("Lesson_8\\surname_base.txt",'r')
    for line in surnames:
        surnamesList.append(line.rstrip("\n"))
    surnames.close()
    if len(surnamesList)==0:
            PrintMessage(f"File with surnames is empty!")
    else:
        PrintMessage(f"{len(surnamesList)} surnames were load from FILE")
        return surnamesList   

# Reading disciplines from FILE function
def ReadDisciplinesListFromFile():
    disciplinesList=[]
    disciplines=open("Lesson_8\\discipline_base.txt",'r')
    for line in disciplines:
        disciplinesList.append(line.rstrip("\n"))
    disciplines.close()
    if len(disciplinesList)==0:
            PrintMessage(f"File with disciplines is empty!")
    else:
        PrintMessage(f"{len(disciplinesList)} disciplines were load from FILE")
        return disciplinesList   

def PrintMessage(*text):
    quantityOfSeparators=max([len(i) for i in text])+10
    messageSeparator='*'
    print(messageSeparator*quantityOfSeparators)
    print(*text,sep='\n')
    print(messageSeparator*quantityOfSeparators)