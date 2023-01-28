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


def Convert(text):
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

        
convertedText=Convert(textString)

for i in range(len(convertedText)):
    print(convertedText[i][0]+str(convertedText[i][1]),end='')

print()
print('Recovered text:')

Recover(convertedText)




