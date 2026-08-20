# Inheritance #

class Animal:

    def __init__(self, name):
        self.name = name
        self.is_hungry = True
        print(f"Creating animal {name}...")

    def __repr__(self):
        return f"Animal(name='{self.name}', is_hungry={self.is_hungry})"

    def eat(self):
        self.is_hungry = False
        return "NOM NOM NOM"



# the parentheses show what superclass this class inherits from
# superclass - this is what we're inheriting from
# subclass - the class derived from the superclass
class Cat( Animal ):

    # the __repr__ here replaces the one we would use from the Animal class
    def __repr__(self):
        return f"Cat(name='{self.name}', is_hungry={self.is_hungry})"

    # new methods will only be for the subclass
    def meow(self):
        return "MEOW MEOW MEOW MEOW MEOW MEOW MEOW MEOW MEOW MEOW MEOW MEOW MEOW MEOW MEOW MEOW MEOW MEOW MEOW MEOW MEOW MEOW MEOW MEOW MEOW MEOW MEOW MEOW MEOW MEOW MEOW MEOW MEOW MEOW MEOW MEOW MEOW MEOW MEOW MEOW"

    # super() allows us to get the methods from the superclass
    # super().__init__() specifically calls the __init__ method from Animal
    # you still need to pass any arguments to the method
    def __init__(self, name, number_of_lives=9):
        super().__init__(name)
        self.number_of_lives = number_of_lives
        print(f"Adding cat attributes for {name}...")

jimothy = Animal("Jimothy")
ursula = Cat("Ursula")


# Sets #


# Tuples #


# List Comprehension #


# Lambda Functions #


# Libraries & Modules #


# Requests Library #


# Executables #


