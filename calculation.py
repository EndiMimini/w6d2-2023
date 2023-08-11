class User():
    def __init__(self, name):
        self.name = name
        self.account = BankAccount(100)

    def depositMoney(self):
        ammountDeposited = input('Please write the ammount that you want to deposit:')
        self.account.addMoney(ammountDeposited)
        self.printAccountInfo()
        return self

    def printAccountInfo(self):
        print(f'You have ${self.account.ammount} in your bank account')


class BankAccount():
    def __init__(self, ammount):
        self.ammount = ammount
    
    def addMoney(self, ammountAdded):
        self.ammount += int(ammountAdded)
        return self.ammount



endi = User('Endi')
endi.printAccountInfo()

endi.depositMoney()