# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.



def DecomposeToSimple(number):
    if number in simpleNumbers: 
        print(number,end=' ')
        return
    for simple in simpleNumbers:
        if number%simple==0: 
            DecomposeToSimple(number//simple)
            print(simple,end=' ')
            break
    return



while True:
    try:
        n=int(input('Insert N: '))
        break
    except Exception:
        print('Your value is NOT a number.')
simpleNumbers=[]
for i in range(1,n+1):
    isSimple=True
    for j in range(i-1,1,-1):
        if i%j==0: isSimple=False
    if isSimple and i!=1:simpleNumbers.append(i)
print(simpleNumbers)
DecomposeToSimple(n)