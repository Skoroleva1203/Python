# 34.Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

from random import randint
import os
os.system('cls')

def str_polinim (n, list):  # Функция для записи многочлена в строку
    pol = ''
    for i in range (n, -1, -1):
        if i > 1:
            pol += str(list[i]) + ' * x ^ ' + str(i) + ' + '
        elif i == 1:
            pol += str(list[i]) + ' * x + '
        elif i == 0:
            pol += str(list[i]) + ' = 0'    
    return pol   


def create_polinom ():   # Функция для создания рандомного многочлена
    k = (int(input('Введите степень многочлена: ')))
    list=[]
    for i in range (0, k + 1):
        list.append(randint(1, 101))
    print('Список коэффициентов:', list)
    polinom = str_polinim(k, list)
    print('Получили многочлен: ', polinom)
    return list, polinom
      
list_1, polinom_1 =  create_polinom ()    # Создаем многочлены (при помощи функции create_polinom), записываем их в отдельные файлы
file = open('34_1.txt', 'w')
file.write(polinom_1)
print('Запись многочлена произведена в файл 34_1.txt\n')
file.close 

list_2, polinom_2 =  create_polinom ()
file = open('34_2.txt', 'w')
file.write(polinom_2)
print('Запись многочлена произведена в файл 34_2.txt')
file.close 

list_3 = []
difference_len = len(list_1) - len(list_2) # сравниваем многочлены на равенство количества коэффициентов

if  difference_len == 0:  # многочлены равнозначные
    for i in range (0, len(list_1)):
        list_3.append(list_1[i] + list_2[i])
elif difference_len > 0:
    for i in range (0,difference_len):
        list_2.append(0)
    for i in range (0, len(list_1)):
        list_3.append(list_1[i] + list_2[i])
else:
    for i in range (0,-(difference_len)):
        list_1.append(0)
    for i in range (0, len(list_1)):
        list_3.append(list_1[i] + list_2[i])
print ('\nКоэффициенты первого многочлена:                  ',list_1)
print ('Коэффициенты второго многочлена:                  ',list_2)
print('Коэффициенты полученного от сложения многочленов: ', list_3)

polinom_3 =  str_polinim(len(list_3)-1, list_3)    
print('\nПолучили новый многочлен: ', polinom_3)
file = open('34_3.txt', 'w')
file.write(polinom_3)
print('Запись полученного многочлена произведена в файл 34_3.txt')
file.close 





