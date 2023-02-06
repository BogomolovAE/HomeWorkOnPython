def PhonesShow(fields):
    phoneBook=open("Telephone_book.txt","r")
    for record in phoneBook:
        print("="*30)
        currentRecord=record.split("|")
        for i in range(len(fields)):
            print(fields[i]+currentRecord[i])
    phoneBook.close()
 
def PhonesSort(fields):
    phoneBook=open("Telephone_book.txt","r")
    book=list(map(lambda x:x.split('|'),phoneBook.readlines()))
    nameIndex=fields.index("Name: ")
    minPosition=0
    currentPosition=0
    tempRecord=[[]]
    for element in range(len(book)):
        minRecord=book[currentPosition]
        for compareElement in range(currentPosition,len(book)):
            if book[compareElement][nameIndex]<minRecord[nameIndex]:
                minRecord=book[compareElement]
                minPosition=compareElement
        tempRecord=book[currentPosition]
        book[currentPosition]=minRecord
        book[minPosition]=tempRecord
        currentPosition+=1
        minPosition=currentPosition
    for record in book:
        print("="*30)
        for i in range(len(fields)):
            print(fields[i]+record[i])

def PhonesNameOnly(fields):
    nameIndex=fields.index("Name: ")
    surnameIndex=fields.index("Surname: ")
    phoneBook=open("Telephone_book.txt","r")
    for record in phoneBook:
        print("="*30)
        currentRecord=record.split("|")
        print(fields[nameIndex]+currentRecord[nameIndex])
        print(fields[surnameIndex]+currentRecord[surnameIndex])   
    phoneBook.close()