# Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
# для всех значений предикат
x = True
y = False
z = False
if ((not (x or y or z)) == (not x and not y and not z)):
    print (True, ' - Утверждение истинно')
else:
    print (False, ' - Утверждение ложно')