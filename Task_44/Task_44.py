# - С помощью использования лямбд, filter, map, zip, enumerate, list comprehension
# **44. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:

# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21
pointA=tuple(list(map(float,input("Insert X and Y coordinates for point A, separated with space: ").split())))
pointB=tuple(list(map(float,input("Insert X and Y coordinate for point B, separated with space: ").split())))
answer=lambda a,b:((a[0]-b[0])**2+(a[1]-b[1])**2)**0.5

print("Distance betwin A and B point: ",round(answer(pointA,pointB),3))