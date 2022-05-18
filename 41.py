# 41.	Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. 
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# Пример:
# На сжатие: Входные данные: WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
# Входные данные: 12W1B12W3B24W1B14W
import os
os.system('cls')

# Кодирование строки
def rle(stroka):
    result = ''
    count = 1
    char = stroka[0]
    for i in range(1, len(stroka)):
        if stroka[i] == char:
            count += 1 
        else:
            result = result + str(count) + char
            char = stroka[i]
            count =1
    result = result + str(count)+char
    return result    

string = 'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW'
with open ('41_str.txt', 'w') as file:
    file.write(string)
print('Кодируем строку: ', string)
rle_stroka = rle(string)
print('Результат кодирования: ', rle_stroka)
with open ('41_str_rle.txt', 'w') as file:
    file.write(rle_stroka)
