# Monday Review Practice #


# Define a new function create_full_name() which takes in two arguments: first_name and last_name as strings
# 	the function returns the first_name and last_name as a single string
# 	Example:	create_full_name("Bob", "Marley") >>> "Bob Marley"

def create_full_name(first_name, last_name):
    # formatted (f) string
    return f"{first_name} {last_name}"
    # concatenation
    return first_name + " " + last_name


print( create_full_name("Chett", "Tiller") )


# Define a new function c_to_f() which takes in one argument: temp_celsius as a number
# 	the function returns the temperature as farenheit, you may return either an int or a float
# 	the formula for conversion is F = (C * 9/5) + 32
# 	Example:	c_to_f(30) >>> 86.0

def c_to_f(temp_celsius):
	return (temp_celsius * 9/5) + 32


print( c_to_f(32) )
print( c_to_f(100) )
print( c_to_f(0) )
print( c_to_f(50) )