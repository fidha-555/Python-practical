class laptop:
    def price(self):
        return "Price of Laptop is:50000"

class GamingLaptop(laptop):
    def price(self):
        return "Price of Gaming Laptop:120000"
class BusinessLaptop(laptop):
    def price(self):
        return "Price of Business Laptop:85000"

laptops = [laptop(),GamingLaptop(),BusinessLaptop()]
for laptop in laptops:
    print(laptop.price())
