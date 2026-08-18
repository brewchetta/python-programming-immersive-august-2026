# In order to use this file, open a new terminal and type
# python day-02/main.py
# OR
# python3 day-02/main.py

# Conditionals #

# boolean
True
False

free_coffee_counter = 4

# comparison operator
free_coffee_counter >= 10

# >
free_coffee_counter > 10 # False
free_coffee_counter > 0 # True
free_coffee_counter > 4 # False
# <
free_coffee_counter < 10 # True
free_coffee_counter < 0 # False
free_coffee_counter < 4 # False
# >=
free_coffee_counter >= 10 # False
free_coffee_counter >= 0 # True
free_coffee_counter >= 4 # True
# <=
free_coffee_counter <= 10 # True
free_coffee_counter <= 0 # False
free_coffee_counter <= 4 # True
# ==
free_coffee_counter == 10 # False
free_coffee_counter == 0 # False
free_coffee_counter == 4 # True
# !=
free_coffee_counter != 10 # True
free_coffee_counter != 0 # True
free_coffee_counter != 4 # False

def purchase_coffee():
    global free_coffee_counter
    free_coffee_counter += 1
    if (free_coffee_counter >= 10):
        free_coffee_counter = 0
        return "You've purchased 10 coffees, enjoy a free one on us!"
    else:
        return f"You've purchased {free_coffee_counter} coffees, when you have 10 or more you will get a free coffee!"


# if (condition):
#     do whatever we want if true
#     another line for if true
#     more lines for if true
# the if has ended <<< here

def calculator(num_1, num_2, operation):
    # the `or` allows either condition to be true
    if (operation == "+" or operation == "plus"):
        return num_1 + num_2
    # check the elif if the previous condition is not true
    elif (operation == "-" or operation == "minus"):
        return num_1 - num_2
    elif (operation == "*" or operation == "multiply"):
        return num_1 * num_2
    elif (operation == "/" or operation == "divide"):
        return num_1 / num_2

    return "Operation not supported"


valid_username = "admin"
valid_password = "password123"

def check_credentials(username, password):
    # `and` means both must be true
    if (username == valid_username and password == valid_password):
        return "Access Granted"
    else:
        return "Access DENIED"


# The Input Function #

# favorite_drink = input("What is your favorite drink? ")

# favorite_animal = input("What is your favorite animal? ")

def check_credentials():
    username = input("Username: ")
    password = input("Password: ")
    
    if (username == valid_username and password == valid_password):
        return "Access Granted"
    else:
        return "Access DENIED"


# While Loops #

animals = ["aardvark", "alligator", "bat"]
#           0           1            2

# looping - go through each item one at a time and doing something with that item

def print_all_animals():
    index = 0

    while (index < 3):
        current_animal = animals[index]
        print( current_animal )
        index += 1

    print("all done")


def ask_for_valid_password():
    pw = ""
    # this will keep asking until the pw == valid_password
    while (pw != valid_password):
        pw = input("What is the password? ")

    print("Yes that is the password")


def infinite_loops():
    # this will never stop because True will never be False!
    while(True):
        print("This is the song that never ends")
        print("It goes on and on my friends")



# For Loops #

def print_each_animal():
    for animal in animals:
        print(animal)

def find_animal(animal_name):
    for animal in animals:
        if (animal_name == animal):
            return animal
    
    return f"Did not find {animal_name} in animals"

def filter_out_long_animal_names(threshold):
    filtered_animals = []

    for animal in animals:
        if (len(animal) <= threshold):
            filtered_animals.append( animal )
    
    return filtered_animals

def has_three_letters(string):
    return len(string) == 3

def filter_animals( callback ):
    filtered_animals = []

    for animal in animals:
        if ( callback(animal) == True ):
            filtered_animals.append(animal)
    
    return filtered_animals


# Truthiness
# every variable that exists has an inherent truthiness to it

def truthy_or_falsey(item):
    if (item):
        print(f"{item} is truthy!")
    else:
        print(f"{item} is falsey...")

# string:
"bat"   # truthy
"   "   # truthy
""      # falsey

# numbers:
0       # falsey
1       # truthy
1000    # truthy
0.0001  # truthy
-1      # truthy

# booleans:
True    # True
False   # False

# dictionaries:
{ "name": "Chett" } # truthy
{}                  # falsey

# lists:
["hello"]           # truthy
[]                  # falsey

def get_user_input():
    name = input("What is your name? ")
    if (name):
        return "Continue"
    else:
        return "Invalid name"