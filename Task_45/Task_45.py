# - С помощью использования лямбд, filter, map, zip, enumerate, list comprehension
# 45. Найти сумму чисел списка стоящих на нечетной позиции
sum1=0
list1=[1,2,4,2,5,3,2,1]
sum1=sum(list(map(lambda x:x[1],(filter(lambda x:x[0]%2>0,list(enumerate(list1)))))))
# map(lambda x: if x[0]%2>0:sum+=x[1],enumerate(list1))
print("Summ of NOT odd elements: ",sum1)