# Для натурального n создать словарь индекс-значение, 
# состоящий из элементов последовательности 3n + 1.
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

import os
os.system('cls')

# Вариант 1
#Словарь = {n:3*n+1 for n in range (1, 7)}
#print (Словарь)

# Вариант 2
print('\nСловарь:', {n: 3 * n + 1 for n in range(1,
      int(input('Задайте количество элементов последовательности: '))+1)}, '\n')