# - С помощью использования лямбд, filter, map, zip, enumerate, list comprehension
# 47.Сформировать список из N членов последовательности
# Для N=5: 1,-3,9,-27,81 (каждый член больше предыдущего в три раза, знак чередуется)
n=int(input("Input N: "))
list1=list(map(lambda i:(-3)**i, range (n)))
print(list1)