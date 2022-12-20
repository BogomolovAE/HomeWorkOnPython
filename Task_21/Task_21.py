# 21. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1
# -1


mainstring=[]#input('Insert string ').split()
subString="123"#input('Insert substring ')
count=0
position=0
for i in mainstring:
    if i==subString: count+=1
    if count==2:break
    position+=1
if count<2:position=-1
print('Answer: ',position)
# second=mainstring[mainstring.find(subString)+1:].find(subString)
# if second==-1: 
#     print ('There is only one substring: '+subString+' in string')
# else: 
#     print('Second position of substring: '+subString+' is '+str(second))