#Дано число. Проверить кратно ли оно 5 и 10 или 15 но не 30
#n = int (input('Enter: '))
#n = 45
#print(bool(((n % 5 == 0 and n % 10 == 0) or n % 15 == 0) and not n % 30 != 0))

from random import randint
a = randint(0,100)
if a % 5 == 0 and a % 10 == 0:
    print ('Число', a , ' кратно 5 и 10')
else:
    print ('Число', a , ' не кратно 5 и 10')    
if a % 15 == 0:
    print ('Число', a, 'кратно 15')
else:
    print ('Число', a, 'не кратно 15')
if a % 30 == 0:
    print ('Число', a , ' кратно 30')
else:
    print ('Число', a , ' не кратно 30')  