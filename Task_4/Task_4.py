#Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
while (True):
    n=input('insert number of quadrant: ')
    if '1'<=n<='4':break
    else: print ('Error: n must be between 1 and 4')
if n=='1':print ('x>0, y>0')
elif n=='2':print ('x<0, y>0')
elif n=='3':print ('x<0, y<0')
else:print ('x>0, y<0')