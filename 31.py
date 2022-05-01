# 31.	Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.
from functools import reduce
from operator import mul
from random import randint
from re import I
a = randint(1,100)
print('Заданное число:', a)
list = []
delit = 2 
while a > 1:
    if a % delit == 0:
        list.append(delit)
        a = a / delit
    else:
        delit+=1
print('Число',reduce(mul, list) ,'состоит из простых множителей:', list)   