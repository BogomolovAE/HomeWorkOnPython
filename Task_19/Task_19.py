# 19. Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.
import datetime

def random_int(num):
    rand = datetime.datetime.now().microsecond/10**6
    return int(num*rand)
print(random_int(int(input('insert n: '))))
