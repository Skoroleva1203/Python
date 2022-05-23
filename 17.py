# Задать список из N элементов, заполненных числами из [-N, N]. 
# Найти произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число

#from functools import reduce
import os
os.system("cls")

N = int(input('Введите число N: ' ))
list = [i for i in range(-N,N+1)]
print('Создана последовательность: ', list)
path = '17.txt'
data = open(path,'r')
count = 1
for line in data:
    print('Заданные индексы: ',line)
    if int(line) > len(list)-1:
        count*=1
    else:    
        count *= list[int(line)]
print('Произведение элементов c указанными индексами = ', count)
data.close


