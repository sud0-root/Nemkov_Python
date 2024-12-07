# Даны три целых числа: A, B, C. Проверить истинность высказывания: «Ровно одно
# из чисел A, B, C положительное».


while True:
    try:
        a = int(input("Введите число A: "))
        b = int(input("Введите число B: "))
        c = int(input("Введите число C: "))
        break
    except ValueError:
        print("Пожалуйста, введите целые числа.")

positive_count = 0
if a > 0:
    positive_count += 1
if b > 0:
    positive_count += 1
if c > 0:
    positive_count += 1

print (positive_count == 1)

