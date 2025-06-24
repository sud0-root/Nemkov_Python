import sqlite3 as sq

with sq.connect('PZ_15/raskhody.db') as con:
    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS raskhody")
    con.execute("""CREATE TABLE IF NOT EXISTS raskhody(
            data_r DATE,    
            prod_id INTEGER PRIMARY KEY, 
            imya_prod VARCHAR NOT NULL,
            raskh_res INTEGER NOT NULL,
            summa INTEGER NOT NULL)""")
    info = [
    ('2024-07-12', 1, 'Хлеб', 200, 2000),
    ('2024-06-12', 2, 'Молоко', 20, 1500),
    ('2025-05-12', 3, 'Булочка', 300, 3000),
    ('2024-07-04', 4, 'Кроссовки', 40, 4000),
    ('2024-06-16', 5, 'Порошок', 30, 600),
    ('2022-09-11', 6, 'Рулет', 50, 500),
    ('2023-08-23', 7, 'Одеяло', 15, 6000),
    ('2021-07-13', 8, 'Чайник', 400, 4000),
    ('2024-02-19', 9, 'Брюки', 23, 5500),
    ('2024-04-10', 10, 'Футболка', 55, 3500)
]
    cur.executemany("INSERT INTO raskhody VALUES (?, ?, ?, ?, ?)", info)
    con.commit()

    print("--- Исходные данные ---")
    cur.execute("SELECT * FROM raskhody")
    print(cur.fetchall())
    print("\n")

    print("--- 3 SELECT запроса ---")
    cur.execute("SELECT * FROM raskhody WHERE summa < 1000")
    print("Продукты с суммой расходов < 1000:", cur.fetchall())

    cur.execute("SELECT * FROM raskhody WHERE imya_prod = 'Хлеб'")
    print("Продукты с наименованием 'Хлеб':", cur.fetchall())

    cur.execute("SELECT * FROM raskhody WHERE raskh_res > 100")
    print("Продукты с расходом ресурсов > 100:", cur.fetchall())
    print("\n")

    print("--- 3 UPDATE запроса ---")
    cur.execute("UPDATE raskhody SET summa = summa + 500 WHERE imya_prod = 'Молоко'")
    con.commit()
    print("После UPDATE (Молоко):")
    cur.execute("SELECT * FROM raskhody WHERE imya_prod = 'Молоко'")
    print(cur.fetchall())

    cur.execute("UPDATE raskhody SET raskh_res = 100 WHERE summa > 3000")
    con.commit()
    print("После UPDATE (raskh_res = 100 WHERE summa > 3000):")
    cur.execute("SELECT * FROM raskhody WHERE summa > 3000")
    print(cur.fetchall())

    cur.execute("UPDATE raskhody SET imya_prod = 'Кекс' WHERE imya_prod = 'Булочка'")
    con.commit()
    print("После UPDATE (Булочка -> Кекс):")
    cur.execute("SELECT * FROM raskhody WHERE imya_prod = 'Кекс'")
    print(cur.fetchall())
    print("\n")

    print("--- 3 DELETE запроса ---")
    cur.execute("DELETE FROM raskhody WHERE raskh_res > 300")
    con.commit()
    print("После DELETE (raskh_res > 300):")
    cur.execute("SELECT * FROM raskhody")
    print(cur.fetchall())

    cur.execute("DELETE FROM raskhody WHERE prod_id = 2")
    con.commit()
    print("После DELETE (prod_id = 2):")
    cur.execute("SELECT * FROM raskhody")
    print(cur.fetchall())

    cur.execute("DELETE FROM raskhody WHERE summa = 4000")
    con.commit()
    print("После DELETE (summa = 4000):")
    cur.execute("SELECT * FROM raskhody")
    print(cur.fetchall())
    print("\n")

    print("--- Окончательное состояние таблицы ---")
    cur.execute("SELECT * FROM raskhody")
    print(cur.fetchall())
