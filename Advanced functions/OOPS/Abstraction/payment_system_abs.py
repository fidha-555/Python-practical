from abc import ABC,abstractmethod

class Payment(ABC):
    def pay(self,amount):
        pass

class UPI(Payment):
    def pay(self,amount):
        print("Paid",amount,"using UPI")

class Card(Payment):
    def pay(self,amount):
        print("Paid",amount,"using UPI")

p1 = UPI()
p2 = Card()

print(p1.pay(500))
print(p2.pay(1000))