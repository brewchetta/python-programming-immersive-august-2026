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

# a set does not allow for duplicate entries
my_set = {1,2,2,2,2,2,3} # {1,2,3}
my_list = [1,2,2,2,2,2,2,3] # [1,2,2,2,2,2,2,3]

# we can use this to remove any duplicates from a list and then reconvert it into a list
def remove_duplicates(l:list):
    return list(set(l))

# Tuples #
# it's pronounced tuh-ple
# a tuple is like a list however it cannot be changed, we cannot reassign the elements, we can not append or remove data, etc.

my_list = [1,2,3]
my_tuple = (1,2,3)

# my_tuple.append(4) # will throw an error!
# my_tuple[0] = 5 # will throw an error

# even if you only have 1 item you must STILL USE A COMMA
my_tuple = (1,)


# List Comprehension #

my_list = [1,2,3]

new_list = [ num + 1 for num in my_list ]

# list comprehension creates a new list
my_list # [1,2,3]
new_list # [2,3,4]

# list comprehension can be used for any iterable
my_tuple = (2,4,6)
new_list = [ num * 2 for num in my_tuple ]
# [4, 8, 12]

# it can even be used for a range
# a range is all the numbers between 0 (or another number) and an upper limit
range(100) # all the numbers up to 99
range(50,100) # all the numbers from 50 to 99

squares = [ num ** 2 for num in range(1,100) ]
# creates a list of squares for 1-99

# filtering using list comprehension:

# all odd numbers 1-9
odds = [ num for num in range(1,10) if num % 2 == 1 ]
# all even numbers 1-9
evens = [ num for num in range(1,10) if num % 2 == 0 ]

# you can both filter and create a product:

odd_squares = [ num ** 2 for num in range(1,10) if num % 2 == 1 ]



# Lambda Functions #

def normal_function(name):
    return f"Greetings {name}"

normal_function("Jimothy") # "Greetings Jimothy"

lambda_function = lambda name: f"Greetings {name}"
lambda_function("Jimothy") # "Greetings Jimothy"

add = lambda x,y: x + y
add(1,2) # 3


# Requests Library #

# CRUD - CREATE READ UPDATE DELETE

# GET - read info from the server
# POST - create new info in the server
# PUT/PATCH - update info in the server
# DELETE - delete info in the server

import requests

# requests makes a http request to the server
response = requests('https://ecommerce-backend-api-dusky.vercel.app/api/products')

# check that we get a 200 OK status
if (response.status_code == 200):

    # .json() parses the data into a dictionary or list so that we can look at it in python
    data = response.json()
    print( data["message"] ) # "Products retrieved successfully"

    # pull out the products data
    products = data["products"]

    products[0] # first product
    products[0]["name"] # the name of the first product
    data["products"][0]["name"] # the same thing but without our nice `products` variable

    # use list comprehension to see all the names
    all_names = [ prod["name"] for prod in products ]

    # use list comprehension to see all the names for only electronics
    all_electronic_names = [ 
        prod["name"] 
        for prod 
        in products 
        if prod["category"] == "Electronics"
    ]

# if we don't get a 200 we let the user know
else:
    print("Unable to fetch from server")


# Executables #
