#Указав номер четверти прямоугольной системы координат, 
# показать допустимые значения координат для точек этой четверти
number = (int(input('Введите номер четверти координат: ')))
if number == 1:
    print('Допустимые значения 1 четверти координатной плоскости:')
    print('Область определния для X и Y от 0 до плюс бесконечности')
elif number == 2:
    print('Допустимые значения 2 четверти координатной плоскости:')
    print('Область определения для X от 0 до минус бесконечности; для Y от 0 до плюс бесконечности')
elif number == 3:
    print('Допустимые значения 3 четверти координатной плоскости:')
    print('Область определения для X и Y от 0 до минус бесконечности')
elif number == 4:
    print('Допустимые значения 2 четверти координатной плоскости:')
    print('Область определения для X от 0 до плюс бесконечности; для Y от 0 до минус бесконечности')