
class Product:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


class Book(Product):

    def __init__(self, name, price, quantity, author):
        super().__init__(name, price, quantity)
        self.author = author

    def read(cls, filename):
        instances = []
        with open(filename) as file:
            for row in file:
                instances.append(cls(name=row[0], author=row[1]))
