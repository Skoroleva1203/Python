# Подсчитать сумму цифр в вещественном числе.
import os
import random
os.system('cls')

# Вариант 1
#a = random.uniform(1, 1001)
#print('Задано число:', a)
#a = str(a).replace('.', '')  #переводим в строковый тип и убираем точку
#print(a)
#p = list(map(int,a))  # переводим в числовой вид
#print(p)
#summa = sum(p) 
#print('Сумма цифр числа ', a, 'равна:', summa,"\n")

# Вариант 2
a = random.uniform(1, 1001)
print('Задано число:', a)
print('Сумма цифр числа ', a, ' равна:', 
    sum(map(int, str(a).replace('.', ''))), '\n')