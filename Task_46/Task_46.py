# - С помощью использования лямбд, filter, map, zip, enumerate, list comprehension
# 46. Найти произведение пар чисел списка(парой считаем первый и последний, второй предпоследний и тд)
mainList=[1,2,4,2,5,3,2,1,6]
list1=mainList[:int(len(mainList)/2+0.5*(len(mainList)%2>0))]
list2=mainList[len(mainList)//2:]
list2.reverse()
newList=list(zip(list1,list2))
for i in newList:
    print(i[0]*i[1],end=' ')