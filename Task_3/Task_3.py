# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта 
# точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3
while (True):
    try:
        x=float(input('insert X: '))
        if x==0:print('Error: x cant\'t be zero')
        else: break
    except Exception: print('Error: Check your value!')
while (True):    
    try:
        y=float(input('insert Y: '))
        if y==0:print('Error: y cant\'t be zero')
        else: break
    except Exception: print('Error: Check your value!')    
if (x>0)and(y>0):print('first quadrant')
elif (x<0)and(y>0):print('second quadrant')
elif (x<0)and(y<0):print('third quadrant')
else:print('fourth quadrant')
