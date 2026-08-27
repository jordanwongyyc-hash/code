import random

class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.tricks = []
        self.isSitting = False
    def learn_trick(self,newtrick):
        self.tricks.append(newtrick)

    def sit_down(self):
        self.isSitting = True
    def get_up(self):
        self.isSitting = False
    def get_state(self):
        if self.isSitting == True:
            return self.name + " is sitting"
        else:
            return self.name + " is not sitting"
    def __str__(self):
        return (f'name:{self.name}| Age: {self.age}| Tricks {self.tricks}| state: {self.get_state()}')



ToTo = Dog("ToTo",1)

print(ToTo.name)
print(ToTo.age)
print(ToTo.tricks)
print(ToTo.isSitting)

ToTo.name = "ToTo"

print(ToTo.name)

ToTo.learn_trick("Sitting")

print(ToTo.tricks)

ToTo.sit_down()

print(ToTo.isSitting)

print(ToTo.get_state())

print(ToTo)

Cat = Dog("cat",0)

print(Cat.name)

print(Cat.age)