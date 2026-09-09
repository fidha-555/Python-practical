class car:
    def start(self):
        return"Car Starts"
class bike:
    def start(self):
        return"Bike starts"
vehicles = [car(),bike()]
for v in vehicles:
    print(v.start())