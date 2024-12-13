# Дано вещественное число A и целое число N (>0). Используя один цикл, найти сумму
# 1 + A + A^2 + A^3 + ... + A^N

A = float(input("Введите вещественное число A: "))
while True:
    try:
        N = int(input("Введите целое число N (>0): "))
        if N <= 0:
            raise ValueError
        break
    except ValueError:
        print("Пожалуйста, введите целое число больше 0.")

sum = 1
for i in range(1, N + 1):
    sum += A ** i

print(f"Сумма 1 + A + A^2 +... + A^N = {sum}")




