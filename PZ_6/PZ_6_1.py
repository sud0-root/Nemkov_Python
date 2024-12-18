# Дан список A размера N. Вывести его элементы в следующем порядке: A1, AN, A2,
# AN-1, A3, AN-2, ….

N = int(input("Введите размер списка: "))
A = []
for _ in range(N):
    A.append(int(input("Введите элемент списка: ")))

for i in range(N // 2):
    print(A[i], A[N - 1 - i], end=' ')
if N % 2 != 0:
    print(A[N // 2])