"""###EXERCISE: Human Class"""

# Create a new class `Human` which has required attributes `first_name:str`, `last_name:str`, `address:str`, `age:int`, and `is_hungry:bool`.

class Human:

	def __init__(self, 
			  first_name:str, 
			  last_name:str, 
			  address:str, 
			  age:int, 
			  is_hungry:bool):

		if (type(first_name) != str): # optional type checking
			raise TypeError("first_name must be a string")

		# set attributes
		self.first_name = first_name
		self.last_name = last_name
		self.address = address
		self.age = age
		self.is_hungry = is_hungry


	# A `Human` instance has a `__repr__` that shows their attributes.

	def __repr__(self):
		return f"Human(first_name={self.first_name}, last_name={self.last_name}, address={self.address}, age={self.age}, is_hungry={self.is_hungry})"


	# A `Human` instance has a `full_name()` method which returns their `first_name` and `last_name` in a single string, for example `"Bob Dylan"`.

	def full_name(self):
		return f"{self.first_name} {self.last_name}"


	# A `Human` instance has an `order_drinks()` method which either returns `"Party time!"` if their age is 21 or older and returns `"Denied"` if their age is 20 or younger.

	def order_drinks(self):
		if (self.age >= 21):
			return "Party time!"
		else:
			return "Denied"


	# A `Human` instance has an `eat()` method which sets their attribute `is_hungry` equal to `False`.

	def eat(self):
		self.is_hungry = False


	# A `Human` instance has a `workout()` method which sets their attributes `is_hungry` equal to `True`.

	def workout(self):
		self.is_hungry = True


	# A `Human` instance has a `win_lottery()` method which sets their attribute `address` equal to `"Disneyworld"`.

	def win_lottery(self):
		self.address = "Disneyworld"


	# A `Human` instance has a `change_first_name()` method which creates an input with the prompt `"Change Name >>> "`. When a user completes the input the `first_name` attribute changes to their input.

	def change_first_name(self):
		new_name = input("Change Name >>> ")
		if (len(new_name.replace(" ", "")) >= 1):
			self.first_name = new_name
		else:
			raise Exception("New name must be at least one character")
		# Exception is the most generic error


chett = Human(
	first_name="Chett", 
	last_name="Tiller", 
	address="123", 
	age=12, 
	is_hungry=False
)

greyson = Human(
	first_name="Greyson", 
	last_name="Grey", 
	address="456 Somewhere place", 
	age=22, 
	is_hungry=True
)