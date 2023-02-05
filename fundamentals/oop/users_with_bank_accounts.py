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

class Users:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = {
            "checking": BankAccount(.02, 0),
            "savings": BankAccount(.02, 0)
            }

    def make_deposit(self, account_name, amount):
        self.account[account_name].deposit(amount)
        return self

    def make_withdrawal(self, account_name, amount):
        self.account[account_name].withdraw(amount)
        return self

    def display_user_balance(self, account_name="both"):
        if account_name == "both":
            for actval in self.account:
                print(self.account[actval].balance)
        else:
            print(self.account[account_name].balance)
        return self
        

    def transfer_money(self, amount, account_name, other_user):
        self.account[account_name].withdraw(amount)
        other_user.account[account_name].deposit(amount)
        return self

user_1= Users("John Smith", "noemail@noemail.com")
user_2= Users("Adam Jobes", "noemail@noemail.com")
user_1.make_deposit("checking", 100).display_user_balance("checking").transfer_money(40, "checking", user_2).display_user_balance("checking")
user_2.display_user_balance()
user_2.display_user_balance('checking')
