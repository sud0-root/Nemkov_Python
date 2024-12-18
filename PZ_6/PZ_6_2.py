# Дан целочисленный список размера N, все элементы которого упорядочены (по
# возрастанию или по убыванию). Найти количество различных элементов в данном
# списке.

N = int(input("Введите размер списка: "))
A = []

for _ in range(N):
    while True:
        try:
            element = int(input("Введите элемент списка: "))
            A.append(element)
            break
        except ValueError:
            print("Ошибка: Введите целое число.")

A.sort()

unique_count = 1
for i in range(1, N):
    if A[i] != A[i - 1]:
        unique_count += 1

print("Количество различных элементов:", unique_count)

