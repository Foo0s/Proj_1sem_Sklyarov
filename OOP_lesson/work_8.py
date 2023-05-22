
class BankAccount:
    def __init__(self, balance, account_number):
        self.__balance = balance
        self.__account_number = account_number

    def get_balance(self):
        return "Текущий баланc {}".format(self.__balance)

    def deposit(self, number):
        if type(number) == int:
            self.__balance += number
        else:
            return "Ошибка, пополнение невозможно!"

    def withdraw(self, number):
        if type(number) == int:
            if self.__balance <= 0:
                return "Ошибка ваш баланс меньше или равен 0."
            else:
                self.__balance -= number
                return f"Текущий баланс {self.__balance}"
        else:
            return "Ошибка, невозможно снять деньги со счета!"


obj3 = BankAccount(3400, 4)
print(obj3.deposit(34))
print(obj3.get_balance())
print(obj3.withdraw(34))


print()

obj4 = BankAccount(0, 1)
print(obj4.deposit(1))
print(obj4.get_balance())
print(obj4.withdraw(1))
print(obj4.withdraw(2))
