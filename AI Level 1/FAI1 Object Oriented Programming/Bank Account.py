class BankAccount:
    def __init__(self,owner,InterestRate):
        self.owner = owner
        self.interestrate = InterestRate
        self.balance = 0

    def deposit(self,deposit):
        self.balance += deposit
    def withdraw(self,withdraw):
        if withdraw > self.balance:
            print("Your withdraw is to much")
        else:
            self.balance -= withdraw
    def calculateintrest(self):
        intrest = self.balance * self.interestrate
        self.balance += intrest

    def __str__(self):
        return(f"Owner:{self.owner},Balance:{self.balance}")


Bob = BankAccount("bob", 0.05)
print(Bob.owner)
print(Bob.balance)
print(Bob.interestrate)

Bob.deposit(100)

print(Bob.balance)

print(Bob)

Bob.withdraw(10)

print(Bob.balance)

Bob.withdraw(200)

Bob.calculateintrest()

print(Bob.balance)