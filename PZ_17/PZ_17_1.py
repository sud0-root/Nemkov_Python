# В соответствии с номером варианта перейти по ссылке на прототип. Реализовать
# его в IDE PyCharm Community с применением пакета tk. Получить интерфейс максимально
# приближенный к оригиналу

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Создание заказа")
root.geometry("450x520")

top_frame = tk.Frame(root, bg="#3c7b8f", width=600, height=50)
top_frame.pack(side="top", fill="x")

main_name = tk.Label(top_frame, text="Создайте заказ", font=("Arial", 14), bg="#3c7b8f", fg="white")
main_name.pack(pady=10)


section_1 = tk.Label(root, text="1. Информация о заказе", font=("Arial", 12, "bold"), fg="#3c7b8f")
section_1.place(x=5, y=90)

order_num = tk.Label(root, text="Номер заказа*", fg="black")
order_num.place(x=20, y=120)
order_num = tk.Entry(root, width=45)
order_num.place(x=150, y=120)

prod_name = tk.Label(root, text="Название товара", fg="black")
prod_name.place(x=20, y=150)
prod_name = tk.Entry(root, width=45)
prod_name.place(x=150, y=150)

amount = tk.Label(root, text="Количество*", fg="black")
amount.place(x=20, y=180)
amount = tk.Entry(root, width=10)
amount.place(x=150, y=180)


section_2 = tk.Label(root, text="2. Контактная информация", font=("Arial", 12, "bold"), fg="#3c7b8f")
section_2.place(x=5, y=220)

name = tk.Label(root, text="Ваше имя", fg="black")
name.place(x=20, y=250)
name = tk.Entry(root, width=45)
name.place(x=150, y=250)

email = tk.Label(root, text="Ваш email*", fg="black")
email.place(x=20, y=280)
email = tk.Entry(root, width=45)
email.place(x=150, y=280)

phone = tk.Label(root, text="Ваш телефон*", fg="black")
phone.place(x=20, y=310)
phone = tk.Entry(root, width=18)
phone.insert(0, "+7(")
phone.place(x=150, y=310)


section_3 = tk.Label(root, text="3. Информация о доставке", font=("Arial", 12, "bold"), fg="#3c7b8f")
section_3.place(x=5, y=350)

adres = tk.Label(root, text="Адрес*", fg="black")
adres.place(x=20, y=380)
adres = tk.Text(root, width=34, height=4)
adres.place(x=150, y=380)

time_dost = tk.Label(root, text="Время доставки", fg="black")
time_dost.place(x=20, y=460)

hours = [f"{i:02d}" for i in range(0, 24)]
time_dost_1 = ttk.Combobox(root, values=hours, width=5)
time_dost_1.place(x=150, y=460)
time_dost_1.set("00")

minutes = [f"{i:02d}" for i in range(0, 60, 15)]
time_dost_2 = ttk.Combobox(root, values=minutes, width=5)
time_dost_2.place(x=220, y=460)
time_dost_2.set("00")

root.mainloop()