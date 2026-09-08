from abc import ABC,abstractmethod

class ATM(ABC):
    def withdraw(self):
        pass

class MyBankATM(ATM):
    def withdraw(self):
        self.__verify_pin()
        self.__check_balance()
        self.__update_server()
        print("Cash withdraw Successfully..")

    def __verify_pin(self):
        print("Pin verified")

    def __check_balance(self):
        print("Balance checked")

    def  __update_server(self):
        print("Server updated")


atm = MyBankATM()
atm.withdraw()




