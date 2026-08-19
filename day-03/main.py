# Class Syntax #

# class - type of object

my_string = "I am a string"
type( my_string ) # <class 'str'>

other_string = "I am another string"
type( other_string ) # <class 'str'>

# my_string and other_string are "instances"

# <class 'str'> is the "class" that they belong to


# class names are almost always going to be upper camel case

class Car:

    # a method is just a function attached to a class / instance
    def drive( self ):
        return "VROOOOOOM"
    # self is the car that's using the method
    # ex: taurus.drive() ---> self == taurus

    def print_make_and_model(self):
        print(f"{self.make} {self.model}")


    # magic/dunder (double underscore) method
    # special methods which aren't called directly
    # they usually are called in special circumstances

    # init stands for initialize
    # __init__ happens whenever we create a new car instance
    def __init__(self, make, model):
        self.make = make
        self.model = model
        print(f"{self} has been created!")
    # only one __init__ per class


    # __repr__ stands for representation
    # this is the string that will show when we use `print` with the car or see it as a string
    def __repr__(self):
        return f"Car(make={self.make}, model={self.model})"


f40 = Car("Ferrari", "F40")
taurus = Car("Ford", "Taurus")
thunderbird = Car(model="Thunderbird", make="Ford")
delorean = Car("DMC","Delorean")

# Car is the class
# f40 / taurus / thunderbird are the instances
        




# Instances vs Classes #


# Class Instance Attributes #


# Instance Methods #


# Self #


# Class Attributes #


# Class Methods #


