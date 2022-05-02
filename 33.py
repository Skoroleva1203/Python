# 33.Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:	k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint
import os
os.system('cls')

k = (int(input('Введите степень многочлена: ')))
list=[]
pol = ''

for i in range (0, k + 1):
    list.append(randint(1, 101))

print('Список коэффициентов:', list)
file = open('33.txt', 'w')

for i in range (k, -1, -1):
    if i > 1:
        pol += str(list[i]) + ' * x ^ ' + str(i) + ' + '
    elif i == 1:
        pol += str(list[i]) + ' * x + '
    elif i == 0:
        pol += str(list[i]) + ' = 0'

print('Получили многочлен: ', pol)
print('Запись многочлена произведена в файл 33.txt')
file.write(pol)
file.close




exit()

k = 2
list=[]
pol = ''

for i in range (0, k + 1):
    list.append(randint(1, 101))

print('Список коэффициентов:', list)
file = open('33.txt', 'w')

for i in range (k, -1, -1):
    if i > 1:
        pol += str(list[i]) + ' * x ^ ' + str(i) + ' + '
    elif i == 1:
        pol += str(list[i]) + ' * x + '
    elif i == 0:
        pol += str(list[i]) + ' = 0'

print('Получили многочлен: ', pol)
print('Запись многочлена произведена в файл 33.txt')
file.write(pol)
file.close

