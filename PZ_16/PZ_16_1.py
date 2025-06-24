# Создайте класс «Банк», который имеет атрибуты суммы денег и процентной ставки.
# Добавьте методы для вычисления процентных начислений и снятия денег.

class Bank:
    def __init__(self, balance, interest_rate):
        self.balance = balance
        self.interest_rate = interest_rate

    def calc_interest(self, time_period):
        interest = self.balance * (self.interest_rate / 100) * time_period
        return interest

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Недостаточно средств на балансе.")
        self.balance -= amount


bal = float(input("Введите текущий баланс: "))
int_r = float(input("Введите текущую ставку: "))
my_bank = Bank(bal, int_r)
print(f"Текущий баланс: {my_bank.balance:.2f} руб.")


time_p = int(input("Введите период вложения: "))
interest_earned = my_bank.calc_interest(time_p)
print(f"Начисленные проценты за {time_p} года: {interest_earned:.2f} руб.")

try:
    wd = float(input("Введите сумму для снятия: "))
    my_bank.withdraw(wd)
    print(f"Новый баланс: {my_bank.balance:.2f} руб.")
except ValueError as e:
    print(e)