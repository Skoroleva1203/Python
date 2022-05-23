# Сформировать список из  N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

import os
os.system('cls')

# Вариант 1
#f1 = lambda x: 3**x
#f2 = lambda x: 3**x*-1
#list = [] 
#N = int(input('Введите количество членов последовательности: '))
#for i in range(N):
#    if i% 2 == 0:
#        list.append(f1(i))
#    else:
#        list.append(f2(i))
#print(list)

# Вариант 2
list = [(-3) ** num for num in range (int(input('Введите количество элементов: ')))]
print(list)