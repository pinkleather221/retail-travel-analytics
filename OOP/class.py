# # In Python, every data type is a class,
# #  and every value you create is an object.

# class Item:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity

#     def calculate_total_value(self):
#         return self.price * self.quantity


# item1 = Item(name = "phone", price = 5000, quantity = 5)

# print(item1.calculate_total_value())

# # class variables and instance variables 
# # an instance variable belongs to one object
# # a class variable is shared from every object from that class

# class Student:
#     class_year = 2025
#     num_students = 0

#     def __init__(self, name: str, age: int): #using guard rails to prevent users from inputing wrong data type
#         assert age > 0, f"Age {age} has to be greater than zero" #this is also another guard rail
#         self.name = name  #instance variable
#         self.age = age   #instance variable
#         Student.num_students += 1 #class variable


# student1 = Student(name = "nelly", age = 20)
# student2 = Student(name = "elly", age = 23)
# student3 = Student(name = "nel", age = 22)
# student4 = Student(name = "lly", age = 21)

# print(f"My graduating class of {Student.class_year} has {Student.num_students} students")


# #pillars of OOP
# # ENCAPSULATION == keeping an objects data safe inside the object and the outside world can only 
# #                 acces it through methods you control
# # 3 levels of encapsulation is public, protected and private
# #     public: "name" = anyone can read or change 
# #     protected: '_name' = a hint that says "This is outside code, leave it alone" kinda like bro code
# #     private: '__name' = python renames it behind the scenes so that its hard to reach from outside the class

# class BankAccount:
#     def __init__(self, owner, balance, password):
#         self.owner = owner #public can read directly
#         self.__balance = balance #private hiding the real money value
#         self._password = password #protected handled with care

#     def get_balance(self):
#         return self.__balance #a safe way to return the private balance 

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount #safe ,controlled way to change the private balance 

#     def get_password(self):
#         return self._password #getting the password safely 

# account = BankAccount(owner = "Nelly", balance = 500, password ="winner1")

# account.deposit(4000)
# print(account.owner)
# print(account.get_balance())

#INHERITANCE 
# lets a new class reuse attributes of 
# an existing class , instead of creating a new class from scratch 
# parent class = the iriginal class 
# child class = the class that inherits from the parent class 

# a parameter is a variable defined inside a function's signature to 
# receive inputs, while an attribute is a variable associated directly
# with an object or class, accessed using dot notation.

# class Animal: #parent class
#     def __init__(self, name):
#         self.name = name 
#         self.is_alive = True # attributes that are boolean are not included in the dunder init method

#     def eat(self):
#         print(f"{self.name} is eating")

#     def sleep(self):
#         print(f"{self.name} is sleeping.")

# class Dog(Animal): #child class
#     def speak(self):
#         print("WOOF")


# class Cat(Animal): #child class
#     def speak(self):
#         print("Miiiaaauuu")

# class Elephant(Animal): #child class 
#     def speak(self):
#         print("Fruuuuuuuuu")

# dog = Dog(name = "Mia")
# cat = Cat(name = "Luna")
# elephant = Elephant(name = "Tembo")

# dog.eat()
# cat.sleep()
# dog.speak()
# elephant.sleep()


# # multiple inheritance 
# # a child class can inherit from more than one parent class at once
# # multilevel inheritance 
# # its a chain or inheritance between classes ,,,, eg a class c iherits from b and b inherits from a class A

# class Predator(Animal):
#     def hunt(self):
#         print(f"{self.name} has to eat to survive ")

# class Prey(Animal):
#     def escape(self):
#         print(f"{self.name} has to escape to live another day")

# class Hawk(Predator):
#     pass

# class Rabbit(Prey):
#     pass

# class Fish(Prey, Predator):
#     pass

# hawk = Hawk(name ="viky")
# rabbit = Rabbit(name = "jojo")
# fish = Fish(name = "momo")
# rabbit.escape()
# fish.escape()
# hawk.hunt()
# fish.hunt()
# hawk.sleep()
# rabbit.is_alive  #inherited from Animal


# #super() enables a child class to call
# #  a method from its parent class then 
# # add its own extra steps on top it avoids copy pasting the parents code into each child 

# class Shape:
#     def __init__(self, color, is_filled):
#         self.color = color
#         self.is_filled = is_filled 

#     def describe(self):
#         print(f"It is {self.color} and {"filled" if self.is_filled else "not filled"}.")

# class Circle(Shape):
#     def __init__(self, color, is_filled, radius):
#         super().__init__(color, is_filled)
#         self.side = radius

#         def describe(self):
#             super().describe()
#             print(f"The area of the circle is {3.142 * self.radius * self.radius}")

# class Square(Shape):
#     def __init__(self, color, is_filled, side):
#         super().__init__(color, is_filled)
#         self.side = side

#     def describe(self):
#                 super().describe()
#                 print(f"The area of the square is {self.side **2} cm^2")

# circle = Circle(color = "blue", is_filled = True, radius = 7)
# square = Square(color = "pink", is_filled = False, side = 7)

# circle.describe()
# square.describe()



# Abstraction involves showing what the user needs and hiding the messy details behind it 
# its done in python using the abstract class and the rule 
# is that every class that inherits from it must provide its
# own version of certain methods the abstractclass itself cannot be turned into an object it only sets exists to set rules for its children
# to implement we use ABC and abstract method 
from abc import ABC, abstractmethod

class Payment(ABC):
    def __init__(self, amount):
        self.amount = amount

    @abstractmethod
    #no code here this forces child class to
    #  write its own pay method or python will refuse to create an object from it 
    def pay(self):
        pass

    def receipt(self):
        print(f"Receipt: KES {self.amount} processed")

class Card(Payment):
    def __init__(self, amount, card_number):
        super().__init__(amount)
        self.card_number = card_number

    def pay(self):
        last_four = self.card_number[-4:]
        print(f"Charging card ending in {last_four} for KES {self.amount}")

class Mpesa(Payment):
    def __init__(self, amount, phone_number):
        super().__init__(amount)
        self.phone_number = phone_number

    def pay(self):
        print(f"Sending mobile money prompt through {self.phone_number} for KES {self.amount}.")

payments = [Card(amount = 10000, card_number = "1111222233334444"), Mpesa(amount = 75000, phone_number = "0799887765")]
for payment in payments:
    payment.pay()
    payment.receipt()