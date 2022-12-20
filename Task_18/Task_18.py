# Реализуйте алгоритм перемешивания списка.

import random
a=input("Insert list: ").split()
b=['' for i in range (len(a))]
indexList=[]
for i in range(len(a)):
    
    if (i in indexList): continue 
    while (True):
        k=random.randint(0,len(a)-1)
        if (k not in indexList):
            b[k]=a[i]
            b[i]=a[k]
            indexList.append(i)
            indexList.append(k)
            break

print(a)
print(b)