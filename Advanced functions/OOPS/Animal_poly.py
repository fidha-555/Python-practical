class Animal:
    def sound(self):
        return"some generic animal sound"

class lion(Animal):
    def sound(self):
        return"Lion sounds - Roar!"
class elephant(Animal):
    def sound(self):
        return"Elephant sounds - Trumpet!"

Animals = [lion(),elephant()]
for a in Animals:
    print(a.sound())
