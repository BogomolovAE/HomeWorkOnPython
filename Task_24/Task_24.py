#24. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
import random as r
while True:
    try:
        n=int(input('Insert N: '))
        break
    except Exception:
        print('Your value is NOT a number.')
numbers=[]
digitsAfterDecimalSeparator=100
max=0
min=0
for i in range(0,n):
    numbers.append(r.randint(1,digitsAfterDecimalSeparator*2)/digitsAfterDecimalSeparator)
# numbers=[1.1, 1.2, 3.1, 5, 10.01]
max=numbers[0]%1
min=numbers[0]%1
valuesAfterDecimalSeparator=[]
for i in numbers:
    valuesAfterDecimalSeparator.append(round(i%1,2))
    if i%1==0: continue
    elif i%1<min: min=i%1
    elif i%1>max: max=i%1

print('numbers = ',numbers)
print('valuesAfterDecimalSeparator = ',valuesAfterDecimalSeparator)
print(f"max-min = {round(max,2)} - {round(min,2)} = {round(max-min,2)}")