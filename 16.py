# Задать список из n чисел последовательности (1+1n)n 
# и вывести на экран их сумму

import os
import random
os.system('cls')

# Вариант 1
#n = random.randint(6, 16)
#print(n)
#massive = []
#for i in range (1, n+1):
#    massive.append(1+(1/i)**i)
#print(massive)
#print(f'{sum(massive):.2f}')

# Вариант 2
n = random.randint(6, 16)
massive = [1+(1/i)**i for i in range(1, n+1)]
print('Задана последовательность из ', n,
      'чисел:\n', *massive, '\nСумма чисел = ', round(sum(massive), 4), '\n')