# Найти расстояние между двумя точками пространства
# Формула для вычисления расстояния между двумя точками A(xa, ya) и B(xb, yb) на плоскости  AB = корень кв. из ((xb - xa)2 + (yb - ya)2)
import math
from random import randint
xa = randint(-40, 40)
ya = randint(-40, 40)
xb = randint(-40, 40)
yb = randint(-40, 40)
print('Найдем расстояние AB между точками A (',xa,';',ya,') и B (',xb,';',yb,')')
ab = math.sqrt((xb-xa)**2+(yb-ya)**2)
print('Расстояние АВ между точками A (',xa,';',ya,') и B (',xb,';',yb,') равно ',round (ab,2))
