# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
#  (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random



def main(k):
    coefficients=CoefficientssGeneration(k)
    polinomial=CreatePolynomial(coefficients)
    WritePolynomial(polinomial)


def CoefficientssGeneration(quantity):
    coefficientsArray=[]
    for i in range(quantity+1):
        coefficientsArray.append(random.randint(0,100))
    return coefficientsArray
    


def CreatePolynomial(coefficients):
    polynomial=''
    for i in range(len(coefficients)-1,-1,-1):
        polynomial+=(str(coefficients[i])+('*x**'+str(i))*(i!=0))*(coefficients[i]!=0)
        if i==0: polynomial += ' = 0'
        else: polynomial += ' + '
    return polynomial



def WritePolynomial(polinomial):
    n=0
    while True:
        try:
            open('output_'+str(n)+'.txt','r')
            n+=1
        except Exception:
            break

    with open('output_'+str(n)+'.txt','w') as f:
        f.write(polinomial+'\n')



main(5)
main(7)