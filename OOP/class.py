# In Python, every data type is a class,
#  and every value you create is an object.

class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_value(self):
        return self.price * self.quantity


item1 = Item(name = "phone", price = 5000, quantity = 5)

print(item1.calculate_total_value())





