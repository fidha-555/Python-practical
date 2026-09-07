class Person:
    def __init__(self,name):
        self.name = name 
    def walk(self):
        print(self.name, "is walking..")
class Student(Person):
    def study(self):
        print(self.name,"is studying..")
s= Student("Ram")
s.walk()
s.study()