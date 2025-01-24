# Дана строка-предложение на русском языке. Подсчитать количество содержащихся
# в строке знаков препинания.

def count_punctuations(string):
    punctuations = '.,?!:"()-'
    count = 0
    for char in string:
        if char in punctuations:
            count += 1
    return count

input_string = input("Введите предложение: ")
result = count_punctuations(input_string)
print(f"Количество знаков препинания в строке-предложении: {result}")