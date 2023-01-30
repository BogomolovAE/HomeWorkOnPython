# 40. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Модуль сжатия:
# Для чисел:
# Входные данные:
# 111112222334445
# Выходные данные:
# 5142233415
# Также должно работать и для букв:
# Входные данные:
# AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE
# Выходные данные:
# 6A1F2D7C1A17E
# (5 - количество единиц, далее сама единица, 4 - количество двоек, далее сама двойка и т.д)
# Модуль восстановления работет в обратную сторону - из строки выходных данных, получить строку входных данных.
textString=input('Input you string: ')


def Encrypt(text):
    currentIndex=0
    newText=[['',0]]
    for i in text:
        if newText[currentIndex][0]==i:
            newText[currentIndex][1]+=1
        else: 
            newText.append([i,1])
            currentIndex+=1
    newText.pop(0)
    return newText


def Recover(newText):
    for i in range(len(newText)):
        for j in range(newText[i][1]):
            print(newText[i][0],end='')
    print()


def Convert(textToConvert):
    enteredText=[['',0]]
    numStart=-1
    numEnd=0
    currentSymbolPosition=0
    for i in range(len(textToConvert)):
        if textToConvert[i].isdigit():
            if numStart==-1:
                numStart=i
            numEnd=i+1
        else:
            enteredText.append([textToConvert[i],0])
            currentSymbolPosition+=1
            enteredText[currentSymbolPosition][1]=int(textToConvert[numStart:numEnd])
            numStart=-1
    enteredText.pop(0)
    return enteredText


convertedText=Encrypt(textString)
print('Encrypted text:')
for i in range(len(convertedText)):
    print(str(convertedText[i][1])+convertedText[i][0],end='')

print()
print('Recovered text:')
Recover(convertedText)
newRLEString=input("Input string to decode: ")
print('Recovered text:')
Recover(Convert(newRLEString))





