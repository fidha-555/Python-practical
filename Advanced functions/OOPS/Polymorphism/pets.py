class Dog:
    def speak(self):
        return "Bark!"
class Cat:
    def speak(self):
        return "Meow!"
class Cow:
    def speak(self):
        return"Baah!"
pets = [Dog(),Cat(),Cow()]
for pet in pets:
    print(pet.speak()) 