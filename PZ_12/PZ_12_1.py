# В последовательности на n целых чисел найти и вывести:
# 1. максимальный среди положительных
# 2. минимальный среди отрицательных
# 3. произведение элементов

import random
from functools import reduce

n = 10
num = [random.randint(-100, 100) for _ in range(n)]
max_positive = max(filter(lambda x: x > 0, num), default=None)
min_negative = min(filter(lambda x: x < 0, num), default=None)

prod = reduce(lambda x, y: x * y, num, 1)

print("Последовательность чисел:", num)
print("Максимальное положительное число:", max_positive)
print("Минимальное отрицательное число:", min_negative)
print("Произведение всех элементов:", prod)