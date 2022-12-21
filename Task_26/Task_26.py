# 26 Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
while True:
    try:
        k=int(input('Insert k: '))
        break
    except Exception:
        print('Your value is NOT a number.')
fib=[]
for i in range(0,k+1):
    if i==0:
        fib.append(0)
    elif i==1:
        fib.append(1)
        fib.insert(0,1)
    else:
        fib.append(fib[-1]+fib[-2])
        fib.insert(0,(abs(fib[0])+abs(fib[1]))*(-1)**(i+1))
print(fib)