#     Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11
number=input("Input your number: ")
sum=0
for i in range(len(number)):
    if number[i].isalnum():sum+=int(number[i])
print("Sum of digits in number is: ",sum)