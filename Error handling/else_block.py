try:
    number =int(input("Enter a number:"))
    result = 10/number
    print(result)
except ValueError:
    print("Please Enter a Valid Number!")
except ZeroDivisionError:
    print("Cannot Divide by Zero")
else:
    print("Calculation Successfull")