# В матрице найти суммы элементов каждого столбца и поместить их в новый массив.
# Выполнить замену элементов второй строки исходной матрицы на полученные суммы.
import random
from functools import reduce

N = int(input("Введите размерность матрицы: "))
matrix = [[random.randint(-10, 10) for el in range(N)] for row in range(N)]
print("Исходная матрица:")
for row in matrix:
    print(row)


cols_sums = [reduce(lambda x, y: x + y, [row[i] for row in matrix]) for i in range(N)]
print('\nСумма элементов каждого столбца', cols_sums)

matrix[1] = cols_sums
print("\nМатрица после замены второй строки на суммы столбцов:")
for row in matrix:
    print(row)