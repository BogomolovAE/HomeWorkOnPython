#Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
x=float(input('insert X'))
y=float(input('insert Y'))
z=float(input('insert Z'))
print((not(x or y or z)) == (not(x) and not(y) and not(z)))
