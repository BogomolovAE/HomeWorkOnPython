# 20. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
list1=input('Insert numbers: ')
newList=list(map(int,list1.split()))
n=int(input('Insert N: '))
if n in newList:print(f"number {n} is in list {list1}")
else: print(f"number {n} is NOT in list {list1}")
