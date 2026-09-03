balance =5000

def show_menu():
    print("\n=====ATM=====")
    print("\n1.Check Balance")
    print("\n2.Deposit")
    print("\n3.Withdraw")
    print("\n4.Exit")

def check_balance():
    print("Your Current Balance is :  ",balance)

def deposit():
    global balance
    amount = int(input("Enter the amount to deposit: "))
    balance = balance + amount
    print("Deposit Successfull!")
    print("New balance is : ",balance)

def withdraw():
    global balance
    amount= int(input("Enter the amount to withdraw:"))
    if amount > balance:
        print("Cannot withdraw more than Balance!")
    else:
      balance = balance - amount
      print("Withdrawal Successfull!")
      print("Remaining balance is :",balance)

while True:
    show_menu()
    choice = input("Enter your choice(1-4): ")
    if choice == "1":
        check_balance()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        print("Thank you!Exit>>")
    else:
        print("Invalid choice,try again.")

