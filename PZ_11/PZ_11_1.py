# Средствами языка Python сформировать текстовый файл (.txt),
# содержащий полследовательность из целых положительных и отрицательных чисел.
# Сформировать новый текстовый файл (.txt) следующего вида,
# предварительно выполнив требуемую обработку элементов
# Исходные данные:
# Количество элементов:
# Индекс последнего минимального элемента:
# Умножаем все элементы на первый элемент:

num = ['22 10 -18 12 -91 76']
file1 = open('PZ_11/data.txt', 'w')
file1.writelines(num)
file1.close()
file2 = open('PZ_11/data_1.txt', 'w')
file2.write('Исходные данные: ')
file2.writelines(num)
file2.close()
file1 = open('PZ_11/data.txt')
i = 0
d = file1.read()
d = d.split()
d_int = []
for i in range(len(d)):
    d_int = [int(j) for j in d]
file1.close()
file1 = open('PZ_11/data.txt')
sh = 0
for i in range(len(d_int)):
    sh = sh if sh < d_int[i] else d_int[i]
file2 = open('PZ_11/data_1.txt', 'a')
file2.write('\n')
print('Количество элементов: ', len(d_int), file=file2)
print('Индекс минимального элемента: ', i - 1, file=file2)
file2.close()
B = []
g = 0
file1 = open('PZ_11/data.txt')
for i in range(len(d_int)):
    g = d_int[i]*d_int[0]
    B.append(g)
file1.close()
file2 = open('PZ_11/data_1.txt', 'a')
print('Умножаем все элементы на первый элемент:', B, file=file2)
file2.close()
