# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
def DexIntoBin(number):
    if number//2!=0:
         DexIntoBin(number//2)
    print(number%2,end='')     


import random as r


while True:
    try:
        n=int(input('Insert N: '))
        break
    except Exception:
        print('Your value is NOT a number.')


DexIntoBin(n)