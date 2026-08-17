# In order to use this file, open a new terminal and type
# python day-01/main.py
# OR
# python3 day-01/main.py

# a comment starts with a # and is for humans to read, the computer doesn't read or execute comments


# To run a file like this: python day-01/main.py


# To exit the REPL --> ctrl + D


# Using Print Statements #

# print("hello world")
print("hello world")

print(1 + 2 + 3)


# Declaring Variables #
# store short term data

# var name = var value
animal = "I am a python"

print(animal)

# declaring a variable
name = "Chett"

print(name)

# change a variable -- reassignment
name = "Python Programmer Man"

CONSTANT = "I shouldn't changed but I can be if you really want to"


# Data Types #

# STRINGS
my_string = "I am a string a.k.a. text"

print( "Hello " + name )
# adding strings with a + is concatenation

# formatted strings / "f" strings
domain = "google.com"
resource = "maps"
location = "eiffel_tower"
f"https://www.{domain}/{resource}/{location}"

# snake_case - normal variable
# camelCase
# UpperCaseCase - python classes

# variable names usually use snake case
a_brand_new_variable = "This uses snake case!"


# NUMBERS

# integer   - whole number
1
5
-30
2000

# float     - number with a decimal
1.1
5.312345
3.14159
-0.8

3 + 3
3 - 2
3 * 3
3 / 2
3 ** 3

counter = 0

# set counter equal to itself + 1
counter = counter + 1

# does the same thing as above
counter += 1

# same thing but adding 10 at a time now
counter += 10

price_one = 3.99
price_two = 6.20
price_three = 1.05

# PEMDAS
# parentheses / exponent / multiplication / division / add / subtract

# sum of all prices divided by the number of prices
average = (price_one + price_two + price_three) / 3

# round to 2 decimals
average = round(average, 2)


# BOOLEAN

True
False

lights_on = True

fire_alarm_blaring = False

average > 2 # True

# Getting Types

type("I am a string") # str

# different types don't always play together...

# 22 > "hello" 
# creates an error because they are not compatible data types




# Functions #
# fn --> function
# fn allows us to do stuff - we can activate functions to do work for us without having to type out all the different aspects of work
# repeat a unit of work very easily by activating a fn

# DEFINE A FN - use def
def say_hello():
    # this is where we tell the fn what it does
    # everything tabbed in is part of the fn
    print("why hello there")
    print("I didn't see you")

# tabbing back in signals the end of the fn instructions

# CALLING A FN - use the parentheses ()
say_hello()
say_hello()
say_hello()

result = say_hello()

print("RESULT:")
print(result)


# a parameter allows us to put data into a fn
def add_five( parameter ):
    return parameter + 5
# parameter is a stand in for whatever we'll be giving the fn when we call it

# return allows us to get data from the fn
add_five(20) # 25

# you can save a fn output to a variable too!
six_plus_five = add_five(6)

def multiple_returns():
    return "first thing"    # the fn is over after the first return
    return "second thing"   # this never fires
    return "third thing"    # this never fires


# Variable Scopes #

counter = 0
counter += 1
counter += 1
counter += 1
counter += 1
counter += 1

def reset_counter():
    counter = 0

reset_counter()
# the external counter is still 5 because it created an internal variable with the same name, not change the external counter

# global scope
global_variable = "I am an external variable"

# local scope
def show_local_scope():
    internal_variable = "I am locally scoped"
    print( internal_variable )

print( global_variable )
# print( internal_variable )

def print_global_var():
    print(global_variable)

def reset_counter():
    global counter 
    # get the global counter variable
    counter = 0
    # set the global counter = 0


def subtraction(num1, num2):
    return num1 - num2


# with type hints
# type hints tell a user what data type the parameter is expecting
def exponential(num:int, exponent:int):
    return num ** exponent

exponential(3,3)

# parameters vs arguments
# parameter is the named stand in before we have called the fn
# argument is the specific item we pass into the fn

# parameters: num,exponent
# arguments: 3,3


# Lists #


# Dictionaries #


