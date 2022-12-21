# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
import random as r
while True:
    try:
        n=int(input('Insert N: '))
        break
    except Exception:
        print('Your value is NOT a number.')
numbers=[]
multList=[]
mult=1
for i in range(0,n):
    numbers.append(r.randint(1,10))
for i in range(0,len(numbers)//2):   
    m=numbers[i]*numbers[-(i+1)]
    print(f"Multiplication of {i+1} pair: ({numbers[i]} and {numbers[-(i+1)]} )is: {m}")
    multList.append(m)
if len(numbers)%2!=0:
    m=numbers[len(numbers)//2]**2
    print(f"Multiplication of {len(numbers)//2+1} pair: ({numbers[len(numbers)//2]} and {numbers[(len(numbers)//2)]} )is: {m}")
    multList.append(m)
print(numbers)
print(multList)
