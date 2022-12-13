# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
while (True):
    try:
       a=list(map(float,input('insert A(x1,y1), for example: "34.1 45.2" : ').split()))
       break
    except Exception: print('Error: Check your value!')
while (True):    
    try:
       b=list(map(float,input('insert B(x2,y2), for example: "-14.1 -545.2" : ').split()))
       break
    except Exception: print('Error: Check your value!')
print(f'Distanse between A{a} and B{b} is: {round(((a[0]-b[0])**2+(a[1]-b[1])**2)**0.5,3)}')