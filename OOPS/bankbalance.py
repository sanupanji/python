'''
create a bank account class that has two attribute
. owner
. balance

and two methods
. deposit
. withdraw

withdrawal value should not exist current bank balance
print class also  '''


class Account():

    def __init__(self, owner, balance):

        self.owner = owner
        self.balance = balance

    def __str__(self):

        return f"account owner : {self.owner}\nCurrent balance: {self.balance}"

    def deposit(self, amount):

        self.balance += amount
        print(f"{amount} added to bank account")

    def withdraw(self, amount):

        if self.balance - amount < 0:
            print("Account balance is low!! Please maintain sufficient balance")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn from account")

    def passbook(self):
        pass


owner = input("Enter account owner's name: ")
ini = int(input("Enter initial balance: "))

acc = Account(owner, ini)
print(acc)


while True:
    m = int(input(f"""
    Hello {owner}, what you like to do:
    ENTER 
    1 for deposit
    2 for withdraw
    3 for current balance
    4 for quit
    """))

    if m == 1:
        a = int(input("Enter the diposit amount: "))
        acc.deposit(a)
    elif m == 2:
        a = int(input("Enter the withdraw amount: "))
        acc.withdraw(a)
    elif m == 3:
        print(acc)
    else:
        quit()
