#Сообщить в какой четверти координатной плоскости 
# или на какой оси находится точка с координатами Х и У 
#В декартовой системе координат четверти нумеруются против часовой стрелки, начиная с верхней правой.
# 1 четверть  X>0, Y>0
# 2 четверть X<0, Y>0
# 3 четверть X<0, Y<0
# 4 четверть X>0, Y<0

print ('Задайте точку  А с координатами (х, y)')
x = int(input('Введите x: '))
y = int(input('Введите y: '))
if (x > 0 and y > 0):
    print ('Точка A(',x,';',y,') лежит в 1 четверти координатной плоскости')
elif (x < 0 and y > 0):
    print ('Точка A(',x,';',y,') лежит во 2 четверти координатной плоскости')
elif (x < 0 and y < 0):
    print ('Точка A(',x,';',y,') лежит в 3 четверти координатной плоскости')
elif (x > 0 and y < 0):
    print ('Точка A(',x,';',y,') лежит в 4 четверти координатной плоскости')
elif (x == 0 and y > 0):
    print ('Точка A(',x,';',y,') лежит на координатной оси ОY между 1 и 2 четвертями координатной плоскости')
elif (x == 0 and y < 0):
    print ('Точка A(',x,';',y,') лежит на координатной оси ОY между 3 и 4 четвертями координатной плоскости')
elif (x > 0 and y == 0):
    print ('Точка A(',x,';',y,') лежит на координатной оси ОХ между 1 и 4 четвертями координатной плоскости')
elif (x < 0 and y == 0):
    print ('Точка A(',x,';',y,') лежит на координатной оси ОX между 2 и 3 четвертями координатной плоскости')