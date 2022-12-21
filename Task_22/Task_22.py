# 22. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
import random as r
while True:
    try:
        n=int(input('Insert N: '))
        break
    except Exception:
        print('Your value is NOT a number.')
numbers=[]
mult=1
for i in range(0,n):
    numbers.append(r.randint(1,10))
    if i%2!=0:
        mult*=numbers[i]
print(numbers)
print("Multiplication of numbers in odd positions in number is: ",mult)