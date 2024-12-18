# Составить функцию, которая выведет на экран строку, содержащую задаваемое с
# клавиатуры число символов.

def print_string(num_chars):
    s = '*' * num_chars

    print(s)

while True:
    try:
        num_chars = int(input("Введите положительное число символов: "))

        if num_chars <= 0:
            print("Ошибка: Введено неположительное число. Попробуйте снова.")
            continue

        print_string(num_chars)
        break
    except ValueError:
        print("Ошибка: Введено нецелое число. Попробуйте снова.")
