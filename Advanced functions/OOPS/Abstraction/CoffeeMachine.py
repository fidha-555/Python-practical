class CoffeeMachine:
    def __grind_beans(self):
        print("Griding fresh Coffee Beans")
    def __heat_water(self):
        print("Heating water")
    def __brew(self):
        print("Brewing expresso..")
    def make_coffee(self):
        self.__grind_beans()
        self.__heat_water()
        self.__brew()
        print("Coffee is served!")
machine = CoffeeMachine()
machine.make_coffee()
