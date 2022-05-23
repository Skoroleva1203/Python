# Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ]

import os
os.system('cls')

# Вариант 1
#n = int(input('Введите число N: '))
#list = [1]
#for i in range(2, n+1):
#    list.append(i * list[i-2])
#print(list, '\n') 

# Вариант 2
from itertools import accumulate
import operator

n = int(input('Введите число N: '))
print('Получили последовательность:', *list(accumulate([x for x in range(1, n + 1)], operator.mul)), '\n')