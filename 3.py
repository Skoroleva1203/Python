#Вывести на экран числа от -N до N
from random import randint
a = randint(0,10)
for i in range(-a, a+1):
    print(i, end='  ')
