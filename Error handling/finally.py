try:
    num =int(input("Enter a number:"))
    result =10/num
    print(result)
except ValueError:
    print("Please Enter a Valid Number!")
except ZeroDivisionError:
    print("Cannot Divide by Zero")
else:
    print("Calculation Successfull")
finally:
    print("Program ended.Thank you for using!")