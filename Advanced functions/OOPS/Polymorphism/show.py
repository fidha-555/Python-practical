class Book:
    def show(self):
        print("Displaying Book details : Mystery")
class Movie:
    def show(self):
        print("Displaying movie details : Inception(2010)")
def display(item):
    item.show()
b = Book()
m = Movie()
display(b)
display(m)