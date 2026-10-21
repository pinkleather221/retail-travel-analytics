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

# class variables and instance variables 
# an instance variable belongs to one object
# a class variable is shared from every object from that class

class Student:
    class_year = 2025
    num_students = 0

    def __init__(self, name: str, age: int): #using guard rails to prevent users from inputing wrong data type
        assert age > 0, f"Age {age} has to be greater than zero" #this is also another guard rail
        self.name = name  #instance variable
        self.age = age   #instance variable
        Student.num_students += 1 #class variable


student1 = Student(name = "nelly", age = 20)
student2 = Student(name = "elly", age = 23)
student3 = Student(name = "nel", age = 22)
student4 = Student(name = "lly", age = 21)

print(f"My graduating class of {Student.class_year} has {Student.num_students} students")


#pillars of OOP
# ENCAPSULATION == keeping an objects data safe inside the object and the outside world can only 
#                 acces it through methods you control
# 3 levels of encapsulation is public, protected and private
#     public: "name" = anyone can read or change 
#     protected: '_name' = a hint that says "This is outside code, leave it alone" kinda like bro code
#     private: '__name' = python renames it behind the scenes so that its hard to reach from outside the class

class BankAccount:
    def __init__(self, owner, balance, password):
        self.owner = owner
        self.balance = balance 
        self.password = password