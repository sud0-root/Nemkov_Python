# Дано трехзначное число. Производится вывод его последней цифры (единицы), а затем — его средней цифры (десятки).

num = None

while num is None:
    try:
        num = int(input("Введите число: "))
        if not 100 <= num <= 999:
            print("Ошибка: Число не трехзначное!")
            num = None
    except ValueError:
        print("Ошибка: Введено не число!")

last_dig = num % 10

mid_dig = (num // 10) % 10

print(f"Последняя цифра: {last_dig}")
print(f"Средняя цифра: {mid_dig}")
