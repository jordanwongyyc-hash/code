class BankAccount:
    def __init__(self,owner,InterestRate):
        self.owner = owner
        self.interestrate = InterestRate
        self.balance = 0

    def deposit(self,deposit):
        self.balance += deposit
    def withdraw(self,withdraw):
        if withdraw > self.balance:
            print("Your withdraw is to much fool")
        else:
            self.balance -= withdraw
    def calculateintrest(self):
        intrest = self.balance * self.interestrate
        self.balance += intrest

