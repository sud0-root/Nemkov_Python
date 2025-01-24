# Дана строка. Подсчитать общее количество содержащихся в ней строчных
# латинских и русских букв.

def count_letters(string):
    latin = 'abcdefghijklmnopqrstuvwxyz'
    russian = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    count = 0
    for char in string:
        if char in latin or char in russian:
            count += 1
    return count

input_string = input("Введите строку: ")
result = count_letters(input_string)
print(f"Количество строчных латинских и русских букв: {result}")