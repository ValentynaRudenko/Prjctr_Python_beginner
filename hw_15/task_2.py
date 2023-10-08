
class Restaurant:

    def __init__(self, name, cuisine, menu):
        self.name = name
        self.cuisine = cuisine
        self.menu = menu


class FastFood(Restaurant):
    def __init__(self, name, cuisine, menu, drive_thru):
        super().__init__(name, cuisine, menu)
        self.drive_trhu = drive_thru

    def order(self, dish, quantity_order):
        if dish in menu:
            if quantity_order > menu[dish]["quantity"]:
                return "Requested quantity not available"
            else:
                cost = menu[dish]["price"] * quantity_order
                menu[dish]["quantity"] = menu[dish]["quantity"]
                - quantity_order
                return cost
        else:
            return "Dish is not available"


menu = {
    'burger': {'price': 5, 'quantity': 10},
    'pizza': {'price': 10, 'quantity': 20},
    'drink': {'price': 1, 'quantity': 15}
}

mc = FastFood('McDonalds', 'Fast Food', menu, True)

print(mc.order('burger', 5))  # 25
print(mc.order('burger', 15))  # Requested quantity not available
print(mc.order('soup', 5))  # Dish not available
