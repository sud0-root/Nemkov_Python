# Разработать программу с применением пакета tk, взяв в качестве условия одну
# любую задачу из ПЗ №№ 2 – 9.

# Даны три целых числа A, B, C
# Проверить истинность высказывания: «Ровно одно из чисел A, B, C положительное.»

import tkinter as tk


def check_num():
    try:
        a = int(entry_a.get())
        b = int(entry_b.get())
        c = int(entry_c.get())
    except ValueError:
        label_res.config(text="Вы ввели неправильные данные!")
        return

    positive_count = 0
    if a > 0:
        positive_count += 1
    if b > 0:
        positive_count += 1
    if c > 0:
        positive_count += 1

    if positive_count == 1:
        label_res.config(text="Высказывание истинно")
    else:
        label_res.config(text="Высказывание ложно")


root = tk.Tk()
root.title("Проверка чисел")
root.geometry("300x300")

label_a = tk.Label(root, text="Введите число A:", font=("Arial", 12))
label_a.pack(pady=5)

entry_a = tk.Entry(root, font=("Arial", 12), width=10, justify=tk.CENTER)
entry_a.pack(pady=5)

label_b = tk.Label(root, text="Введите число B:", font=("Arial", 12))
label_b.pack(pady=5)

entry_b = tk.Entry(root, font=("Arial", 12), width=10, justify=tk.CENTER)
entry_b.pack(pady=5)

label_c = tk.Label(root, text="Введите число C:", font=("Arial", 12))
label_c.pack(pady=5)

entry_c = tk.Entry(root, font=("Arial", 12), width=10, justify=tk.CENTER)
entry_c.pack(pady=5)

check = tk.Button(root, text="Проверить", command=check_num, font=("Arial", 12), pady=5)
check.pack(pady=5)

label_res = tk.Label(root, text="", font=("Arial", 12))
label_res.pack(pady=5)

root.mainloop()