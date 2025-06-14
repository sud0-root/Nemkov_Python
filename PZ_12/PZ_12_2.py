# Составить генератор (yield), который выводит из строки только буквы.
# -*- coding: utf-8 -*-

def letters_only(input_str):
    for char in input_str:
        if char.isalpha():
            yield char


input_string = "Hello, World!123@# "
letters = ''.join(letters_only(input_string))
print("Буквы: ", letters)