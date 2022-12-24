# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.



def main():
    fileName='Output_0.txt'
    polynomial1=GetPolynomial(fileName)
    fileName='Output_1.txt'
    polynomial2=GetPolynomial(fileName)
    coefficients1=GetCoefficients(polynomial1)
    coefficients2=GetCoefficients(polynomial2)
    coefficientsSum=GetPolynomialSum(coefficients1,coefficients2)
    polynomialSum=CreatePolynomial(coefficientsSum)
    WritePolynomial(polynomialSum)



def GetPolynomial(fileName):   
    with open (fileName,'r') as f:
        polynomial=f.readline().rstrip()
    return polynomial



def GetCoefficients(polynomial):
    coefficients=[]
    polynomial=polynomial.replace('=','+')
    summand=polynomial.split('+')
    summand.pop()
    members=[[],[]]
    
    for i in summand:
        k=i.split('*')
        if len(k)>1:
            members[0].append(int(k[0]))
            members[1].append(int(k[len(k)-1]))
        else:
            members[0].append(int(k[0]))
            members[1].append(0)  

    for i in range(1,len(members[1])):
        if members[1][i-1]-1!=members[1][i]:
            members[1].insert(i,members[1][i-1]-1)
            members[0].insert(i,0)

    coefficients=members[0].copy()
    coefficients.reverse()
    return coefficients



def GetPolynomialSum(polynomial1,polynomial2):
    sum=[]
    for i in range(min(min(len(polynomial2),len(polynomial1)),len(polynomial1))):
        sum.append(polynomial1[i]+polynomial2[i])
    for i in range(min(len(polynomial2),len(polynomial1)),max(len(polynomial2),len(polynomial1))):
        if len(polynomial2)>len(polynomial1):sum.append(polynomial2[i])
        else: sum.append(polynomial1[i])

    return sum



def CreatePolynomial(coefficients):
    polynomial=''
    for i in range(len(coefficients)-1,-1,-1):
        polynomial+=(str(coefficients[i])+('*x**'+str(i))*(i!=0))*(coefficients[i]!=0)
        if i==0: polynomial += ' = 0'
        else: polynomial += ' + '
    return polynomial

def WritePolynomial(polinomial):
    n=0
    fileName='Output_Task_34_'
    while True:
        try:
            open(fileName+str(n)+'.txt','r')
            n+=1
        except Exception:
            break

    with open(fileName+str(n)+'.txt','w') as f:
        f.write(polinomial+'\n')


main()

