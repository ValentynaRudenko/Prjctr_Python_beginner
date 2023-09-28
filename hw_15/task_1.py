
class Product:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


class Book(Product):

    def __init__(self, name, price, quantity, author):
        super().__init__(name, price, quantity)
        self.author = author

    def read(self):
        print(f"The book {self.name} by author {self.author}.\n"
              f"Price is ${self.price}")


# Creating an instance of Product
apple = Product('Apple', 0.5, 10)

# Creating an instance of Book
book = Book('Python Programming', 30, 5, 'John Doe')

# Calling the read method of Book
book.read()
