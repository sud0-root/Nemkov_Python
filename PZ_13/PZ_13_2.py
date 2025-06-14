# В матрице найти минимальный элемент в предпоследней строке.
import random
# -*- coding: utf-8 -*-

N = int(input("Введите размерность матрицы: "))
matrix = [[random.randint(-10, 10) for el in range(N)] for row in range(N)]
print("Исходная матрица:")
for row in matrix:
    print(row)


min_element = min(matrix[-2])
print("Минимальный элемент в предпоследней строке:", min_element)