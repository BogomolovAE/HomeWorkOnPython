def AddNumber(header):
    
    record=""
    
    for i in range(1,len(header)):
        record+="|"+input("Input "+header[i]).strip()
 
    telephoneBook=open("Telephone_Book.txt","w+")
    id=len(telephoneBook.readlines())+1
    record=str(id)+record+"\n"
    telephoneBook.write(record)
    telephoneBook.close()
