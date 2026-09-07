class Book:
    def __init__(self,name,author):
        self.name = name
        self.author = author
    def read(self):
        print("I'm reading the book",self.name,"written by",self.author)
b1 = Book("The Alchemist","Paulo Coelho")
b2 = Book("Wings of Fire","APJ Abdul kalam") 

b1.read()
b2.read()

