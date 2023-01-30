# 38. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".(Задание из семинара)
text=input("Insert string: ").split()
subString="абв"
newString=list(filter(lambda x: x.find(subString)==-1, text))
for i in newString:
    print(i,end=" ")