# Составить функцию, которая выведет на экран строку, содержащую задаваемое с
# клавиатуры число символов.

def print_string(num_chars):
    s = '*' * num_chars

    print(s)

num_chars = int(input("Введите число символов: "))
print_string(num_chars)


