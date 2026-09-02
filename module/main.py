import utility
from my_package import calculator,greeter

print(utility.greet("Fidha"))
print(utility.add(6,7))

print (greeter.say_hello("Ram"))
added = calculator.add(5,9)
print("Added:",added)

sub = calculator.subtract(added, 6)
print("Sub: ",sub)