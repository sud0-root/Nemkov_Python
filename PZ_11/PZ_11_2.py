# Из предложенного текстового файла (text18-15.txt)
# вывести на экран его содержимое, количество букв в нижнем регистре.
# Сформировать новый файл, в который поместить текст в стихотворной форме
# предварительно заменив символы нижнего регистра на верхний.
# -*- coding: utf-8 -*-

file1 = open('PZ_11/18-15.txt', encoding='UTF-8')
print('Содержимое файла:')
print(file1.read())
file1.close()
count = 0
for i in open('PZ_11/18-15.txt', encoding='UTF-8'):
    for j in i:
        if j.islower()==True:
            count = count + 1
print('Количество букв в нижнем регистре:', count)
file1.close()
file2 = open('PZ_11/18-15-1.txt', 'w', encoding='UTF-8')
for i in open('PZ_11/18-15.txt', encoding='UTF-8'):
    file2.writelines(i.upper())
file2.close()
