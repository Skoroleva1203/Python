# Дано число обозначающее день недели. 
# Вывести его название и указать является ли он выходным.

day = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресение']
from random import randint
a = randint(1,7)
print ('Число ', a, ' - какой день недели?')
if ((a-1) == 6 or (a-1) == 7):
    print(day[a-1],' - выходной день!')
else:
    print(day[a-1])