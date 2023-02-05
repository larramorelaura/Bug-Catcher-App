class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        self.int_rate=int_rate
        self.balance=balance

    def deposit(self, amount):
        self.balance+=amount
        return self

    def withdraw(self, amount):
        self.balance-=amount
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance=self.balance*(1+self.int_rate)
            print(self.balance)
        return self

    def bank_account_info(self):
        print(f"Interest rate: {self.int_rate} Balance: {self.balance}", sep="\n")

account_1= BankAccount(.25, 100)
account_2= BankAccount(.35, 500)

account_1.deposit(100).deposit(300).deposit(50).withdraw(45).yield_interest().display_account_info()
account_2.deposit(500).deposit(400).withdraw(100).withdraw(100.50).withdraw(100).withdraw(60).yield_interest().display_account_info()
account_1.bank_account_info()
account_2.bank_account_info()