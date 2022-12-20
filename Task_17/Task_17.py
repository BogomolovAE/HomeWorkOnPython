# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
while True:
    try:
        n=int(input('Insert N: '))
        break
    except Exception:
        print('Your value is NOT a number.')
numbers=[]
for i in range(-n,n+1):
    numbers.append(i)
sum=0
mult=1
f=open('File.txt','r')
print('Positions from file:',end=' ')
for line in f:
    mult*=numbers[int(line)]
    print(line.rstrip(),end=' ')
print()
print(numbers)
print('Multiplication of numbers: ',mult)