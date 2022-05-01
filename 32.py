#32.Задайте последовательность чисел. 
# Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности.
import os
import random 
os.system('cls')

list = [random.randint (1, 100 ) for i in range (1, 26)]
print('Исходная последовательность, созданная генератором случайных чисел: ')
print(list)
listing1 = []
listing2 = []
for i in list:
    if list.count(i) == 1:
        listing1.append(i)
    else:
        listing2.append(i)
print('\nСписок неповторяющихся элементов из исходной послеовательности: ')
print(listing1)
print('\nСписок повторяющихся элементов из исходной послеовательности: ')
print(listing2)
