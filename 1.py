# по двум заданным числам определить является ли одно квадратом другого
a = int(input('Введите число: '))
b = int(input('Введите число: '))
if a ** 2 == b or b ** 2 == a:
    print ('true')
else:
    print('false')
a, b = map(int, input().split())
print(bool(a == b ** 2 or b == a ** 2))
 

