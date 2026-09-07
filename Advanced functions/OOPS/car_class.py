class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def start(self):
        print(self.brand,self.model ,"Is starting..",)
c1 = Car("Tesla", "Model S")
c2 = Car("BMW","X5")

c1.start()
c2.start()