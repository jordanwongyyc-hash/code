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

ToTo = Dog("ToTo",1)

print(ToTo.name)
print(ToTo.age)
print(ToTo.tricks)
print(ToTo.isSitting)

ToTo.name = "ToTo"

print(ToTo.name)

ToTo.learn_trick("Sitting")

print(ToTo.tricks)
hjbbhjgyj
ToTo.sit_down()

print(ToTo.isSitting)

print(ToTo.get_state())
