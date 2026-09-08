from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        return "Car is starting.."

class Bike(Vehicle):
    def start(self):
        return"Bike is starting.."

c = Car()
b = Bike()
print(c.start())
print(b.start())

