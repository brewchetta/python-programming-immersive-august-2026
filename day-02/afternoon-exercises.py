# python -i day-02/afternoon-exercises.py

"""
1. Build a function `is_it_cake()` which accepts an argument `string` and returns `True` if the `string` is "cake" and `False` otherwise.
"""

def is_it_cake( string:str ):
    return string.lower().replace(" ", "") == "cake"



"""
2. Write a function get_average() which accepts list_of_numbers
	Return all of those numbers averaged together. Begin by using a `for` loop or a `while` loop to add all the numbers together.
"""

numbers = [1,2,3,4,5]
numbers_two = [0,4,28,6]

def get_average( list_of_numbers:list ):
    # add numbers
    total = 0
    for number in list_of_numbers:
        total += number

    # divide by number of numbers
    number_of_items = len( list_of_numbers )

    average = total / number_of_items

    return average



"""
3. Write a function open_thieves_cave() which takes in one argument passphrase
 	the function returns True if the passphrase is "open sesame" and False if the passphrase is anything else
 	Example:	open_thieves_cave("open sesame") >>> True
 	Example:	open_thieves_cave("speak friend and enter") >>> False
"""

def open_thieves_cave( passphrase:str ):
    return passphrase == "open sesame"



"""
4. Define a new function fungus_among_us() which accepts a list `plants` as an argument
    return True if the list contains the string "fungus" and False if not
    don't overthink this one, there's a very simple method to doing it...
    Example: fungus_among_us( ["tree", "flower", "fungus", "moss"] ) >>> True
"""

plants = ["tree", "flower", "fungus", "moss"]
plants_two = ["tree", "flower", "moss"]

def fungus_among_us( plants:list ):
    for plant in plants:
        if (plant == "fungus"):
            return True

    return False



"""
5. Define a new function halfway_there() which accepts a list of arbitrary data `items` longer than 1 item
    insert the string "HALFWAY" at the middle of the list and return the altered list
    when inserting, you will need to make sure your index is an integer...
    Example: halfway_there( [1,2,3,4,5,6] ) >>> [1,2,3,"HALFWAY",4,5,6]
"""

random_items = ["chair", "table", "drawer", "spoon"]
#                0        1        2         3

def halfway_there( items:list ):
    if (len( items ) > 1):
        halfway_index = int( len( items ) / 2 )
        items.insert(halfway_index, "HALFWAY")
