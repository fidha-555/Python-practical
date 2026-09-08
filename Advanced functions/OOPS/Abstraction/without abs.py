class MyBankATM:
    def withdraw(self):
        print("Cash withraw Successfully")

    def verify_pin (self):
        print("Pin verified Successfully")
    def check_balance(self):
        print("Balance Checked Successfully")
    def update_server(self):
        print("Server Updated Successfully")
atm = MyBankATM()
atm.verify_pin
atm.check_balance
atm.update_server
atm.withdraw()

