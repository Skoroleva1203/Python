# Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ]

import os
import random
os.system('cls')

n = int(input('Введите число N: '))
list = [1]
    
for i in range(2, n+1):
    list.append(i * list[i-2])
print(list, '\n') 
