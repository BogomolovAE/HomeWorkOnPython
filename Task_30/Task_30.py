# Вычислить число c заданной точностью d

# Пример:

# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
import math
while True:
    try:
        d=float(input("Input d between 0,1 and 0,0000000001: "))
        k=math.log10(d)
        if k%1>0: print ("d must be negative power of 10! Try again!")
        elif -10>k or k>-1: print ("Your number is out of range 0,1 and 0,0000000001! Try again!")
        else: 
            print("Pi:",round(math.pi,int(abs(k))))
            break 
    except Exception:
        print("your d is NOT a number! Try again!")