from abc import ABC, abstractmethod
class LoginSystem(ABC):
    def calculate_interest(self):
        pass

class SavingAccount(LoginSystem):
    def calculate_interest(self):
        return"This is Savings Account"

class CurrentAccount(LoginSystem):
    def calculate_interest(self):
        return"This is Current Account"

s = SavingAccount()
c = CurrentAccount()
print(s.calculate_interest())
print(c.calculate_interest())