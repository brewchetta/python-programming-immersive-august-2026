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


# While Loops #


# For Loops #


