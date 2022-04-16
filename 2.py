# Найти максимальное из пяти чисел
import os
os.system("cls") #Очистка терминала

from random import randint
a = randint(0,5)
print(a)
b = randint(0,5)
print(b)
c = randint(0,5)
print(c)
d = randint(0,5)
print(d)
e = randint(0,5)
print(e)
print ('Максимальное число ', max(a,b,c,d,e))