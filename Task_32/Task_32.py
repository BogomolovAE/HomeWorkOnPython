# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

while True:
    try:
        numbers=list(map(int,input('Insert numbers: ').split()))
        break
    except Exception:
        print('Your value is NOT a number.')

for i in range(len(numbers)):
    isUnique=True
    for j in range(len(numbers)):
        if j==i:continue
        if numbers[i]==numbers[j]:
            isUnique=False
            break
    if isUnique: print(numbers[i],end=" ")
